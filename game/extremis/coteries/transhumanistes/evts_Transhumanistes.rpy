init -5 python:
    import random
    from extremis.coteries.transhumanistes import transhumanistes
    from extremis.socio_eco.metiers import metier
    from extremis.humanite import identite
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
