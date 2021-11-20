init -5 python:
    import random
    from extremis.coteries.elfes import elfes
    from abs.humanite import metier
    from abs.religions import religion

    def AjouterEvtsUnivElfes():
        """
        Quand on s'enrôle dans une université on doit accomplir un certain nombre de modules
        """
        global selecteur_
        conditionDansUniv = condition.Condition(coterie.Coterie.Carac_UNIV_COURANTE, elfes.Elfes.ID, condition.Condition.EGAL)

        # très forte chance (proba absolue) de suivre des modules tant qu'on n'en a pas fait 6
        univElfes = declencheur.Declencheur(proba.Proba(0.6, False), "univElfes")
        univElfes.AjouterCondition(conditionDansUniv)
        selecteur_.ajouterDeclencheur(univElfes)

    def evtUnivElfesSuivant():
        global situation_

        evts = ["univElfes_evt1", "univElfes_evt2", "univElfes_evt3",
        "univElfes_evt4", "univElfes_evt5", "univElfes_evt6",
        "univElfes_evt7", "univElfes_evt8", "univElfes_evt9",
        "univElfes_evt10", "univElfes_evt11", "univElfes_evt12" ]

        prochainEvt = random.choice(evts)
        while situation_.GetValCaracInt(prochainEvt) == 1:
            prochainEvt = random.choice(evts)

        situation_.SetValCarac(prochainEvt, 1)
        renpy.jump( prochainEvt)

label univElfes:
    scene bg univ_elfes

    $ situation_.SetCarac(coterie.Coterie.Carac_UNIV_COURANTE, elfes.Elfes.ID)
    $ numMoisRestants = situation_.GetValCaracInt(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE)
    if numMoisRestants == coterie.Coterie.NB_MOIS_UNIV_TOTAL_A_FAIRE:
        # intro :
        "intro univ elfes PAS FAITE. "

    if numMoisRestants < 1:
        # fin d'université
        $ situation_.SetCarac(coterie.Coterie.Carac_UNIV_COURANTE, "")
        jump decUnivCoterie
    else:
        $ situation_.RetirerACarac(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE, 1)
        $ situation_.TourSuivant()
        $ evtUnivElfesSuivant()
    jump fin_cycle

label univElfes_evt1:
    # est rendu plus beau
    $ beaute = situation_.GetValCaracInt(trait.Beaute.NOM)
    if beaute < 1 :
        "Votre laideur offense tellement vos maître qu'ils font une priorité de vous rendre présentable."
    else:
        "La beauté est primordiale pour les elfes et ils font en sorte que votre médiocrité ne soit pas un frein pour vous intégrer et vous sentir l'un des leurs. "
    "Pour cela ils utilisent une myriades d'outils et d'objets merveilleux. Des pommades, des bains, des amulettes et même des potions enchantées."
    "Le résultat est stupéfiant. "
    $ AjouterACarac(trait.Beaute.NOM, 2)
    jump fin_cycle

label univElfes_evt2:
    # effet devient artiste
    "Tous les elfes doivent être artistes, sinon ils redeviennent lentement de simples humains. "
    "L'université se doit de consacrer un grand nombre d'heures à rendre votre esprit ouvert à l'art et à la beauté."
    $ AjouterACarac(trait.Artiste.NOM, 2)
    jump fin_cycle

label univElfes_evt3:
    # effet frustration sexuelle
    "Vous êtes fasciné et tout émoustillé par la quantité incroyable de jeunes beautés que vous rencontrez à l'université elfique. "
    "Malheureusement elles n'ont que mépris et moquerie pour vous et votre physique médiocre."
    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.6:
        "Vous en intériosez une forte angoisse sur votre propre valeur."
        $ situation_.RetirerACarac(trait.Serenite.NOM, 1)
    elif resProba < 0.75:
        "Vous trouvez ça injuste et vous sentez profondément énervé contre elles et contre la société en général."
        $ AjouterACarac(trait.Violence.NOM, 1)
    else:
        "Vous décidez de vous concentrer sur votre propre amélioration et enrichissement pour un jour avoir votre chance avec une femme aussi belle"
        $ AjouterACarac(trait.Ambition.NOM, 1)
    jump fin_cycle

label univElfes_evt4:
    # effet devient Musicien
    scene bg musicien
    if situation_.GetValCarac(trait.Artiste.NOM) < 1:
        jump univElfes_evt2
    "Vu votre potentiel d'artiste les elfes trouvent indispensable de vous former à la musique, le plus noble de tous les arts."
    $ AjouterACarac(metier.Musicien.NOM, 1)
    jump fin_cycle

label univElfes_evt5:
    # effet devient Poète
    scene bg poesie
    if situation_.GetValCarac(trait.Artiste.NOM) < 1:
        jump univElfes_evt2
    "Vu votre potentiel d'artiste les elfes trouvent indispensable de vous former à la poésie, la pierre angulaire de la sensibilité elfique."
    $ AjouterACarac(metier.Poete.NOM, 1)
    jump fin_cycle

label univElfes_evt6:
    # effet devient Alchimiste
    scene bg alchimiste
    "La fabrication de potions, de filtres, de pommades est une composante essentielle de l'art elfique. "
    "Leurs usages sont innombrables et vont de potions de soins aux meilleurs produits de beauté du monde. "
    "Un maître herboriste détecte un certain potentiel chez vous et décide de vous apprendre les bases."
    $ AjouterACarac(metier.Alchimiste.NOM, 1)
    jump fin_cycle

label univElfes_evt7:
    # effet devient Cuisinier
    "L'art de vivre elfique est légendaire. Il touche tous les aspects de la vie, de l'achitecture des plus grands édifices à la cuisine de tous les jours."
    "Vos maîres vous font travailler la préparation des mets de base de la cuisine elfique. Que vous deveniez cuisiner ou pas il est hors de question de vivre sans ces compétences."
    $ AjouterACarac(metier.Cuisinier.NOM, 1)
    jump fin_cycle

label univElfes_evt8:
    # effet devient acteur
    "La vie des elfes est une représentation permanente. Même quand ils ne font pas théâtre amateur pendant leurs loisirs ils deviennent inévitablement un peu comédien ne serait-ce que par l'application des innombrables usages de leur société."
    "Vous faites tout votre possible pour vous intégrer dans cet étrange système."
    $ AjouterACarac(metier.Acteur.NOM, 2)
    $ RetirerACarac(trait.Sincerite.NOM, 1)
    jump fin_cycle

label univElfes_evt9:
    # Méditation
    "Les elfes vivent une vie calme et douce, loin du stress des humains. Vous appreznez à leur contact à méditer dans la paix et la sérénité."
    $ AjouterACarac(trait.Serenite.NOM, 2)
    $ RetirerACarac(trait.Cupidite.NOM, 1)
    $ RetirerACarac(trait.Opportunisme.NOM, 1)
    jump fin_cycle

label univElfes_evt10:
    # Sensibilité
    "Au contact des elfes et au fur et à mesure que vous ouvrez votre esprit vous commencez à percevoir des beautés que vous ne soupçonniez pas autour de vous."
    "L'art elfique qui paraît souvent prétentieux et sans intérêt aux humains grossiers, vous apparaît dans toute sa splendeur."
    $ AjouterACarac(trait.Sensibilite.NOM, 2)
    jump fin_cycle

label univElfes_evt11:
    # Danse
    "Pour les elfes la danse n'est pas une simple distraction. C'est un moyen d'expression très profond durant lequel les histoires et les sentiments sont exprimés de la manière la plus subtile."
    "Sans avoir la prétention de vous faire atteindre ce niveau, l'université implique des cours de danse et une participation aux bals."
    $ AjouterACarac(metier.Danseur.NOM, 2)
    jump fin_cycle

label univElfes_evt12:
    "univElfes_evt12 PAS FAIT"
    jump fin_cycle
