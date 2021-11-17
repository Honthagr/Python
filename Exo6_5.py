#Exo6_5
def is_Happy(n):
    """
    Retourne si le nombre entier passé en paramètre est un nombre entier ou non
    Paramètre : Un nombre entier
    Return : Boolean si le nombre entier est heureux ou non
    >>> is_Happy(13)
    True
    >>> is_Happy(14)
    False
    """
    
    if n == 1:
        return True
    elif n in (4,16,37,58,89,145,42,20):
        return False
    else: return is_Happy(sum([int(digit)**2 for digit in str(n)]))
    

def main():
    A = [i for i in range(1,100) if is_Happy(i)]
    print(A)

    import doctest
    doctest.testmod()
    pass

if __name__ == '__main__':
    main()