init -2 python:
    from despin.abs import carac
    from despin.gen_vie import situation
    from extremis.socio_eco import metier
    from extremis.humanite import trait
    import random

    situation_ = situation.Situation() # dictionnaire contenant toutes les caracs courantes de la partie
    filtre_ = filtres_action.FiltreAction()
    traits_ = trait.CollectionTraits()

    def DeterminerPerso():
        global situation_
        # TODO : tout ce qui suit devra être déterminé aléatoirement mais en attendant valeur par défaut :
        situation_["Nom"] = "Deharbe"
        situation_["Prenom"] = "Mathieu"
        situation_["Sante"] = "Bonne"
        situation_[metier.Metier.METIER] = "Fonctionnaire administratif"
        metier.regenererCaracsMetier(situation_)
        renpy.jump("generationUnivers_Perso")

label generationUnivers_Perso:
    #"Vous avez 20 ans."
    #"Vous vous appelez [situation_[Prenom]] [situation_[Nom]]."
    #if metier.aUnMetier(situation_):
    #    "Vous êtes [situation_[Métier]]."
    "Liste des traits : [traits_]."
    #"Le nom de ce trait en statique est [trait.Trait.CUPIDE]."
    #"Le nom de ce trait via tableau est [traits_[Cupidité]]."
    #"Niveau de cupidité '[situation_[Cupidité]]'."
    #$ descriptionCupiditeJoueur = traitCupidite_.GetDescription(situation_)
    #"Vous êtes [descriptionCupiditeJoueur]."
    #"Liste des traits : [traits_]."
    jump debut_cycle
