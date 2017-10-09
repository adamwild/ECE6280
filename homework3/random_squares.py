import numpy as np
from fractions import gcd

n = 256961
print(np.sqrt(n))

def make_vector(num, B):
    sol = []
    for i in B:
        if num%i == 0 and (num/i)%i != 0:
            sol.append(1)
        else:
            sol.append(0)
    if num>0:
        sol[0] = 0
    else:
        sol[0] = 1
    return sol

def random_squares(l, B, n):
    for j in range(1, l):
        z1 = int(np.sqrt(j*n))
        z1_p = (z1**2%n)-n

        z2 = int(np.sqrt(j*n)) + 1
        z2_p = (z2**2)%n

        print(z1, make_vector(z1_p, B))
        print(z2, make_vector(z2_p, B))

def random_squares_linear(beg, end, B, n):
    for j in range(beg, end):
        z = (j**2)%n
        if make_vector(z, B) == [0]*len(B):
            print(j, make_vector(z-n, B))
        else:
            print(j, make_vector(z, B))

B = [-1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
#B = [-1, 2, 3, 5, 7, 11, 13]

random_squares_linear(500, 520, B, 256961)
