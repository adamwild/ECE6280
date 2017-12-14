'''
Most of the code came from 'John'.
Source : https://stackoverflow.com/a/4293123
'''

import numpy
import math
from numpy import matrix
from numpy import linalg

def modMatInv(A,p):       # Finds the inverse of matrix A mod p
  n=len(A)
  A=matrix(A)
  adj=numpy.zeros(shape=(n,n))
  for i in range(0,n):
    for j in range(0,n):
      adj[i][j]=((-1)**(i+j)*int(round(linalg.det(minor(A,j,i)))))%p
  return (modInv(int(round(linalg.det(A))),p)*adj)%p

def modInv(a,p):          # Finds the inverse of a mod p, if it exists
  for i in range(1,p):
    if (i*a)%p==1:
      return i
  raise ValueError(str(a)+" has no inverse mod "+str(p))

def minor(A,i,j):    # Return matrix A with the ith row and jth column deleted
  A=numpy.array(A)
  minor=numpy.zeros(shape=(len(A)-1,len(A)-1))
  p=0
  for s in range(0,len(minor)):
    if p==i:
      p=p+1
    q=0
    for t in range(0,len(minor)):
      if q==j:
        q=q+1
      minor[s][t]=A[p][q]
      q=q+1
    p=p+1
  return minor

def mul_mod(A,b,p):
    sol = [0]*len(b)
    val = 0
    for i in range(len(b)):
        for j in range(len(b)):
            val += (A[i,j]*b[j]) %p
        sol[i] = int(val) %p
        val = 0
    return sol

a = numpy.matrix([[3, 1, 6], [3, 9, 1], [1, 2, 4]])
a_inv = modMatInv(a, 10930888)
b = [37419,48349,57952]
print (a_inv)
print (b)
print (mul_mod(a_inv,b,10930888))
