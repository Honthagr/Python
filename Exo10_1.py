import csv
from collections import namedtuple

def build_stations_dict(csvfile):
    """
    retourne un dictionnaire des stations météo du fichier passé en argument

    Args:
        csvfile: un fichier au format csv contenant une liste de stations météo

    Returns:
        dictionnaire de namedtuple des informations relatives aux stations météo
        
    >>> d = build_stations_dict('stations-meteo.csv')
    >>> print(d['NICE'])
    Station(ID='07690', Latitude=43.648833, Longitude=7.209, Altitude=2)
    >>> print(d['BELLE ILE-LE TALUT'])
    Station(ID='07207', Latitude=47.294333, Longitude=-3.218333, Altitude=34)
    >>> print(d['CAYENNE-MATOURY'])
    Station(ID='81405', Latitude=4.822333, Longitude=-52.365333, Altitude=4)
    >>> print(d['NICE'].Latitude)
    43.648833
    """
    # votre code ici...
    with open("c:/Users/nicol/Desktop/Esiee/PythonE2/Python/"+csvfile, 'r') as f:
        r = csv.reader(f, delimiter=';')
        l = list(r)
    Station_meteo = namedtuple('Station',['ID','Latitude','Longitude','Altitude'])

    return {l[i][1]:Station_meteo(l[i][0],float(l[i][2]),float(l[i][3]),int(l[i][4])) for i in range(1,len(l))}

if __name__ == '__main__':
    import doctest
    doctest.testmod()
