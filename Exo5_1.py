def MortAuxVoyelles(A):
    """
    Retourne une string sans voyelle

    Args :
        A = String dont on veux enlever les voyelles

    Return :
        Une string sans voyelle

    >>> MortAuxVoyelles("abcde")
    'bcd'
    >>> MortAuxVoyelles("cdd")
    'cdd'
    """
    for i in range(len(A)):
        if A[i] in "aeiouy":
            B = MortAuxVoyelles(A[:i] + A[i+1:])
            return B
    else : B = A
    return B

def MortAuxEspaces(C):
    """
    Retourne une string sans espace

    Args :
        A = String dont on veux enlever les espaces

    Return :
        Une string sans espaces

    >>> MortAuxEspaces("a bcd e")
    'abcde'
    >>> MortAuxEspaces("cd  d")
    'cdd'
    """
    for i in range(len(C)):
        if C[i] in " ":
            D = MortAuxEspaces(C[:i] + C[i+1:])
            return D
    else : D = C
    return D

if __name__ == '__main__':
    import doctest
    doctest.testmod()