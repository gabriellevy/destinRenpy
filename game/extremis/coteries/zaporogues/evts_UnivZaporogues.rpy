# musiques
# define audio.principale_temple = "musique/templiers/principale.mp3"

init -5 python:
    import random
    from extremis.coteries.zaporogues import zaporogues
    from extremis.socio_eco.metiers import metier
    from abs.religions import religion

    def AjouterEvtsUnivZaporogues():
        """
        Quand on s'enrôle dans une université on doit accomplir un certain nombre de modules
        """
        global selecteur_
        conditionDansUniv = condition.Condition(coterie.Coterie.Carac_UNIV_COURANTE, zaporogues.Zaporogues.ID, condition.Condition.EGAL)

        # très forte chance (proba absolue) de suivre des modules tant qu'on n'en a pas fait 6
        univZaporogues = declencheur.Declencheur(proba.Proba(0.6, False), "univZaporogues")
        univZaporogues.AjouterCondition(conditionDansUniv)
        selecteur_.ajouterDeclencheur(univZaporogues)

    def evtUnivZaporoguesSuivant():
        global situation_

        evts = ["univZaporogues_evt1", "univZaporogues_evt2", "univZaporogues_evt3",
        "univZaporogues_evt4", "univZaporogues_evt5", "univZaporogues_evt6",
        "univZaporogues_evt7", "univZaporogues_evt8", "univZaporogues_evt9",
        "univZaporogues_evt10", "univZaporogues_evt11", "univZaporogues_evt12"  ]

        prochainEvt = random.choice(evts)
        while situation_.GetValCaracInt(prochainEvt) == 1:
            prochainEvt = random.choice(evts)

        situation_.SetValCarac(prochainEvt, 1)
        renpy.jump( prochainEvt)

label univZaporogues:
    #scene bg univ_zaporogues

    $ situation_.SetCarac(coterie.Coterie.Carac_UNIV_COURANTE, zaporogues.Zaporogues.ID)
    $ numMoisRestants = situation_.GetValCaracInt(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE)
    if numMoisRestants == coterie.Coterie.NB_MOIS_UNIV_TOTAL_A_FAIRE:
        # intro :
        # play music principale_temple
        "PAS FAIT intro univ Zaporogues"

    $ numMoisRestants = situation_.GetValCaracInt(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE)
    if numMoisRestants < 1:
        # fin d'université
        $ situation_.SetCarac(coterie.Coterie.Carac_UNIV_COURANTE, "")
        jump decUnivCoterie
    else:
        $ situation_.RetirerACarac(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE, 1)
        $ situation_.TourSuivant()
        $ evtUnivZaporoguesSuivant()
    jump fin_cycle

label univZaporogues_evt1:
    "PAS FAIT univZaporogues_evt1"
    jump fin_cycle

label univZaporogues_evt2:
    "PAS FAIT univZaporogues_evt2"
    jump fin_cycle

label univZaporogues_evt3:
    "PAS FAIT univZaporogues_evt3"
    jump fin_cycle

label univZaporogues_evt4:
    "PAS FAIT univZaporogues_evt4"
    jump fin_cycle

label univZaporogues_evt5:
    "PAS FAIT univZaporogues_evt5"
    jump fin_cycle

label univZaporogues_evt6:
    "PAS FAIT univZaporogues_evt6"
    jump fin_cycle

label univZaporogues_evt7:
    "PAS FAIT univZaporogues_evt7"
    jump fin_cycle

label univZaporogues_evt8:
    "PAS FAIT univZaporogues_evt8"
    jump fin_cycle

label univZaporogues_evt9:
    "PAS FAIT univZaporogues_evt9"
    jump fin_cycle

label univZaporogues_evt10:
    "PAS FAIT univZaporogues_evt10"
    jump fin_cycle

label univZaporogues_evt11:
    "PAS FAIT univZaporogues_evt11"
    jump fin_cycle

label univZaporogues_evt12:
    "PAS FAIT univZaporogues_evt12"
    jump fin_cycle
