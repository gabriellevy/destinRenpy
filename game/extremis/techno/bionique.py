import random
from abs.humanite.sante import pbsante

class Bionique:
    """
    chaque classe héritant de celle ci concerne un bionique et contient tous ses effets et textes propres
    """

    def __init__(self):
        self.nom_ = u"pas de nom de bionique, doit être overridé"

    def __repr__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        return u"Bionique : {}".format(self.nom_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        return u"{}".format(self.nom_)

    def GetPrix(self):
        """
        prix en crédit
         """
        return 2000

    def GetNbJoursConvalescence(self):
        """
        nombre de jours théoriques à passer à l'hopital (ou juste à reposer chez soi) pour bien récupérer de l'opération
        """
        return 15

    def EffetAuxCaracs(self, situation):
        """
        ce qui arrive aux caracs du perso si on lui pose ce bionique
        """
        return

    def GetDescriptionRecu(self):
        """
        texte affiché quand le personnage se fait poser ce bionique
        """
        return u"GetDescriptionRecu pas faite pour {}".format(self.nom_)

class BioniqueLongevite(Bionique):
    """
    augmente l'espérance de vie
    niveau va de 1 à 10
    """

    NOM = u"Bionique de longévité"

    def __init__(self):
        self.nom_ = BioniqueLongevite.NOM

class OeilBionique(Bionique):
    NOM = u"Oeil bionique"

    def __init__(self):
        self.nom_ = OeilBionique.NOM

class JambeBionique(Bionique):
    NOM = u"Jambe bionique"

    def __init__(self):
        self.nom_ = JambeBionique.NOM

class BrasBionique(Bionique):
    NOM = u"Bras Bionique"

    def __init__(self):
        self.nom_ = BrasBionique.NOM

class StimulantReflexe(Bionique):
    NOM = u"Stimulant de réflexe"

    def __init__(self):
        self.nom_ = StimulantReflexe.NOM

class CollectionBioniques:

    def __init__(self):
        self.lBioniques_ = dict()

        bioniqueLongevite = BioniqueLongevite()
        self.SetBionique(BioniqueLongevite.NOM, bioniqueLongevite)

        oeilBionique = OeilBionique()
        self.SetBionique(OeilBionique.NOM, oeilBionique)

        jambeBionique = JambeBionique()
        self.SetBionique(JambeBionique.NOM, jambeBionique)

        brasBionique = BrasBionique()
        self.SetBionique(BrasBionique.NOM, brasBionique)

        stimulantReflexe = StimulantReflexe()
        self.SetBionique(StimulantReflexe.NOM, stimulantReflexe)

    def getBioniqueAleatoire(self):
        return random.choice(list(self.lBioniques_.values()))

    def PoserBioniqueAleatoire(self, situation):
        """
        inclue les jours de convalescence et le message
        """
        bioniqueObj = self.getBioniqueAleatoire()
        if bioniqueObj is not None:
            nbConvalescence = situation.GetValCaracInt(pbsante.PbSante.C_JOURS_DHOPITAL)
            situation[pbsante.PbSante.C_JOURS_DHOPITAL] = nbConvalescence + bioniqueObj.GetNbJoursConvalescence()
            situation[bioniqueObj.nom_] = 1
        return bioniqueObj

    def __getitem__(self, idBionique):
        if not idBionique in self.lBioniques_:
            self.CreerBionique(idBionique)
        return self.lBioniques_[idBionique]

    def __setitem__(self, idBionique, bionique):
        self.SetBionique(idBionique, bionique)

    def SetBionique (self, idBionique, bionique):
        self.lBioniques_[idBionique] = bionique

    def __len__(self):
        return len(self.lBioniques_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        if len(self.lBioniques_) == 0:
            return "Aucun Bionique."
        str = u"Liste de tous les bioniques : "
        for bionique in self.lBioniques_:
            str = str + bionique + ","
        return str
