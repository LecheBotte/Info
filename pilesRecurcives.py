def puissance(a,n):
    if n == 0:
        return 1
    elif n%2 == 0:
        return puissance(a,n/2)**2
    else :
        return a * puissance(a,(n-1)/2)**2