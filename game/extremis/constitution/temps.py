import random

class Date:
    """
    date au format plus ou moins calendrier révolutionnaire
    """

    def __init__(self, nbJours = None):
        if nbJours is None:
            self.nbJours_ = 40000 + random.randint(0, 40000) # nombre de jours semi aléatoire pour destin extermis
        else:
            self.nbJours_ = nbJours # nombre de jours depuis

    def AjouterJours(self, nbJours):
        self.nbJours_ = self.nbJours_ + nbJours

    def TourSuivant(self):
        """
        Passage au "tour" suivant dans un destin extermis c'est à dire grosso modo à un mois un peu randomisé
        """
        nbJours = 20 + random.randint(0, 20)
        self.AjouterJours(nbJours)

    def GetStrJourSemaine(self):
        val = self.nbJours_%10 + 1 # calculer selon nbJours
        switcheurJour = {
            1: u"Primidi",
            2: u"Duodi",
            3: u"Tridi",
            4: u"Quartidi",
            5: u"Quintidi",
            6: u"Sextidi",
            7: u"Septidi",
            8: u"Octidi",
            9: u"Nonidi ",
            10: u"Décadi"
        }
        return u"{}".format(switcheurJour.get(val, u"Jour de semaine introuvable : {} !".format(val)))

    def GetNbAnnees(self):
        return self.nbJours_/365

    def GetNbJourAnnees(self):
        """
        numéro du jour dans l'année de 1 à 365
        """
        return self.nbJours_%365 + 1

    def GetNbJourDuMois(self):
        nbAnnees = self.GetNbAnnees()
        nbJoursARetirer = nbAnnees * 5 # je pars sur toujours 365 jours par and parce que bon voilà
        nbJoursModifies = self.nbJours_ - nbJoursARetirer
        return nbJoursModifies%30 + 1

    def GetStrMois(self):
        nbJourAnnees = self.GetNbJourAnnees()
        numMois = nbJourAnnees/30 + 1
        switcheurMois = {
            1: u"Vendémiaire",
            2: u"Brumaire",
            3: u"Frimaire",
            4: u"Nivôse",
            5: u"Pluviôse",
            6: u"Ventôse",
            7: u"Germinal",
            8: u"Floréal",
            9: u"Prairial",
            10: u"Messidor",
            11: u"Thermidor",
            12: u"Fructidor",
            13: u"Jours intercalaires"
        }
        return u"{}".format(switcheurMois.get(numMois, u"Mois introuvable : {} !".format(numMois)))

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        return u"{} {} {} {}".format(self.GetStrJourSemaine(), self.GetNbJourDuMois(), self.GetStrMois(), self.GetNbAnnees())
