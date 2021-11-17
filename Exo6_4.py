#Exo6_4
def is_Harshad(n):
    """
    Retourne si le nombre en paramètre est un nombre d'Harshad
    Paramètre : un entier
    Return : si l'entier est un nombre d'Harshad ou non
    >>> is_Harshad(12)
    True
    >>> is_Harshad(13)
    False
    """
    S = sum([int(digit) for digit in str(n)])
    return n%S == 0


def main():
    A = [i for i in range(10,100) if is_Harshad(i)]
    print(A)
    import doctest
    doctest.testmod()
    pass

if __name__ == '__main__':
    main()