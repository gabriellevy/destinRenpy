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

    def MajStatutCriminel(situation):
        # si au moins un nveau de 1 dans un crime c'est un délinquant
        # si au moins un nveau de 5 dans un crime c'est un criminel
        estDelinquant = False

        for crimeK in situation.collectionCrimes.lCrimes_.keys():
            crimeCarac = crimes[crimeK]
            if crimeCarac > 0:
                estDelinquant = True
                if crimeCarac > 4:
                    situation.SetValCarac(crime.Crime.C_CRIMINEL, crime.Crime.CRIMINEL)
                    return
        if estDelinquant:
            situation.SetValCarac(crime.Crime.C_CRIMINEL, crime.Crime.DELINQUANT)

    # notes sur les probas : les métiers très courant ont une proba de base de 0.1 (payson, employé)
    # métier courant mais faible à l'échelle de la population proba 0.01 (boutiquier, médecin
    # les très rares ont une proba de 0.0001 (tueur de monstre,
    def AjouterEvtsCrime():
        global selecteur_
        estPauvre = condition.Condition(trait.Richesse.NOM, -3, condition.Condition.INFERIEUR_EGAL)
        estMiserable = condition.Condition(trait.Richesse.NOM, -13, condition.Condition.INFERIEUR_EGAL)
        aUnMetier = condition.Condition(metier.Metier.C_METIER, "", condition.Condition.DIFFERENT)
        # statut criminel
        estPasCriminel = condition.Condition(crime.Crime.C_CRIMINEL, "", condition.Condition.EGAL)
        estCriminel = condition.Condition(crime.Crime.C_CRIMINEL, "", condition.Condition.DIFFERENT)
        estPasDansGang = condition.Condition(crime.Crime.C_GANG, "", condition.Condition.EGAL)
        estDansGang = condition.Condition(crime.Crime.C_GANG, "", condition.Condition.DIFFERENT)
        estDelinquant = condition.Condition(crime.Crime.C_CRIMINEL, crime.Crime.DELINQUANT, condition.Condition.EGAL)
        estPasVioleur = condition.Condition(crime.Violeur.NOM, "", condition.Condition.EGAL)
        estPasVoleur = condition.Condition(crime.Voleur.NOM, "", condition.Condition.EGAL)
        estPasCriminelViolent = condition.Condition(crime.CriminelViolent.NOM, "", condition.Condition.EGAL)
        estCriminelViolent = condition.Condition(crime.CriminelViolent.NOM, 1, condition.Condition.SUPERIEUR_EGAL)
        estPasVendeurDrogue = condition.Condition(crime.VendeurDrogue.NOM, "", condition.Condition.EGAL)
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
        estViolent = condition.Condition(trait.Violence.NOM, 1, condition.Condition.SUPERIEUR_EGAL)
        estRancunier = condition.Condition(trait.Rancune.NOM, 1, condition.Condition.SUPERIEUR_EGAL)
        estUltraViolent = condition.Condition(trait.Violence.NOM, 11, condition.Condition.SUPERIEUR_EGAL)

        # devient petit voleur
        prob = proba.Proba(0.0, True)
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

        # A FAIRE : événement devient un voleur de plus en plus dangereux

        # devient violeur
        prob = proba.Proba(0.0, True)
        prob.ajouterModifProbaViaVals(0.01, estCruel)
        prob.ajouterModifProbaViaVals(0.01, estObsede)
        prob.ajouterModifProbaViaVals(0.01, estPerversSexuel)
        prob.ajouterModifProbaViaVals(0.01, estSournois)
        decDevientVioleur = declencheur.Declencheur(prob, "decDevientVioleur")
        decDevientVioleur.AjouterCondition(estPasVioleur)
        selecteur_.ajouterDeclencheur(decDevientVioleur)

        # A FAIRE : événement devient un violeur de plus en plus dangereux

        # devient criminel violent
        prob = proba.Proba(0.0, True)
        prob.ajouterModifProbaViaVals(0.01, estAventureux)
        prob.ajouterModifProbaViaVals(0.01, estCupide)
        prob.ajouterModifProbaViaVals(0.01, estOpportuniste)
        prob.ajouterModifProbaViaVals(0.01, estParesseux)
        prob.ajouterModifProbaViaVals(0.01, estInstinctif)
        decDevientCriminelViolent = declencheur.Declencheur(prob, "decDevientCriminelViolent")
        decDevientCriminelViolent.AjouterCondition(estPasCriminelViolent)
        selecteur_.ajouterDeclencheur(decDevientCriminelViolent)

        # A FAIRE : événement devient une brute de plus en plus dangereuse

        # si déjà criminel et au travail => devient vendeur de drogue
        prob = proba.Proba(0.001, True)
        prob.ajouterModifProbaViaVals(0.01, estCupide)
        prob.ajouterModifProbaViaVals(0.01, estOpportuniste)
        prob.ajouterModifProbaViaVals(0.01, estViolent)
        prob.ajouterModifProbaViaVals(0.01, estUltraViolent)
        prob.ajouterModifProbaViaVals(0.01, estSournois)
        prob.ajouterModifProbaViaVals(0.01, estInstinctif)
        decVendeurDeDrogueAuBoulot = declencheur.Declencheur(prob, "decVendeurDeDrogueAuBoulot")
        decVendeurDeDrogueAuBoulot.AjouterCondition(estPasVendeurDrogue)
        decVendeurDeDrogueAuBoulot.AjouterCondition(aUnMetier)
        selecteur_.ajouterDeclencheur(decVendeurDeDrogueAuBoulot)

        # honnête devient petit délinquant par violence et désoeuvrement
        prob = proba.Proba(0.002, True)
        prob.ajouterModifProbaViaVals(0.01, estViolent)
        prob.ajouterModifProbaViaVals(0.01, estUltraViolent)
        prob.ajouterModifProbaViaVals(0.01, estRancunier)
        prob.ajouterModifProbaViaVals(0.01, estCruel)
        prob.ajouterModifProbaViaVals(0.01, estSournois)
        prob.ajouterModifProbaViaVals(0.01, estParesseux)
        prob.ajouterModifProbaViaVals(0.01, estInstinctif)
        decDevientMalhonnete = declencheur.Declencheur(prob, "decDevientMalhonnete")
        decDevientMalhonnete.AjouterCondition(estPasCriminel)
        decDevientMalhonnete.AjouterCondition(estPauvre)
        selecteur_.ajouterDeclencheur(decDevientMalhonnete)

        # rejoindre un gang
        prob = proba.Proba(0.002, True)
        decRejoindreGang = declencheur.Declencheur(prob, "decRejoindreGang")
        decRejoindreGang.AjouterCondition(estDelinquant)
        decRejoindreGang.AjouterCondition(estCriminelViolent)
        decRejoindreGang.AjouterCondition(estPasDansGang)
        selecteur_.ajouterDeclencheur(decRejoindreGang)

        # Misérable qui devient pauvre par le crime
        prob = proba.Proba(0.002, True)
        prob.ajouterModifProbaViaVals(0.01, estCriminel)
        prob.ajouterModifProbaViaVals(0.01, estOpportuniste)
        prob.ajouterModifProbaViaVals(0.01, estInstinctif)
        decMiserableDevientPauvreCriminel = declencheur.Declencheur(prob, "decMiserableDevientPauvreCriminel")
        decDevientMalhonnete.AjouterCondition(estMiserable)
        selecteur_.ajouterDeclencheur(decMiserableDevientPauvreCriminel)

        # Pauvre qui s'enrichit par le crime
        prob = proba.Proba(0.002, True)
        prob.ajouterModifProbaViaVals(0.01, estCriminel)
        prob.ajouterModifProbaViaVals(0.01, estOpportuniste)
        prob.ajouterModifProbaViaVals(0.01, estInstinctif)
        decPauvreDevientMoyenCriminel = declencheur.Declencheur(prob, "decPauvreDevientMoyenCriminel")
        decPauvreDevientMoyenCriminel.AjouterCondition(estPauvre)
        selecteur_.ajouterDeclencheur(decPauvreDevientMoyenCriminel)

label decPauvreDevientMoyenCriminel:
    $ situation_.SetValCaracSiInferieur(crime.Voleur.NOM, 3)
    $ situation_.AjouterACarac(trait.Richesse.NOM, 3)
    "Par un crime très astucieux vous parvenez à vous enrichir considérablement."
    $ MajStatutCriminel(situation_)
    jump fin_cycle

label decMiserableDevientPauvreCriminel:
    $ situation_.SetValCaracSiInferieur(crime.Voleur.NOM, 3)
    $ situation_.AjouterACarac(trait.Richesse.NOM, 3)
    "Par un crime très astucieux vous parvenez à vous enrichir considérablement."
    $ MajStatutCriminel(situation_)
    jump fin_cycle

label decRejoindreGang:
    $ gang = crime.Crime.GenererNomGang();
    $ situation_.SetValCarac(crime.Crime.C_GANG, gang)
    "Vous rejoignez le gang [gang]."
    $ MajStatutCriminel(situation_)
    jump fin_cycle

label decDevientMalhonnete:
    "Par désoeuvrement et mépris du monde vous prenez l'habitude de vous battre et de voler."
    menu:
        "TMP : devient petit criminel voleur et violent"
        "zut":
            pass
    $ situation_.SetValCarac(crime.CriminelViolent.NOM, 1)
    $ situation_.SetValCarac(crime.Voleur.NOM, 1)
    $ MajStatutCriminel(situation_)
    jump fin_cycle

label decVendeurDeDrogueAuBoulot:
    "Vous mettez en place un petit réseau de revente de drogue sur votre lieu de travail qui vous fait bien voir de certains de vos collègues mais qui arrondit surtout confortablement vos revenus."
    $ situation_.SetValCarac(crime.VendeurDrogue.NOM, 3)
    $ situation_.AjouterACarac(trait.Richesse.NOM, 1)
    $ MajStatutCriminel(situation_)
    jump fin_cycle

label decDevientCriminelViolent:
    # devient criminel violent
    "Vous vous battez de plus en plus souvent, au point d'avoir plusieurs blessés à votre actif et d'être signalé à la police."
    menu:
        "TMP : devient criminel violent!"
        "zut":
            pass
    $ situation_.SetValCarac(crime.CriminelViolent.NOM, 1)
    $ MajStatutCriminel(situation_)
    jump fin_cycle

label decDevientDelinquant:
    # devient petit voleur délinquant
    "Vous vous mettez à voler à droite à gauche pour survivre et échapper à la misère."
    menu:
        "TMP : devient petit voleur!"
        "zut":
            pass
    $ situation_.SetValCarac(crime.Voleur.NOM, 1)
    $ MajStatutCriminel(situation_)
    jump fin_cycle

label decDevientVioleur:
    # devient obsédé sexuel
    "Vos obsessions sexuels sont de plus en plus obsessionnelles. Vous vous mettez à suivre des femmes dans la rue, à les tripoter, à fantasmer sur leur viol."
    menu:
        "TMP : devient violeur!"
        "zut":
            pass
    $ situation_.SetValCarac(crime.Violeur.NOM, 1)
    $ MajStatutCriminel(situation_)
    jump fin_cycle
    # A FAIRE : devient un vrai violeur :
    # "Vos perversions vous poussent à devenir un violeur de plus en plus dépravé."
