

class Metier:
    """
    Classe contenant les fonctions statiques de base liées à tous les métiers
    Comme le métier en tant que carac n'est qu'une String il faut appeler ces fonctions pour avoir les valeurs liées au métier comme par exemple :
     - le salaire
     - si il est de bureau
     - si il est dangereux
     - etc
    """

    METIER = "Métier"

    # types de métiers
    ADMINISTRATIF = "MétierAdministratif"

def estDeBureau(strMetier):
    if "administratif" in strMetier.lower():
        return True

    return False

def regenererCaracsMetier(situation):
    print("regenererCaracsMetier")
    if not aUnMetier(situation):
        # pas de métier
        return
    nomMetier = situation[Metier.METIER]
    if estDeBureau(nomMetier):
        situation[Metier.ADMINISTRATIF] = 1

def aUnMetier(situation):
    return situation[Metier.METIER] != ""
