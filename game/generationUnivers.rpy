init -2 python:
    from despin.abs import carac
    from despin.gen_vie import situation
    from despin.extremis import metier
    import random

    situation_ = situation.Situation() # dictionnaire contenant toutes les caracs courantes de la partie

    def DeterminerPerso():
        global situation_
        # tout ce qui suit devra être déterminé aléatoirement mais en attendant valeur par défaut :
        situation_["Nom"] = "Deharbe"
        situation_["Prénom"] = "Mathieu"
        situation_["Santé"] = "Bonne"
        # situation_["Métier"] = "Fonctionnaire administratif"
        metier.regenererCaracsMetier(situation_)
        renpy.jump("generationUnivers_Perso")

label generationUnivers_Perso:
    "Vous avez 20 ans."
    "Vous vous appelez [situation_[Prénom]] [situation_[Nom]]."
    if metier.aUnMetier(situation_):
        "Vous êtes [situation_[Métier]]."
    jump debut_cycle
