init -2 python:
    from despin.abs import carac
    from despin.gen_vie import situation
    from extremis.humanite import trait
    from extremis.constitution import temps
    from extremis.coteries import collection_coteries
    from extremis.socio_eco.metiers import metier
    from extremis.humanite.sante import pbsante
    import random

    situation_ = situation.Situation() # dictionnaire contenant toutes les caracs courantes de la partie
    filtre_ = filtres_action.FiltreAction()
    traits_ = trait.CollectionTraits()
    coteries_ = collection_coteries.CollectionCoteries()
    metiers_ = metier.CollectionMetiers()
    blessures_ = pbsante.CollectionBlessures()
    maladies_ = pbsante.CollectionMaladies()

    def DeterminerPerso():
        global situation_
        renpy.jump("generationUnivers_Perso")

label generationUnivers_Perso:
    jump naissance
