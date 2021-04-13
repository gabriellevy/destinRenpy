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
    filtre_ = filtres_action.FiltreAction() # objet contenant les préférences du joueur pour les actions à afficher ou cacher en priorité
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
    interfaceMode_ = 0
    nbInterfaceMode_ = 11

    # text fade system
    time_ = 2.0 # seconds of fade
    x_debut = 100
    y_debut = 10
    x_fin = 650
    y_fin = 10

    def AjouterACarac(caracId, num):
        global situation_
        textChangtCarac = u"{} + {}".format(caracId, num)
        renpy.show_screen("fading_text", textChangtCarac, time_, x_debut, y_debut, x_fin, y_fin, color="#fff", size=24, alpha=1.0)
        renpy.pause(time_)
        renpy.hide_screen("fading_text")
        situation_.AjouterACarac(caracId, num)

    def RetirerACarac(caracId, num):
        global situation_
        textChangtCarac = u"{} - {}".format(caracId, num)
        renpy.show_screen("fading_text", textChangtCarac, time_, x_debut, y_debut, x_fin, y_fin, color="#e11", size=24, alpha=1.0)
        renpy.pause(time_)
        renpy.hide_screen("fading_text")
        situation_.RetirerACarac(caracId, num)

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
