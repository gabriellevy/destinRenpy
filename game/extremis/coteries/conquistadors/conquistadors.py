from extremis.coteries import coterie
from extremis.socio_eco.metiers import metier
from extremis.humanite import trait

class Conquistadors(coterie.Coterie):

    NOM = u"Conquistadors"
    ID = u"conquistadors"

    def __init__(self):
        self.nom_ = Conquistadors.NOM
        self.id_ = Conquistadors.ID

    def getLabelUniversite(self):
        return "univConquistadors"

    def GetTraitsCompatibles(self):
        """
        si le perso a ces caracs il a plus de chances de vouloir rejoindre cette coterie
        """
        return [ \
            trait.Ambition.NOM, \
            trait.Opportunisme.NOM, \
            trait.Cupidite.NOM, \
            trait.Constitution.NOM, \
            trait.Pragmatisme.NOM, \
            trait.Violence.NOM
            ]

    def GetMetiersCompatibles(self):
        """
        si le perso a des compétences dans ces métiers il a plus de chances de vouloir rejoindre cette coterie où ils sont souvent pratiqués
        """
        return [ \
            metier.Cartographe.NOM, \
            metier.Marchand.NOM, \
            metier.Forgeron.NOM, \
            metier.TueurDeMonstres.NOM, \
            metier.Guerrier.NOM
            ]

    def GetTraitsIncompatibles(self):
        """
        si le perso a ces caracs il a plus de chances de ne pas vouloir rejoindre cette coterie
        """
        return [ \
            trait.Prudence.NOM, \
            trait.Altruisme.NOM, \
            trait.Industrie.NOM, \
            trait.Sexualite.NOM, \
            trait.Poids.NOM, \
            trait.Richesse.NOM # les riches laissent rarement leur possession pour les aventures dangereuses
            ]

    # pour intégrer la coterie tests sur : beauté (dur) taille, habileté, poids
