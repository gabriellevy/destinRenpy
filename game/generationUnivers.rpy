init -2 python:
    from despin.abs import carac
    from despin.gen_vie import situation
    import random

    situation_ = situation.Situation() # dictionnaire contenant toutes les caracs courantes de la partie

    def DeterminerPerso():
        global situation_
        # tout ce qui suit devra être déterminé aléatoirement mais en attendant valeur par défaut :
        situation_.SetCarac("Nom", "Deharbe")
        situation_.SetCarac("Prénom", "Mathieu")
        situation_.SetCarac("Santé", "Bonne")
        situation_.SetCarac("Métier", "Fonctionnaire administratif")
        renpy.jump("generationUnivers_Perso")

label generationUnivers_Perso:
    "Vous avez 20 ans."
    "Vous vous appelez [situation_[Prénom]] [situation_[Nom]]."
    "Vous êtes [situation_[Métier]]."
    jump debut_cycle
