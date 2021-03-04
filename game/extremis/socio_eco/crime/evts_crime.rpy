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

    # notes sur les probas : les métiers très courant ont une proba de base de 0.1 (payson, employé)
    # métier courant mais faible à l'échelle de la population proba 0.01 (boutiquier, médecin
    # les très rares ont une proba de 0.0001 (tueur de monstre,
    def AjouterEvtsCrime():
        global selecteur_
        estPauvre = condition.Condition(trait.Richesse.NOM, -5, condition.Condition.INFERIEUR_EGAL)
        estPasCriminel = condition.Condition(crime.Crime.C_CRIMINEL, "", condition.Condition.EGAL)
        estPasVioleur = condition.Condition(crime.Violeur.NOM, "", condition.Condition.EGAL)
        estPasVoleur = condition.Condition(crime.Voleur.NOM, "", condition.Condition.EGAL)
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

        # devient petit délinquant
        prob = proba.Proba(0.002, True)
        prob.ajouterModifProbaViaVals(0.01, estParesseux)
        prob.ajouterModifProbaViaVals(0.01, estMenteur)
        prob.ajouterModifProbaViaVals(0.01, estSournois)
        prob.ajouterModifProbaViaVals(0.01, estInstinctif)
        prob.ajouterModifProbaViaVals(0.01, estCupide)
        prob.ajouterModifProbaViaVals(0.01, estOpportuniste)
        decDevientDelinquant = declencheur.Declencheur(prob, "decDevientDelinquant")
        decDevientDelinquant.AjouterCondition(estPauvre)
        decDevientDelinquant.AjouterCondition(estPasVoleur)
        selecteur_.ajouterDeclencheur(decDevientDelinquant)

        # devient violeur
        prob = proba.Proba(0.0001, True)
        prob.ajouterModifProbaViaVals(0.01, estCruel)
        prob.ajouterModifProbaViaVals(0.01, estObsede)
        prob.ajouterModifProbaViaVals(0.01, estPerversSexuel)
        prob.ajouterModifProbaViaVals(0.01, estSournois)
        decDevientVioleur = declencheur.Declencheur(prob, "decDevientVioleur")
        decDevientVioleur.AjouterCondition(estPasVioleur)
        selecteur_.ajouterDeclencheur(decDevientVioleur)

        # A FAIRE : événement devient un voleur de plus en plus dangereux

label decDevientDelinquant:
    # devient petit voleur délinquant
    "Vous vous mettez à voler à droite à gauche pour survivre et échapper à la misère."
    $ situation_.SetValCarac(crime.Crime.C_CRIMINEL, crime.Crime.DELINQUANT)
    $ situation_.SetValCarac(crime.Voleur.NOM, 1)
    jump fin_cycle

label decDevientVioleur:
    # devient obsédé sexuel
    "Vos obsessions sexuels sont de plus en plus obsessionnelles. Vous vous mettez à suivre des femmes dans la rue, à les tripoter, à fantasmer sur leur viol."
    $ situation_.SetValCarac(crime.Crime.C_CRIMINEL, crime.Crime.DELINQUANT)
    $ situation_.SetValCarac(crime.Violeur.NOM, 1)
    jump fin_cycle
    # A FAIRE : devient un vrai violeur :
    # "Vos perversions vous poussent à devenir un violeur de plus en plus dépravé."
