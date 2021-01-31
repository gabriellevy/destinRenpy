init -5 python:
    import random
    from extremis.coteries.transhumanistes import transhumanistes

    def AjouterEvtsUnivTranshumanistes():
        """
        Quand on s'enrôle dans une université on doit accomplir un certain nombre de modules
        """
        global selecteur_
        conditionDansUniv = condition.Condition(coterie.Coterie.Carac_UNIV_COURANTE, transhumanistes.Transhumanistes.NOM, condition.Condition.EGAL)

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

        renpy.jump( random.choice(evts))

label univTranshumanistes:
    scene bg univ_transhumanistes

    $ situation_.SetCarac(coterie.Coterie.Carac_UNIV_COURANTE, transhumanistes.Transhumanistes.NOM)
    $ numMoisRestants = situation_.GetValCaracInt(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE)
    if numMoisRestants == coterie.Coterie.NB_MOIS_UNIV_TOTAL_A_FAIRE:
        # intro :
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
    scene bg labo
    "La génétique et la cybernétique sont les base du transhumanisme. Une initiation à ces sciences est indispensable dans cette université. "
    "univTranshumanistes_evt1 PAS FAIT"
    jump fin_cycle

label univTranshumanistes_evt2:
    "univTranshumanistes_evt2 PAS FAIT"
    jump fin_cycle
label univTranshumanistes_evt3:
    "univTranshumanistes_evt3 PAS FAIT"
    jump fin_cycle
label univTranshumanistes_evt4:
    "univTranshumanistes_evt4 PAS FAIT"
    jump fin_cycle
label univTranshumanistes_evt5:
    "univTranshumanistes_evt5 PAS FAIT"
    jump fin_cycle
label univTranshumanistes_evt6:
    "univTranshumanistes_evt6 PAS FAIT"
    jump fin_cycle
label univTranshumanistes_evt7:
    "univTranshumanistes_evt7 PAS FAIT"
    jump univTranshumanistes
label univTranshumanistes_evt8:
    "univTranshumanistes_evt8 PAS FAIT"
    jump fin_cycle
label univTranshumanistes_evt9:
    "univTranshumanistes_evt9 PAS FAIT"
    jump fin_cycle
label univTranshumanistes_evt10:
    "univTranshumanistes_evt10 PAS FAIT"
    jump fin_cycle
label univTranshumanistes_evt11:
    "univTranshumanistes_evt11 PAS FAIT"
    jump fin_cycle
label univTranshumanistes_evt12:
    "univTranshumanistes_evt12 PAS FAIT"
    jump fin_cycle
