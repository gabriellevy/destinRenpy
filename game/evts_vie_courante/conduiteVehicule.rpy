image medecin_peste = "medecine/medecin_peste.png"

define med = Character('Médecin', who_outlines=[(2, "#894646",1,1)], color="#580404")

init -5 python:
    import random
    from despin.gen_vie import declencheur
    from despin.gen_vie import selecteur
    from despin.gen_vie import proba
    from despin.abs import condition
    from extremis.socio_eco import metier
    from despin.reglages import filtres_action
    from extremis.humanite import trait
    from extremis.constitution import temps

    def AjouterEvtsPilotage():
        global selecteur_
        conditionSaitConduire = condition.Condition(trait.Pilotage.NOM, 1, condition.Condition.SUPERIEUR_EGAL)
        conditionAgePermis = condition.Condition(temps.Date.AGE_ANNEES, 18, condition.Condition.SUPERIEUR_EGAL)
        pas_decPermisJamais = condition.Condition("decPermisJamais", 1, condition.Condition.DIFFERENT)
        pasTropPauvre = condition.Condition(trait.Richesse.NOM, trait.Trait.SEUIL_A_PAS_EXTREME, condition.Condition.SUPERIEUR) # substitut pour ' a les moyens d'avoir une voiture'

        decAccident = declencheur.Declencheur(0.02, "decAccident")
        decAccident.AjouterCondition(conditionSaitConduire)
        selecteur_.ajouterDeclencheur(decAccident)

        decPermis = declencheur.Declencheur(10.02, "decPermis")
        decPermis.AjouterCondition(conditionAgePermis)
        decPermis.AjouterCondition(pasTropPauvre)
        decPermis.AjouterCondition(pas_decPermisJamais)
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
            jump decAccident_debut
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
    label decPermisCheval:
        "decPermisCheval pas fait"
    label decPermisVoitureVolante:
        "decPermisVoitureVolante pas fait"
    label decPermis_debut:
        "decPermis_debut pas fait"

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
            $ resisteBlessure = situation_.TesterDifficulte(trait.Resistance.NOM, 7)
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
            $ resisteBlessure = situation_.TesterDifficulte(trait.Resistance.NOM, 7)
            if resisteBlessure:
                jump decAccident_blessureLegere
            else:
                jump decAccident_blessureGrave

    label decAccident_Choc:
        "Vous avez moins d'une seconde pour constater que votre ceinture était bien attachée puis vous vous couvrez le visage."
        $ resisteBlessure = situation_.TesterDifficulte(trait.Resistance.NOM, 6)
        if resisteBlessure:
            jump decAccident_blessureLegere
        else:
            jump decAccident_blessureGrave

    label decAccident_blessureLegere:
        show medecin_peste at right
        with moveinright
        "decAccident_blessureLegere -> PAS FAIT"

    label decAccident_blessureGrave:
        show medecin_peste at right
        with moveinright
        "decAccident_blessureGrave -> PAS FAIT"

    label decAccident_assuranceVoiture:
        "decAccident_assuranceVoiture -> PAS FAIT"
        "Faire une genre de test sur le niveau d'assurance du personnage pour voir si il perd de la richesse."

    label decAccident_fin:
    $ actionFinConduiteVehicule()
    jump fin_cycle
