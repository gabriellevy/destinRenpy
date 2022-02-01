import random
from abs.humanite import portrait
from abs.univers import temps
from abs.humanite.amour import relationAmoureuse
from abs.humanite import identite

class Pnj:

    C_PERE = u"Père"
    C_MERE = u"Mère"

    def __init__(self, sexeMasculin, situation):
        self.sexeMasculin_ = sexeMasculin
        self.CreerNomNeutre(situation) # self.nom_
        self.nbJours_ = -1
        self.traits_ = {} # dico contenant une liste de traits comme clés et leur valeur comme valeur
        self.portraitStr_ = ""
        self.relationAmoureuse_ = None
        self.vivant_ = True

    def Tuer(self):
        self.vivant_ = False

    def __format__(self, format):
        # if(format == 'age'):
        #     return '23'
        # return u"PNJ({})".format(self.nom_)
        return self.__str__()

    def __getattr__(self, nom):
        """Si Python ne trouve pas l'attribut nommé nom, il appelle
             cette méthode. On affiche une alerte"""
        print("Alerte ! Il n'y a pas d'attribut '{}' dans l'objet '{}' !".format(nom, self.nom_))

    def __str__(self):
        str = u"{}".format(self.nom_)

        if self.vivant_:
            nbJoursVecus = self.nbJours_
            if isinstance(nbJoursVecus, int):
                nbAnnees = nbJoursVecus/365
                nbJoursPasses = nbJoursVecus%365
                nbMois = nbJoursPasses/30
                if nbMois > 0:
                    str = u"{}\n{} ans, {} mois".format(str, nbAnnees, nbMois)
                else:
                    str = u"{}\n{} ans".format(str, nbAnnees)
        else:
            if self.sexeMasculin_:
                str = u"{}\nDécédé".format(str)
            else:
                str = u"{}\nDécédée".format(str)

        return str

    def MajPortrait(self, situation):
        """
        à appeler de temps en temps (changement de boulot, passage de dizaines en âge etc, je sais pas trop
        """
        portr = portrait.Portrait()
        ageNbAnnees = self.nbJours_/365
        cotObj = None
        metObj = None
        self.portraitStr_ = portr.DeterminerPortraits(situation, ageNbAnnees)

    def CreerNomNeutre(self, situation):
        """
        TODO : adapter selon l'univers : ici ajouter les noms Francs
        """
        self.nom_ = "Sigebert (tmp)"

def GenererPNJ(sexeMasculin, situation, ageJours):
    """
    Génère un PNJ aléatoire avec un ensemble de caracs
    Il pourra ensuite être stocké dans la situation
    """
    ageAnnees = ageJours/360
    pnj = Pnj(sexeMasculin, situation)

    pnj.nbJours_ = ageJours
    pnj.sexeMasculin_ = sexeMasculin
    pnj.portraitStr_ = ""
    # génération des traits :
    nbTraits = 2 + random.randint(0,5)
    m_Traits = []
    while nbTraits > 0:
        trait = situation.collectionTraits.getTraitAleatoire()
        if trait.PeutEtrePrisALaNaissance():
            pnj.traits_[trait.eTrait_] = trait.GetValeurALaNaissance()
            nbTraits = nbTraits - 1

    pnj.MajPortrait(situation)

    # ajouter ce nouveau pnj à la liste des pnjs de l'histoire
    situation.collectionPnjs[pnj.nom_] = pnj

    return pnj

def GenererPNJPapa(situation):
    nbJoursVecusPerso = temps.Date(situation.caracs_[temps.Date.DATE]).nbJours_ - temps.Date(situation.caracs_[temps.Date.DATE_NAISSANCE]).nbJours_
    ageJours = (30 + random.randint(0, 35)) * 12 *30 # âge 29 minimum (14 + 15 de l'âge du perso joué)
    return GenererPNJ(True, situation, ageJours)

def GenererPNJMaman(situation):
    nbJoursVecusPerso = temps.Date(situation.caracs_[temps.Date.DATE]).nbJours_ - temps.Date(situation.caracs_[temps.Date.DATE_NAISSANCE]).nbJours_
    ageJours = (30 + random.randint(0, 25)) * 12 *30 # âge 29 minimum (14 + 15 de l'âge du perso joué)
    pnj = GenererPNJ(False, situation, ageJours)
    return pnj

def GenererRelationAmoureuse(situation):
    nbJoursVecusPerso = temps.Date(situation.caracs_[temps.Date.DATE]).nbJours_ - temps.Date(situation.caracs_[temps.Date.DATE_NAISSANCE]).nbJours_
    ageAnnees = nbJoursVecusPerso/360 + (random.randint(0, 13) - random.randint(0, 15))
    if ageAnnees < 15:
        ageAnnees = 15
    ageJours = ageAnnees * 12 *30
    pnj = GenererPNJ(False, situation, ageJours)
    # calculer les niveaux d'intérêt des persos l'un envers l'autre
    interetPnjEnversJoueur = relationAmoureuse.CalculerAmabiliteHommePremierContact(situation.GetDicoTraits())
    interetJoueurEnversPnj = relationAmoureuse.CalculerAmabiliteFemmePremierContact(pnj.traits_)
    pnj.relationAmoureuse_ = relationAmoureuse.RelA(interetPnjEnversJoueur, interetJoueurEnversPnj)
    return pnj
