import random
from extremis.humanite import portrait

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
        cotObj = None
        metObj = None
        if self.coterie_ != "":
            cotObj = situation.collectionCoteries[self.coterie_]
        if self.metier_ != "":
            metObj = situation.collectionMetiers[self.metier_]
        self.portraitStr_ = portr.DeterminerPortraits(situation, self.nbJours_, cotObj, metObj, [], self.sexeMasculin_)

def GenererPNJ(sexeMasculin, situation):
    """

    """
    pnj = Pnj()
    pnj.nom_ = u"Deharbe"
    pnj.prenom_ = u"Mathieu"
    pnj.nbJours_ = 20*12*30
    pnj.coterie_ = ""
    pnj.metier_ = u"Médecin"
    pnj.sexeMasculin_ = sexeMasculin
    pnj.portraitStr_ = ""
    pnj.MajPortrait(situation)
    return pnj

def GenererPNJPapa(situation):
    return GenererPNJ(True, situation)

def GenererPNJMaman(situation):
    return GenererPNJ(False, situation)
