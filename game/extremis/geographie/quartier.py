import random

class Quartier:
    """
    quartier de Paris principal du perso
    sert à identifier où se trouve le perso, où il travaille et des événements liés
    """
    C_QUARTIER = "Quartier"

    def __init__(self):
        self.nom_ = u"nom à overrider"
        self.imageDeFond_ = u"adresse image de fond à overrider"
        self.poidsDemographique_ = 1 # poids par rapport aux autres quartiers de Paris (1 étant le poids "moyen"

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
        self.poidsDemographique_ = 1

class SaintGermainEnLaye(Quartier):
    """
    quartier des elfes
    """

    NOM = u"Saint Germain en Laye"

    def __init__(self):
        self.nom_ = SaintGermainEnLaye.NOM
        self.imageDeFond_ = u"bg saint_germain_en_laye"
        self.poidsDemographique_ = 1

class LaDefense(Quartier):
    """
    quartier des transhumanistes
    """

    NOM = u"La Défense"

    def __init__(self):
        self.nom_ = LaDefense.NOM
        self.imageDeFond_ = u"bg la_defense"
        self.poidsDemographique_ = 1

class Poissy(Quartier):
    """
    quartier des orks
    """

    NOM = u"Poissy"

    def __init__(self):
        self.nom_ = Poissy.NOM
        self.imageDeFond_ = u"bg poissy"
        self.poidsDemographique_ = 1

class SaintMalo(Quartier):
    """
    quartier des conquistadors
    """

    NOM = u"Saint Malo"

    def __init__(self):
        self.nom_ = SaintMalo.NOM
        self.imageDeFond_ = u"bg saint_malo"
        self.poidsDemographique_ = 1

class CollectionQuartiers:

    def __init__(self):
        self.lQuartiers_ = dict()

        saintDenis = SaintDenis()
        self.SetQuartier(SaintDenis.NOM, saintDenis)

        laDefense = LaDefense()
        self.SetQuartier(LaDefense.NOM, laDefense)

        saintGermainEnLaye = SaintGermainEnLaye()
        self.SetQuartier(SaintGermainEnLaye.NOM, saintGermainEnLaye)

        saintMalo = SaintMalo()
        self.SetQuartier(SaintMalo.NOM, saintMalo)

        poissy = Poissy()
        self.SetQuartier(Poissy.NOM, poissy)

    def getQuartierAleatoire(self, selonPoidsDemo):
        if selonPoidsDemo:
            poidsTotal = 0
            for quartierObj in self.lQuartiers_.values():
                poidsTotal = poidsTotal + quartierObj.poidsDemographique_

            randVal = random.uniform(0, poidsTotal)

            for quartierObj in self.lQuartiers_.values():
                if randVal <= quartierObj.poidsDemographique_:
                    return quartierObj
                else:
                    randVal = randVal - quartierObj.poidsDemographique_

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
