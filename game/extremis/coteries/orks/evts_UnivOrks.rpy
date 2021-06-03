init -5 python:
    import random
    from extremis.coteries.orks import orks
    from extremis.socio_eco.metiers import metier
    from extremis.religions import religion

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
        "intro univ orks PAS FAITE. "

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
    "univOrks_evt1 PAS FAIT"
    jump fin_cycle

label univOrks_evt2:
    "univOrks_evt2 PAS FAIT"
    jump fin_cycle

label univOrks_evt3:
    "univOrks_evt3 PAS FAIT"
    jump fin_cycle

label univOrks_evt4:
    "univOrks_evt4 PAS FAIT"
    jump fin_cycle

label univOrks_evt5:
    "univOrks_evt5 PAS FAIT"
    jump fin_cycle

label univOrks_evt6:
    "univOrks_evt6 PAS FAIT"
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
