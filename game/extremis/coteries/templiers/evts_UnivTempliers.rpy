
image ordonnateur = "coteries/templiers/ordonnateur.png"

define ordo = Character('Ordonnateur', color="#e30909")

init -5 python:
    import random
    from extremis.coteries.templiers import templiers
    from extremis.socio_eco.metiers import metier
    from extremis.religions import religion

    def AjouterEvtsUnivTempliers():
        """
        Quand on s'enrôle dans une université on doit accomplir un certain nombre de modules
        """
        global selecteur_
        conditionDansUniv = condition.Condition(coterie.Coterie.Carac_UNIV_COURANTE, templiers.Templiers.NOM, condition.Condition.EGAL)

        # très forte chance (proba absolue) de suivre des modules tant qu'on n'en a pas fait 6
        univTempliers = declencheur.Declencheur(proba.Proba(0.6, False), "univTempliers")
        univTempliers.AjouterCondition(conditionDansUniv)
        selecteur_.ajouterDeclencheur(univTempliers)

    def evtUnivTempliersSuivant():
        global situation_

        evts = ["univTempliers_evt1", "univTempliers_evt2", "univTempliers_evt3",
        "univTempliers_evt4", "univTempliers_evt5", "univTempliers_evt6",
        "univTempliers_evt7", "univTempliers_evt8", "univTempliers_evt9",
        "univTempliers_evt10", "univTempliers_evt11", "univTempliers_evt12",
        "univTempliers_evt13"  ]

        prochainEvt = random.choice(evts)
        while situation_.GetValCaracInt(prochainEvt) == 1:
            prochainEvt = random.choice(evts)

        situation_.SetValCarac(prochainEvt, 1)
        renpy.jump( prochainEvt)

label univTempliers:
    scene bg univ_templiers

    $ situation_.SetCarac(coterie.Coterie.Carac_UNIV_COURANTE, templiers.Templiers.NOM)
    $ numMoisRestants = situation_.GetValCaracInt(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE)
    if numMoisRestants == coterie.Coterie.NB_MOIS_UNIV_TOTAL_A_FAIRE:
        # intro :
        "Le temple est basée sur la foi inébranlable en Dieu et sur l'honneur guerrier de l'aristocratie franque."
        "Les templiers sont avant tout des guerriers saints avec un code de l'honneur très strict. "
        "Ce code de l'honneur méprise la cupidité et l'ostentation mais l'enrichissement n'est pas interdit, surtout lorsqu'il est utilisé pour financer les nombreux hopitaux de l'ordre. "
        "Ainsi les templiers sont aussi mercenaires tant que la cause est jugée honorable par l'ordre. "
        "L'université du temple est une somptueuse abbaye de pierre. "
        "Le confort y est médiocre comme y pousse la doctrine du temple mais la camaraderie et la foi inébranlable des occupants réchauffent le coeur de tous les apprentis."

    $ numMoisRestants = situation_.GetValCaracInt(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE)
    if numMoisRestants < 1:
        # fin d'université
        $ situation_.SetCarac(coterie.Coterie.Carac_UNIV_COURANTE, "")
        jump decUnivCoterie
    else:
        $ situation_.RetirerACarac(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE, 1)
        $ situation_.TourSuivant()
        $ evtUnivTempliersSuivant()
    jump fin_cycle

label univTempliers_evt1:
    # formation religieuse
    scene bg priant
    "Un templier se doit d'être un fervent chrétien dévoué à la guerre sainte. "
    "Vous passez des jours entiers à prier dans la dévotion des images saintes à suivre les cours de catéchisme des franciscains."
    $ religionActuelle = situation_.GetValCarac(religion.Religion.C_RELIGION)
    if religionActuelle != religion.Christianisme.NOM:
        $ conversion = conversionReligieuse(religion.Christianisme.NOM)
        if conversion:
            "Vous vous convertissez au christianisme."
        else:
            "Mais votre propre foi était trop forte, vous restez sourd à celle ci."
    jump fin_cycle

label univTempliers_evt2:
    # effet Combat
    "On ne peut devenir templier qu'une fois qu'on maîtrise le système de combat ancestral du templier franc. "
    "De plus, comme l'essentiel des querelles sont réglés par un duel sous le jugement de Dieu il est indispensable de savoir se défendre pour se faire respecter dans les quartiers du temple."
    "Votre formation contient bien sûr un entrainement avec de célèbres maîtres d'armes."
    $ situation_.AjouterACarac(metier.Guerrier.NOM, 1)
    jump fin_cycle

label univTempliers_evt3:
    # faiseur de miracles
    $ religionCourante = situation_.GetValCarac(religion.Religion.C_RELIGION)
    if religionCourante != religion.Christianisme.NOM:
        jump univTempliers_evt1
    scene bg priant
    "Votre foi à toute épreuve vous rend digne de recevoir le plus noble des enseignements accessibles aux templier : puiser dans sa foi et sa volonté pour accomplir des miracles divins."
    $ situation_.AjouterACarac(religion.Religion.C_MIRACLE, 1)
    jump fin_cycle

label univTempliers_evt4:
    # effet Cavalerie
    "Savoir s'occuper d'un cheval est indispensable chez les templiers. Que ce soit pour être chevalier ou simple paysan."
    "Votre formateur vous apprends les bases de l'équitation et de tout ce qui tourne autour de l'entretien des chevaux."
    $ situation_.AjouterACarac(metier.Paysan.NOM, 1)
    $ situation_.AjouterACarac(metier.Chevalier.NOM, 2)
    jump fin_cycle

label univTempliers_evt5:
    # effet prêtre
    $ religionCourante = situation_.GetValCarac(religion.Religion.C_RELIGION)
    if religionCourante != religion.Christianisme.NOM:
        jump univTempliers_evt1
    scene bg priant
    "Le christianisme est au coeur du temple ; apprendre les rudiments de la prêtrise est à la base de la formation d'un bon templier."
    "C'est aussi son rêve le plus cher d'aller au bout de formation si il s'en montre digne. Pour l'heure vous apprenez suffisament pour aiderun prêtre à l'office."
    $ situation_.AjouterACarac(metier.Pretre.NOM, 1)
    jump fin_cycle

label univTempliers_evt6:
    # effet architecte
    scene bg chateau
    "La construction de châteaux imprenables est la spécialité des templiers. Avec l'interdiction des guerres les châteaux sont peu importants. Les compétences en architecture des templiers restent bien utiles et votre tuteur vous en fait profiter"
    $ situation_.AjouterACarac(metier.Architecte.NOM, 2)
    jump fin_cycle

label univTempliers_evt7:
    # effet banquier
    "Les circonstances, et surtout leur grande intégrité, ont fait des templiers des banquiers exceptionnels. Avoir des connaissances à ce sujet ne sera pas de trop pour prospérer dans l'ordre."
    $ situation_.AjouterACarac(metier.Banquier.NOM, 2)
    jump fin_cycle

label univTempliers_evt8:
    # hospitaliers
    scene bg hospice
    "Les hospitaliers sont des templiers qui ont juré de protéger et soigner les faibles quelle que soit leur race, religion ou coterie et ce gratuitement de manière complètement désintéressée."
    "Vous êtes amenés à travailler durement dans un de leurs hospices à soigner les vieux, les malades et les femmes enceintes."
    $ situation_.AjouterACarac(metier.Medecin.NOM, 1)
    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.4:
        "Vous vous portez volontaires pour nettoyer les lépreux tant vous êtes prêt à prendre tous les risques pour les malades."
        $ situation_.AjouterACarac(trait.Altruisme.NOM, 1)
    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.4:
        "Vous vous sentez vraiment à votre place parmi eux. En quelques jours seulement vous faites passer leurs problèmes avant les votres."
        $ situation_.AjouterACarac(trait.Altruisme.NOM, 1)
    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.4:
        "Le spectacle de toute cette misère vous affecte durement."
        $ situation_.RetirerACarac(trait.Serenite.NOM, 1)
    jump fin_cycle

label univTempliers_evt9:
    # chasseur de sorciers
    scene bg formation_demon
    "Les templiers méprisent la magie égoïste et imprévisible qui vient des hommes car c'est le diable qui la leur inspire. Ils vous forment donc dans la compréhension de ce qu'est la magie maléfique et de la différence avec les miracles divins."
    "Ils vous montrent aussi comment repérer les monstres et les démons qui complotent toujours dans l'ombre des hommes."
    $ situation_.AjouterACarac(metier.TueurDeMonstres.NOM, 1)
    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.4:
        "Vous devenez redoutable dans la détection des détails."
        $ situation_.AjouterACarac(trait.Observation.NOM, 1)
    jump fin_cycle

label univTempliers_evt10:
    # honneur et traditions
    "Un templier digne de ce nom doit avoir un honneur sans faille ce qui passe avant tout par le respect de la parole donné et la fidélité au seigneur."
    "Est requis aussi un grand courage dans la guerre comme dans la protection de la veuve et de l'orphelin."
    $ situation_.AjouterACarac(trait.Honorabilite.NOM, 1)
    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.4:
        $ situation_.AjouterACarac(trait.Altruisme.NOM, 1)
    jump fin_cycle

label univTempliers_evt11:
    # techniques policiers/vigiles/garde du corps
    "Les templiers combinent deux ensembles de qualités précieuses : des capacités martiales redoutables avec armes et à main nues. Et surtout une éthique sans faille."
    " Ces qualités en font les meilleurs policiers du monde mais aussi de remarquables vigiles et garde du corps. Vous êtes formé aux bases de tous ces métiers."
    $ situation_.AjouterACarac(metier.Policier.NOM, 1)
    $ situation_.AjouterACarac(metier.Vigile.NOM, 1)
    $ situation_.AjouterACarac(metier.GardeDuCorps.NOM, 1)
    jump fin_cycle

label univTempliers_evt12:
    # ascétisme dans les forêts
    scene bg ermite
    "L'introspection et la solitude forgent la foi en Dieu et la détermination disent les écritures."
    "Les templiers croient en cette devise et à l'image de Saint-François ils envoient leurs apprentis vivre dans les bois avec les oiseaux pour unique compagnie."
    "Vous restez ainsi en pleine forêt dans une petite cabane avec juste le nécessaire pour manger et vous recueillir en paix."
    $ religionActuelle = situation_.GetValCarac(religion.Religion.C_RELIGION)
    if religionActuelle != religion.Christianisme.NOM:
        $ conversion = conversionReligieuse(religion.Christianisme.NOM)
        if conversion:
            "Vous vous convertissez au christianisme."
            $ situation_.AjouterACarac(religion.Religion.C_FOI,  1)
    $ situation_.AjouterACarac(trait.Ascetisme.NOM, 2)
    "Quand votre maître vient vous chercher un mois plus tard vous êtes profondément transformé par l'expérience."
    jump fin_cycle

label univTempliers_evt13:
    # enluminure
    scene bg bibliotheque
    "L'entretien de la grande biblothèque est une tâche sacrée de l'ordre des templiers tout comme reproduire, propager et commenter ses manuscrits innombrables."
    "Vous recevez une formation dans toutes ces tâches et avez l'honneur d'approcher une partie des manuscrits anciens. Un jour peut-être serez vous autorisé à les lire."
    $ situation_.AjouterACarac(metier.Dessinateur.NOM, 1)
    $ situation_.AjouterACarac(metier.Bibliothecaire.NOM, 1)


label TempliersPostule:
    $ conversionReligieuse(religion.Christianisme.NOM) # tmp !!!
    "Vous souhaitez rejoindre l'Ordre du Temple."
    scene bg catacombes
    $ religionActuelle = situation_.GetValCarac(religion.Religion.C_RELIGION)
    if religionActuelle != religion.Christianisme.NOM:
        "Malheureusement seul un chrétien à la foi pure et désintéressée peut entrer dans l'Ordre. Quelles que soient vos protestations les ordonnateurs sentent la faiblesse de votre foi et vous refusent."
    show ordonnateur at right
    with moveinright
    "Vous vous trouvez dans un noir tunnel. Vous et chacun des deux ordonnateurs avez une torche en main qui peine à éclairer à quelques mètres alors que le tunnel semble très long vu la résonnance de vos voix."
    ordo "Nous sommes dans les souterrains de la basilique de Saint Denis, les catacombes du Temple."
    ordo "Nous avons jugé votre demande sincère ; maintenant vous allez devoir prouver votre pureté, votre courage et votre détermination."
    ordo "Votre tâche est simple : suivez le tunnel, ne vous en écartez sous aucun prétexte et vous serez digne de devenir un des nôtres."
    ordo "Que Dieu soit avec vous."
    hide ordonnateur
    with moveoutright
    "Vous suivez le tunnel et réalisez qu'il est infiniment plus long que vous ne le pensiez."
    "Vous dépassez plusieurs croisements mais n'en empruntez aucun."
    "Vous perdez très vite la notion du temps. L'humidité vous gèle, vous vous mettez déjà à avoir faim. Des vapeurs étranges montent depuis les grilles sous vos pieds."
    "Plusieurs fois vous titubez et vous écorchez sur une pierre tant le chemin est plein de trous et votre lumière de plus en plus faible."
    "Vous croyez entendre une musique."
    "Vous voyez de la lumière au loin."
    "Ce n'était pas un rêve. Une salle luxueuse se trouve à votre droite au bout d'un court tunnel. De bonnez odeurs de nourriture en viennent ainsi que des rires."
    $ diffTests = 3
    $ affDiff = situation_.AffichagePourcentageReussite(trait.Ascetisme.NOM, diffTests)
    menu:
        "Si vous vous penchez pour voir un peu.":
            jump TempliersPostule_t1_phase2
        "Si vous continuez. [affDiff]":
            jump TempliersPostule_t1

    label TempliersPostule_t1:
    $ reussi = situation_.TesterDifficulte(trait.Ascetisme.NOM, diffTests)
    if reussi:
        jump TempliersPostule_t2
    else:
        "La curiosité est trop forte, vous vous penchez pour  jeter juste un petit coup d'oeil."
        jump TempliersPostule_t1_phase2

    label TempliersPostule_t1_phase2:
        scene bg banquet
        "Vous apercevez nettement une grande tablée entourée de convives vêtues étrangement et s'amusant beaucoup."
        "La pièce est très sombre comme votre tunnel mais ça ajoute encore à l'ambiance et les convives semblent profiter avec plaisir des coins sombres."
        "Une d'entre elles vous apperçoit. D'abord surprise elle prend vite une attitude accueillante et vous fait signe de la rejoindre."
    menu:
        "Si vous acceptez l'invitation.":
            jump TempliersPostule_t1_rate
        "Si vous continuez. [affDiff]":
            jump TempliersPostule_t1_phase3

    label TempliersPostule_t1_phase3:
    $ reussi = situation_.TesterDifficulte(trait.Ascetisme.NOM, diffTests)
    if reussi:
        jump TempliersPostule_t2
    else:
        "Vous êtes comme hypnotisé par la musique, les odeurs, et le charmant souvenir de la belle inconnue et vous marchez dans la grande salle."
        jump TempliersPostule_t1_rate

    label TempliersPostule_t1_rate:
        "Échouer si rapidement à des instructions si simples. L'Ordre est très déçu, vous aurez peut-être ue autre chance un jour..."
        "PAS FAIT : développer cette rencontre pourrait être marrant !"
        jump fin_cycle


    label TempliersPostule_t2:
        scene bg catacombes
        "Votre reprenez votre longue marche pendant Dieu seul sait combien de longues très longues minutes ou heures."
        "Bientôt un large gouffre se trouve devant vous. Aucune issue à droite, aucune issue à gauche. De toute façon vous devez suivre le tunnel jusqu'au bout."
        "Vous pouvez en voir la suite de l'autre côté du trou mais il s'agit d'un saut de plus de 4 mètres à accomplir ! Vous ne voyez pas le fond du trou mais vu la faible portée de votre torche ça ne veut pas dire pour autant qu'il est profond."
        menu:
            "Si vous préférez retourner en arrière.":
                jump TempliersPostule_t2_rate
            "Si vous prenez votre élan pour tenter de sauter de l'autre côté.":
                jump TempliersPostule_t2_saute
            "Si vous marchez droit dans le vide.":
                jump TempliersPostule_t2_marche

    label TempliersPostule_t2_saute:
        $ reussi = situation_.TesterDifficulte(trait.Force.NOM, 6)
        if reussi:
            "C'est à peine croyable mais vous parvenez à bondir de l'autre côté du gouffre sans même vous blesser à l'arrivée."
            jump TempliersPostule_t3
        else:
            "Vous prenez courageusement votre élan mais au moment de suter c'est la catastrophe, vous doutez, perdez pied et tombez dans le gouffre."
            jump TempliersPostule_t2_tombe

    label TempliersPostule_t2_marche:
        $ reussi = situation_.TesterDifficulte(religion.Religion.C_MIRACLE, 2)
        if reussi:
            "C'est un miracle ! Vos pieds restent suspendus en l'air et vous parvenez de l'autre côté du gouffre en marchant doucement sans ressentir aucune peur."
            jump TempliersPostule_t3
        else:
            "Vous avez beau vous concentrer, il n'y a pas de miracle. Votre pied lancé en avant ne rencontre que le vide et vous vous écrasez piteusement au fond du gouffre."
            jump TempliersPostule_t2_tombe


    label TempliersPostule_t2_tombe:
        $ blessure = blessures_.InfligerBlessureAleatoire(situation_, 1, 8)
        $ texteBlessure = blessure.GetDescriptionRecu()
        "Il n'est heureusement pas très profond mais tomber sur des caillous pointus dans le noir est une dure expérience. [texteBlessure]"
        jump TempliersPostule_t2_rate

    label TempliersPostule_t2_rate:
        "Quel triste manque de foi. Vous n'avez pas le coeur d'un templier voilà tout. Vous trouverez votre propre voie un jour."
        jump fin_cycle

    label TempliersPostule_t3:
        "PAS FAIT : seulement deux tests pour l'instant, un de plus ça serait bien !"

    label TempliersPostule_reussi:
        "Vous marcez encore presque une heure dans l'obscurité quandenfin vous appercevez des rayons de lumière du jour."
        "Le tunnel finit en un escalier de métal qui remonte en plein quinzième arrondissement."
        show ordonnateur at right
        with moveinright
        ordo "Bravo mon fils tu as prouvé ta valeur morale et physique. Tu es digne de nous rejoindre dès aujourd'hui"
        jump TempliersRejoindre

    jump fin_cycle

label TempliersRejoindre:
    $ coterieTempliers = coteries_[templiers.Templiers.NOM]
    $ print(coterieTempliers)
    $ coterieTempliers.RejoindreCoterie(situation_)
    jump fin_cycle
