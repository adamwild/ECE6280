import numpy as np

def conti_frac_expan(b, n, sol):
    sol.append(b/n)
    if b%n == 0:
        return sol
    else:
        conti_frac_expan(n, b%n, sol)

def convergents(Q):
    c_list = []
    d_list = []
    for j in range(len(Q)):
        if j == 0:
            c_list.append(1)
            d_list.append(0)
        elif j == 1:
            c_list.append(Q[1])
            d_list.append(1)
        else:
            c_list.append(Q[j]*c_list[j-1]+c_list[j-2])
            d_list.append(Q[j]*d_list[j-1]+d_list[j-2])
    return c_list, d_list

def wiener(b, n):
    val = []
    conti_frac_expan(b, n, val)
    d, c= convergents(val)
    print('Convergents : ' + str(val))
    for j in range(1, len(c)):
        n_prime = float(d[j]*b-1)/float(c[j])
        if n_prime-int(n_prime) == 0:
            a_quad = 1
            b_quad = -(n - n_prime +1)
            c_quad = n
            delta = b_quad**2 - 4 * a_quad*c_quad
            root1 = float((-b_quad + np.sqrt(delta)))/(2*a_quad)
            root2 = float((-b_quad - np.sqrt(delta)))/(2*a_quad)
            if root1-int(root1) == 0 and root1>0 and root2-int(root2) == 0 and root2>0:
                print ('n_prime : ' + str(int(n_prime)) + ' C_j = ' + str (c[j]) +'/' + str (d[j]))
                return int(root1), int(root2)

print(wiener(77537081, 317940011))
