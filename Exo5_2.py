from Exo5_1 import MortAuxEspaces

def pal(s):
    """
    Teste si s est un palindrome.

    Args:
        s: chaine de caractères

    Returns:
        True or False
        
    >>> pal("ressasser")
    True
    >>> pal("Hannah")
    True
    >>> pal("Engage le jeu que je le gagne")
    True
    >>> pal("Esope reste ici et se repose")
    True
    >>> pal("Elu par cette crapule")
    True
    >>> pal("Cette phrase n'est pas un palindrome")
    False
    """

    # Ecriture "bas niveau"
    # i = 0
    # j = len(s) - 1
    # while i < j:
    #     while s[i] == ' ': i +=1
    #     while s[j] == ' ': j -=1
    #     if s[i].lower() != s[j].lower():
    #         return False
    #     i += 1
    #     j -= 1
    # return True
    
    # Ecriture Pythonique (3 lignes max)
    # votre code ici...

    A = MortAuxEspaces(s.lower())
    B = MortAuxEspaces(s[::-1].lower())
    if A == B:
        return True
    else : return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
