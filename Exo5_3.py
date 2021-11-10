def check_password(password):
    """
    Teste la robustesse d'un password

    Args:
        password: chaine de caractères

    Returns:
        True or False

    >>> check_password('A1213pokl')
    False
    >>> check_password('bAse730onE')
    True
    >>> check_password('asasasasasasasaas')
    False
    >>> check_password('QWERTYqwerty')
    False
    >>> check_password('123456123456')
    False
    >>> check_password('QwErTy911poqqqq')
    True
    """
    # votre code ici...

    return len(password) >=10 and any(c.isdigit() for c in password) and any(c.islower() for c in password) and any(c.isupper() for c in password)

if __name__ == '__main__':
    import doctest
    doctest.testmod()