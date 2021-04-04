import random
from extremis.humanite import portrait
from extremis.constitution import temps
from extremis.humanite.amour import relationAmoureuse

class Pnj:

    C_PERE = u"Père"
    C_MERE = u"Mère"
    C_NOM = u"Nom"
    C_PRENOM = u"Prénom"

    def __init__(self, sexeMasculin, situation):
        self.sexeMasculin_ = sexeMasculin
        self.CreerNomNeutre(situation) # self.nom_
        self.CreerPrenomNeutre(situation) # self.prenom_
        self.nbJours_ = -1
        self.coterie_ = ""
        self.metier_ = ""
        self.traits_ = {} # dico contenant une liste de traits comme clés et leur valeur comme valeur
        self.portraitStr_ = ""
        self.relationAmoureuse_ = None

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
        self.portraitStr_ = portr.DeterminerPortraits(situation, ageNbAnnees, cotObj, metObj, self.traits_, self.sexeMasculin_)

    def CreerNomNeutre(self, situation):
        """
        à utiliser quand le personnage n'a pas de coterie ou une coterie qui n'a aps de nom spécifique :
        on crée un patronyme aléatoire à partir des noms de toutes els coteries
        """
        self.nom_ = ""
        while self.nom_ == "" or self.nom_ == None:
            cotObj = situation.collectionCoteries.getCoterieAleatoire(False)
            self.nom_ = cotObj.CreerNom(self.sexeMasculin_)

    def CreerPrenomNeutre(self, situation):
        self.prenom_ = ""
        while self.prenom_ == "" or self.prenom_ == None:
            cotObj = situation.collectionCoteries.getCoterieAleatoire(False)
            self.prenom_ = cotObj.CreerPrenom(self.sexeMasculin_)

def GenererPNJ(sexeMasculin, situation, ageJours):
    """
    Génère un PNJ aléatoire avec un ensemble de caracs
    Il pourra ensuite être stocké dans la situation
    """
    ageAnnees = ageJours/360
    pnj = Pnj(sexeMasculin, situation)
    cotObj = situation.collectionCoteries.getCoterieAleatoire(True)
    nomStr = cotObj.CreerNom(sexeMasculin)
    if nomStr != None:
        pnj.nom_ = nomStr
    prenomStr = cotObj.CreerPrenom(sexeMasculin)
    if prenomStr != None:
        pnj.prenom_ = prenomStr

    pnj.nbJours_ = ageJours
    pnj.coterie_ = cotObj.id_
    # métier :
    metierStr = ""
    if ageAnnees >= 20:
        # a un métier
        metier = situation.collectionMetiers.getMetierAleatoire(True, sexeMasculin, cotObj)
        metierStr = metier.nom_
    pnj.metier_ = metierStr
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
    situation.collectionPnjs[pnj.prenom_] = pnj

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
    pnj.relationAmoureuse_ = relationAmoureuse.RelationAmoureuse(interetPnjEnversJoueur, interetJoueurEnversPnj)
    return pnj
