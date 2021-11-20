init -5 python:
    import random
    from extremis.coteries.transhumanistes import transhumanistes
    from abs.humanite import metier
    from abs.humanite.sante import pbsante
    from abs.religions import religion

    # santé
    estAHopital = condition.Condition(pbsante.PbSante.C_JOURS_DHOPITAL, 0, condition.Condition.SUPERIEUR)

    def AjouterEvtsTranshumanistes():
        """
        événements génriques qui concernent les transhumanistes
        """
        global selecteur_
        estTranshumaniste = condition.Condition(coterie.Coterie.C_COTERIE, transhumanistes.Transhumanistes.ID, condition.Condition.EGAL)
        estPasTranshumaniste = condition.Condition(coterie.Coterie.C_COTERIE, transhumanistes.Transhumanistes.ID, condition.Condition.DIFFERENT)
        estEnPrison = condition.Condition(justice.Justice.C_LIBERTE, justice.Justice.PRISON, condition.Condition.EGAL) # vraie prison, déjà condamné pas préventif
        estDansQuartierTranshumaniste = condition.Condition(quartier.Quartier.C_QUARTIER, quartier.LaDefense.NOM, condition.Condition.EGAL)

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
    $ texteSoin = maladies_.SoignerMaladieAleatoire(situation_)
    if texteSoin == "":
        $ texteSoin = blessures_.SoignerBlessureAleatoire(situation_)
    if texteSoin != "" and len(texteSoin) > 0:
        $ print(u"texteSoin : {}".format(texteSoin))
        "[texteSoin]"
    jump fin_cycle
