init -5 python:
    import random
    from extremis.coteries.elfes import elfes

    def AjouterEvtsUnivElfes():
        """
        Quand on s'enrôle dans une université on doit accomplir un certain nombre de modules
        """
        global selecteur_
        conditionDansUniv = condition.Condition(coterie.Coterie.Carac_UNIV_COURANTE, elfes.Elfes.NOM, condition.Condition.EGAL)

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

        renpy.jump( random.choice(evts))

label univElfes:
    scene bg univ_elfes

    $ situation_.SetCarac(coterie.Coterie.Carac_UNIV_COURANTE, elfes.Elfes.NOM)
    $ numMoisRestants = situation_.GetValCaracInt(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE)
    if numMoisRestants == coterie.Coterie.NB_MOIS_UNIV_TOTAL_A_FAIRE:
        # intro :
        "intro univ elfes PAS FAITE. "

    $ numMoisRestants = situation_.GetValCaracInt(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE)
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
    "univElfes_evt1 PAS FAIT"
    jump fin_cycle
label univElfes_evt2:
    "univElfes_evt2 PAS FAIT"
    jump fin_cycle
label univElfes_evt3:
    "univElfes_evt3 PAS FAIT"
    jump fin_cycle
label univElfes_evt4:
    "univElfes_evt4 PAS FAIT"
    jump fin_cycle
label univElfes_evt5:
    "univElfes_evt5 PAS FAIT"
    jump fin_cycle
label univElfes_evt6:
    "univElfes_evt PAS FAIT6"
    jump fin_cycle
label univElfes_evt7:
    "univElfes_evt7 PAS FAIT"
    jump fin_cycle
label univElfes_evt8:
    "univElfes_evt8 PAS FAIT"
    jump fin_cycle
label univElfes_evt9:
    "univElfes_evt9 PAS FAIT"
    jump fin_cycle
label univElfes_evt10:
    "univElfes_evt10 PAS FAIT"
    jump fin_cycle
label univElfes_evt11:
    "univElfes_evt11 PAS FAIT"
    jump fin_cycle
label univElfes_evt12:
    "univElfes_evt12 PAS FAIT"
    jump fin_cycle
