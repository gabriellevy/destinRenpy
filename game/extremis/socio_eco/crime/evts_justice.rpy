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
        estEnPrison = condition.Condition(justice.Justice.C_LIBERTE, justice.Justice.PRISON, condition.Condition.EGAL) # vraie prison, déjà condamné pas préventif
        aZeroMoisDePrison = condition.Condition(justice.Justice.C_JOURS_PRISON, 0, condition.Condition.EGAL)
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
        prob = proba.Proba(0.01, True)
        decCaptureParPolice = declencheur.Declencheur(prob, "decCaptureParPolice")
        decCaptureParPolice.AjouterCondition(estCriminel)
        selecteur_.ajouterDeclencheur(decCaptureParPolice)

        # jugement
        prob = proba.Proba(0.1, True)
        decProces = declencheur.Declencheur(prob, "decProces")
        decProces.AjouterCondition(estEnPrisonPreventive)
        selecteur_.ajouterDeclencheur(decProces)

        # Libéré de prison
        prob = proba.Proba(0.5, False)
        decLiberePrison = declencheur.Declencheur(prob, "decLiberePrison")
        decLiberePrison.AjouterCondition(estEnPrison)
        decLiberePrison.AjouterCondition(aZeroMoisDePrison)
        selecteur_.ajouterDeclencheur(decLiberePrison)

    def CalculerGraviteCrime(situation, crimes):
        graviteCrime = random.randint(0, 5)
        # < 5  = petit délinquant
        # > 10 crime capital
        for crimeK in crimes.lCrimes_.keys():
            crimeCarac = crimes[crimeK]
            valCrime = situation.GetValCaracInt(crimeK)
            if valCrime > 0:
                graviteCrime = graviteCrime + 1
                if valCrime > 3:
                    graviteCrime = graviteCrime + 1
                    if valCrime > 5:
                        graviteCrime = graviteCrime + 1
                        if valCrime > 8:
                            graviteCrime = graviteCrime + 1
        print("graviteCrime : {}".format(graviteCrime))

        return graviteCrime

    def CalculerNbJoursPrison(graviteCrime):
        nbMoisPrison = random.randint(graviteCrime, graviteCrime * 5 * 12) # 1 mois à 50 ans de prison
        nbJoursPrison =nbMoisPrison * 30
        return nbJoursPrison


label decLiberePrison:
    "Vous êtes enfin libéré de prison."
    $ situation_.SetValCarac(justice.Justice.C_LIBERTE, "")
    jump fin_cycle

label decProces:
    menu:
        "ATTENTION DEBUT DE PROCES : message temp pour jauger":
            pass

    "Le jour de votre procès est venu."

    $ graviteCrime = CalculerGraviteCrime(situation_, crimes_)

    if graviteCrime < 5:
        # relaché
        $ situation_.SetValCarac(justice.Justice.C_LIBERTE, "")
        $ situation_.SetValCarac(crime.Crime.C_CRIMINEL, "")
        "Miracle ! Vous êtes jugé innocent et relâché."
    elif graviteCrime < 10:
        # prison
        $ nbJoursPrison = CalculerNbJoursPrison(graviteCrime)
        $ situation_.SetValCarac(justice.Justice.C_LIBERTE, justice.Justice.PRISON)
        $ situation_.SetValCarac(crime.Crime.C_CRIMINEL, "")
        $ situation_.SetValCarac(justice.Justice.C_JOURS_PRISON, nbJoursPrison)
        $ nbAnneesPrison = (nbJoursPrison / 360) + 1

        "Vous êtes condamné à [nbAnneesPrison] années de prison."

    else:
        "Vous êtes jugé et condamné à mort pour vos crimes. La sentence est exécutée le mois suivant."
        jump mort

    jump fin_cycle

label decCaptureParPolice:
    # devient criminel violent
    "Vous avez été capturé par la police pour vos méfaits."
    menu:
        "TMP : capturé par la police!"
        "zut":
            pass
    $ situation_.SetValCarac(justice.Justice.C_LIBERTE, justice.Justice.CAPTURE_POLICE)
    # perd son métier :
    $ situation_.SetValCarac(metier.Metier.C_METIER, "")
    $ situation_.SetValCarac(metier.Metier.C_COMPETENCE_METIER, "")

    jump fin_cycle
