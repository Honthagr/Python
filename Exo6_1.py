#Exo6_1
import os

def scand(r):
    """
    Sépare les fichiers et les répertoires du répertoire passé en argument
    Args:
        r: répertoire à analyser
    Returns:
        Liste des noms de fichier sous forme de chaine de caractères
        Liste des noms de répertoire sous forme de chaine de caractères
    >>> f, d = scand('C:\Windows')
    >>> isinstance(f, list) # vrai si f est une liste
    True
    >>> len(f) == 0
    False
    >>> isinstance(f, list) # vrai si d est une liste
    True
    >>> len(d) == 0
    False
    """
    # le contenu des répertoires étant dépendant de la configuration
    # les doctests sont limités
    Liste = os.listdir(r)

    f = [i for i in Liste if os.path.isfile(os.path.join(r,i))]
    d = [i for i in Liste if os.path.isdir(os.path.join(r,i))]

    return f, d

def main():
    import doctest
    doctest.testmod()
    pass

if __name__ == '__main__':
    main()