import random

class Date:
    """
    date au format plus ou moins calendrier révolutionnaire
    """

    DATE = u"Date" # date actuelle depuis le début du calendrier (en jours)
    DATE_ANNEES = u"Date en années" # date actuelle depuis le début du calendrier (en années)
    DATE_NAISSANCE = u"Date de naissance" # date de naissance du perso depuis le début du calendrier (en jours)
    MOIS_ACTUEL = u"Mois" # numéro de mois actuel (de 1 à 12)
    AGE_ANNEES = u"Age" # age du perso (en années)

    HIVER = "Hiver"
    ETE = "Été"
    PRINTEMPS = "Printemps"
    AUTOMNE = "Automne"

    NB_JOURS_PAR_MOIS_GREG = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    NOMS_MOIS_GREG = [u"janvier", u"février", u"mars", u"avril", u"mai", u"juin", u"juillet", u"août", u"septembre", u"octobre", u"novembre", u"décembre"]

    def __init__(self, nbJours = None):
        if nbJours is None:
            self.nbJours_ = 40000 + random.randint(0, 40000) # nombre de jours semi aléatoire pour destin extermis
        else:
            self.nbJours_ = nbJours # nombre de jours depuis
        self.numJourGregorien = -1
        self.numMoisGregorien = -1
        self.CalculerJourEtMoisGregorien()

    def NbJours(self):
        return self.nbJours_

    def AjouterJours(self, nbJours):
        self.nbJours_ = self.nbJours_ + nbJours

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

    def GetNumMois(self):
        return self.numMoisGregorien

    def GetSaison(self):
        numMois = self.GetNumMois()
        if numMois == 0 or numMois == 1 or numMois == 11:
            return Date.HIVER
        if numMois == 5 or numMois == 6 or numMois == 7:
            return Date.ETE
        if numMois == 2 or numMois == 3 or numMois == 4:
            return Date.PRINTEMPS
        if numMois == 8 or numMois == 9 or numMois == 10:
            return Date.AUTOMNE

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

    def GetNbJoursDepuisDebutAnnee(self):
        return self.nbJours_ % 365 + 1

    def CalculerJourEtMoisGregorien(self):
        numJour = self.GetNbJoursDepuisDebutAnnee()
        index = 0
        while index < 12:
            if numJour <= Date.NB_JOURS_PAR_MOIS_GREG[index]:
                self.numJourGregorien = numJour
                self.numMoisGregorien = index + 1
                return
            numJour = numJour - Date.NB_JOURS_PAR_MOIS_GREG[index]
            index = index + 1

    def GetStrMoisGregorien(self):
        return Date.NOMS_MOIS_GREG[self.numMoisGregorien - 1]

    def formatConstitution(self):
        return u"{} {} {} {}".format(self.GetStrJourSemaine(), self.GetNbJourDuMois(), self.GetStrMois(), self.GetNbAnnees())

    def formatGregorien(self):
        self.CalculerJourEtMoisGregorien()
        return u"{} {} {}".format(self.numJourGregorien, self.GetStrMoisGregorien(), self.GetNbAnnees())

    def formatGregorienAvantJC(self):
        self.CalculerJourEtMoisGregorien()
        return u"{} {} {}".format(self.numJourGregorien, self.GetStrMoisGregorien(), self.GetNbAnnees())

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        return u"{} {} {} {}".format(self.GetStrJourSemaine(), self.GetNbJourDuMois(), self.GetStrMois(), self.GetNbAnnees())
