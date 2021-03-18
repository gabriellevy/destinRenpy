image medecin_peste = "medecine/medecin_peste.png"
image moniteur_auto_ecole = "metiers/moniteur_auto_ecole.png"

define med = Character('Médecin', who_outlines=[(2, "#894646",1,1)], color="#580404")
define monit = Character('Moniteur', color="#e30909")

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

    def AjouterEvtsPilotage():
        global selecteur_
        conditionSaitConduire = condition.Condition(trait.Pilotage.NOM, 1, condition.Condition.SUPERIEUR_EGAL)
        conditionSaitPasConduire = condition.Condition(trait.Pilotage.NOM, 0, condition.Condition.INFERIEUR_EGAL)
        conditionAgePermis = condition.Condition(temps.Date.AGE_ANNEES, 18, condition.Condition.SUPERIEUR_EGAL)
        pas_decPermisJamais = condition.Condition("decPermisJamais", 1, condition.Condition.DIFFERENT)
        pasTropPauvre = condition.Condition(trait.Richesse.NOM, trait.Trait.SEUIL_A_PAS_EXTREME, condition.Condition.SUPERIEUR) # substitut pour ' a les moyens d'avoir une voiture'

        decAccident = declencheur.Declencheur(0.01, "decAccident")
        decAccident.AjouterCondition(conditionSaitConduire)
        selecteur_.ajouterDeclencheur(decAccident)

        # passer le permis ?
        decPermis = declencheur.Declencheur(0.1, "decPermis")
        decPermis.AjouterCondition(conditionAgePermis)
        decPermis.AjouterCondition(pasTropPauvre)
        decPermis.AjouterCondition(pas_decPermisJamais)
        decPermis.AjouterCondition(conditionSaitPasConduire)
        selecteur_.ajouterDeclencheur(decPermis)

    # attention des actions sont à exécuter au début et à la fin de chaque événement administratif :
    def actionDebutConduiteVehicule():
        global situation_
        renpy.transition(dissolve)
        renpy.scene()
        renpy.show("bg route_campagne")

    # attention des actions sont à exécuter au début et à al fin de chaque événement administratif :
    def actionFinConduiteVehicule():
        global situation_

label decPermis:
    $ actionDebutConduiteVehicule()
    "Vous êtes éligible au permis et vous avez les moyens de vous le payer."
    menu:
        "Cela vous intéresse-t'il ?."
        "Oui c'est parti.":
            jump decPermis_debut
        "Plus tard peut-être.":
            jump decPermis_fin
        "Jamais.":
            $ situation_.SetCarac("decPermisJamais", 1)
            jump decPermis_fin
        "Vous préféreriez le permis moto.":
            jump decPermisMoto
        "Vous préféreriez le permis cheval.":
            jump decPermisCheval
        "Vous préféreriez le permis spécifique voiture volante.":
            jump decPermisVoitureVolante

    label decPermisMoto:
        "decPermisMoto pas fait"
        jump decPermis
    label decPermisCheval:
        "decPermisCheval pas fait"
        jump decPermis
    label decPermisVoitureVolante:
        "decPermisVoitureVolante pas fait"
        jump decPermis
    label decPermis_debut:
        "Vous prenez un peu de temps pour apprendre le code de la route ; dès la semaine suivante vous participez à vos premiers entrainements au code."
        show moniteur_auto_ecole at right
        with moveinright
        monit "Quarante questions, une minute par question. C'est parti on se revoit pour la correction."
        "Les questions sont bien plus difficiles et ambiguës que vous ne l'auriez cru."
        $ diffCode = 4
        $ affdiffCode = situation_.AffichagePourcentageReussite(trait.Intelligence.NOM, diffCode)
        menu:
            "Voyons le résultat. [affdiffCode]":
                jump decPermis_PremierCode

        label decPermis_PremierCode:
            $ reussi = situation_.TesterDifficulte(trait.Intelligence.NOM, diffCode)
            if reussi:
                "11/20"
                monit "Ça n'a pas l'air impressionnant mais c'est un bon résultat pour un premier essai."
            else:
                "04/20"
                monit "Hum il a eu des difficultés mais c'est le tout début."
                $ situation_.RetirerACarac(trait.Assurance.NOM, 1)
            monit "Les questions posées à ce test sont plus difficiles que celles du test de code final."
            monit "Si il s'entraîne régulièrement je suis sûr qu'il l'aura."
            jump decPermis_PremiereConduite

        label decPermis_PremiereConduite:
            "Deux jours plus tard vous suivez votre première leçon de conduite."
            monit "Je m'occupe des pédales et du changement de vitesse, qu'il se contente du volant et de bien observer."
            monit "On va rester dans une zone sans passant ni voitures le temps de faire quelques tours."
            $ affdiffCode = situation_.AffichagePourcentageReussite(trait.Observation.NOM, diffCode)
            menu:
                "Vous roulez le long d'une file de voitures garées. [affdiffCode]":
                    jump decPermis_PremiereConduite_1

            label decPermis_PremiereConduite_1:
                $ reussi = situation_.TesterDifficulte(trait.Observation.NOM, diffCode)
                if reussi:
                    monit "Bravo tu as une bonne tenue de route, tu vas pouvoir commencer à essayer de passer des vitesses."
                else:
                    "Le moniteur attrape le volant brusquement et fait un léger écart."
                    monit "He ben il veut arracher des rétroviseurs ou quoi ?"
                    monit "Faut pas qu'il prenne des risques comme ça pour rien."
                    monit "Faut qu'il reste détendu."
                    $ situation_.RetirerACarac(trait.Assurance.NOM, 1)
                monit "La prochaine fois il essayera quelques manoeuvres. Mais il faut qu'il continue les leçons de code surtout."
                jump decPermis_PremiereManoeuvre

                label decPermis_PremiereManoeuvre:
                    monit "Cette fois il va apprendre des manoeuvres de base."
                    monit "Qu'il essaye de stationner entre les deux voitures là bas. Il a deux fois plus de place que nécessaire."
                    $ affdiffCode = situation_.AffichagePourcentageReussite(trait.Habilete.NOM, diffCode)
                    menu:
                        "Vous approchez de l'emplacement désigné. [affdiffCode]":
                            jump decPermis_PremiereManoeuvre_1

                    label decPermis_PremiereManoeuvre_1:
                        $ reussi = situation_.TesterDifficulte(trait.Habilete.NOM, diffCode)
                        if reussi:
                            "Vous parvenez à vous glisser entre les voitures et à vous garer presque aligné au trottoir."
                        else:
                            "Après six essais infructueux pour se rapprocher le moniteur finit par accompagner tous vos mouvements pour réussir un stationnement potable."
                            $ situation_.RetirerACarac(trait.Assurance.NOM, 1)
                        monit "Bien. La prochaine fois on fera le stationnement en épi. Ramène nous à l'auto-école, c'est moi qui garerai la voiture."
                        jump decPermis_PasserPermis

                        label decPermis_PasserPermis:
                            "Les jours se suivent et vous faites de sensibles progrès. Enfin le moniteur vous juge prêt."
                            $ affdiffCode = situation_.AffichagePourcentageReussite(\
                                [trait.Habilete.NOM, trait.Assurance.NOM, trait.Intelligence.NOM, trait.Observation.NOM], diffCode)
                            menu:
                                "C'est le grand jour. [affdiffCode]":
                                    jump decPermis_PasserPermis_1
                            label decPermis_PasserPermis_1:
                                $ nivReussite = situation_.TesterDegreReussite([trait.Habilete.NOM, trait.Assurance.NOM, trait.Intelligence.NOM, trait.Observation.NOM], diffCode)
                                if nivReussite>0:
                                    "Bravo c'est une réussite vous avez maintenant le code et le permis."
                                    $ AjouterACarac(trait.Assurance.NOM, 2)
                                    $ SetCarac(trait.Pilotage.NOM, 1)
                                    jump decPermis_fin
                                elif nivReussite <-1:
                                    "C'est un échec catastrophique. Vous êtes tellement angoissé que vous démarrez avec le frein à main enclenché. Vous avez même failli causer un accident."
                                    "L'examinateur ne s'abaisse même pas à vous dire à que c'est un échec."
                                    $ situation_.RetirerACarac(trait.Assurance.NOM, 2)
                                    jump decPermis_ReessayerPermis
                                else:
                                    "Vous faites presque un sans faute mais une erreur d'inattention et une petite erreur de code vous font échouer."
                                    monit "Il a fait une petite erreur mais il fera mieux la prochaine fois."
                                    $ AjouterACarac(trait.Assurance.NOM, 1)
                                    jump decPermis_ReessayerPermis
                                label decPermis_ReessayerPermis:
                                    $ diffRepasser = 2
                                    $ affdiffRepasser = situation_.AffichagePourcentageReussite(trait.Assurance.NOM, diffRepasser)
                                    menu:
                                        "Voulez vous tenter de repasser le permis ?"
                                        "Oui [affdiffRepasser]":
                                            $ reussi = situation_.TesterDifficulte(trait.Assurance.NOM, diffRepasser)
                                            if reussi:
                                                jump decPermis_ReessayerPermis_Payer
                                            else:
                                                "Vous avez perdu toute confiance en vos capacités, et puis vous détestez conduire. Tant pis vous abandonnez. Une autre fois peut-être ?"
                                                jump decPermis_fin
                                        "Non":
                                            jump decPermis_fin
                                label decPermis_ReessayerPermis_Payer:
                                    $ situation_.TourSuivant() # le temps passe
                                    $ affdiffRepasser = situation_.AffichagePourcentageReussite(trait.Richesse.NOM, diffRepasser)
                                    menu:
                                        "Il va falloir reprendre plusieurs leçons [affdiffRepasser]":
                                            $ reussi = situation_.TesterDifficulte(trait.Richesse.NOM, diffRepasser)
                                            if not reussi:
                                                "Ça commence à coûter cher."
                                                $ situation_.RetirerACarac(trait.Richesse.NOM, 2)
                                            jump decPermis_PasserPermis

    label decPermis_fin:
    $ actionFinConduiteVehicule()
    jump fin_cycle

label decAccident:
    $ actionDebutConduiteVehicule()
    "Alors que vous roulez à grande vitesse sur une nationale en banlieue parisienne votre voiture dérape violemment et vous perdez le contrôle."
    $ diffRepriseControle = 6
    $ affPilotageExpert = situation_.AffichagePourcentageReussite(trait.Pilotage.NOM, diffRepriseControle)
    $ diffRouleBoule = 6
    $ affHabileteExpert = situation_.AffichagePourcentageReussite(trait.Habilete.NOM, diffRouleBoule)
    menu:
        "Vous allez heurter un camion à pleine vitesse."
        "vous tentez de reprendre le contrôle. [affPilotageExpert]":
            jump decAccident_repriseControle
        "vous sautez en marche. [affHabileteExpert]":
            jump decAccident_SauteEnMarche
        "Vous vérifiez votre ceinture et vous préparez au choc.":
            jump decAccident_Choc

    label decAccident_SauteEnMarche:
        $ reussi = situation_.TesterDifficulte(trait.Habilete.NOM, diffRouleBoule)
        if reussi:
            "Vous bondissez de la voiture dans un superbe roulé boulé d'expert."
            "Devant vous la voiture continue sa trajectoire à pleine vitesse et percute le camion."
            "La voiture est broyée, toutes ses vitres éclatent."
            "Mais vous vous en sortez avec seulement quelques égratinures et des douleurs dans les articulations."
            "Vous avez même la force de vous trainer au borde la route pour éviter d'être écrasé."
            jump decAccident_assuranceVoiture
        else:
            "Vous bondissez de la voiture mais c'est déjà dangereux à petite vitesse, sur l'autoroute c'est presque du suicide."
            "Vous vous brisez plusieurs os dans votre chute et restez inconscient."
            $ resisteBlessure = situation_.TesterDifficulte(trait.Constitution.NOM, 7)
            if resisteBlessure:
                jump decAccident_blessureLegere
            else:
                jump decAccident_blessureGrave

    label decAccident_repriseControle:
        $ reussi = situation_.TesterDifficulte(trait.Pilotage.NOM, diffRepriseControle)
        if reussi:
            "Vous effectuez un dérapage contrôlé exceptionnel qui vous permet de glisser avec une relative douceur jusqu'au bord de la route."
            jump decAccident_fin
        else:
            "Impossible de reprendre le contrôle, vous arrivez sur le camion à pleine vitesse."
            $ resisteBlessure = situation_.TesterDifficulte(trait.Constitution.NOM, 7)
            if resisteBlessure:
                jump decAccident_blessureLegere
            else:
                jump decAccident_blessureGrave

    label decAccident_Choc:
        "Vous avez moins d'une seconde pour constater que votre ceinture était bien attachée puis vous vous couvrez le visage."
        $ resisteBlessure = situation_.TesterDifficulte(trait.Constitution.NOM, 6)
        if resisteBlessure:
            jump decAccident_blessureLegere
        else:
            jump decAccident_blessureGrave

    label decAccident_blessureLegere:
        show medecin_peste at right
        with moveinright
        $ blessure = blessures_.InfligerBlessureAleatoire(situation_, 0, 5)
        jump decAccident_blessureTexte

    label decAccident_blessureGrave:
        show medecin_peste at right
        with moveinright
        $ blessure = blessures_.InfligerBlessureAleatoire(situation_, 6, 10)
        jump decAccident_blessureTexte

    label decAccident_blessureTexte:
        $ texteBlessure = blessure.GetDescriptionRecu()
        "[texteBlessure]."
        jump decAccident_assuranceVoiture

    label decAccident_assuranceVoiture:
        # pour tester si les frais l'appauvrissent on fait un test de richesse (substitut pour l'assurance)
        $ diffAssurance = 4
        $ affdiffAssurance = situation_.AffichagePourcentageReussite(trait.Richesse.NOM, diffAssurance)
        menu:
            "La voiture est dans un état catastrophique. [affdiffAssurance]":
                $ reussi = situation_.TesterDifficulte(trait.Richesse.NOM, diffAssurance)
                if not reussi:
                    "L'assurance couvre très mal les frais de réparation, la réparation vous revient cher."
                    $ situation_.RetirerACarac(trait.Richesse.NOM, 2)
        "Mais c'est l'affaire d'un mois avant d'en avoir une nouvelle, avec cette fois de meilleurs freins espérons le."

    label decAccident_fin:
        $ actionFinConduiteVehicule()
        jump fin_cycle
