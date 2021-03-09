
define audio.tedonimum = "musique/templiers/tedonimum.mp3"

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
        estPasTemplier = condition.Condition(coterie.Coterie.C_COTERIE, templiers.Templiers.ID, condition.Condition.DIFFERENT)
        estEnPrison = condition.Condition(justice.Justice.C_LIBERTE, justice.Justice.PRISON, condition.Condition.EGAL) # vraie prison, déjà condamné pas préventif

        # très forte chance (proba absolue) de suivre des modules tant qu'on n'en a pas fait 6
        recrutementTemplierEnPrison = declencheur.Declencheur(proba.Proba(0.1, False), "recrutementTemplierEnPrison")
        recrutementTemplierEnPrison.AjouterCondition(estPasTemplier)
        recrutementTemplierEnPrison.AjouterCondition(estEnPrison)
        selecteur_.ajouterDeclencheur(recrutementTemplierEnPrison)

        # Grande cérémonie
        templiersGrandeCeremonie = declencheur.Declencheur(proba.Proba(0.01, False), "templiersGrandeCeremonie")
        templiersGrandeCeremonie.AjouterCondition(estChretien)
        selecteur_.ajouterDeclencheur(templiersGrandeCeremonie)

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
