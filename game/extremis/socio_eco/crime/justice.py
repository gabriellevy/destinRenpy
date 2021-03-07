import random
from extremis.socio_eco.crime import crime

class Justice:
    """

    """

    C_LIBERTE = u"Liberté"
    C_MOIS_PRISON = u"Mois de prison restants";

    # valeurs de C_LIBERTE :
    CAPTURE_POLICE = u"Capturé par la police";
    PRISON = u"En prison";

    def __init__(self):
        """
        
        """
        self.nom_ = "justice, nom à overrider ?"
