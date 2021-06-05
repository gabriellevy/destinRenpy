# persos
image mediko = "coteries/orks/persos/mediko.png"
define mediko = Character('Médiko', color="#001a00")

init -5 python:
    import random
    from extremis.coteries.orks import orks

    estOrk = condition.Condition(coterie.Coterie.C_COTERIE, orks.Orks.ID, condition.Condition.EGAL)
    estPasOrk = condition.Condition(coterie.Coterie.C_COTERIE, orks.Orks.ID, condition.Condition.DIFFERENT)
    estDansQuartierOrk = condition.Condition(quartier.Quartier.C_QUARTIER, quartier.Poissy.NOM, condition.Condition.EGAL)

    def AjouterEvtsOrks():
        """
        événements génériques qui concernent les templiers
        """
        global selecteur_

        # visite de médiko à l'hôpital pour recruter
        prob = proba.Proba(0.1, True)
        recrutementOrkAHopital = declencheur.Declencheur(prob, "recrutementOrkAHopital")
        recrutementOrkAHopital.AjouterCondition(estAHopital)
        recrutementOrkAHopital.AjouterCondition(estPasOrk)
        selecteur_.ajouterDeclencheur(recrutementOrkAHopital)

        # Opération surprise médiko dans un hopital ork
        prob = proba.Proba(0.15, True)
        operationSupriseMediko = declencheur.Declencheur(prob, "operationSupriseMediko")
        operationSupriseMediko.AjouterCondition(estAHopital)
        operationSupriseMediko.AjouterCondition(estDansQuartierOrk)
        selecteur_.ajouterDeclencheur(operationSupriseMediko)

label operationSupriseMediko:
    # Opération surprise médiko dans un hopital ork
    show mediko at right
    with moveinright
    "Un médiko ork vient rendre des visites à l'hopital et s'attarde dans votre chambre."
    "Il trouve que vous êtes idéal pour faire une expérience amusante et vous assomme pour que vous arrêtiez de vous plaindre."
    $ blessure = blessures_.InfligerBlessureAleatoire(situation_, 0, 4)
    $ texteBlessure = blessure.GetDescriptionRecu()
    $ bionique = bioniques_.PoserBioniqueAleatoire(situation_)
    $ texteBionique = bionique.GetDescriptionRecu()
    "[texteBlessure] \n [texteBionique]"
    jump fin_cycle


label recrutementOrkAHopital:
    # visite de médiko à l'hôpital pour recruter
    show mediko at right
    with moveinright
    "Un médiko ork vient rendre des visites à l'hopital et s'attarde dans votre chambre."
    "D'ordinaire les médikos sont plutôt des être terrifiants vu leurs habitudes de faire des expériences sur leurs patients mais cette fois et vu votre état ses arguments attirent votre attention. En particulier quand il parle du miracle du sérum orkoïde qui quand on le boît guérit presque toutes les blessures."
    "Ca a l'air fou mais vous avez entendu beaucoup de témoignages sur la résistance surnaturelle des orks."
    $ orksCot = coteries_[orks.Orks.ID]
    $ affinite = orksCot.CalculerAffinite(situation_)
    if affinite > 0:
        "Dans votre état postuler à une coterie aussi violente que les orks est dangereux mais la tentation est trop grande. Vous acceptez l'offre du médiko qui vous emmènent à Poissy sur le champs."
        jump orksPostule
    else:
        "Ca ne suffit néanmoins pas à vous convaincre de devenir un ork."
    jump fin_cycle
