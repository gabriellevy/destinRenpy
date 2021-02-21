# ne concerne que les événements génériques non spécifiques à un métier donné (plus l'enrolement dans un métier)


init -5 python:
    import random
    from despin.gen_vie import declencheur
    from despin.gen_vie import selecteur
    from despin.gen_vie import proba
    from despin.abs import condition
    from despin.reglages import filtres_action
    from extremis.humanite import trait
    from extremis.constitution import temps
    from extremis.socio_eco.metiers import metier

    # notes sur les probas : les métiers très courant ont une proba de base de 0.1 (payson, employé)
    # les très rares ont une proba de 0.001 (tueur de monstre,
    def AjouterEvtsRejMetier():
        global selecteur_
        aPasDeMetier = condition.Condition(metier.Metier.C_METIER, "", condition.Condition.EGAL)
        univFinie = condition.Condition(coterie.Coterie.Carac_NB_UNIV, coterie.Coterie.NB_UNIV_TOTAL, condition.Condition.SUPERIEUR_EGAL)
        # a telle carac
        aArtiste = condition.Condition(trait.Artiste.NOM, 1, condition.Condition.SUPERIEUR_EGAL)

        decRejPaysan = declencheur.Declencheur(0.1, "decRejPaysan")
        decRejPaysan.AjouterCondition(aPasDeMetier)
        selecteur_.ajouterDeclencheur(decRejPaysan)

        probaMusicien = proba.Proba(0.0005, True)
        probaMusicien.ajouterModifProbaViaVals(0.3, aArtiste)
        decRejMusicien = declencheur.Declencheur(probaMusicien, "decRejMusicien")
        decRejMusicien.AjouterCondition(aPasDeMetier)
        selecteur_.ajouterDeclencheur(decRejMusicien)

label decRejPaysan:
    # devient paysan
    "Vous êtes maintenant un paysan."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Paysan.NOM)
    jump fin_cycle

label decRejMusicien:
    # devient paysan
    "Vous êtes maintenant un Musicien."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Musicien.NOM)
    jump fin_cycle
