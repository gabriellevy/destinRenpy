init -5 python:
    import random
    from extremis.coteries.templiers import templiers

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
        "univTempliers_evt10", "univTempliers_evt11", "univTempliers_evt12" ]

        renpy.jump( random.choice(evts))

label univTempliers:
    scene bg univ_templiers

    $ situation_.SetCarac(coterie.Coterie.Carac_UNIV_COURANTE, templiers.Templiers.NOM)
    $ numMoisRestants = situation_.GetValCaracInt(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE)
    if numMoisRestants == coterie.Coterie.NB_MOIS_UNIV_TOTAL_A_FAIRE:
        # intro :
        "Basée sur la foi inébranlable en Dieu et sur l'honneur guerrier de l'aristocratie franque."
        "Les templiers sont avant tout des guerriers saints avec un code de l'honneur très strict. "
        "Ce code de l'honneur méprise la cupidité et l'ostentation mais l'enrichissement n'est pas interdit, surtout lorsqu'il est utilisé pour financer les nombreux hpoitaux de l'ordre. "
        "Ainsi les templiers sont aussi mercenaires tant que la cause est jugée honorable par l'ordre. "
        "Leurs cibles favorites sont les magiciens maléfiques et les hérétiques."
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
    "univTempliers_evt1 PAS FAIT"
    jump fin_cycle
label univTempliers_evt2:
    "univTempliers_evt2 PAS FAIT"
    jump fin_cycle
label univTempliers_evt3:
    "univTempliers_evt3 PAS FAIT"
    jump fin_cycle
label univTempliers_evt4:
    "univTempliers_evt4 PAS FAIT"
    jump fin_cycle
label univTempliers_evt5:
    "univTempliers_evt5 PAS FAIT"
    jump fin_cycle
label univTempliers_evt6:
    "univTempliers_evt6 PAS FAIT"
    jump fin_cycle
label univTempliers_evt7:
    "univTempliers_evt7 PAS FAIT"
    jump fin_cycle
label univTempliers_evt8:
    "univTempliers_evt8 PAS FAIT"
    jump fin_cycle
label univTempliers_evt9:
    "univTempliers_evt9 PAS FAIT"
    jump fin_cycle
label univTempliers_evt10:
    "univTempliers_evt10 PAS FAIT"
    jump fin_cycle
label univTempliers_evt11:
    "univTempliers_evt11 PAS FAIT"
    jump fin_cycle
label univTempliers_evt12:
    "univTempliers_evt12 PAS FAIT"
    jump fin_cycle
