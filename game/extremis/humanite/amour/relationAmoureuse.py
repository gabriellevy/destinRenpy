import random
from extremis.humanite import portrait
from extremis.constitution import temps

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
        self.typeRelation_ = RelationAmoureuse.SEDUCTION
