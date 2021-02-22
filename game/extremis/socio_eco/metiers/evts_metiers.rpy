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
    # métier courant mais faible à l'échelle de la population proba 0.01 (boutiquier,
    # les très rares ont une proba de 0.0001 (tueur de monstre,
    def AjouterEvtsRejMetier():
        global selecteur_
        aPasDeMetier = condition.Condition(metier.Metier.C_METIER, "", condition.Condition.EGAL)
        univFinie = condition.Condition(coterie.Coterie.Carac_NB_UNIV, coterie.Coterie.NB_UNIV_TOTAL, condition.Condition.SUPERIEUR_EGAL)
        # a telle carac
        aArtiste = condition.Condition(trait.Artiste.NOM, 1, condition.Condition.SUPERIEUR_EGAL)
        # est de telle coterie
        estElfe = condition.Condition(coterie.Coterie.C_COTERIE, elfes.Elfes.ID, condition.Condition.EGAL)
        estConquistaror = condition.Condition(coterie.Coterie.C_COTERIE, conquistadors.Conquistadors.ID, condition.Condition.EGAL)
        estTemplier = condition.Condition(coterie.Coterie.C_COTERIE, templiers.Templiers.ID, condition.Condition.EGAL)

        # paysan
        decRejPaysan = declencheur.Declencheur(0.1, "decRejPaysan")
        decRejPaysan.AjouterCondition(aPasDeMetier)
        decRejPaysan.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejPaysan)

        # musicien
        prob = proba.Proba(0.0005, True)
        prob.ajouterModifProbaViaVals(0.1, aArtiste)
        prob.ajouterModifProbaViaVals(0.05, estConquistaror)
        prob.ajouterModifProbaViaVals(0.03, estElfe)
        decRejMusicien = declencheur.Declencheur(prob, "decRejMusicien")
        decRejMusicien.AjouterCondition(aPasDeMetier)
        decRejMusicien.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejMusicien)

        # dessinateur
        prob = proba.Proba(0.0005, True)
        prob.ajouterModifProbaViaVals(0.05, aArtiste)
        decRejDessinateur = declencheur.Declencheur(prob, "decRejDessinateur")
        decRejDessinateur.AjouterCondition(aPasDeMetier)
        decRejDessinateur.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejDessinateur)

        # poète
        prob = proba.Proba(0.0005, True)
        prob.ajouterModifProbaViaVals(0.1, aArtiste)
        prob.ajouterModifProbaViaVals(0.03, estElfe)
        decRejPoete = declencheur.Declencheur(prob, "decRejPoete")
        decRejPoete.AjouterCondition(aPasDeMetier)
        decRejPoete.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejPoete)

        # Bibliothecaire
        prob = proba.Proba(0.001, True)
        prob.ajouterModifProbaViaVals(0.03, estTemplier)
        decRejBibliothecaire = declencheur.Declencheur(prob, "decRejBibliothecaire")
        decRejBibliothecaire.AjouterCondition(aPasDeMetier)
        decRejBibliothecaire.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejBibliothecaire)

        # Cartographe
        prob = proba.Proba(0.001, True)
        decRejCartographe = declencheur.Declencheur(prob, "decRejCartographe")
        decRejCartographe.AjouterCondition(aPasDeMetier)
        decRejCartographe.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejCartographe)

        # Marchand
        prob = proba.Proba(0.01, True)
        decRejMarchand = declencheur.Declencheur(prob, "decRejMarchand")
        decRejMarchand.AjouterCondition(aPasDeMetier)
        decRejMarchand.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejMarchand)

        # Mineur
        prob = proba.Proba(0.01, True)
        decRejMineur = declencheur.Declencheur(prob, "decRejMineur")
        decRejMineur.AjouterCondition(aPasDeMetier)
        decRejMineur.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejMineur)

        # Pretre
        prob = proba.Proba(0.002, True)
        decRejPretre = declencheur.Declencheur(prob, "decRejPretre")
        decRejPretre.AjouterCondition(aPasDeMetier)
        decRejPretre.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejPretre)

        # Ouvrier
        prob = proba.Proba(0.1, True)
        decRejOuvrier = declencheur.Declencheur(prob, "decRejOuvrier")
        decRejOuvrier.AjouterCondition(aPasDeMetier)
        decRejOuvrier.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejOuvrier)

        # Politique
        prob = proba.Proba(0.002, True)
        decRejPolitique = declencheur.Declencheur(prob, "decRejPolitique")
        decRejPolitique.AjouterCondition(aPasDeMetier)
        decRejPolitique.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejPolitique)

        # Forgeron
        prob = proba.Proba(0.002, True)
        decRejForgeron = declencheur.Declencheur(prob, "decRejForgeron")
        decRejForgeron.AjouterCondition(aPasDeMetier)
        decRejForgeron.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejForgeron)

        # Alchimiste
        prob = proba.Proba(0.0001, True)
        prob.ajouterModifProbaViaVals(0.03, estElfe)
        decRejAlchimiste = declencheur.Declencheur(prob, "decRejAlchimiste")
        decRejAlchimiste.AjouterCondition(aPasDeMetier)
        decRejAlchimiste.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejAlchimiste)

label decRejForgeron:
    # devient Forgeron
    "Vous êtes maintenant un Forgeron."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Forgeron.NOM)
    jump fin_cycle

label decRejAlchimiste:
    # devient Alchimiste
    "Vous êtes maintenant un Alchimiste."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Alchimiste.NOM)
    jump fin_cycle

label decRejPaysan:
    # devient paysan
    "Vous êtes maintenant un paysan."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Paysan.NOM)
    jump fin_cycle

label decRejPolitique:
    # devient Politique
    "Vous êtes maintenant un Politique."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Politique.NOM)
    jump fin_cycle

label decRejOuvrier:
    # devient Ouvrier
    "Vous êtes maintenant un Ouvrier."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Ouvrier.NOM)
    jump fin_cycle

label decRejMusicien:
    "Vous êtes maintenant un Musicien."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Musicien.NOM)
    jump fin_cycle

label decRejDessinateur:
    "Vous êtes maintenant un Dessinateur."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Dessinateur.NOM)
    jump fin_cycle

label decRejPoete:
    "Vous êtes maintenant un Poète."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Poete.NOM)
    jump fin_cycle

label decRejBibliothecaire:
    "Vous êtes maintenant un bibliothécaire."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Bibliothecaire.NOM)
    jump fin_cycle

label decRejCartographe:
    "Vous êtes maintenant un cartographe."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Cartographe.NOM)
    jump fin_cycle

label decRejMarchand:
    "Vous êtes maintenant un marchand."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Marchand.NOM)
    jump fin_cycle

label decRejMineur:
    "Vous êtes maintenant un Mineur."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Mineur.NOM)
    jump fin_cycle

label decRejPretre:
    "Vous êtes maintenant un Prêtre."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Pretre.NOM)
    jump fin_cycle
