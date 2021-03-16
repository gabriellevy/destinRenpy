from extremis.coteries import coterie
from extremis.socio_eco.metiers import metier
from extremis.humanite import trait
from extremis.geographie import quartier

class Elfes(coterie.Coterie):

    NOM = u"Elfes"
    ID = u"elfes"

    def __init__(self):
        self.nom_ = Elfes.NOM
        self.id_ = Elfes.ID
        self.quartier_ = quartier.SaintGermainEnLaye.NOM

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

    def GenererPortraits(self, age, masculin, metier, portraits):
        """
        ajoute des portraits correspondants aux caracs en paramtre (et à la coterie courante)
        """
        if masculin:
            if age > 15:
                if age > 20:
                    if age > 30:
                        portraits.append("images/coteries/elfes/portraits/portrait_30+.jpg")
                        if age > 50:
                            portraits.append("images/coteries/elfes/portraits/portrait_50+.jpg")
                            portraits.append("images/coteries/elfes/portraits/portrait50+.png")
                    if age < 40:
                        portraits.append("images/coteries/elfes/portraits/portrait20-40.png")
                if age < 40:
                    portraits.append("images/coteries/elfes/portraits/portrait_15-40_b.jpg")
                    portraits.append("images/coteries/elfes/portraits/portrait_15-40_c.jpg")
                    portraits.append("images/coteries/elfes/portraits/portrait_15-40_d.jpg")
                    if age < 30:
                        portraits.append("images/coteries/elfes/portraits/portrait_15-30.jpg")
        else:
            if age > 20:
                if age < 40:
                    portraits.append("images/coteries/elfes/portraits/Fportrait20-40.png")
                    portraits.append("images/coteries/elfes/portraits/Fportrait20-40_2.png")

        return portraits

    # pour intégrer la coterie tests sur : beauté (dur) taille, habileté, poids
