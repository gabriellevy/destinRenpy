init -2 python:
    from despin.abs import carac
    import random

    situation_ = {} # dictionnaire contenant toutes les caracs courantes de la partie

    def DeterminerPerso():
        global situation_
        situation_["Nom"] = "Deharbe"
        situation_["Prénom"] = "Mathieu"
        situation_["Santé"] = "Bonne"
        renpy.jump("generationUnivers_Perso")

label generationUnivers_Perso:
    "Vous avez 15 ans."
    "Vous vous appelez [situation_[Prénom]]."
    jump debut_cycle
