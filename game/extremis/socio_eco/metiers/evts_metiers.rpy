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
    # métier courant mais faible à l'échelle de la population proba 0.01 (boutiquier, médecin
    # les très rares ont une proba de 0.0001 (tueur de monstre,
    def AjouterEvtsRejMetier():
        global selecteur_
        aPasDeMetier = condition.Condition(metier.Metier.C_METIER, "", condition.Condition.EGAL)
        univFinie = condition.Condition(coterie.Coterie.Carac_UNIV_COURANTE, "fini", condition.Condition.EGAL)
        # a telle carac
        aArtiste = condition.Condition(trait.Artiste.NOM, 1, condition.Condition.SUPERIEUR_EGAL)
        aBeaute = condition.Condition(trait.Beaute.NOM, 1, condition.Condition.SUPERIEUR_EGAL)
        aCharme = condition.Condition(trait.Charme.NOM, 1, condition.Condition.SUPERIEUR_EGAL)
        estSournois = condition.Condition(trait.Franchise.NOM, -3, condition.Condition.INFERIEUR_EGAL)
        estParesseux = condition.Condition(trait.Industrie.NOM, -3, condition.Condition.INFERIEUR_EGAL)
        # est de telle coterie
        estElfe = condition.Condition(coterie.Coterie.C_COTERIE, elfes.Elfes.ID, condition.Condition.EGAL)
        estConquistaror = condition.Condition(coterie.Coterie.C_COTERIE, conquistadors.Conquistadors.ID, condition.Condition.EGAL)
        estTemplier = condition.Condition(coterie.Coterie.C_COTERIE, templiers.Templiers.ID, condition.Condition.EGAL)

        # paysan
        prob = proba.Proba(0.1, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Paysan.NOM)
        decRejPaysan = declencheur.Declencheur(prob, "decRejPaysan")
        decRejPaysan.AjouterCondition(aPasDeMetier)
        decRejPaysan.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejPaysan)

        # musicien
        prob = proba.Proba(0.0005, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Musicien.NOM)
        prob.ajouterModifProbaViaVals(0.1, aArtiste)
        prob.ajouterModifProbaViaVals(0.05, estConquistaror)
        prob.ajouterModifProbaViaVals(0.03, estElfe)
        decRejMusicien = declencheur.Declencheur(prob, "decRejMusicien")
        decRejMusicien.AjouterCondition(aPasDeMetier)
        decRejMusicien.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejMusicien)

        # dessinateur
        prob = proba.Proba(0.0005, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Dessinateur.NOM)
        prob.ajouterModifProbaViaVals(0.05, aArtiste)
        decRejDessinateur = declencheur.Declencheur(prob, "decRejDessinateur")
        decRejDessinateur.AjouterCondition(aPasDeMetier)
        decRejDessinateur.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejDessinateur)

        # poète
        prob = proba.Proba(0.0005, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Poete.NOM)
        prob.ajouterModifProbaViaVals(0.1, aArtiste)
        prob.ajouterModifProbaViaVals(0.03, estElfe)
        decRejPoete = declencheur.Declencheur(prob, "decRejPoete")
        decRejPoete.AjouterCondition(aPasDeMetier)
        decRejPoete.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejPoete)

        # Bibliothecaire
        prob = proba.Proba(0.001, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Bibliothecaire.NOM)
        prob.ajouterModifProbaViaVals(0.03, estTemplier)
        decRejBibliothecaire = declencheur.Declencheur(prob, "decRejBibliothecaire")
        decRejBibliothecaire.AjouterCondition(aPasDeMetier)
        decRejBibliothecaire.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejBibliothecaire)

        # Cartographe
        prob = proba.Proba(0.001, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Cartographe.NOM)
        decRejCartographe = declencheur.Declencheur(prob, "decRejCartographe")
        decRejCartographe.AjouterCondition(aPasDeMetier)
        decRejCartographe.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejCartographe)

        # Marchand
        prob = proba.Proba(0.01, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Marchand.NOM)
        decRejMarchand = declencheur.Declencheur(prob, "decRejMarchand")
        decRejMarchand.AjouterCondition(aPasDeMetier)
        decRejMarchand.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejMarchand)

        # Mineur
        prob = proba.Proba(0.01, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Mineur.NOM)
        decRejMineur = declencheur.Declencheur(prob, "decRejMineur")
        decRejMineur.AjouterCondition(aPasDeMetier)
        decRejMineur.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejMineur)

        # Pretre
        prob = proba.Proba(0.002, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Pretre.NOM)
        decRejPretre = declencheur.Declencheur(prob, "decRejPretre")
        decRejPretre.AjouterCondition(aPasDeMetier)
        decRejPretre.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejPretre)

        # Ouvrier
        prob = proba.Proba(0.1, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Ouvrier.NOM)
        decRejOuvrier = declencheur.Declencheur(prob, "decRejOuvrier")
        decRejOuvrier.AjouterCondition(aPasDeMetier)
        decRejOuvrier.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejOuvrier)

        # Politique
        prob = proba.Proba(0.002, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Politique.NOM)
        decRejPolitique = declencheur.Declencheur(prob, "decRejPolitique")
        decRejPolitique.AjouterCondition(aPasDeMetier)
        decRejPolitique.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejPolitique)

        # Forgeron
        prob = proba.Proba(0.002, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Forgeron.NOM)
        decRejForgeron = declencheur.Declencheur(prob, "decRejForgeron")
        decRejForgeron.AjouterCondition(aPasDeMetier)
        decRejForgeron.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejForgeron)

        # Alchimiste
        prob = proba.Proba(0.0001, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Alchimiste.NOM)
        prob.ajouterModifProbaViaVals(0.03, estElfe)
        decRejAlchimiste = declencheur.Declencheur(prob, "decRejAlchimiste")
        decRejAlchimiste.AjouterCondition(aPasDeMetier)
        decRejAlchimiste.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejAlchimiste)

        # Medecin
        prob = proba.Proba(0.01, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Medecin.NOM)
        decRejMedecin = declencheur.Declencheur(prob, "decRejMedecin")
        decRejMedecin.AjouterCondition(aPasDeMetier)
        decRejMedecin.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejMedecin)

        # TueurDeMonstres
        prob = proba.Proba(0.0, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.TueurDeMonstres.NOM)
        decRejTueurDeMonstres = declencheur.Declencheur(prob, "decRejTueurDeMonstres")
        decRejTueurDeMonstres.AjouterCondition(aPasDeMetier)
        decRejTueurDeMonstres.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejTueurDeMonstres)

        # Architecte
        prob = proba.Proba(0.003, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Architecte.NOM)
        decRejArchitecte = declencheur.Declencheur(prob, "decRejArchitecte")
        decRejArchitecte.AjouterCondition(aPasDeMetier)
        decRejArchitecte.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejArchitecte)

        # Parasite
        prob = proba.Proba(0.003, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Parasite.NOM)
        prob.ajouterModifProbaViaVals(0.01, estParesseux)
        prob.ajouterModifProbaViaVals(0.03, estSournois)
        prob.ajouterModifProbaViaVals(0.01, aBeaute)
        prob.ajouterModifProbaViaVals(0.02, aCharme)
        decRejParasite = declencheur.Declencheur(prob, "decRejParasite")
        decRejParasite.AjouterCondition(aPasDeMetier)
        decRejParasite.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejParasite)

        # Guerrier
        prob = proba.Proba(0.003, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Guerrier.NOM)
        decRejGuerrier = declencheur.Declencheur(prob, "decRejGuerrier")
        decRejGuerrier.AjouterCondition(aPasDeMetier)
        decRejGuerrier.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejGuerrier)

        # Chauffeur
        prob = proba.Proba(0.001, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Chauffeur.NOM)
        decRejConducteur = declencheur.Declencheur(prob, "decRejConducteur")
        decRejConducteur.AjouterCondition(aPasDeMetier)
        decRejConducteur.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejConducteur)

        # Pilote
        prob = proba.Proba(0.0001, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Pilote.NOM)
        decRejPilote = declencheur.Declencheur(prob, "decRejPilote")
        decRejPilote.AjouterCondition(aPasDeMetier)
        decRejPilote.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejPilote)

        # Chevalier
        prob = proba.Proba(0.0001, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Chevalier.NOM)
        decRejChevalier = declencheur.Declencheur(prob, "decRejChevalier")
        decRejChevalier.AjouterCondition(aPasDeMetier)
        decRejChevalier.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejChevalier)

        # Informaticien
        prob = proba.Proba(0.0001, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Informaticien.NOM)
        decRejInformaticien = declencheur.Declencheur(prob, "decRejInformaticien")
        decRejInformaticien.AjouterCondition(aPasDeMetier)
        decRejInformaticien.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejInformaticien)

        # Cyberneticien
        prob = proba.Proba(0.0001, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Cyberneticien.NOM)
        decRejCyberneticien = declencheur.Declencheur(prob, "decRejCyberneticien")
        decRejCyberneticien.AjouterCondition(aPasDeMetier)
        decRejCyberneticien.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejCyberneticien)

        # Geneticien
        prob = proba.Proba(0.0001, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Geneticien.NOM)
        decRejGeneticien = declencheur.Declencheur(prob, "decRejGeneticien")
        decRejGeneticien.AjouterCondition(aPasDeMetier)
        decRejGeneticien.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejGeneticien)

        # Commercial
        prob = proba.Proba(0.01, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Commercial.NOM)
        decRejCommercial = declencheur.Declencheur(prob, "decRejCommercial")
        decRejCommercial.AjouterCondition(aPasDeMetier)
        decRejCommercial.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejCommercial)

        # Policier
        prob = proba.Proba(0.03, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Policier.NOM)
        decRejPolicier = declencheur.Declencheur(prob, "decRejPolicier")
        decRejPolicier.AjouterCondition(aPasDeMetier)
        decRejPolicier.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejPolicier)

        # Vigile
        prob = proba.Proba(0.01, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Vigile.NOM)
        decRejVigile = declencheur.Declencheur(prob, "decRejVigile")
        decRejVigile.AjouterCondition(aPasDeMetier)
        decRejVigile.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejVigile)

        # Banquier
        prob = proba.Proba(0.01, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Banquier.NOM)
        decRejBanquier = declencheur.Declencheur(prob, "decRejBanquier")
        decRejBanquier.AjouterCondition(aPasDeMetier)
        decRejBanquier.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejBanquier)

        # GardeDuCorps
        prob = proba.Proba(0.002, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.GardeDuCorps.NOM)
        decRejGardeDuCorps = declencheur.Declencheur(prob, "decRejGardeDuCorps")
        decRejGardeDuCorps.AjouterCondition(aPasDeMetier)
        decRejGardeDuCorps.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejGardeDuCorps)

    def AjouterModifDeProbaProressifPourMetier(prob, nomMetier):
        condNiv1 = condition.Condition(nomMetier, 1, condition.Condition.SUPERIEUR_EGAL)
        prob.ajouterModifProbaViaVals(0.05, condNiv1)
        condNiv2 = condition.Condition(nomMetier, 2, condition.Condition.SUPERIEUR_EGAL)
        prob.ajouterModifProbaViaVals(0.05, condNiv2)
        condNiv3 = condition.Condition(nomMetier, 3, condition.Condition.SUPERIEUR_EGAL)
        prob.ajouterModifProbaViaVals(0.05, condNiv3)
        condNiv4 = condition.Condition(nomMetier, 4, condition.Condition.SUPERIEUR_EGAL)
        prob.ajouterModifProbaViaVals(0.05, condNiv4)
        condNiv5 = condition.Condition(nomMetier, 5, condition.Condition.SUPERIEUR_EGAL)
        prob.ajouterModifProbaViaVals(0.05, condNiv5)
        condNiv6 = condition.Condition(nomMetier, 6, condition.Condition.SUPERIEUR_EGAL)
        prob.ajouterModifProbaViaVals(0.05, condNiv6)
        condNiv7 = condition.Condition(nomMetier, 7, condition.Condition.SUPERIEUR_EGAL)
        prob.ajouterModifProbaViaVals(0.05, condNiv7)
        condNiv8 = condition.Condition(nomMetier, 8, condition.Condition.SUPERIEUR_EGAL)
        prob.ajouterModifProbaViaVals(0.05, condNiv8)
        condNiv9 = condition.Condition(nomMetier, 9, condition.Condition.SUPERIEUR_EGAL)
        prob.ajouterModifProbaViaVals(0.05, condNiv9)
        condNiv10 = condition.Condition(nomMetier, 10, condition.Condition.SUPERIEUR_EGAL)
        prob.ajouterModifProbaViaVals(0.05, condNiv10)

    def DeterminerProfessionLaPlusMaitrisee():
        """
        renvoie l'id de la profession la plus maitrisée par le personnage
        "" si aucune
        """
        global situation_
        professionMaitrisee = ""
        valMaxCourante = 0

        for metierK in situation_.collectionMetiers.lMetiers_.keys():
            valMetier = situation_.GetValCaracInt(metierK)
            if valMetier > valMaxCourante:
                valMaxCourante = valMetier
                professionMaitrisee = metierK

        return professionMaitrisee

label decRejGardeDuCorps:
    # devient GardeDuCorps
    "Vous êtes maintenant un garde du corps."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.GardeDuCorps.NOM)
    jump fin_cycle

label decRejBanquier:
    # devient Banquier
    "Vous êtes maintenant un Banquier."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Banquier.NOM)
    jump fin_cycle

label decRejVigile:
    # devient Vigile
    "Vous êtes maintenant un Vigile."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Vigile.NOM)
    jump fin_cycle

label decRejPolicier:
    # devient Policier
    "Vous êtes maintenant un Policier."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Policier.NOM)
    jump fin_cycle

label decRejCommercial:
    # devient Commercial
    "Vous êtes maintenant un Commercial."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Commercial.NOM)
    jump fin_cycle

label decRejGeneticien:
    # devient Geneticien
    "Vous êtes maintenant un Geneticien."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Geneticien.NOM)
    jump fin_cycle

label decRejCyberneticien:
    # devient Cyberneticien
    "Vous êtes maintenant un Cyberneticien."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Cyberneticien.NOM)
    jump fin_cycle

label decRejInformaticien:
    # devient Informaticien
    "Vous êtes maintenant un Informaticien."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Informaticien.NOM)
    jump fin_cycle

label decRejChevalier:
    # devient Chevalier
    "Vous êtes maintenant un Chevalier."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Chevalier.NOM)
    jump fin_cycle

label decRejPilote:
    # devient Pilote
    "Vous êtes maintenant un Pilote."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Pilote.NOM)
    jump fin_cycle

label decRejConducteur:
    # devient Conducteur
    "Vous êtes maintenant un Chauffeur."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Conducteur.NOM)
    jump fin_cycle

label decRejGuerrier:
    # devient Guerrier
    "Vous êtes maintenant un Guerrier."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Guerrier.NOM)
    jump fin_cycle

label decRejParasite:
    # devient Parasite
    "Vous êtes maintenant un Parasite."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Parasite.NOM)
    jump fin_cycle

label decRejArchitecte:
    # devient Architecte
    "Vous êtes maintenant un Architecte."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Architecte.NOM)
    jump fin_cycle

label decRejTueurDeMonstres:
    # devient TueurDeMonstres
    "Vous êtes maintenant un tueur de monstre."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.TueurDeMonstres.NOM)
    jump fin_cycle

label decRejMedecin:
    # devient Medecin
    "Vous êtes maintenant un Medecin."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Medecin.NOM)
    jump fin_cycle

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
