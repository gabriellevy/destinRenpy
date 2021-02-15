from extremis.coteries import coterie
from extremis.socio_eco.metiers import metier
from extremis.humanite import trait

class Templiers(coterie.Coterie):

    NOM = u"Templiers"

    def __init__(self):
        self.nom_ = Templiers.NOM

    def getLabelUniversite(self):
        return "univTempliers"

    def GetCaracsCompatibles(self):
        """
        si le perso a ces caracs il a plus de chances de vouloir rejoindre cette coterie
        """
        return [ \
            trait.Spiritualite.NOM, \
            trait.Honorabilite.NOM, \
            trait.Violence.NOM, \
            trait.Ascetisme.NOM, \
            trait.Altruisme.NOM, \
            metier.Pretre.NOM, \
            metier.TueurDeMonstres.NOM, \
            trait.Franchise.NOM, \
            metier.Guerrier.NOM, \
            metier.Chevalier.NOM, \
            metier.Policier.NOM, \
            metier.Vigile.NOM, \
            metier.Dessinateur.NOM, \
            metier.Bibliothecaire.NOM, \
            metier.GardeDuCorps.NOM \
            ]

    def GetCaracsIncompatibles(self):
        """
        si le perso a ces caracs il a plus de chances de ne pas vouloir rejoindre cette coterie
        """
        return [ \
            trait.Cupidite.NOM, \
            trait.Opportunisme.NOM, \
            trait.Sexualite.NOM \
            ]

    # condition : être chrétien
