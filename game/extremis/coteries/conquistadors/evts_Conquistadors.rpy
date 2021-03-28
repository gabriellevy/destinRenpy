

init -5 python:
    import random
    from extremis.coteries.conquistadors import conquistadors
    from extremis.socio_eco.metiers import metier
    from extremis.religions import religion

    def AjouterEvtsConquistadors():
        """
        événements génériques qui concernent les conquistadors
        """
        global selecteur_
        estConquistador = condition.Condition(coterie.Coterie.C_COTERIE, conquistadors.Conquistadors.ID, condition.Condition.EGAL)
        estPasConquistador = condition.Condition(coterie.Coterie.C_COTERIE, conquistadors.Conquistadors.ID, condition.Condition.DIFFERENT)
        estDansQuartierConquistador = condition.Condition(quartier.Quartier.C_QUARTIER, quartier.SaintMalo.NOM, condition.Condition.EGAL)
        # guerrier
        estGuerrierNul = condition.Condition(metier.Guerrier.NOM, 4, condition.Condition.INFERIEUR)
        estPasGrandGuerrier = condition.Condition(metier.Guerrier.NOM, 8, condition.Condition.INFERIEUR)
        estBonGuerrier = condition.Condition(metier.Guerrier.NOM, 4, condition.Condition.SUPERIEUR)
        estGuerrierSupreme = condition.Condition(metier.Guerrier.NOM, 10, condition.Condition.EGAL)
        estPasGuerrierSupreme = condition.Condition(metier.Guerrier.NOM, 10, condition.Condition.DIFFERENT)

        # très forte chance (proba absolue) de suivre des modules tant qu'on n'en a pas fait 6
        recrutementDesPauvresParConquistadors = declencheur.Declencheur(proba.Proba(0.1, True), "recrutementDesPauvresParConquistadors")
        recrutementDesPauvresParConquistadors.AjouterCondition(estPasConquistador)
        recrutementDesPauvresParConquistadors.AjouterCondition(estPauvre)
        selecteur_.ajouterDeclencheur(recrutementDesPauvresParConquistadors)

label recrutementDesPauvresParConquistadors:
    # Conversion des pauvres
    "Alors que vous êtes au plus bas à déprimer dans un bar vous êtes abordé par un jovial conquistador en armure resplendissante. Il vous vante la vie aventureuse aux confins du monde où vous pourrez avoir une vie aventureuse pleine de combats et de pillages. "
    "Là où la fortune se fait au mérite loin des magouilles politiciennes."
    $ affecte = False # est-ce que le prêche l'a affecté
    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.3:
        $ RetirerACarac(trait.Prudence.NOM, 1)
        $ affecte = True
    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.3:
        $ AjouterACarac(trait.Cupidite.NOM, 1)
        $ affecte = True
    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.3:
        $ AjouterACarac(trait.Opportunisme.NOM, 1)
        $ affecte = True

    $ conquistadorsCot = coteries_[conquistadors.Conquistadors.ID]
    $ affinite = conquistadorsCot.CalculerAffinite(situation_)
    if affinite > 0:
        "Ses arguments vous convainquent de postuler."
        jump conquistadorsPostule
    elif affecte:
        "Quoique son discours vous ait beaucoup affecté, ses arguments ne vous convainquent pas de rejoindre les conquisstadors."
    else:
        "Ca ne suffit néanmoins pas à vous convaincre de devenir un conquistador."
