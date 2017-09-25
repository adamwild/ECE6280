from random import shuffle

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

def self_xor(v):
    sol = 0
    for i in (bin(v)[2:]):
        if i == '1':
            sol = 1-sol
    return sol


S_prof = [6, 1, 2, 4, 0, 8, 12, 5, 11, 15, 3, 7, 14, 10, 9, 13]
S_stinson = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]

def print_approximation_table(sub_box):
    sol = ''
    for a in range(16):
        for b in range(16):
            N_l_ab = 0
            for x in range(16):
                y = sub_box[x]
                val = (self_xor(a&x))^(self_xor(b&y))
                if val == 0:
                    N_l_ab += 1
            sol += str(N_l_ab)
            if len(str(N_l_ab)) == 1:
                sol+=' '
            sol += ' | '
        sol+='\n'
    print(sol)

def test_approximation_table(sub_box, lower, upper):
    for a in range(16):
        for b in range(16):
            N_l_ab = 0
            for x in range(16):
                y = sub_box[x]
                val = (self_xor(a&x))^(self_xor(b&y))
                if val == 0:
                    N_l_ab += 1
            if a!=0 and b!=0 and (N_l_ab<lower or N_l_ab > upper):
                return False
    return True

def print_difference_distribution_table(sub_box):
    for x_prime in range(16):
        vect = [0]*16
        for x in range(16):
            x_star = x^x_prime
            y = sub_box[x]
            y_star = sub_box[x_star]
            y_prime = y^y_star
            vect[y_prime] += 1
        print(str(vect) + '\n')

def test_difference_distribution_table(sub_box, val):
    for x_prime in range(16):
        vect = [0]*16
        for x in range(16):
            x_star = x^x_prime
            y = sub_box[x]
            y_star = sub_box[x_star]
            y_prime = y^y_star
            vect[y_prime] += 1
        for i in vect:
            if i > val and x_prime != 0:
                return False
    return True

def exhaustive_search():
    i=0
    Sbox = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    t1=[]
    t2=[]
    boolean = False
    while not boolean:
        shuffle(Sbox)
        test1 = test_approximation_table(Sbox, 6, 10)
        test2 = test_difference_distribution_table(Sbox, 4)
        boolean = test1 and test2
        if test1:
            t1.append(Sbox)
        if test2:
            t2.append(Sbox)
        i+=1
        if i%50000 == 0:
            print(i, len(t1), len(t2))
    print(i)
    print(Sbox)

def fast_search():
    i=0
    Sbox = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    boolean = False
    while not boolean:
        shuffle(Sbox)
        boolean = test_approximation_table(Sbox, 4, 12) and test_difference_distribution_table(Sbox, 4)
        i+=1
        if i%50000 == 0:
            print(i)
    print(i)
    print(Sbox)
    return Sbox

def from_string_tosbox(string):
    sol = []
    for i in string:
        sol.append(int(i,16))
    return sol

Sbox = fast_search()
print_approximation_table(Sbox)
print_difference_distribution_table(Sbox)
