from abs.humanite import pnj
from abs.humanite.amour import relationAmoureuse

class AffichagePortrait:
    """
    classes permettant l'affichage esthétique d'un portrait avec caractéristiques d'un personnage
    fonctionne avec une fonction d'affichage dans screen.rpy
    """

    def __init__(self, pnj):
        self.nom_ = u"{}".format(pnj.nom_)

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


        if pnj.relationAmoureuse_ is not None:
            # éventuellement affichage d'un statut de relation
            if pnj.relationAmoureuse_.typeRelation_ == relationAmoureuse.RelA.FAIT_LA_COUR:
                self.description_ = u"{}\nVous lui faites la cour.".format(self.description_)
            else:
                self.description_ = u"{}\nTmp test type relation : {}.".format(self.description_, pnj.relationAmoureuse_.typeRelation_)
            self.description_ = u"{}\n{}({})".format(self.description_, pnj.relationAmoureuse_.DescriptionInteretPnjEnversJoueur(), pnj.relationAmoureuse_.interetPnjEnversJoueur_)
            self.description_ = u"{}\n{}({})".format(self.description_, pnj.relationAmoureuse_.DescriptionInteretJoueurEnversPnj(), pnj.relationAmoureuse_.interetJoueurEnversPnj_)
        else:
            # je n'affiche aps ça pour les amoureux mais c'est discutable. De toute façon le mieux ce serait de l'afficher par infobulle
            if pnj.coterie_ != "":
                self.description_ = u"{}\n{}".format(self.description_, pnj.coterie_)
            if pnj.metier_ != "":
                self.description_ = u"{}\n{}".format(self.description_, pnj.metier_)



        self.adresseImgPortrait = pnj.portraitStr_
