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

        decRejPaysan = declencheur.Declencheur(0.1, "decRejPaysan")
        decRejPaysan.AjouterCondition(aPasDeMetier)
        selecteur_.ajouterDeclencheur(decRejPaysan)

    # actions maj poste changement de métier
    def majPosteCHangementMetier():
        global situation_

label decRejPaysan:
    # devient paysan
    "Vous êtes maintenant un paysan."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Paysan.NOM)
    $ majPosteCHangementMetier()
    menu:
        "tmp pause":
            "ok !!!!!"
    jump fin_cycle
