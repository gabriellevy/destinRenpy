# musiques
define audio.principale_orks = "musique/orks/principale.mp3"

# persos
image instructeur_ork = "coteries/orks/persos/instructeur_ork.png"
define instructeur_ork = Character('Instructeur', color="#001a00")

init -5 python:
    import random
    from extremis.coteries.orks import orks
    from extremis.socio_eco.metiers import metier
    from extremis.religions import religion
    from extremis.humanite.sante import pbsante

    conditionDansUnivOrks = condition.Condition(coterie.Coterie.Carac_UNIV_COURANTE, orks.Orks.ID, condition.Condition.EGAL)

    def AjouterEvtsUnivOrks():
        """
        Quand on s'enrôle dans une université on doit accomplir un certain nombre de modules
        """
        global selecteur_

        # très forte chance (proba absolue) de suivre des modules tant qu'on n'en a pas fait 6
        univOrks = declencheur.Declencheur(proba.Proba(0.6, False), "univOrks")
        univOrks.AjouterCondition(conditionDansUnivOrks)
        selecteur_.ajouterDeclencheur(univOrks)

    def evtUnivOrksSuivant():
        global situation_

        evts = ["univOrks_evt1", "univOrks_evt2", "univOrks_evt3",
        "univOrks_evt4", "univOrks_evt5", "univOrks_evt6",
        "univOrks_evt7", "univOrks_evt8", "univOrks_evt9",
        "univOrks_evt10", "univOrks_evt11", "univOrks_evt12" ]

        prochainEvt = random.choice(evts)
        while situation_.GetValCaracInt(prochainEvt) == 1:
            prochainEvt = random.choice(evts)

        situation_.SetValCarac(prochainEvt, 1)
        renpy.jump( prochainEvt)

label univOrks:
    scene bg poissy

    $ situation_.SetCarac(coterie.Coterie.Carac_UNIV_COURANTE, orks.Orks.ID)
    $ numMoisRestants = situation_.GetValCaracInt(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE)
    if numMoisRestants == coterie.Coterie.NB_MOIS_UNIV_TOTAL_A_FAIRE:
        # intro :
        play music principale_orks
        "Les orks sont des mutants qui embrassent avant tout une vie simple et brutale sans prise de tête."

    if numMoisRestants < 1:
        # fin d'université
        $ situation_.SetCarac(coterie.Coterie.Carac_UNIV_COURANTE, "")
        jump decUnivCoterie
    else:
        $ situation_.RetirerACarac(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE, 1)
        $ situation_.TourSuivant()
        $ evtUnivOrksSuivant()
    jump fin_cycle

label univOrks_evt1:
    # blessure dans la fosse
    scene bg fosse
    $ blessure = blessures_.InfligerBlessureAleatoire(situation_, 0, 7)
    $ texteBlessure = blessure.GetDescriptionRecu()
    "Au cours d'un entrainement au combat dans les fosses vous recevez une blessure : [texteBlessure]"
    "Les orks en rigolent un bon coup et vous tappent dans le dos joyeusement."
    show instructeur_ork at right
    with moveinright
    instructeur_ork "Tu verras quand tu s'ras un vrai ork ça r'poussera"
    $ AjouterACarac(metier.Guerrier.NOM, 1)
    jump fin_cycle

label univOrks_evt2:
    # fou de la vitesse
    scene bg buggy
    "Tout ork se doit de savoir piloter les bolides et aimer la vitesse. Vos instructeurs font en sorte que vous fassiez un bon paquet de tours de pistes sans faire vot' mauviet'."
    $ test = testDeCarac.TestDeCarac(metier.Chauffeur.NOM, 4, situation_)
    menu:
        "Attention au virage [test.affichage_]":
            pass
    $ reussi = test.TesterDifficulte(situation_)
    if reussi:
        "Votre maîtrise impressionne votre instructeur."
    else:
        $ blessure = blessures_.InfligerBlessureAleatoire(situation_, 0, 7)
        $ texteBlessure = blessure.GetDescriptionRecu()
        "Malheureusement vous faites quelques chutes violentes sous les moqueries de votre instructeur. Vous avez maintenant la blessure : [texteBlessure]"

    $ AjouterACarac(metier.Chauffeur.NOM, 2)
    jump fin_cycle

label univOrks_evt3:
    # pilote d'avion
    scene bg avion_ork
    "Les autres coteries se moquent de l'aspect rudimentaire de la technologie ork et pourtant ils sont une des rares à être capable de produire et faire tourner des avions grâces à leurs techniques très économiques en énergie."
    "Votre instructeur vous offre l'insigne honneur de voler avec lui et vous montre les bases du pilotage."
    $ AjouterACarac(metier.Pilotage.NOM, 2)
    jump fin_cycle

label univOrks_evt4:
    # soulé à la bière
    "Personne ne respecte un ork qui ne tient pas la bière aux champignons. Votre instructeur fait en sorte que vous goûtiez de tous les alcools ork. Et en grande quantité."
    "Aucun humain ayant subi une telle épreuve n'en ressort indemne."

    $ resProba = random.uniform(0, 1.0)
    if resProba <= 0.3:
        "Votre organisme est durement affecté."
        $ RetirerACarac(trait.Constitution.NOM, 1)
    elif resProba > 0.7:
        "Après des gueules de bois violentes vous êtes surpris de constater que vous vous êtes habitué même à leurs pires bières frelatées."
        $ AjouterACarac(trait.Constitution.NOM, 1)

    $ resProba = random.uniform(0, 1.0)
    if resProba <= 0.4:
        "Toutes vos angoisses profondes fondent définitivement."
        $ AjouterACarac(trait.Serenite.NOM, 1)

    $ resProba = random.uniform(0, 1.0)
    if resProba <= 0.5:
        "Durablement affecté par la boisson empoisonnée mais violemment addictive, vous devenez alcoolique."
        $ maladie = maladies_.TomberMaladeStr(situation_, pbsante.Alcoolisme.NOM)

    $ resProba = random.uniform(0, 1.0)
    if resProba <= 0.2:
        "L'alcool vous a salement endommagé le cerveau."
        $ RetirerACarac(trait.Intelligence.NOM, 1)
        $ RetirerACarac(trait.Intellectualisme.NOM, 1)

    $ resProba = random.uniform(0, 1.0)
    if resProba <= 0.2:
        "L'alcool est tellement persistant qu'il vous fait sauter vos inhibitions et votre prudence sur le coup mais aussi à long terme."
        $ AjouterACarac(trait.Assurance.NOM, 1)
        $ AjouterACarac(trait.Franchise.NOM, 1)
    jump fin_cycle

label univOrks_evt5:
    # formation mékano
    scene bg mekano
    "Un mékano a remarqué vos capacités et vous a formé aux bases de la réparation de moteurs. Bien que sa technique semble rudimentaire à première vue il est véritablement doué et très entousiaste comme enseignant."
    "Il vous promet que quand vous serez un vrai ork il vous apprendra à fabriquer des armes, ce qui est encore plus rigolo."
    $ AjouterACarac(metier.Mecanicien.NOM, 1)
    jump fin_cycle

label univOrks_evt6:
    # formation médiko
    "Un médiko a remarqué vos capacités et vous a formé aux bases de la rudimentaire médecine ork."
    "Leur vrai point fort est leur obsession des améliorations bioniques combinée à la capacité des patients orques à accepter à peu près toutes les greffes. "
    $ AjouterACarac(metier.Medecin.NOM, 1)
    $ AjouterACarac(metier.Cyberneticien.NOM, 1)

    $ resProba = random.uniform(0, 1.0)
    if resProba <= 0.8:
        "Malheureusement il en profite pour faire des expériences amusantes sur vous après vous avoir assomé avec un maillet."
        $ blessure = blessures_.InfligerBlessureAleatoire(situation_, 0, 4)
        $ texteBlessure = blessure.GetDescriptionRecu()
        "Vous avez maintenant la blessure : [texteBlessure]"

        # QString bionique = Bionique::AppliquerBionique(humain);
        # "\nEt vous avez le bionique : " + bionique
    jump fin_cycle

label univOrks_evt7:
    "univOrks_evt7 PAS FAIT"
    jump fin_cycle

label univOrks_evt8:
    "univOrks_evt8 PAS FAIT"
    jump fin_cycle

label univOrks_evt9:
    "univOrks_evt9 PAS FAIT"
    jump fin_cycle

label univOrks_evt10:
    "univOrks_evt10 PAS FAIT"
    jump fin_cycle

label univOrks_evt11:
    "univOrks_evt11 PAS FAIT"
    jump fin_cycle

label univOrks_evt12:
    "univOrks_evt12 PAS FAIT"
    jump fin_cycle
