init -5 python:
    import random
    from despin.gen_vie import declencheur
    from despin.gen_vie import selecteur
    from despin.gen_vie import proba
    from despin.abs import condition
    from extremis.socio_eco.metiers import metier
    from despin.reglages import filtres_action
    from extremis.humanite import trait
    from extremis.constitution import temps
    from extremis.coteries import coterie
    from extremis.humanite.sante import pbsante


    ageSup30 = condition.Condition(temps.Date.AGE_ANNEES, 30, condition.Condition.SUPERIEUR_EGAL)
    ageSup40 = condition.Condition(temps.Date.AGE_ANNEES, 40, condition.Condition.SUPERIEUR_EGAL)
    ageSup50 = condition.Condition(temps.Date.AGE_ANNEES, 50, condition.Condition.SUPERIEUR_EGAL)
    ageSup60 = condition.Condition(temps.Date.AGE_ANNEES, 60, condition.Condition.SUPERIEUR_EGAL)
    ageSup70 = condition.Condition(temps.Date.AGE_ANNEES, 70, condition.Condition.SUPERIEUR_EGAL)
    ageSup80 = condition.Condition(temps.Date.AGE_ANNEES, 80, condition.Condition.SUPERIEUR_EGAL)
    ageSup90 = condition.Condition(temps.Date.AGE_ANNEES, 90, condition.Condition.SUPERIEUR_EGAL)
    ageSup100 = condition.Condition(temps.Date.AGE_ANNEES, 100, condition.Condition.SUPERIEUR_EGAL)
    # conditions Richesse
    estMiserable = condition.Condition(trait.Richesse.NOM, trait.Trait.SEUIL_A_PAS_EXTREME, condition.Condition.INFERIEUR_EGAL)
    estPauvre = condition.Condition(trait.Richesse.NOM, trait.Trait.SEUIL_A_PAS, condition.Condition.INFERIEUR_EGAL)
    estAise = condition.Condition(trait.Richesse.NOM, trait.Trait.SEUIL_A, condition.Condition.SUPERIEUR_EGAL)
    estRichissime = condition.Condition(trait.Richesse.NOM, trait.Trait.SEUIL_A_EXTREME, condition.Condition.SUPERIEUR_EGAL)

    def AjouterEvtsVieillesse():
        global selecteur_
        # pas d'événement vieillesse avant 30 ans
        probaVieillesse = proba.Proba(0.01, False)
        # ageBonus
        probaVieillesse.ajouterModifProbaViaVals(0.01, ageSup40)
        probaVieillesse.ajouterModifProbaViaVals(0.01, ageSup50)
        probaVieillesse.ajouterModifProbaViaVals(0.02, ageSup60)
        probaVieillesse.ajouterModifProbaViaVals(0.02, ageSup70)
        probaVieillesse.ajouterModifProbaViaVals(0.04, ageSup80)
        probaVieillesse.ajouterModifProbaViaVals(0.05, ageSup90)
        probaVieillesse.ajouterModifProbaViaVals(0.08, ageSup100)
        # constitution
        probaVieillesse.ajouterModifProbaViaVals(0.01, estChetif)
        probaVieillesse.ajouterModifProbaViaVals(0.005, estFragile)
        probaVieillesse.ajouterModifProbaViaVals(-0.05, estResistant)
        probaVieillesse.ajouterModifProbaViaVals(-0.01, estIndestructible)
        # richesse
        probaVieillesse.ajouterModifProbaViaVals(0.01, estMiserable)
        probaVieillesse.ajouterModifProbaViaVals(0.005, estPauvre)
        probaVieillesse.ajouterModifProbaViaVals(-0.005, estAise)
        probaVieillesse.ajouterModifProbaViaVals(-0.01, estRichissime)
        # A FAIRE : impliants longévité (les ajouter dans les trucs de bionique)

        decVieillir = declencheur.Declencheur(probaVieillesse, "decVieillir")
        decVieillir.AjouterCondition(ageSup30)
        selecteur_.ajouterDeclencheur(decVieillir)

label decVieillir:
    $ nbEffets = random.randint(1, 3)
    label effetVieillir:
        while nbEffets > 0:
            $ res100 = random.randint(0, 85)
            $ ageBonus = situation_.AgeEnAnnees()
            # plus on est vieux plus le score est augmenté :
            $ effetVieillesse = res100 + ageBonus - 30

            if effetVieillesse<30:
                # événements qui ont tendance à arriver au début de la vieillesse
                # res100 est entre 0 et 30 (mais vu le système de bonus je répartis selon le résultat original)
                if res100 < 10:
                    "Vous prenez du poids."
                    $ AjouterACarac(trait.Poids.NOM, 1)
                    $ nbEffets = nbEffets - 1
                    jump effetVieillir
                elif res100 < 16:
                    "Vous prenez de plus en plus d'intérêt à vos possessions et gérez votre épargne plus efficacement."
                    $ AjouterACarac(trait.Cupidite.NOM, 1)
                    $ AjouterACarac(trait.Richesse.NOM, 1)
                    $ nbEffets = nbEffets - 1
                    jump effetVieillir
                elif res100 < 23:
                    "Vous vous sentez plus calme, votre agressivité diminue."
                    $ RetirerACarac(trait.Violence.NOM, 1)
                    $ nbEffets = nbEffets - 1
                    jump effetVieillir
                elif res100 < 30:
                    "Vous êtes de plus en plus raisonnable, moins impulsif."
                    $ AjouterACarac(trait.Prudence.NOM, 1)
                    $ nbEffets = nbEffets - 1
                    jump effetVieillir

            elif effetVieillesse< 45:
                "Votre peau est de moins en moins belle."
                $ RetirerACarac(trait.Beaute.NOM, 1)
                $ nbEffets = nbEffets - 1
                jump effetVieillir
            elif effetVieillesse< 55:
                "Vous êtes de moins en moins intéressé par les femmes."
                $ RetirerACarac(trait.Sexualite.NOM, 1)
                $ nbEffets = nbEffets - 1
                jump effetVieillir
            elif effetVieillesse< 65:
                "Vos mains sont moins sûres qu'autrefois."
                $ RetirerACarac(trait.Habilete.NOM, 1)
                $ nbEffets = nbEffets - 1
                jump effetVieillir
            elif effetVieillesse< 75:
                "Vos muscles vous font souffrir aujourd'hui."
                $ RetirerACarac(trait.Force.NOM, 1)
                $ nbEffets = nbEffets - 1
                jump effetVieillir
            elif effetVieillesse< 86:
                "Vous vous sentez très fatigué."
                $ RetirerACarac(trait.Constitution.NOM, 1)
                $ nbEffets = nbEffets - 1
                jump effetVieillir
            elif effetVieillesse< 98:
                "Votre esprit est de moins en moins vif."
                $ RetirerACarac(trait.Intelligence.NOM, 1)
                $ nbEffets = nbEffets - 1
                jump effetVieillir
            elif effetVieillesse< 105:
                $ valCelebrite = situation_.GetValCaracInt(trait.Celebrite.NOM)
                if valCelebrite <= 0:
                    jump effetVieillir
                "Le temps passe, vous êtes de moins en moins connu."
                $ RetirerACarac(trait.Celebrite.NOM, 1)
                $ nbEffets = nbEffets - 1
                jump effetVieillir
            else:
                # >= 100 : mort
                "Vous êtes mort de vieillesse."
                jump mort

    jump fin_cycle
