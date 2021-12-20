import math
import numpy as np

def vec(A,B):
    return B-A

def ps(v1,v2):
    return v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2]

def norme(v):
    return np.sqrt(ps(v, v))

def unitaire(v):
    if norme(v) != 0:
        return (1/norme(v))*v

def pt(r,t):
    assert t>=0
    (S,u)=r
    return S+t*u

def dir(A,B):
    return unitaire(vec(A,B))

def ra(A,B):
    return A, dir(A,B)

def sp(A,B):
    return A, norme(vec(A, B))

def intersection(r,s):
    (A,u)=r
    (C, rayonSphere)=s
    b = 2*ps(vec(C,A),u)
    a = 1
    c = norme(vec(C,A))**2-r**2
    Delta = b**2 - 4*a*c
    if Delta > 0:
        return None
    else :
        distance = (-b-np.sqrt(Delta))//(2*a)
        point = pt(A, distance)
        return (point, distance)

noir = np.array([0.,0.,0.])
blanc = np.array([1.,1.,1.])

# Q9) il faut que la source de lumière soit au dessus du plant tangent a la sphere au point P

def au_dessus(s, P, src): #dériver (x-x0)²+(y-y0)²+(z-z0)²-r² >= 0
    if 2(v1[0]-pt(0,t)) + 2(v1[1]-pt(0,t)) + 2(v1[2]-pt(0,t)) -ra(v1,v2) >= 0:
        return True
    return False
