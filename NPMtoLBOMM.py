def lbomcompat(A,decimal_separator=','):
    B = []
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            B.append(str(A[i,j]))
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