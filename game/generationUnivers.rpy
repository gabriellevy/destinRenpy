init -2 python:
    from despin.abs import carac
    from despin.gen_vie import situation
    from extremis.socio_eco import metier
    from extremis.humanite import trait
    import random

    situation_ = situation.Situation() # dictionnaire contenant toutes les caracs courantes de la partie
    filtre_ = filtres_action.FiltreAction()
    traits_ = trait.Trait.TOUS_LES_TRAITS

    def DeterminerPerso():
        global situation_
        # TODO : tout ce qui suit devra être déterminé aléatoirement mais en attendant valeur par défaut :
        situation_["Nom"] = "Deharbe"
        situation_["Prénom"] = "Mathieu"
        situation_["Santé"] = "Bonne"
        situation_[metier.Metier.METIER] = "Fonctionnaire administratif"
        metier.regenererCaracsMetier(situation_)
        renpy.jump("generationUnivers_Perso")

label generationUnivers_Perso:
    #"Vous avez 20 ans."
    #"Vous vous appelez [situation_[Prénom]] [situation_[Nom]]."
    #if metier.aUnMetier(situation_):
    #    "Vous êtes [situation_[Metier]]."
    "Vous êtes aussi [traits_]."
    "Vous êtes aussi [trait.Trait.CUPIDE]."
    jump debut_cycle
