import numpy as np
import matplotlib.pyplot as plt
from random import randint

#tri par insertion
listea = [randint(0,100) for i in range(10)]
print(listea,"liste non triée")
def tri_insertion(liste):
    for i in range(1,len(liste)):
        j = i
        while j > 0 and liste[j] < liste[j-1]:
            liste[j],liste[j-1] = liste[j-1],liste[j]
            j -= 1
    return liste
print(tri_insertion(listea),"liste triée")

#tri par selection
listeb = [randint(0,100) for i in range(10)]
print(listeb,"liste non triée")
def tri_selection(liste):
    for i in range(len(liste)):
        min = i
        for j in range(i+1,len(liste)):
            if liste[j] < liste[min]:
                min = j
        liste[i],liste[min] = liste[min],liste[i]
    return liste
print(tri_selection(listeb),"liste triée")

#tri par fusion
listec = [randint(0,100) for i in range(10)]
print(listec,"liste non triée")
def tri_fusion(liste):
    if len(liste) > 1:
        mid = len(liste)//2
        L = liste[:mid]
        R = liste[mid:]
        tri_fusion(L)
        tri_fusion(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                liste[k] = L[i]
                i += 1
            else:
                liste[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            liste[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            liste[k] = R[j]
            j += 1
            k += 1
    return liste
print(tri_fusion(listec),"liste triée")
