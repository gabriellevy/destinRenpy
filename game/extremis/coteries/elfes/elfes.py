from extremis.coteries import coterie
from extremis.socio_eco.metiers import metier
from extremis.humanite import trait

class Elfes(coterie.Coterie):

    NOM = u"Elfes"
    ID = u"elfes"

    def __init__(self):
        self.nom_ = Elfes.NOM

    def getLabelUniversite(self):
        return "univElfes"

    def GetTraitsCompatibles(self):
        """
        si le perso a ces caracs il a plus de chances de vouloir rejoindre cette coterie
        """
        return [ \
            trait.Nature.NOM, \
            trait.Artiste.NOM, \
            trait.Serenite.NOM, \
            trait.Sensibilite.NOM, \
            ]

    def GetMetiersCompatibles(self):
        """
        si le perso a des compétences dans ces métiers il a plus de chances de vouloir rejoindre cette coterie où ils sont souvent pratiqués
        """
        return [ \
            metier.Musicien.NOM, \
            metier.Poete.NOM, \
            metier.Alchimiste.NOM \
            ]

    def GetTraitsIncompatibles(self):
        """
        si le perso a ces caracs il a plus de chances de ne pas vouloir rejoindre cette coterie
        """
        return [ \
            trait.Violence.NOM, \
            trait.Franchise.NOM, \
            trait.Ambition.NOM \
            # les blessures en particuliers être défiguré
            ]

    # pour intégrer la coterie tests sur : beauté (dur) taille, habileté, poids
