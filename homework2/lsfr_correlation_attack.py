def incr(val):
    """
    Increments a binary number stored in a string
    Loops, 111+1 -> 000
    """
    n = len(val)
    num = int(val, 2)
    num += 1
    num = bin(num)[2:]
    while len(num)<n:
        num = '0' + num
    return num[len(num)-n:]
            
def xor(v1, v2):
    if (v1 == '0' and v2 == '0') or (v1 == '1' and v2 == '1'):
        return '0'
    else:
        return '1'

def mult(v1, v2):
    if v1 == '1' and v2 == '1':
        return '1'
    else:
        return '0'

def x(Init_val, length):
    """
    Computes a bit stream of length 'length' given an initial value
    """
    sol = Init_val
    while len(sol) < length:
        n = len(sol) - 1
        val = xor(sol[n-2], sol[n-1])
        sol += val
    return sol

def y(Init_val, length):
    """
    Computes a bit stream of length 'length' given an initial value
    """
    sol = Init_val
    while len(sol) < length:
        n = len(sol) - 1
        val = xor(sol[n-3], sol[n])
        sol += val
    return sol

def z(Init_val, length):
    """
    Computes a bit stream of length 'length' given an initial value
    """
    sol = Init_val
    while len(sol) < length:
        n = len(sol) - 1
        val = xor(sol[n-2], sol[n-4])
        sol += val
    return sol

def f(x, i_x, y, i_y, z, i_z, length):
    """
    Computes the f functions based on the initial values for x, y and z functions
    """
    s_x = x(i_x, length)
    s_y = y(i_y, length)
    s_z = z(i_z, length)
    sol = ''
    i=0
    while len(sol)<length:
        sol += xor(xor(mult(s_x[i],s_y[i]) , mult(s_y[i], s_z[i])),s_z[i])
        i+=1
    return sol

def exhaustive_search():
    """
    Just to check!
    """
    n = len(keystream)
    v_x = "001"
    while v_x != "000":
        v_y = "0001"
        while v_y !="0000":
            v_z = "00001"
            while v_z != "00000":
                sol = f(x, v_x, y, v_y, z, v_z, n)
                if sol == keystream :
                    print("v_x : " + str(v_x) + ", v_y : " + str(v_y) + ", v_z : " + str(v_z))
                v_z = incr(v_z)
            v_y = incr(v_y)
        v_x = incr(v_x)

def correlation(func, len_Init_val, keystream):
    """
    Computes all sequences possible for a given function
    Compares it with the keystream and computes the percentage
    of bits being identical
    """
    val = '1'
    final_value = '0'
    while len(val) < len_Init_val:
        val = '0' + val
        final_value += '0'

    while val != final_value:
        stream = func(val, len(keystream))
        freq = 0.
        for i in range(len(keystream)):
            if stream[i] == keystream[i]:
                freq += 1
        freq = freq/len(keystream)
        print(val + ' : ' + str(freq))
        val = incr(val)
    print('')

keystream = '0000110011001001011101100010010'

correlation(x, 3, keystream)
correlation(z, 5, keystream)

print(f(x, '010', y, '1010', z, '10101', len(keystream)))
print(keystream)




