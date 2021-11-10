def est_premier(x):
    """
    Retourne si x est premier ou non.

    Args : 
        x : valeur entière positive

    Return : 
        True or False

    >>> est_premier(11)
    True
    >>> est_premier(6)
    False
    >>> est_premier(3)
    True
    """

    a = int(x**1/2)

    for i in range(2,a+1):
        if x%i == 0 or x%2 == 0:
            return False
            break
    else:
        return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()