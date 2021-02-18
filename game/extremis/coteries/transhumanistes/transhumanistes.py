from extremis.coteries import coterie
from extremis.socio_eco.metiers import metier
from extremis.humanite import trait

class Transhumanistes(coterie.Coterie):

    NOM = u"Transhumanistes"

    def __init__(self):
        self.nom_ = Transhumanistes.NOM

    def getLabelUniversite(self):
        return "univTranshumanistes"

    def GetTraitsCompatibles(self):
        """
        si le perso a ces caracs il a plus de chances de vouloir rejoindre cette coterie
        """
        return [ \
            trait.Cupidite.NOM, \
            trait.Pragmatisme.NOM, \
            trait.Individualisme.NOM, \
            trait.Opportunisme.NOM, \
            trait.Ambition.NOM, \
            trait.Industrie.NOM, \
            # classe sociale élevée
            ]

    def GetMetiersCompatibles(self):
        """
        si le perso a des compétences dans ces métiers il a plus de chances de vouloir rejoindre cette coterie où ils sont souvent pratiqués
        """
        return [ \
            metier.Marchand.NOM, \
            metier.Informaticien.NOM, \
            metier.Cyberneticien.NOM, \
            metier.Geneticien.NOM, \
            metier.Commercial.NOM \
            ]

    def GetTraitsIncompatibles(self):
        """
        si le perso a ces caracs il a plus de chances de ne pas vouloir rejoindre cette coterie
        """
        return [ \
            trait.Spiritualite.NOM, \
            trait.Ascetisme.NOM, \
            trait.Nature.NOM, \
            trait.Artiste.NOM, \
            trait.Serenite.NOM, \
            metier.Pretre.NOM \
            # classe sociale basse
            ]
