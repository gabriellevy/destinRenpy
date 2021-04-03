from extremis.humanite import pnj

class AffichagePortrait:
    """
    classes permettant l'affichage esthétique d'un portrait avec caractéristiques d'un personnage
    fonctionne avec une fonction d'affichage dans screen.rpy
    """

    def __init__(self, pnj):
        self.nom_ = u"{} {}".format(pnj.prenom_, pnj.nom_)

        # description
        self.description_ = u""
        nbJoursVecus = pnj.nbJours_
        if isinstance(nbJoursVecus, int):
            nbAnnees = nbJoursVecus/365
            nbJoursPasses = nbJoursVecus%365
            nbMois = nbJoursPasses/30
            if nbMois > 0:
                self.description_ = u"{} ans, {} mois".format(nbAnnees, nbMois)
            else:
                self.description_ = u"{} ans".format(nbAnnees)

        if pnj.coterie_ != "":
            self.description_ = u"{}\n{}".format(self.description_, pnj.coterie_)
        if pnj.metier_ != "":
            self.description_ = u"{}\n{}".format(self.description_, pnj.metier_)

        self.adresseImgPortrait = pnj.portraitStr_
