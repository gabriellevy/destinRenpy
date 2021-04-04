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
    FAIT_LA_COUR = u"Fait la cour" # quand les deux connaissent les intentions de l'autre amis qu'ils se jaugent encore avant engagement
    OCCASIONNEL = u"Occasionnel" # relations sexuelles occasionnelles
    COHABITATION = u"Cohabitation"
    MARIAGE = u"Mariage"

    def __init__(self, interetPnjEnversJoueur, interetJoueurEnversPnj):
        self.interetPnjEnversJoueur_ = interetPnjEnversJoueur # de 1 à 10 selon que le pnj aime le perso du joueur
        self.interetJoueurEnversPnj_ = interetJoueurEnversPnj # de 1 à 10 selon que le joueur aime le pnj
        self.typeRelation_ = RelationAmoureuse.SEDUCTION # toutes les relations commencent dans la pahse "séduction"

    def DescriptionInteretPnjEnversJoueur(self):
        if self.interetPnjEnversJoueur_ <= 2:
            return u"Vous a à peine remarqué"
        elif self.interetPnjEnversJoueur_ <= 5:
            return u"Intéressée"
        elif self.interetPnjEnversJoueur_ <= 7:
            return u"Très intéressée"
        else:
            return u"Folle amoureuse"

    def DescriptionInteretJoueurEnversPnj(self):
        if self.interetPnjEnversJoueur_ <= 2:
            return u"Vous la trouvez mignonne"
        elif self.interetPnjEnversJoueur_ <= 5:
            return u"Vous la trouvez intéressante et attirante"
        elif self.interetPnjEnversJoueur_ <= 7:
            return u"Vous pensez à elle tout le temps"
        else:
            return u"Amour fou"


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

    niveauAmabilite = niveauAmabilite + random.randint(0,4) - random.randint(0,3)
    # en théorie un réétalonnage serait une onne idée mais en bourrin pour l'instant :
    if niveauAmabilite < 1:
        niveauAmabilite = 1
    if niveauAmabilite > 10:
        niveauAmabilite = 10

    return niveauAmabilite

def CalculerAmabiliteFemmePremierContact(dicoTraitsPnjF):
    """
    renvoie un chiffre entre 1 et 10 qui est un degré à quel point le pnj (femme) est attiré par le personnage (homme) au premier contact
    prend en compte les traits du personnage, pourrait un de ces jours rpendre en compte une "compatibilité" selon les traits de la femme aussi
    """
    niveauAmabilite = 0
    for traitJoueurStr in dicoTraitsPnjF.keys():
        if traitJoueurStr == trait.Franchise.NOM:
            # lors d'un premier contact il vaut mieux être sournois que franc
            val = dicoTraitsPnjF[traitJoueurStr]
            if val <= trait.Trait.SEUIL_A_PAS:
                niveauAmabilite = niveauAmabilite + 1
            elif val >= trait.Trait.SEUIL_A:
                niveauAmabilite = niveauAmabilite - 1
        elif traitJoueurStr == trait.Intelligence.NOM:
            val = dicoTraitsPnjF[traitJoueurStr]
            if val <= trait.Trait.SEUIL_A_PAS:
                niveauAmabilite = niveauAmabilite - 1
            elif val >= trait.Trait.SEUIL_A:
                niveauAmabilite = niveauAmabilite + 1
        elif traitJoueurStr == trait.Poids.NOM:
            val = dicoTraitsPnjF[traitJoueurStr]
            if val <= trait.Trait.SEUIL_A_PAS:
                niveauAmabilite = niveauAmabilite + 1
            elif val >= trait.Trait.SEUIL_A:
                if val >= trait.Trait.SEUIL_A_EXTREME:
                    niveauAmabilite = niveauAmabilite -2
                niveauAmabilite = niveauAmabilite -1
        elif traitJoueurStr == trait.Taille.NOM:
            val = dicoTraitsPnjF[traitJoueurStr]
            if val <= trait.Trait.SEUIL_A_PAS:
                niveauAmabilite = niveauAmabilite -1
            elif val >= trait.Trait.SEUIL_A:
                niveauAmabilite = niveauAmabilite +1
        elif traitJoueurStr == trait.Beaute.NOM:
            val = dicoTraitsPnjF[traitJoueurStr]
            if val <= trait.Trait.SEUIL_A_PAS:
                if val <= trait.Trait.SEUIL_A_PAS_EXTREME:
                    niveauAmabilite = niveauAmabilite -1
                niveauAmabilite = niveauAmabilite -2
            elif val >= trait.Trait.SEUIL_A:
                if val >= trait.Trait.SEUIL_A_EXTREME:
                    niveauAmabilite = niveauAmabilite +1
                niveauAmabilite = niveauAmabilite +2
        elif traitJoueurStr == trait.Charme.NOM:
            val = dicoTraitsPnjF[traitJoueurStr]
            if val <= trait.Trait.SEUIL_A_PAS:
                if val <= trait.Trait.SEUIL_A_PAS_EXTREME:
                    niveauAmabilite = niveauAmabilite -1
                niveauAmabilite = niveauAmabilite -1
            elif val >= trait.Trait.SEUIL_A:
                if val >= trait.Trait.SEUIL_A_EXTREME:
                    niveauAmabilite = niveauAmabilite +1
                niveauAmabilite = niveauAmabilite +1
        elif traitJoueurStr == trait.Richesse.NOM:
            val = dicoTraitsPnjF[traitJoueurStr]
            if val <= trait.Trait.SEUIL_A_PAS_EXTREME:
                niveauAmabilite = niveauAmabilite -1
            elif val >= trait.Trait.SEUIL_A_EXTREME:
                niveauAmabilite = niveauAmabilite +1

    niveauAmabilite = niveauAmabilite + random.randint(0,4) - random.randint(0,3)
    # en théorie un réétalonnage serait une onne idée mais en bourrin pour l'instant :
    if niveauAmabilite < 1:
        niveauAmabilite = 1
    if niveauAmabilite > 10:
        niveauAmabilite = 10

    return niveauAmabilite
