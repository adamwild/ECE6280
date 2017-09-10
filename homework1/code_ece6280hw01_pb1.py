"""
2 - Problem 1
"""

from fractions import gcd
import numpy as np
import matplotlib.pyplot as plt


cipher = "yysjxbysjxnkwkpjucfhyeswwyysotqcvwbxrzdinessgizoetugzwhwtvskidmsiucslkjvgobqcbwojiuwmftfglxrbvxfkhzxhfbwlzerwkmzghbsvgamjczzbrysggqpgsrxxcgwkvbuxxdocxlfcvgjzuzutigkiwzbybxkvwfnjqzbjwwffjrbvbbfbvxwztavtlzvizkofhyzcfbsywkajrroaduclajpasdjxcgwsvwyagffkbxehambysjxyysjxfisuhbjpmmmvfwmmvfwtwvbgvtngtxkffwbglwdmfnodenuokdyfyfhbnvsmnnokpfczaglzbgkbrzdbsxcmmferlhbycebbrgdbpvhgznmsgykvbkxxfawmmzbymmvfwbxkvsmifskgyccnxfnodeyyolpfehkbyucogntcmeijoqxqmskmtyweuzkwllsfhweavgwqfthdrferawwrhzxwysktnuwlytivafxvzxbxvszbrkvwkjsfaglzbytxkcfxliokijutakrcmtryyslhuzbwthyvsgicwcxfecdwxkcfxxrjszjrfexiysehavgagirfcgjjgslnkgwxrjhgfjeclhkncgwxfbdrferlajjvswjftlkjvgzxbzzdgtkugujywfwmzgxtyysjlxrmaglrbvajcwcxxyonbsxhzhzxvlhkzhkhbvzdajjoqlfxoaglfcvyjeqwlrrywztfrfxnxvthwj"
proba = [0.082,0.015,0.028,0.043,0.127,0.022,0.020,0.061,0.070,0.002,0.008,0.040,0.024,0.067,0.075,0.019,0.001,0.060,0.063,0.091,0.028,0.010,0.023,0.001,0.020,0.001]
alph = "abcdefghijklmnopqrstuvwxyz"

def kasiski(cipher_t, length):
    sol = {}
    for i in range(len(cipher_t)-length+1):
        motif = cipher_t[i:i+length]
        for j in range(i+1, len(cipher_t)-length+1):
            if cipher_t[j:j+length] == motif:
                if motif in sol:
                    sol[motif][0] += 1
                    sol[motif][1].append((j-i))
                else:
                    sol[motif] = [2,[i,(j-i)]]
    return sol

def clean_dic(dic, length):
    list_keys = list(dic.keys())
    for i in list_keys:
        if dic[i][0] <= length:
            dic.pop(i)
    return dic

def substrings(cipher, length):
    sol = []
    for j in range(length):
        sub_string = ""
        for i in range(len(cipher)/length):
            sub_string += cipher[j+i*length]
        sol.append(sub_string)
    return sol

def frequency(string):
    """
    Computes the frequency of appearance for each letter
    """
    freq = np.zeros(26)
    for i in string:
        freq[alph.index(i)] += 1
    return freq

def I_c(string):
    """
    Computes the index of coincidence of a string
    """
    freq = frequency(string)

    sol = 0
    for k in range(26):
        sol += freq[k]*(freq[k]-1)

    n = len(string)
    sol = sol/(n*(n-1))
    return sol

def get_ind_closest(array, val):
    """
    Returns the index of the array that contains the closest value to 'val'
    """
    dist = np.abs(array[0]-val)
    sol = 0
    for i in range(2, len(array)):
        if np.abs(array[i]-val) < dist:
            dist = np.abs(array[i]-val)
            sol = i
    return sol

def IoC_method(cipher, size):
    x = []
    y = []
    e = [] #Standard deviation
    for i in range(2,size):
        Ic_values = []
        x.append(i)
        subs = substrings(cipher, i)
        for j in subs:
            Ic_values.append(I_c(j))
        y.append(np.mean(Ic_values))
        e.append(np.std(Ic_values))
    return (x,y,e)

def show_IoC(cipher, size):
    (x,y,e) = IoC_method(cipher, size)
    plt.errorbar(x, y, e, linestyle='None', marker='o')

    plt.show()

def guess_length_key(cipher, size=10):
    (x,y,e) = IoC_method(cipher, size)
    return get_ind_closest(y, 0.065)+2

def guess_key(cipher, length):
    key = ""
    subs = substrings(cipher, length)
    for i in range(length):
        M_g = []
        for g in range(26):
            n_prime = len(subs[i])
            freq = frequency(subs[i])
            M_gk = 0
            for k in range(26):
                M_gk += (proba[k]*freq[(k+g)%26])/n_prime

            M_g.append(M_gk)
        key += alph[get_ind_closest(M_g, 0.065)]
    return key

def sub(letter1, letter2):
    """
    Substracts letter2 to letter1
    """
    ind = alph.index(letter1)-alph.index(letter2)
    ind = ind%26
    return alph[ind]

def decipher_vigenere(cipher, key):
    sol = ""
    for i in range(len(cipher)):
        sol += sub(cipher[i],key[i%len(key)])
    return sol

def cryptanalysis_vigenere(cipher):
    length_key = guess_length_key(cipher)
    key = guess_key(cipher, length_key)
    return key
