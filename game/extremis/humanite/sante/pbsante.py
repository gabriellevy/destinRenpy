import random

class PbSante:
    """
    Toutes les caracs liées au problèmmes de santé
    que ce soient des blessures, des handicaps ou des maladies
    physiques ou mentaux
    """

    C_JOURS_DHOPITAL = u"Jours d'hopital"

    def __init__(self):
        self.nom_ = "pas de nom de problème de santé, doit être overridé"

    def __repr__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        return "Pb de santé : {}".format(self.nom_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        return "{}".format(self.nom_)

    def GetGravite(self):
        """
        retourne la gravité de ce problème de santé
         0 => rhume

         9 => aveugle, cul de jatte
         10 => cancer, peste,
         """
        return 5

    def GetNbJoursConvalescence(self):
        """
        nombre de jours théoriques à passer à l'hopital (ou juste à reposer chez soi) après cette blessure pour bien récupérer
        """
        return 2

    def EffetAuxCaracs(self, situation):
        """
        ce qui arrive aux caracs du perso si il lui arrive cette maladie ou blessure
        """
        return

    def PeutEtrePrisALaNaissance(self):
        """
        Renvoie true si il s'agit d'une maladie qui peut être acquise dès la création du personnage (malformation ou maladie génétique de naissance)
        """
        return False

class Blessure(PbSante):

    def __repr__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        return "Blessure : {}".format(self.nom_)

class Maladie(PbSante):

    def __repr__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        return "Maladie : {}".format(self.nom_)

class OeilCreve(Blessure):

    NOM = u"Oeil crevé"

    def __init__(self):
        self.eTrait_ = OeilCreve.NOM

    def GetGravite(self):
        return 7

    def GetNbJoursConvalescence(self):
        return 30

class Peste(Maladie):

    NOM = u"Peste"

    def __init__(self):
        self.eTrait_ = Peste.NOM

    def GetGravite(self):
        return 10

    def GetNbJoursConvalescence(self):
        return 60

class CollectionBlessures:

    def __init__(self):
        self.lBlessures_ = dict()
        oeilCreve = OeilCreve()
        self.SetBlessure(OeilCreve.NOM, oeilCreve)

    def getBlessureAleatoire(self, minGravite = 0, maxGravite = 10):
        if minGravite == 0 and maxGravite == 10:
            return random.choice(list(self.lBlessures_.values()))
        # tmp
        return random.choice(list(self.lBlessures_.values()))

    def __getitem__(self, idBlessure):
        if not idBlessure in self.lBlessures_:
            self.CreerBlessure(idBlessure)
        return self.lBlessures_[idBlessure]

    def __setitem__(self, idBlessure, blessure):
        self.SetMaladie(idBlessure, blessure)

    def SetBlessure(self, idBlessure, blessure):
        self.lBlessures_[idBlessure] = blessure

    def __len__(self):
        return len(self.lMaladies_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        if len(self.lBlessures_) == 0:
            return "Aucune Blessure."
        str = u"Liste de toutes les blessures : "
        for blessure in self.lBlessures_:
            str = str + blessure + ","
        return str

class CollectionMaladies:

    def __init__(self):
        self.lMaladies_ = dict()
        peste = Peste()
        self.SetMaladie(Peste.NOM, peste)

    def getMaladieAleatoire(self, minGravite = 0, maxGravite = 10):
        if minGravite == 0 and maxGravite == 10:
            return random.choice(list(self.lMaladies_.values()))
        # tmp
        return random.choice(list(self.lMaladies_.values()))

    def __getitem__(self, idMetier):
        if not idMaladie in self.lMaladies_:
            self.CreerMaladie(idMaladie)
        return self.lMaladies_[idMaladie]

    def __setitem__(self, idMaladie, maladie):
        self.SetMaladie(idMaladie, maladie)

    def SetMaladie(self, idMaladie, maladie):
        self.lMaladies_[idMaladie] = maladie

    def __len__(self):
        return len(self.lMaladies_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        if len(self.lMaladies_) == 0:
            return "Aucun Maladie."
        str = u"Liste de toutes les maladies : "
        for maladie in self.lMaladies_:
            str = str + maladie + ","
        return str
