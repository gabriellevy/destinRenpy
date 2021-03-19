# fichier où sont générés les phrases d'ambiance à afficher quand il ne se passe rien durant un mois particulier

init -5 python:
    import random
    from despin.gen_vie import declencheur
    from despin.gen_vie import selecteur
    from despin.gen_vie import proba
    from despin.abs import condition
    from extremis.socio_eco.metiers import metier
    from extremis.humanite import trait
    from extremis.coteries import coterie
    from extremis.coteries.templiers import templiers
    from extremis.religions import religion
    from extremis.geographie import quartier

    def AjouterEvtsRien():
        global selecteur_, situation_
        selecteurDEvenementVide = declencheur.Declencheur(1.0, "selecteurDEvenementVide")
        selecteur_.ajouterDeclencheur(selecteurDEvenementVide)

    def LancerEvtVide(situation):
        sceneParDefaut = ""
        # régénère les événements compatibles avec la situation
        evtsVides_ = ["evtRien1", "evtRien2", "evtRien3" ]

        if situation_.GetValCaracInt(metier.Metier.ADMINISTRATIF) > 0:
            evtsVides_.append("evtRien_Administratif1")

        if situation_.GetValCaracInt(trait.Pilotage.NOM) > 0:
            evtsVides_.append("evtRien_Conduite")

        nomCoterie = situation_.GetValCarac(coterie.Coterie.C_COTERIE)
        nomCoterieUniv = situation_.GetValCarac(coterie.Coterie.Carac_UNIV_COURANTE)
        if nomCoterie ==  templiers.Templiers.ID or nomCoterieUniv == templiers.Templiers.ID:
            evtsVides_.append("evtRien_Templiers_1")
            evtsVides_.append("evtRien_Templiers_2")
            evtsVides_.append("evtRien_Templiers_3")
            evtsVides_.append("evtRien_Templiers_4")
            evtsVides_.append("evtRien_Templiers_5")

        # fond selon quartier
        if sceneParDefaut == "":
            quartierCourant = situation.GetQuartier()
            if quartierCourant != None:
                sceneParDefaut = quartierCourant.imageDeFond_

        if sceneParDefaut == "":
            sceneParDefaut = "bg rue_haussmann"

        # fond
        if sceneParDefaut != "":
            renpy.scene()
            renpy.show(sceneParDefaut)
        # en lance un au hasard
        renpy.jump(random.choice(evtsVides_))

label selecteurDEvenementVide:
    $ LancerEvtVide(situation_)

label evtRien_Conduite:
    scene bg route_campagne
    with Dissolve(.5)
    "Rien de tel qu'une bonne petit promenade à la campagne."
    jump fin_cycle

label evtRien1:
    with Dissolve(.5)
    "Et encore une journée de plus."
    jump fin_cycle

label evtRien2:
    with Dissolve(.5)
    "Les jours se suivent et se ressemblent."
    jump fin_cycle

label evtRien3:
    with Dissolve(.5)
    "Un jour c'est sûr quelque chose vous arrivera."
    jump fin_cycle

label evtRien_Administratif1:
    scene bg bureau
    with Dissolve(.5)
    "La vie de bureau suit son cours."
    jump fin_cycle
