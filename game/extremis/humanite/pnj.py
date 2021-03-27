import random
from extremis.humanite import portrait
from extremis.constitution import temps

class Pnj:

    C_PERE = u"Père"
    C_MERE = u"Mère"

    def __init__(self):
        self.nom_ = u"nom de pnj non défini"
        self.prenom_ = u"prénom de pnj non défini"
        self.nbJours_ = -1
        self.coterie_ = ""
        self.metier_ = ""
        self.sexeMasculin_ = True
        self.portraitStr_ = ""

    def __format__(self, format):
        # if(format == 'age'):
        #     return '23'
        return str(self)

    def __getattr__(self, nom):
        """Si Python ne trouve pas l'attribut nommé nom, il appelle
             cette méthode. On affiche une alerte"""
        print("Alerte ! Il n'y a pas d'attribut '{}' dans l'objet '{}' !".format(nom, self))

    def __str__(self):
        str = u"{} {}".format(self.prenom_, self.nom_)

        nbJoursVecus = self.nbJours_
        if isinstance(nbJoursVecus, int):
            nbAnnees = nbJoursVecus/365
            nbJoursPasses = nbJoursVecus%365
            nbMois = nbJoursPasses/30
            if nbMois > 0:
                str = u"{}\n{} ans, {} mois".format(str, nbAnnees, nbMois)
            else:
                str = u"{}\n{} ans".format(str, nbAnnees)

        if self.coterie_ != "":
            str = u"{}\n{}".format(str, self.coterie_)
        if self.metier_ != "":
            str = u"{}\n{}".format(str, self.metier_)
        return str

    def MajPortrait(self, situation):
        """
        à appeler de temps en temps (changement de boulot, passage de dizaines en âge etc, je sais pas trop
        """
        portr = portrait.Portrait()
        ageNbAnnees = self.nbJours_/365
        cotObj = None
        metObj = None
        if self.coterie_ != "":
            cotObj = situation.collectionCoteries[self.coterie_]
        if self.metier_ != "":
            metObj = situation.collectionMetiers[self.metier_]
        self.portraitStr_ = portr.DeterminerPortraits(situation, ageNbAnnees, cotObj, metObj, {}, self.sexeMasculin_)

def GenererPNJ(sexeMasculin, situation, ageJours):
    """
    Génère un PNJ aléatoire avec un ensemble de caracs
    Il pourra ensuite être stocké dans la situation
    """
    pnj = Pnj()
    cotObj = situation.collectionCoteries.getCoterieAleatoire(True)
    pnj.nom_ = cotObj.CreerNom(sexeMasculin)
    pnj.prenom_ = cotObj.CreerPrenom(sexeMasculin)
    pnj.nbJours_ = ageJours
    pnj.coterie_ = cotObj.id_
    pnj.metier_ = situation.collectionMetiers.getMetierAleatoire().nom_
    pnj.sexeMasculin_ = sexeMasculin
    pnj.portraitStr_ = ""
    pnj.MajPortrait(situation)
    return pnj

def GenererPNJPapa(situation):
    nbJoursVecusPerso = temps.Date(situation.caracs_[temps.Date.DATE]).nbJours_ - temps.Date(situation.caracs_[temps.Date.DATE_NAISSANCE]).nbJours_
    ageJours = (30 + random.randint(0, 35)) * 12 *30 # âge 29 minimum (14 + 15 de l'âge du perso joué)
    return GenererPNJ(True, situation, ageJours)

def GenererPNJMaman(situation):
    nbJoursVecusPerso = temps.Date(situation.caracs_[temps.Date.DATE]).nbJours_ - temps.Date(situation.caracs_[temps.Date.DATE_NAISSANCE]).nbJours_
    ageJours = (30 + random.randint(0, 25)) * 12 *30 # âge 29 minimum (14 + 15 de l'âge du perso joué)
    return GenererPNJ(False, situation, ageJours)

def GenererRelationAmoureuse(situation):
    nbJoursVecusPerso = temps.Date(situation.caracs_[temps.Date.DATE]).nbJours_ - temps.Date(situation.caracs_[temps.Date.DATE_NAISSANCE]).nbJours_
    ageJours = nbJoursVecusPerso + (random.randint(0, 15) - random.randint(0, 15)) * 12 *30 # âge 29 minimum (14 + 15 de l'âge du perso joué)
    return GenererPNJ(False, situation, ageJours)
