init -2 python:
    from despin.abs import carac
    from despin.gen_vie import situation
    from extremis.socio_eco import metier
    from extremis.humanite import trait
    from extremis.constitution import temps
    import random

    situation_ = situation.Situation() # dictionnaire contenant toutes les caracs courantes de la partie
    filtre_ = filtres_action.FiltreAction()
    traits_ = trait.CollectionTraits()

    def DeterminerPerso():
        global situation_
        renpy.jump("generationUnivers_Perso")

label generationUnivers_Perso:
    jump naissance
