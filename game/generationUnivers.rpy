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
    situation_.collectionTraits = traits_
    coteries_ = collection_coteries.CollectionCoteries()
    situation_.collectionCoteries = coteries_
    metiers_ = metier.CollectionMetiers()
    situation_.collectionMetiers = metiers_
    blessures_ = pbsante.CollectionBlessures()
    situation_.collectionBlessures = blessures_
    maladies_ = pbsante.CollectionMaladies()
    situation_.collectionMaladies = maladies_

    def DeterminerPerso():
        global situation_
        renpy.jump("generationUnivers_Perso")

label generationUnivers_Perso:
    jump naissance
