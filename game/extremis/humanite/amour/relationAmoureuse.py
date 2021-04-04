import random
from extremis.humanite import portrait
from extremis.constitution import temps
from extremis.humanite import trait

class RelationAmoureuse:

    C_AMOUREUSES = u"Amoureuses" # id d'une carac qui contient un tableau de pnjs (qui sont tous des relations amoureuses du perso joueur)

    # valeurs possible de la carac "typeRelation_"
    SEPARE = u"Séparé"
    VEUF = u"Veuf"
    SEDUCTION = u"Séduction" # se tournent autour
    OCCASIONNEL = u"Occasionnel" # relations sexuelles occasionnelles
    COHABITATION = u"Cohabitation"
    MARIAGE = u"Mariage"

    def __init__(self, interetPnjEnversJoueur, interetJoueurEnversPnj):
        self.interetPnjEnversJoueur_ = interetPnjEnversJoueur # de 1 à 10 selon que le pnj aime le perso du joueur
        self.interetJoueurEnversPnj_ = interetJoueurEnversPnj # de 1 à 10 selon que le joueur aime le pnj
        self.typeRelation_ = RelationAmoureuse.SEDUCTION # toutes les relations commencent dans la pahse "séduction"

def CalculerAmabiliteHommePremierContact(dicoTraitsPersoH):
    """
    renvoie un chiffre entre 1 et 10 qui est un degré à quel point le pnj (femme) est attiré par le personnage (homme) au premier contact
    prend en compte les traits du personnage, pourrait un de ces jours rpendre en compte une "compatibilité" selon les traits de la femme aussi
    """
    niveauAmabilite = 0
    for traitJoueurStr in dicoTraitsPersoH.keys():
        if traitJoueurStr == trait.Franchise.NOM:
            # lors d'un premier contact il vaut mieux être sournoisq ue franc
            val = dicoTraitsPersoH[traitJoueurStr]
            if val <= trait.Trait.SEUIL_A_PAS:
                niveauAmabilite = niveauAmabilite + 1
            elif val >= trait.Trait.SEUIL_A:
                niveauAmabilite = niveauAmabilite - 1
        if traitJoueurStr == trait.Poids.NOM:
            # gros = bof
            val = dicoTraitsPersoH[traitJoueurStr]
            if val >= trait.Trait.SEUIL_A:
                niveauAmabilite = niveauAmabilite - 1
        elif traitJoueurStr == trait.Force.NOM:
            val = dicoTraitsPersoH[traitJoueurStr]
            if val <= trait.Trait.SEUIL_A_PAS:
                niveauAmabilite = niveauAmabilite - 1
            elif val >= trait.Trait.SEUIL_A:
                niveauAmabilite = niveauAmabilite + 1
        elif traitJoueurStr == trait.Artiste.NOM:
            # un peu artiste c'est mieux
            val = dicoTraitsPersoH[traitJoueurStr]
            if val >= trait.Trait.SEUIL_A:
                niveauAmabilite = niveauAmabilite + 1
        elif traitJoueurStr == trait.Intelligence.NOM:
            val = dicoTraitsPersoH[traitJoueurStr]
            if val <= trait.Trait.SEUIL_A_PAS:
                niveauAmabilite = niveauAmabilite - 1
            elif val >= trait.Trait.SEUIL_A:
                niveauAmabilite = niveauAmabilite + 1
        elif traitJoueurStr == trait.Assurance.NOM:
            val = dicoTraitsPersoH[traitJoueurStr]
            if val <= trait.Trait.SEUIL_A_PAS:
                if val <= trait.Trait.SEUIL_A_PAS_EXTREME:
                    niveauAmabilite = niveauAmabilite -1
                niveauAmabilite = niveauAmabilite -1
            elif val >= trait.Trait.SEUIL_A:
                if val >= trait.Trait.SEUIL_A_EXTREME:
                    niveauAmabilite = niveauAmabilite +1
                niveauAmabilite = niveauAmabilite +1
        elif traitJoueurStr == trait.Taille.NOM:
            val = dicoTraitsPersoH[traitJoueurStr]
            if val <= trait.Trait.SEUIL_A_PAS:
                if val <= trait.Trait.SEUIL_A_PAS_EXTREME:
                    niveauAmabilite = niveauAmabilite -1
                niveauAmabilite = niveauAmabilite -1
            elif val >= trait.Trait.SEUIL_A:
                if val >= trait.Trait.SEUIL_A_EXTREME:
                    niveauAmabilite = niveauAmabilite +1
                niveauAmabilite = niveauAmabilite +1
        elif traitJoueurStr == trait.Beaute.NOM:
            val = dicoTraitsPersoH[traitJoueurStr]
            if val <= trait.Trait.SEUIL_A_PAS:
                if val <= trait.Trait.SEUIL_A_PAS_EXTREME:
                    niveauAmabilite = niveauAmabilite -1
                niveauAmabilite = niveauAmabilite -1
            elif val >= trait.Trait.SEUIL_A:
                if val >= trait.Trait.SEUIL_A_EXTREME:
                    niveauAmabilite = niveauAmabilite +1
                niveauAmabilite = niveauAmabilite +1
        elif traitJoueurStr == trait.Charme.NOM:
            val = dicoTraitsPersoH[traitJoueurStr]
            if val <= trait.Trait.SEUIL_A_PAS:
                if val <= trait.Trait.SEUIL_A_PAS_EXTREME:
                    niveauAmabilite = niveauAmabilite -1
                niveauAmabilite = niveauAmabilite -1
            elif val >= trait.Trait.SEUIL_A:
                if val >= trait.Trait.SEUIL_A_EXTREME:
                    niveauAmabilite = niveauAmabilite +1
                niveauAmabilite = niveauAmabilite +1
        elif traitJoueurStr == trait.Richesse.NOM:
            val = dicoTraitsPersoH[traitJoueurStr]
            if val <= trait.Trait.SEUIL_A_PAS:
                if val <= trait.Trait.SEUIL_A_PAS_EXTREME:
                    niveauAmabilite = niveauAmabilite -1
                niveauAmabilite = niveauAmabilite -1
            elif val >= trait.Trait.SEUIL_A:
                if val >= trait.Trait.SEUIL_A_EXTREME:
                    niveauAmabilite = niveauAmabilite +1
                niveauAmabilite = niveauAmabilite +1

    print(niveauAmabilite);
    # en théorie un réétalonnage serait une onne idée mais en bourrin pour l'instant :
    if niveauAmabilite < 1:
        niveauAmabilite = 1
    if niveauAmabilite > 10:
        niveauAmabilite = 10

    return niveauAmabilite
