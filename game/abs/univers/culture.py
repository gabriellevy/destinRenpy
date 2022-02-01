import random
# from extremis.geographie import quartier
from abs.humanite import identite

class Culture:
    """
    classe de base de toutes les cultures
    """

    C_CULTURE = "Culture"

    def __init__(self):
        self.nom_ = "pas de nom, à overrider"
        self.id_ = "pas de id, à overrider"
        # self.quartier_ = "pas de quartier, à overrider"

    def __repr__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        return "Culture : {}".format(self.nom_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        return "{}".format(self.nom_)

    def AffichageSituationDansCoterie(self, situation):
        """
        affiche le gentilé de la coterie mais aussi d'éventuelles informations supplémentaires liées à la coterie
        """
        str = self.GetGentile(True)
        return str

    def GetGentile(self, masculin):
        if masculin:
            return "pas de gentilé masculin, à overrider !"
        else:
            return "pas de gentilé féminin, à overrider !"

    def GetPoidsDemo(self):
        """
        à quel point cette coterie est nombreuse dans la population
        1.0 = normal
        0.1 = 10 fois moins que la moyenne
        """
        return 1.0

    def GenererPortraits(self, age, masculin, metObj, portraits, valeursTraits):
        """
        ajoute des portraits correspondants aux caracs en paramtre (et à la coterie courante)
        A OVERRIDER
        """
        return portraits

    def GetMusique(self):
        return ""

    def CreerNom(self, masculin):
        """
        génère un patronyme correspondant à la coterie en question
        None signifie qu'il n'y a pas de prénom spécifique à cette coterie
        """
        return None

    def CreerPrenom(self, masculin):
        """
        génère un patronyme correspondant à la coterie en question
        None signifie qu'il n'y a pas de nom spécifique à cette coterie
        """
        return None
