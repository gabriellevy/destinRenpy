# musiques
define audio.principale_transhumaniste = "musique/transhumanistes/Iron Man Menu DVD.MP3"

init -5 python:
    import random
    from extremis.coteries.transhumanistes import transhumanistes
    from extremis.socio_eco.metiers import metier
    from abs.religions import religion

    def AjouterEvtsUnivTranshumanistes():
        """
        Quand on s'enrôle dans une université on doit accomplir un certain nombre de modules
        """
        global selecteur_
        conditionDansUniv = condition.Condition(coterie.Coterie.Carac_UNIV_COURANTE, transhumanistes.Transhumanistes.ID, condition.Condition.EGAL)

        # très forte chance (proba absolue) de suivre des modules tant qu'on n'en a pas fait 6
        univTranshumanistes = declencheur.Declencheur(proba.Proba(0.6, False), "univTranshumanistes")
        univTranshumanistes.AjouterCondition(conditionDansUniv)
        selecteur_.ajouterDeclencheur(univTranshumanistes)

    def evtUnivTranshumanistesSuivant():
        global situation_

        evts = ["univTranshumanistes_evt1", "univTranshumanistes_evt2", "univTranshumanistes_evt3",
        "univTranshumanistes_evt4", "univTranshumanistes_evt5", "univTranshumanistes_evt6",
        "univTranshumanistes_evt7", "univTranshumanistes_evt8", "univTranshumanistes_evt9",
        "univTranshumanistes_evt10", "univTranshumanistes_evt11", "univTranshumanistes_evt12" ]

        prochainEvt = random.choice(evts)
        while situation_.GetValCaracInt(prochainEvt) == 1:
            prochainEvt = random.choice(evts)

        situation_.SetValCarac(prochainEvt, 1)
        renpy.jump( prochainEvt)

label univTranshumanistes:
    scene bg univ_transhumanistes

    $ situation_.SetCarac(coterie.Coterie.Carac_UNIV_COURANTE, transhumanistes.Transhumanistes.ID)
    $ numMoisRestants = situation_.GetValCaracInt(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE)
    if numMoisRestants == coterie.Coterie.NB_MOIS_UNIV_TOTAL_A_FAIRE:
        # intro :
        play music principale_transhumaniste
        "Les transhumanistes sont la coterie qui embrasse le plus la technologie moderne surtout dans tout ce qui s'applique à la transformation de l'humain. "
        "Ils s'obsèdent en particulier pour la cybernétique et les modifications génétiques et ils sont très loin en avance sur toutes les autres coteries à ce sujet."
        "L'université transhumanistes est un magnifique gratte-ciel d'acier et de verre qui contient tout un campus : les salles de cours, les dortoirs, et une quantité incroyable de bars et de distractions hors de prix."

    $ numMoisRestants = situation_.GetValCaracInt(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE)
    if numMoisRestants < 1:
        # fin d'université
        $ situation_.SetCarac(coterie.Coterie.Carac_UNIV_COURANTE, "")
        jump decUnivCoterie
    else:
        $ situation_.RetirerACarac(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE, 1)
        $ situation_.TourSuivant()
        $ evtUnivTranshumanistesSuivant()
    jump fin_cycle

label univTranshumanistes_evt1:
    # cours scientifique
    scene bg labo
    "La génétique et la cybernétique sont les base du transhumanisme. Une initiation à ces sciences est indispensable dans cette université. "
    "Sans être d'un niveau professionnel vous ressortirez de cette université avec des connaissances très avancées. Vous ressortirez aussi avec les poches moins lourdes car cette université est réellement hors de prix."
    $ AjouterACarac(metier.Geneticien.NOM, 1)
    $ AjouterACarac(metier.Cyberneticien.NOM, 1)
    $ RetirerACarac(trait.Richesse.NOM, 1)
    jump fin_cycle

label univTranshumanistes_evt2:
    # cours informatique
    scene bg informatique
    "L'informatique est indispensable pour garder en fonctionnement les nombreuses organisations techniquement avancées des transhumanistes. "
    "L'université comprend bien sûr des cours variés dans cette discipline."
    $ AjouterACarac(metier.Informaticien.NOM, 1)
    $ RetirerACarac(trait.Richesse.NOM, 1)
    jump fin_cycle

label univTranshumanistes_evt3:
    # cours de commerce
    "La base de la philosophie libérale transhumaniste est que tout se vend. Les produits et les améliorations cybernétique bien sûr. Mais un politique se vend aussi à son électorat comme un gendre à sa belle famille."
    "Que vous fassiez carrière dans le commerce ou pas ces cours de commerce et de manipulation seront utiles."
    $ AjouterACarac(metier.Commercial.NOM, 1)
    $ RetirerACarac(trait.Richesse.NOM, 1)
    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.5:
        $ AjouterACarac(trait.Cupidite.NOM, 1)
    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.5:
        $ AjouterACarac(trait.Charme.NOM, 1)
    jump fin_cycle

label univTranshumanistes_evt4:
    # cours de philosophie libérale transhumaniste
    "Toute coterie a une forme de philosophie et celle des transhumanistes est une des plus développée. Tout vous est expliqué sur plusieurs mois. Du matérialisme au libéralisme. "
    "Le progrès est central et l'amélioration de l'humain en tant qu'individu complet est le but final de toute la coterie. Vous en ressortez transformé."
    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.5:
        $ RetirerACarac(trait.Altruisme.NOM, 1)
    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.5:
        $ AjouterACarac(trait.Ambition.NOM, 1)
    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.5:
        $ AjouterACarac(trait.Cupidite.NOM, 1)
    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.5:
        $ AjouterACarac(trait.Opportunisme.NOM, 1)
    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.5:
        $ AjouterACarac(trait.Individualisme.NOM, 1)
    $ RetirerACarac(trait.Richesse.NOM, 1)
    # Ajouter quand la religion sera ajoutée

    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.5:
        $ devientAthee = devientAthee()
        if devientAthee:
            "Vous avez perdu la foi."

    jump fin_cycle

label univTranshumanistes_evt5:
    # petits boulots
    "L'université transhumaniste est hors de prix. Vous êtes obligé de prendre des petits boulots à côté pour vous en sortir."
    "L'université voit cela d'un bon oeil car ça donne de la main d'oeuvre pas cher à son conglomérat et forme les étudiants au monde du travail."
    $ RetirerACarac(trait.Richesse.NOM, 2)
    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.5:
        $ AjouterACarac(trait.Industrie.NOM, 1)
    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.5:
        $ RetirerACarac(trait.Serenite.NOM, 1)
    jump fin_cycle

label univTranshumanistes_evt6:
    # faire la fête
    scene bg boite_de_nuit
    "L'université transhumaniste n'est pas juste un lieu d'apprentissage universitaire, c'est aussi un lieu de vie et de consommation unique dans tout Extremis. "
    "Impossible de passer à côté des fêtes innombrables, toutes plus surprenantes et chères les unes que les autres."
    $ RetirerACarac(trait.Richesse.NOM, 1)
    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.5:
        $ RetirerACarac(trait.Ascetisme.NOM, 1)
    jump fin_cycle

label univTranshumanistes_evt7:
    # robotique
    scene bg robotique
    "Même si elle n'est pas très répandue dans la société, la robotique est très avancée. Le consul en est la meilleure preuve. Mais rares sont les coteries à la maîtriser."
    "Bien que ce ne soit pas leur domaine de prédilection les transhumanistes tiennent à y tenir leur place comme dans toutes les techniques avancées. Vous recevez donc une formation sommaire."
    $ AjouterACarac(metier.Robotique.NOM, 1)
    $ AjouterACarac(metier.Electronique.NOM, 1)
    jump fin_cycle

label univTranshumanistes_evt8:
    # séminaire de confiance en soi
    "Un bon humaniste se doit d'avoir foi en l'avenir. Un bon séminaire de motivation par l'hypnose et l'effet de foule et vous ne douterez plus jamais de vous et de ce que vous méritez."
    $ AjouterACarac(trait.Assurance.NOM, 3)
    jump fin_cycle

label univTranshumanistes_evt9:
    # médecine
    "Le but principal des transhumanistes est la perfection du corps humain. La médecine en est l'indispensable premier pas et ses bases sont dans le programme."
    $ AjouterACarac(metier.Medecin.NOM, 1)
    jump fin_cycle

label univTranshumanistes_evt10:
    $ professionLaPlusMaitrisee = DeterminerProfessionLaPlusMaitrisee()
    if professionLaPlusMaitrisee == "":
        jump univTranshumanistes_evt1
    "La société transhumaniste est fonctionnelle et la plus optimisée possible. Plutôt que multiplier les connaissances ils préfèrent vous pousser à vous spécialiser là où vous avez déjà des bonnes bases, pour que vous deveniez un bon [professionLaPlusMaitrisee]."
    $ AjouterACarac(professionLaPlusMaitrisee, 1)
    jump fin_cycle

label univTranshumanistes_evt11:
    "univTranshumanistes_evt11 PAS FAIT"
    jump fin_cycle
label univTranshumanistes_evt12:
    "univTranshumanistes_evt12 PAS FAIT"
    jump fin_cycle

label transhumanistesPostule:
    scene bg univ_transhumanistes
    "Postulation aux Transhumanistes : pas fait !"
    jump fin_cycle
