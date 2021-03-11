
define audio.tedonimum = "musique/templiers/tedonimum.mp3"
define audio.saladinbesiegejerusalem = "musique/templiers/saladinbesiegejerusalem.mp3"
define audio.guyderosesquandary = "musique/templiers/guyderosesquandary.mp3"

init -5 python:
    import random
    from extremis.coteries.templiers import templiers
    from extremis.socio_eco.metiers import metier
    from extremis.humanite import identite
    from extremis.religions import religion

    def AjouterEvtsTempliers():
        """
        événements génriques qui concernent les templiers
        """
        global selecteur_
        estTemplier = condition.Condition(coterie.Coterie.C_COTERIE, templiers.Templiers.ID, condition.Condition.EGAL)
        estChretien = condition.Condition(religion.Religion.C_RELIGION, religion.Christianisme.NOM, condition.Condition.EGAL)
        aPasEpeeSacree = condition.Condition(templiers.Templiers.C_EPEE_SACREE, "", condition.Condition.EGAL)
        estPasTemplier = condition.Condition(coterie.Coterie.C_COTERIE, templiers.Templiers.ID, condition.Condition.DIFFERENT)
        estEnPrison = condition.Condition(justice.Justice.C_LIBERTE, justice.Justice.PRISON, condition.Condition.EGAL) # vraie prison, déjà condamné pas préventif
        estDansQuartierTemplier = condition.Condition(quartier.Quartier.C_QUARTIER, quartier.SaintDenis.NOM, condition.Condition.EGAL)
        # guerrier
        estGuerrierNul = condition.Condition(metier.Guerrier.NOM, 4, condition.Condition.INFERIEUR)
        estPasGrandGuerrier = condition.Condition(metier.Guerrier.NOM, 8, condition.Condition.INFERIEUR)
        estBonGuerrier = condition.Condition(metier.Guerrier.NOM, 4, condition.Condition.SUPERIEUR)
        estGuerrierSupreme = condition.Condition(metier.Guerrier.NOM, 10, condition.Condition.EGAL)
        estPasGuerrierSupreme = condition.Condition(metier.Guerrier.NOM, 10, condition.Condition.DIFFERENT)


        # très forte chance (proba absolue) de suivre des modules tant qu'on n'en a pas fait 6
        recrutementTemplierEnPrison = declencheur.Declencheur(proba.Proba(0.1, True), "recrutementTemplierEnPrison")
        recrutementTemplierEnPrison.AjouterCondition(estPasTemplier)
        recrutementTemplierEnPrison.AjouterCondition(estEnPrison)
        selecteur_.ajouterDeclencheur(recrutementTemplierEnPrison)

        # Grande cérémonie
        templiersGrandeCeremonie = declencheur.Declencheur(proba.Proba(0.01, True), "templiersGrandeCeremonie")
        templiersGrandeCeremonie.AjouterCondition(estChretien)
        selecteur_.ajouterDeclencheur(templiersGrandeCeremonie)

        # Entrainement au combat
        prob = proba.Proba(0.01, True)
        prob.ajouterModifProbaViaVals(0.01, estGuerrierNul)
        prob.ajouterModifProbaViaVals(0.005, estPasGrandGuerrier)
        templiersEntrainementAuCombat = declencheur.Declencheur(prob, "templiersEntrainementAuCombat")
        templiersEntrainementAuCombat.AjouterCondition(estTemplier)
        templiersEntrainementAuCombat.AjouterCondition(estPasGuerrierSupreme)
        selecteur_.ajouterDeclencheur(templiersEntrainementAuCombat)

        # Don d'une épée sacrée
        prob = proba.Proba(0.05, True)
        templiersDonEpeeSacree = declencheur.Declencheur(prob, "templiersDonEpeeSacree")
        templiersDonEpeeSacree.AjouterCondition(estTemplier)
        templiersDonEpeeSacree.AjouterCondition(aPasEpeeSacree)
        templiersDonEpeeSacree.AjouterCondition(estChretien)
        templiersDonEpeeSacree.AjouterCondition(estBonGuerrier)
        selecteur_.ajouterDeclencheur(templiersDonEpeeSacree)

        # Recevoir l'aumône
        prob = proba.Proba(0.03, True)
        templiersRecevoirAumone = declencheur.Declencheur(prob, "templiersRecevoirAumone")
        templiersRecevoirAumone.AjouterCondition(estMiserable)
        templiersRecevoirAumone.AjouterCondition(estDansQuartierTemplier)
        selecteur_.ajouterDeclencheur(templiersRecevoirAumone)

label templiersRecevoirAumone:
    # Recevoir l'aumône
    play music guyderosesquandary
    "Votre misère attendrit un chrétien templier qui vous fait un gros don."
    $ situation_.AjouterACarac(trait.Richesse.NOM, 1)

label templiersDonEpeeSacree:
    # Don d'une épée sacrée
    play music saladinbesiegejerusalem
    "Pour votre dévotion chrétienne fervente et en signe que vos compétences au combat sont reconnues suffisantes, l'ordre vous affecte une épée sacrée bénie par un évèque. Nul doute qu'elle facilitera grandement vos miracles."
    $ situation_.AjouterACarac(templiers.Templiers.C_EPEE_SACREE, 1)
    $ situation_.AjouterACarac(religion.Religion.C_MIRACLE, 1)

label templiersEntrainementAuCombat:
    # Entrainement au combat
    "Même quand il n'est pas un guerrier professionnel un templier se doit d'être expert en combat ce qui est encore loin d'être votre cas."
    "Une série de séances avec un maître d'armes améliore grandement vos compétences."
    $ situation_.AjouterACarac(metier.Guerrier.NOM, 1)
    jump fin_cycle

label recrutementTemplierEnPrison:
    # Conversion en prison
    # $ religionActuelle = situation_.GetValCarac(religion.Religion.C_RELIGION)
    show ordonnateur at right
    with moveinright
    "Un prêcheur de la croisade franque rend une visite dans votre prison."
    "Il entame de longs discours sur l'honneur, le devoir la force et le sens de la vie et vous appelle à la rédemption en rejoignant les templiers qui s'engagent à vous aider à votre sortie de prison si vous prêtez serment."
    $ affecte = False # est-ce que le prêche l'a affecté
    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.3:
        $ situation_.AjouterACarac(trait.Honorabilite.NOM, 1)
        $ affecte = True
    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.3:
        $ situation_.AjouterACarac(trait.Franchise.NOM, 1)
        $ affecte = True
    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.3:
        $ conversion = conversionReligieuse(religion.Christianisme.NOM)
        if conversion:
            "Vous vous convertissez au christianisme."
            $ affecte = True
    $ templiersCot = coteries_[templiers.Templiers.ID]
    $ affinite = templiersCot.CalculerAffinite(situation_)
    if affinite > 0:
        "Ses arguments vous convainquent de vous amender et de postuler."
        jump templiersPostule
    elif affecte:
        "Quoique son sermon vous ait beaucoup affecté, ses arguments ne vous convainquent pas de rejoindre l'Ordre."
    else:
        "Ses arguments ne vous convainquent pas de rejoindre l'Ordre."

    jump fin_cycle

label templiersGrandeCeremonie:
    play music tedonimum
    # "Grande cérémonie => A FAIRE transférer ça dans un fichier d'événements chrétiens
    "Vous assistez aux offices de pâques. La cérémonie est si parfaite que vous en êtes très affecté, comme si vous étiez purifié de vos péchés."
    if random.uniform(0, 1.0) < 0.2:
        $ situation_.AjouterACarac(trait.Altruisme.NOM, 1)
    if random.uniform(0, 1.0) < 0.2:
        $ situation_.AjouterACarac(trait.Franchise.NOM, 1)
    if random.uniform(0, 1.0) < 0.2:
        $ situation_.AjouterACarac(trait.Sincerite.NOM, 1)
    if random.uniform(0, 1.0) < 0.2:
        $ situation_.RetirerACarac(trait.Ascetisme.NOM, 1)
    if random.uniform(0, 1.0) < 0.2:
        $ situation_.RetirerACarac(trait.Cupidite.NOM, 1)
    if random.uniform(0, 1.0) < 0.2:
        $ situation_.RetirerACarac(trait.Sexualite.NOM, 1)
    jump fin_cycle
