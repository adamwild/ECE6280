def squares(val):
    for i in range(26):
        if i**2%26 == val:
            print (i)

def ownneg():
    for i in range(26):
        if i%26 == (-i+26)%26:
            print (i)

def det_1():
    sol = 0
    for a in range(26):
        for b in range(26):
            for c in range(26):
                if (a**2 +b*c)%26 == 1:
                    sol+=1
    print (sol)

det_1()
