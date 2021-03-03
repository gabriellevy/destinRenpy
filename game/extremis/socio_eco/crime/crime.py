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
    CRIMINEL = u"Criminel";
    # valeurs de C_LIBERTE :
    CAPTURE_POLICE = u"Capturé par la police";
    PRISON = u"En prison";

    def __init__(self):
        """
        définition plus précise d'un crime (années de prison risquées en le commettant ?
        caracs qui peuvent pousser à le commettre ??
        """
        self.nom_ = "crime, nom à overrider"
