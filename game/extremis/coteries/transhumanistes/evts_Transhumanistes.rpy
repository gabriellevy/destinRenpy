init -5 python:
    import random
    from extremis.coteries.transhumanistes import transhumanistes
    from extremis.socio_eco.metiers import metier
    from extremis.humanite import identite
    from extremis.humanite.sante import pbsante
    from extremis.religions import religion

    def AjouterEvtsTranshumanistes():
        """
        événements génriques qui concernent les transhumanistes
        """
        global selecteur_
        estTranshumaniste = condition.Condition(coterie.Coterie.C_COTERIE, transhumanistes.Transhumanistes.ID, condition.Condition.EGAL)
        estPasTranshumaniste = condition.Condition(coterie.Coterie.C_COTERIE, transhumanistes.Transhumanistes.ID, condition.Condition.DIFFERENT)
        estEnPrison = condition.Condition(justice.Justice.C_LIBERTE, justice.Justice.PRISON, condition.Condition.EGAL) # vraie prison, déjà condamné pas préventif
        estDansQuartierTranshumaniste = condition.Condition(quartier.Quartier.C_QUARTIER, quartier.LaDefense.NOM, condition.Condition.EGAL)
        # guerrier
        estGuerrierNul = condition.Condition(metier.Guerrier.NOM, 4, condition.Condition.INFERIEUR)
        estPasGrandGuerrier = condition.Condition(metier.Guerrier.NOM, 8, condition.Condition.INFERIEUR)
        estBonGuerrier = condition.Condition(metier.Guerrier.NOM, 4, condition.Condition.SUPERIEUR)
        estGuerrierSupreme = condition.Condition(metier.Guerrier.NOM, 10, condition.Condition.EGAL)
        estPasGuerrierSupreme = condition.Condition(metier.Guerrier.NOM, 10, condition.Condition.DIFFERENT)
        # santé
        estAHopital = condition.Condition(pbsante.PbSante.C_JOURS_DHOPITAL, 0, condition.Condition.SUPERIEUR)

        # hôpital transhumaniste
        prob = proba.Proba(0.9, True)
        transhumanistesHopital = declencheur.Declencheur(prob, "transhumanistesHopital")
        transhumanistesHopital.AjouterCondition(estAHopital)
        transhumanistesHopital.AjouterCondition(estDansQuartierTranshumaniste)
        selecteur_.ajouterDeclencheur(transhumanistesHopital)

label transhumanistesHopital:
    # hôpital transhumaniste
    "L'hopital transhumaniste où vous vous trouvez est hors de prix mais d'une qualité exceptionnelle."
    $ situation_.RetirerACarac(trait.Richesse.NOM, 2)
    $ texte = maladies_.SoignerMaladieAleatoire(situation_)
    if texte == "":
        $ texte = blessures_.SoignerBlessureAleatoire(situation_)
    if texte != "":
        "[texte]"
    jump fin_cycle
