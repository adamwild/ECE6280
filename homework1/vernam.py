"""
4 - Problem 3
"""
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y' ,'Z']
mes1 = 'IZTLSXLMEGFKSPLYEHWFZLRPLZRJRAVNERIXQVGOUYUKVFIGPQQAZSRSHKAUTKHQZIRNBQPTNAJTKCPUEWLVJJ'
mes2 = 'CWMBJHTBXKLZFIPYXYLFPDTUWJRWYFWUETHOSIVACOGYFBICTTHIMFRXBFWJIIEMABGIVFISWAKSHBOOWAHOSV'

dicti = open("monthy_small.txt", "r")
dic = dicti.readlines()

def add(letter1, letter2):
    """
    Adds 2 letters
    """
    ind = alphabet.index(letter1)+alphabet.index(letter2)
    ind = ind%26
    return alphabet[ind]

def sub(letter1, letter2):
    """
    Substracts letter2 to letter1
    """
    ind = alphabet.index(letter1)-alphabet.index(letter2)
    ind = ind%26
    return alphabet[ind]

def get_key(plain, cipher):
    """
    Given a letter from the plaintext and the corresponding letter from the ciphertext, returns the key
    """
    return sub(cipher, plain)

def get_key_word(plain, cipher):
    """
    Get the key from plaintext and ciphertext
    """
    sol = ""
    for i in range(len(plain)):
        sol += get_key(plain[i], cipher[i])
    return sol

def encrypt_onetimepad(plain, key):
    """
    Encrypt using the one-time pad technique
    """
    sol = ""
    for i in range(len(plain)):
        sol += add(plain[i], key[i])
    return sol

def decrypt_onetimepad(cipher, key):
    """
    Decrypt using the one-time pad technique
    """
    sol = ""
    for i in range(len(cipher)):
        sol += sub(cipher[i], key[i])
    return sol

def search_words(beginning, dictionary=dic):
    sol = []
    for mot in dictionary:
        if (len(mot)>len(beginning)) and mot[:len(beginning)] == beginning:
            sol.append(mot[:-1])
    return sol

def next_words(cipher, ind, dictionary = dic):
    i = ind
    beg = ""
    while i<len(cipher) and (cipher[i] in alph):
        beg += cipher[i]
        i += 1
    return(search_words(beg, dictionary))

def is_word(word, dictionary=dic):
    words = search_words(word, dictionary)
    for i in words:
        if i == word:
            return True
    return False

def is_beg(beg, dictionary = dic):
    words = search_words(beg, dictionary)
    return len(beg)>0

def d_otp(cipher, key):
    sol = ""
    for i in range(len(cipher)):
        sol += alph[(ALPHA.index(cipher[i]) - alph.index(key[i])) % 26]
    return sol

def g_key(plain, cipher):
    """
    Get the key from plaintext and ciphertext
    """
    sol = ""
    for i in range(len(plain)):
        sol += alph[ (ALPHA.index(cipher[i]) - alph.index(plain[i])) % 26]
    return sol

def cryptanalysis_onetimepad(c1, c2, ind1=0, ind2=0, key="", sol=[], dictionary = dic):
    words = next_words(c2, ind2, dic)
    for word in words:
        if len(word) > 3:
            print(key,c1,c2)
            if max(ind1, ind2) + len(word) > len(c1):
                if (key, c1, c2) not in sol:
                    sol.append((key,c1,c2))
                    print(key,c1,c2)
                if len(sol)%500 == 0 :
                    print(len(sol))
                return 0
            else:
                ind_key = max(ind1, ind2)
                new_key = key + g_key(word[abs(ind1-ind2):], c2[ind1:])
                ind_ext = ind1 + len(word) - abs(ind1-ind2)
                new_c1 = c1[:ind1] + d_otp(c1[ind1:ind_ext], new_key[ind1:ind_ext]) + c1[ind_ext:]
                for i in range(ind1, ind_ext):
                    if is_word(new_c1[ind1: i]) and is_beg(new_c1[i:ind_ext]):
                        new_c2 = c2[:ind2] + word + c2[ind2 + len(word):]
                        new_ind2 = ind2 + len(word)
                        new_ind1 = i
                        cryptanalysis_onetimepad(new_c2, new_c1, new_ind2, new_ind1, new_key, sol)
                        
            
          
alph = "abcdefghijklmnopqrstuvwxyz"
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


mes1 = 'guardhLMEGFKSPLYEHWFZLRPLZRJRAVNERIXQVGOUYUKVFIGPQQAZSRSHKAUTKHQZIRNBQPTNAJTKCPUEWLVJJ'
mes2 = 'arthurTBXKLZFIPYXYLFPDTUWJRWYFWUETHOSIVACOGYFBICTTHIMFRXBFWJIIEMABGIVFISWAKSHBOOWAHOSV'
key = 'cftupq'

analysis = []
cryptanalysis_onetimepad(mes2, mes1, 6, 5, key, sol=analysis)

for i in analysis:
    print(str(i[0]) + " --- " + str(i[1]) + "\n\n")
