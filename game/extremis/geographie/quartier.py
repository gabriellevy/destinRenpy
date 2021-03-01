import random

class Quartier:
    """
    quartier de Paris
    sert à identifier où se trouve le perso, où il travaille et des événements liés
    """
    C_QUARTIER = "Quartier"

    def __init__(self):
        self.nom_ = u"nom à overrider"
        self.imageDeFond_ = u"adresse image de fond à overrider"

    def GetDescription(self, situation):
        return "Valeur de description non trouvée pour : Quartier : {}".format(self.nom_)

    def __repr__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        return "Quartier : {}".format(self.nom_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        return "{}".format(self.nom_)

class SaintDenis(Quartier):
    """
    quartier des templiers
    """

    NOM = u"Saint Denis"

    def __init__(self):
        self.nom_ = SaintDenis.NOM
        self.imageDeFond_ = u"bg saint_denis"

class CollectionQuartiers:

    def __init__(self):
        self.lQuartiers_ = dict()
        saintDenis = SaintDenis()
        self.SetQuartier(SaintDenis.NOM, saintDenis)

    def getQuartierAleatoire(self):
        return random.choice(list(self.lQuartiers_.values()))

    def __getitem__(self, idQuartier):
        if not idQuartier in self.lQuartiers_:
            self.CreerQuartier(idQuartier)
        return self.lQuartiers_[idQuartier]

    def __setitem__(self, idQuartier, quartier):
        self.SetQuartier(idQuartier, quartier)

    def SetQuartier(self, idQuartier, quartier):
        # si la carac n'existe pas encore, la créer
        if not idQuartier in self.lQuartiers_:
            self.CreerQuartier(idQuartier)

        self.lQuartiers_[idQuartier] = quartier

    def CreerQuartier(self, idQuartier):
        quartier = Quartier()
        quartier.nom_ = idQuartier
        self.lQuartiers_[idQuartier] = quartier

    def __len__(self):
        return len(self.lQuartiers_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        if len(self.lQuartiers_) == 0:
            return "Aucun quartier."
        str = u"Liste de tous les quartiers : "
        for quartier in self.lQuartiers_:
            str = str + quartier + ","
        return str
