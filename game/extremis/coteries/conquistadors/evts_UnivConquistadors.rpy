init -5 python:
    import random
    from extremis.coteries.conquistadors import conquistadors
    from extremis.socio_eco.metiers import metier
    from extremis.religions import religion

    def AjouterEvtsUnivConquistadors():
        """
        Quand on s'enrôle dans une université on doit accomplir un certain nombre de modules
        """
        global selecteur_
        conditionDansUniv = condition.Condition(coterie.Coterie.Carac_UNIV_COURANTE, conquistadors.Conquistadors.NOM, condition.Condition.EGAL)

        # très forte chance (proba absolue) de suivre des modules tant qu'on n'en a pas fait 6
        univConquistadors = declencheur.Declencheur(proba.Proba(0.6, False), "univConquistadors")
        univConquistadors.AjouterCondition(conditionDansUniv)
        selecteur_.ajouterDeclencheur(univConquistadors)

    def evtUnivConquistadorsSuivant():
        global situation_

        evts = ["univConquistadors_evt1", "univConquistadors_evt2", "univConquistadors_evt3",
        "univConquistadors_evt4", "univConquistadors_evt5", "univConquistadors_evt6",
        "univConquistadors_evt7", "univConquistadors_evt8", "univConquistadors_evt9",
        "univConquistadors_evt10", "univConquistadors_evt11", "univConquistadors_evt12" ]

        prochainEvt = random.choice(evts)
        while situation_.GetValCaracInt(prochainEvt) == 1:
            prochainEvt = random.choice(evts)

        situation_.SetValCarac(prochainEvt, 1)
        renpy.jump( prochainEvt)

label univConquistadors:
    # scene bg univ_elfes

    $ situation_.SetCarac(coterie.Coterie.Carac_UNIV_COURANTE, conquistadors.Conquistadors.NOM)
    $ numMoisRestants = situation_.GetValCaracInt(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE)
    if numMoisRestants == coterie.Coterie.NB_MOIS_UNIV_TOTAL_A_FAIRE:
        # intro :
        "intro univ conquistadors PAS FAITE. "

    $ numMoisRestants = situation_.GetValCaracInt(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE)
    if numMoisRestants < 1:
        # fin d'université
        $ situation_.SetCarac(coterie.Coterie.Carac_UNIV_COURANTE, "")
        jump decUnivCoterie
    else:
        $ situation_.RetirerACarac(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE, 1)
        $ situation_.TourSuivant()
        $ evtUnivConquistadorsSuivant()
    jump fin_cycle

label univConquistadors_evt1:
    "univConquistadors_evt1 PAS FAIT"
    jump fin_cycle

label univConquistadors_evt2:
    "univConquistadors_evt2 PAS FAIT"
    jump fin_cycle

label univConquistadors_evt3:
    "univConquistadors_evt3 PAS FAIT"
    jump fin_cycle

label univConquistadors_evt4:
    "univConquistadors_evt4 PAS FAIT"
    jump fin_cycle

label univConquistadors_evt5:
    "univConquistadors_evt5 PAS FAIT"
    jump fin_cycle

label univConquistadors_evt6:
    "univConquistadors_evt6 PAS FAIT"
    jump fin_cycle

label univConquistadors_evt7:
    "univConquistadors_evt7 PAS FAIT"
    jump fin_cycle

label univConquistadors_evt8:
    "univConquistadors_evt8 PAS FAIT"
    jump fin_cycle

label univConquistadors_evt9:
    "univConquistadors_evt9 PAS FAIT"
    jump fin_cycle

label univConquistadors_evt10:
    "univConquistadors_evt10 PAS FAIT"
    jump fin_cycle

label univConquistadors_evt11:
    "univConquistadors_evt11 PAS FAIT"
    jump fin_cycle

label univConquistadors_evt12:
    "univConquistadors_evt12 PAS FAIT"
    jump fin_cycle
