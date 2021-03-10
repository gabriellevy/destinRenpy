init -2 python:
    from despin.abs import carac
    from despin.gen_vie import situation
    from extremis.humanite import trait
    from extremis.geographie import quartier
    from extremis.constitution import temps
    from extremis.coteries import collection_coteries
    from extremis.socio_eco.metiers import metier
    from extremis.humanite.sante import pbsante
    from extremis.socio_eco.crime import crime
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
    quartiers_ = quartier.CollectionQuartiers()
    situation_.collectionQuartiers = quartiers_
    crimes_ = crime.CollectionCrimes()
    situation_.collectionCrimes = crimes_
    interfaceMode_ = 4
    nbInterfaceMode_ = 9

    def InterfaceSuivante():
        global interfaceMode_, nbInterfaceMode_
        interfaceMode_ = interfaceMode_ + 1
        if interfaceMode_ >= nbInterfaceMode_:
            interfaceMode_ = 0
        print(interfaceMode_)

    def DeterminerPerso():
        global situation_
        renpy.jump("generationUnivers_Perso")

label generationUnivers_Perso:
    jump naissance
