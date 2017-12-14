import numpy as np

alpha = 2317547
p = 10930889
beta = 4867455
#a_sol = 41192

def inv_mod(val, mod):
    #Returns val^(-1)
    for i in range(mod):
        if val*i % mod == 1:
            return i

def exhaust(alpha, beta, p):
    #Exhaustive search of log_{alpha}(beta) (mod p), only used for checking purposes
    cpt = 0
    val = 1
    while True:
        cpt += 1
        val = int(int(val*alpha)%p)
        if beta == val:
            return cpt


def decompo_overbase(num, facto_base):
    #Returns the powers of the primes when num can be factored over the factor base
    #Returns False if num can not be factored
    val = num
    sol = [0]*len(facto_base)
    i = 0
    while i < len(facto_base):
        if val == 1:
            return sol
        else:
            if val%facto_base[i] == 0:
                sol[i] +=1
                val = val/facto_base[i]
            else:
                i +=1    
    return False

def compute_numbase(alph, p, facto_base):
    #Computes the system to solve to find the log_{alpha} of the factor base
    sol = []
    n_v = []
    val = 1
    cpt = 0
    while len(sol) !=len(facto_base):
        val = val*alph %p
        cpt += 1
        res = False
        if val !=1:
            res = decompo_overbase(val,facto_base)
        if res is not False:
            sol.append(res)
            n_v.append(cpt)
    return sol, n_v

def get_factored(beta, p, alph, facto_base):
    #Finds a s value such that beta*(p**s) can be factored using the primes in facto_base
    s = 1
    val_alph = alph
    sol = decompo_overbase(beta*val_alph % p, facto_base)
    while sol is False:
        s += 1
        val_alph = val_alph*alph % p
        sol = decompo_overbase(beta*val_alph % p, facto_base)
    print('beta*(p**s) = ' + str(beta)+'*('+str(alph)+'**'+str(s)+') = ' + str(int(beta*val_alph % p)))
    return int(beta*val_alph % p), s, sol

def test_prim(num, p):
    #Tests if a number is a primitive element
    pwr = 1
    val = num
    grp = []
    while val not in grp:
        grp.append(val)
        val = val*num%p
        pwr +=1
    if len(grp) == p-1:
        return True
    else:
        return False

factor_b = [2,3,5]
#print decompo_overbase(189, factor_b)
print('--get_factored(4867455, p, 139, factor_b)--')
get_factored(4867455, p, 139, factor_b)
print('\n')

print('--get_factored(16673, p, 139, factor_b)--')
get_factored(16673, p, 139, factor_b)
print('\n')

print('--compute_numbase(139, p, factor_b)--')
print(compute_numbase(139, p, factor_b))
print('\n')

