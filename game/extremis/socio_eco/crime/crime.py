import random

class Crime:
    """

    """

    C_CRIMINEL = u"Est criminel";
    C_LIBERTE = u"Liberté"
    C_GANG = u"Gang";
    C_MOIS_PRISON = u"Mois de prison restants";

    # valeurs de C_CRIMINEL : ("" signifie innocent). Note : être jugé innocent même si n est coupable remet en ""
    DELINQUANT = u"Délinquant";
    CRIMINEL = u"Criminel"; # violeur, assassin, braqueur...
    # valeurs de C_LIBERTE :
    CAPTURE_POLICE = u"Capturé par la police";
    PRISON = u"En prison";

    def __init__(self):
        """
        définition plus précise d'un crime (années de prison risquées en le commettant ?
        caracs qui peuvent pousser à le commettre ??
        """
        self.nom_ = "crime, nom à overrider"

class Voleur(Crime):
    """
    La valeur associée à la carac est la gravité du crime:
     - 1 : petit voleur qui pioche dans les magasins
     - 5 : cambrioleur professionnel
     - 10 : braqueur de banque, de musée...
     """

    NOM = u"Voleur"

    def __init__(self):
        self.nom_ = Voleur.NOM

    def GetDescription(self, situation):
        val = situation[self.nom_]
        if val == "":
            val = 0
            situation[self.nom_] = val
        if not isinstance(val, int):
            assert "Ce type de crime n'a pas comme valeur un int. Crime : {}. Valeur : {}".format(self.nom_, val)

        if val > 8:
            return u"Braqueur professionel"
        elif val > 4:
            return u"Cambrioleur occasionnel"
        elif val > 0:
            return u"Petit voleur occasionnel"
        else:
            return ""

class Violeur(Crime):
    """
    La valeur associée à la carac est la gravité du crime:
     - 1 : tripotteur
     - 2 :  harceleur
     - 5 : violeur
     - 10 : violeur compulsif ultraviolent
     """

    NOM = u"Voleur"

    def __init__(self):
        self.nom_ = Violeur.NOM

    def GetDescription(self, situation):
        val = situation[self.nom_]
        if val == "":
            val = 0
            situation[self.nom_] = val
        if not isinstance(val, int):
            assert "Ce type de crime n'a pas comme valeur un int. Crime : {}. Valeur : {}".format(self.nom_, val)

        if val > 8:
            return u"Violeur en série"
        elif val > 4:
            return u"Violeur"
        elif val > 0:
            return u"Délinquant sexuel"
        else:
            return ""

class CriminelViolent(Crime):
    """
    La valeur associée à la carac est la gravité du crime:
     - 1 : se bat dans les bars
     - 5 : homme de main d'un gang
     - 10 : assassin professionnel
     """

    NOM = u"Criminel violent"

    def __init__(self):
        self.nom_ = CriminelViolent.NOM

    def GetDescription(self, situation):
        val = situation[self.nom_]
        if val == "":
            val = 0
            situation[self.nom_] = val
        if not isinstance(val, int):
            assert "Ce type de crime n'a pas comme valeur un int. Crime : {}. Valeur : {}".format(self.nom_, val)

        if val > 8:
            return u"Assassin professionnel"
        elif val > 4:
            return u"Homme de main"
        elif val > 0:
            return u"Bagarreur des rues"
        else:
            return ""


class CollectionCrimes:

    def __init__(self):
        self.lCrimes_ = dict()

        voleur = Voleur()
        self.SetCrime(Voleur.NOM, voleur)

        violeur = Violeur()
        self.SetCrime(Violeur.NOM, violeur)

        criminelViolent = CriminelViolent()
        self.SetCrime(CriminelViolent.NOM, criminelViolent)

    def getCrimeAleatoire(self):
        return random.choice(list(self.lCrimes_.values()))

    def __getitem__(self, idCrime):
        if not idCrime in self.lCrimes_:
            self.CreerCrime(idCrime)
        return self.lCrimes_[idCrime]

    def __setitem__(self, idCrime, crime):
        self.SetCrime(idCrime, crime)

    def SetCrime(self, idCrime, crime):
        # si la carac n'existe pas encore, la créer
        #if not idCrime in self.lCrimes_:
        #    self.CreerCrime(idCrime)

        self.lCrimes_[idCrime] = crime

    def CreerCrime(self, idCrime):
        trait = Crime(idCrime)
        self.lCrimes_[idCrime] = crime

    def __len__(self):
        return len(self.lCrimes_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        if len(self.lCrimes_) == 0:
            return "Aucun trait."
        str = u"Liste de tous les traits : "
        for trait in self.lCrimes_:
            str = str + trait + ","
        return str
