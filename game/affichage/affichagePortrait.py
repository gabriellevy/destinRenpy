from extremis.humanite import pnj

class AffichagePortrait:
    """
    classes permettant l'affichage esthétique d'un portrait avec caractéristiques d'un personnage
    fonctionne avec une fonction d'affichage dans screen.rpy
    """

    def __init__(self, pnj):
        self.nom_ = u"{} {}".format(pnj.prenom_, pnj.nom_)

        # ------------ description
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


        if pnj.relationAmoureuse_ != None:
            # éventuellement affichage d'un statut de relation
            self.description_ = u"{}\n{}".format(self.description_, pnj.relationAmoureuse_.DescriptionInteretPnjEnversJoueur())
            self.description_ = u"{}\n{}".format(self.description_, pnj.relationAmoureuse_.DescriptionInteretJoueurEnversPnj())
        else:
            # je n'affiche aps ça pour les amoureux mais c'est discutable. De toute façon le mieux ce serait de l'afficher par infobulle
            if pnj.coterie_ != "":
                self.description_ = u"{}\n{}".format(self.description_, pnj.coterie_)
            if pnj.metier_ != "":
                self.description_ = u"{}\n{}".format(self.description_, pnj.metier_)



        self.adresseImgPortrait = pnj.portraitStr_
