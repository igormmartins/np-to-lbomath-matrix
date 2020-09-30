import cmath
import numpy as np

def lbomcompat(A,compmode='normal',decimal_separator=','):
    B = []
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if compmode == 'normal': B.append(str(A[i,j]))
            elif compmode == 'ang': B.append(comptophas(A[i,j]))
            B.append(" # ")
        del B[-1]
        B.append(" ## ")
    del B[-1]

    C = "".join(B)
    L = []
    for i in C:
        if i == ".":
            L.append(decimal_separator)
        elif i == "(" or i ==")":
            pass
        else:
            L.append(i)
    return ("left [ matrix { "+"".join(L) + " } right ]")


def comptophas(Value,angtyp='deg',decimal=4):
    absvalue = abs(Value)
    if angtyp == 'deg': ang = cmath.phase(Value)*(180/cmath.pi)
    elif angtyp == 'rad': ang = cmath.phase(Value)
    return("{0:.{decimal}f}⦟{1:.{decimal}f}".format(absvalue,ang,decimal=decimal))