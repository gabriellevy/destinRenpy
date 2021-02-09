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
        self.nom_ = OeilCreve.NOM

    def GetGravite(self):
        return 7

    def GetNbJoursConvalescence(self):
        return 30

class DoigtArrache(Blessure):

    NOM = u"Doigt arraché"

    def __init__(self):
        self.nom_ = DoigtArrache.NOM

    def GetGravite(self):
        return 5

    def GetNbJoursConvalescence(self):
        return 12

class CicatriceVisage(Blessure):

    NOM = u"Cicatrice au visage"

    def __init__(self):
        self.nom_ = CicatriceVisage.NOM

    def GetGravite(self):
        return 4

    def GetNbJoursConvalescence(self):
        return 12

class Defigure(Blessure):

    NOM = u"Defiguré"

    def __init__(self):
        self.nom_ = Defigure.NOM

    def GetGravite(self):
        return 8

    def GetNbJoursConvalescence(self):
        return 40

class JambeAmputee(Blessure):

    NOM = u"Jambe amputée"

    def __init__(self):
        self.nom_ = JambeAmputee.NOM

    def GetGravite(self):
        return 8

    def GetNbJoursConvalescence(self):
        return 40

class BrasAmpute(Blessure):

    NOM = u"Bras amputé"

    def __init__(self):
        self.nom_ = BrasAmpute.NOM

    def GetGravite(self):
        return 8

    def GetNbJoursConvalescence(self):
        return 40

class TraumatismeCranien(Blessure):

    NOM = u"Traumatisme crânien"

    def __init__(self):
        self.nom_ = TraumatismeCranien.NOM

    def GetGravite(self):
        return 8

    def GetNbJoursConvalescence(self):
        return 30

class HemoragieInterne(Blessure):

    NOM = u"Hemoragie Interne"

    def __init__(self):
        self.nom_ = HemoragieInterne.NOM

    def GetGravite(self):
        return 8

    def GetNbJoursConvalescence(self):
        return 40

class OreilleCoupee(Blessure):

    NOM = u"Oreille coupée"

    def __init__(self):
        self.nom_ = OreilleCoupee.NOM

    def GetGravite(self):
        return 5

    def GetNbJoursConvalescence(self):
        return 25

class CollectionBlessures:

    def __init__(self):
        self.lBlessures_ = dict()

        oreilleCoupee = OreilleCoupee()
        self.SetBlessure(OreilleCoupee.NOM, oreilleCoupee)

        hemoragieInterne = HemoragieInterne()
        self.SetBlessure(HemoragieInterne.NOM, hemoragieInterne)

        oeilCreve = OeilCreve()
        self.SetBlessure(OeilCreve.NOM, oeilCreve)

        traumatismeCranien = TraumatismeCranien()
        self.SetBlessure(TraumatismeCranien.NOM, traumatismeCranien)

        brasAmpute = BrasAmpute()
        self.SetBlessure(BrasAmpute.NOM, brasAmpute)

        doigtArrache = DoigtArrache()
        self.SetBlessure(DoigtArrache.NOM, doigtArrache)

        cicatriceVisage = CicatriceVisage()
        self.SetBlessure(CicatriceVisage.NOM, cicatriceVisage)

        defigure = Defigure()
        self.SetBlessure(Defigure.NOM, defigure)

        jambeAmputee = JambeAmputee()
        self.SetBlessure(JambeAmputee.NOM, jambeAmputee)

    def getBlessureAleatoire(self, minGravite = 0, maxGravite = 10):
        if minGravite == 0 and maxGravite == 10:
            return random.choice(list(self.lBlessures_.values()))

        tabBlessuresOk = list()
        for blessure in list(self.lBlessures_.values()):
            if blessure.GetGravite() >= minGravite and  blessure.GetGravite() <= maxGravite:
                tabBlessuresOk.append(blessure)

        if len(tabBlessuresOk) == 0:
            return "aucune blessure entre gravité {} et {}".format(minGravite, maxGravite)

        return random.choice(tabBlessuresOk)

    def InfligerBlessureAleatoire(self, situation, minGravite = 0, maxGravite = 10):
        blessure = self.getBlessureAleatoire(minGravite, maxGravite)
        if blessure != "":
            situation[PbSante.C_JOURS_DHOPITAL] = blessure.GetNbJoursConvalescence()
            situation[blessure.nom_] = 1
        return blessure

    def __getitem__(self, idBlessure):
        if not idBlessure in self.lBlessures_:
            self.CreerBlessure(idBlessure)
        return self.lBlessures_[idBlessure]

    def __setitem__(self, idBlessure, blessure):
        self.SetMaladie(idBlessure, blessure)

    def SetBlessure (self, idBlessure, blessure):
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


class Peste(Maladie):

    NOM = u"Peste"

    def __init__(self):
        self.nom_ = Peste.NOM

    def GetGravite(self):
        return 10

    def GetNbJoursConvalescence(self):
        return 60

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
