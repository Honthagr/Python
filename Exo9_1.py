FILENAME = "C:/Users/nicol/Desktop/Esiee/PythonE2/Python/data/mots.txt"

def est_dans(mot, ensemble):
    """
    Retourne une chaine de caractère exprimant la vérité de "mot" est dans "l'ensemble"

    Args:
        mot (str)
        ensemble : une séquence ou un set de chaînes de caractères

    Returns:
        str : la vérité de "mot" est dans "l'ensemble"
    """
    # votre code ici
    return str(mot in ensemble)

def read_file(filename):
    """
    Ouvre un fichier et retourne un set contenant chaque ligne sans le caractère "\n"

    Args :
        filename(str) : chemin du fichier

    Returns :
        set : ensemble des lignes du fichier "filename"
    """
    file = open(filename,"r")
    lines = file.readlines()
    file.close
    TableauMots = {line.split("\n")[0] for line in lines}
    return TableauMots

if __name__ == "__main__":
    
    
    # liste

    liste_mots = read_file(FILENAME)

    

    # sets

    tout = { }

    mots = ["chronophage", "procrastinateur", "dangerosité", "gratifiant"]
    A = [(est_dans(a,liste_mots)) for a in mots]
    mots_7lettres = {mot if len(mot) == 7 else None for mot in liste_mots}
    mots_avec_k = {mot if 'k' in mot else None for mot in liste_mots }
    mots_7lettres_avec_k = mots_avec_k & mots_7lettres
    mots_avec_w = {mot if 'k' in mot else None for mot in liste_mots}
    mots_avec_w_and_k = mots_avec_k & mots_avec_w
    mots_avec_z = { mot if 'z' in mot else None for mot in liste_mots}
    mots_commencant_par_z = mots_avec_z & {mot if mot[0]=='z' else None for mot in liste_mots }
    mots_terminant_par_z = mots_avec_z & {mot if mot[-1]=='z' else None for mot in liste_mots }
    mots_avec_z_en_position_non_terminale = mots_avec_z - mots_commencant_par_z - mots_terminant_par_z
    mots_avec_z_en_position_non_terminale_et_k = mots_avec_z_en_position_non_terminale & mots_avec_k
