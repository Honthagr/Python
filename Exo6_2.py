from Exo6_1 import scand
import os
def searchext(l):
    """
    Identifie les extensions de la liste de fichiers passée en argument
    Args:
        l : liste des noms de fichier sous forme de chaine de caractères
    Returns:
        Liste des extensions sous forme de chaine de caractères
        
    >>> l = searchext(['ARJ.PIF', 'atiogl.xml', 'ativpsrm.bin', 'bfsvc.exe'])
    >>> isinstance(l, list) # vrai si l est une liste
    True
    >>> print(l)
    ['pif', 'xml', 'bin', 'exe']
    >>> l = searchext(['HelpPane.exe', 'hh.exe', 'HPMProp.INI', 'IE9_main.log'])
    >>> isinstance(l, list) # vrai si l est une liste
    True
    >>> print(l)
    ['exe', 'exe', 'ini', 'log']
    >>> l = searchext(['win.ini', 'WindowsShell', 'WindowsUpdate.log', 'winhelp.exe'])
    >>> isinstance(l, list) # vrai si l est une liste
    True
    >>> print(l)
    ['ini', 'log', 'exe']
    """
    e = [os.path.splitext(i)[1].replace('.','').lower() for i in l if i.find('.') != -1]
    return e    

def main():
    import doctest
    doctest.testmod()
    pass

if __name__ == '__main__':
    main()