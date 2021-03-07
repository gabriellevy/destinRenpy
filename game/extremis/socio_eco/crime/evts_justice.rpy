init -5 python:
    import random
    from despin.gen_vie import declencheur
    from despin.gen_vie import selecteur
    from despin.gen_vie import proba
    from despin.abs import condition
    from despin.reglages import filtres_action
    from extremis.humanite import trait
    from extremis.constitution import temps
    from extremis.socio_eco.metiers import metier
    from extremis.socio_eco.crime import crime
    from extremis.socio_eco.crime import justice

    # notes sur les probas : les métiers très courant ont une proba de base de 0.1 (payson, employé)
    # métier courant mais faible à l'échelle de la population proba 0.01 (boutiquier, médecin
    # les très rares ont une proba de 0.0001 (tueur de monstre,
    def AjouterEvtsJustice():
        global selecteur_
        estPauvre = condition.Condition(trait.Richesse.NOM, -5, condition.Condition.INFERIEUR_EGAL)
        estCriminel = condition.Condition(crime.Crime.C_CRIMINEL, "", condition.Condition.DIFFERENT)
        # statut criminel
        estPasCriminel = condition.Condition(crime.Crime.C_CRIMINEL, "", condition.Condition.EGAL)
        estPasVioleur = condition.Condition(crime.Violeur.NOM, "", condition.Condition.EGAL)
        estPasVoleur = condition.Condition(crime.Voleur.NOM, "", condition.Condition.EGAL)
        estPasCriminelViolent = condition.Condition(crime.CriminelViolent.NOM, "", condition.Condition.EGAL)
        # statut judiciaire
        estEnPrisonPreventive = condition.Condition(justice.Justice.C_LIBERTE, justice.Justice.CAPTURE_POLICE, condition.Condition.EGAL) # attente de jugement
        # a telle carac
        estCruel = condition.Condition(trait.Altruisme.NOM, -13, condition.Condition.INFERIEUR_EGAL)
        estObsede = condition.Condition(trait.Sexualite.NOM, 1, condition.Condition.SUPERIEUR_EGAL)
        estParesseux = condition.Condition(trait.Industrie.NOM, -3, condition.Condition.INFERIEUR_EGAL)
        estMenteur = condition.Condition(trait.Sincerite.NOM, -3, condition.Condition.INFERIEUR_EGAL)
        estSournois = condition.Condition(trait.Franchise.NOM, -3, condition.Condition.INFERIEUR_EGAL)
        estInstinctif = condition.Condition(trait.Honorabilite.NOM, -3, condition.Condition.INFERIEUR_EGAL) # non honorable /loyal
        estCupide = condition.Condition(trait.Cupidite.NOM, 1, condition.Condition.SUPERIEUR_EGAL)
        estOpportuniste = condition.Condition(trait.Opportunisme.NOM, 1, condition.Condition.SUPERIEUR_EGAL)
        estPerversSexuel = condition.Condition(trait.Sexualite.NOM, 11, condition.Condition.SUPERIEUR_EGAL)
        estAventureux = condition.Condition(trait.Prudence.NOM, -3, condition.Condition.INFERIEUR_EGAL)
        estMenteur = condition.Condition(trait.Sincerite.NOM, -3, condition.Condition.INFERIEUR_EGAL)

        # capturé par la police
        # A FAIRE : complexifier un peu ça
        prob = proba.Proba(0.005, True)
        decCaptureParPolice = declencheur.Declencheur(prob, "decCaptureParPolice")
        decCaptureParPolice.AjouterCondition(estCriminel)
        selecteur_.ajouterDeclencheur(decCaptureParPolice)

        # jugement
        prob = proba.Proba(0.1, True)
        decProces = declencheur.Declencheur(prob, "decProces")
        decProces.AjouterCondition(estEnPrisonPreventive)
        selecteur_.ajouterDeclencheur(decProces)

label decProces:
    "Le jour de votre procès est venu."

    menu:
        "A FAIRE : Crime::PrononcerLaSentence(humain, effet);":
            pass

    jump fin_cycle

label decCaptureParPolice:
    # devient criminel violent
    "Vous avez été capturé par la police pour vos méfaits."
    menu:
        "capturé par la police!"
        "zut":
            pass
    $ situation_.SetValCarac(justice.Justice.C_LIBERTE, justice.Justice.CAPTURE_POLICE)
    # perd son métier :
    $ situation_.SetValCarac(metier.Metier.C_METIER, "")
    $ situation_.SetValCarac(metier.Metier.C_COMPETENCE_METIER, "")

    jump fin_cycle
