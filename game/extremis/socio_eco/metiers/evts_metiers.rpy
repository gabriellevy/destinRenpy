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

    aPasDeMetier = condition.Condition(metier.Metier.C_METIER, "", condition.Condition.EGAL)
    univFinie = condition.Condition(coterie.Coterie.Carac_UNIV_COURANTE, "fini", condition.Condition.EGAL)

    def CreerDeclencheurDebutDeMetier(probaF, strMetier, facteurPourProba):
        """
        proba : probabilité d'avoir ce travail même en n'ayant aucune compétence sérieuse à ce sujet
        """
        prob = proba.Proba(probaF, True)
        AjouterModifDeProbaProressifPourMetier(prob, strMetier, facteurPourProba)
        decRejStr = "decRej{}".format(strMetier)
        decRejStr = decRejStr.replace('é', 'e')
        decRejStr = decRejStr.replace('ê', 'e')
        decRejStr = decRejStr.replace('è', 'e')
        dec = declencheur.Declencheur(prob, decRejStr)
        dec.AjouterCondition(aPasDeMetier)
        dec.AjouterCondition(univFinie)
        return dec

    # notes sur les probas : les métiers très courant ont une proba de base de 0.1 (payson, employé)
    # métier courant mais faible à l'échelle de la population proba 0.01 (boutiquier, médecin
    # les très rares ont une proba de 0.0001 (tueur de monstre,
    def AjouterEvtsRejMetier():
        global selecteur_
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
        decRejPaysan = CreerDeclencheurDebutDeMetier(0.1, metier.Paysan.NOM, 0.04)
        selecteur_.ajouterDeclencheur(decRejPaysan)

        # musicien
        prob = proba.Proba(0.0005, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Musicien.NOM, 0.05)
        prob.ajouterModifProbaViaVals(0.1, aArtiste)
        prob.ajouterModifProbaViaVals(0.05, estConquistaror)
        prob.ajouterModifProbaViaVals(0.03, estElfe)
        decRejMusicien = declencheur.Declencheur(prob, "decRejMusicien")
        decRejMusicien.AjouterCondition(aPasDeMetier)
        decRejMusicien.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejMusicien)

        # dessinateur
        prob = proba.Proba(0.0005, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Dessinateur.NOM, 0.05)
        prob.ajouterModifProbaViaVals(0.05, aArtiste)
        decRejDessinateur = declencheur.Declencheur(prob, "decRejDessinateur")
        decRejDessinateur.AjouterCondition(aPasDeMetier)
        decRejDessinateur.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejDessinateur)

        # poète
        prob = proba.Proba(0.0005, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Poete.NOM, 0.03)
        prob.ajouterModifProbaViaVals(0.1, aArtiste)
        prob.ajouterModifProbaViaVals(0.03, estElfe)
        decRejPoete = declencheur.Declencheur(prob, "decRejPoete")
        decRejPoete.AjouterCondition(aPasDeMetier)
        decRejPoete.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejPoete)

        # Bibliothecaire
        prob = proba.Proba(0.001, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Bibliothecaire.NOM, 0.05)
        prob.ajouterModifProbaViaVals(0.03, estTemplier)
        decRejBibliothecaire = declencheur.Declencheur(prob, "decRejBibliothecaire")
        decRejBibliothecaire.AjouterCondition(aPasDeMetier)
        decRejBibliothecaire.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejBibliothecaire)

        # Cartographe
        decRejCartographe = CreerDeclencheurDebutDeMetier(0.001, metier.Cartographe.NOM, 0.05)
        selecteur_.ajouterDeclencheur(decRejCartographe)

        # Marchand
        decRejMarchand = CreerDeclencheurDebutDeMetier(0.01, metier.Marchand.NOM, 0.05)
        selecteur_.ajouterDeclencheur(decRejMarchand)

        # Mineur
        decRejMineur = CreerDeclencheurDebutDeMetier(0.01, metier.Mineur.NOM, 0.05)
        selecteur_.ajouterDeclencheur(decRejMineur)

        # Pretre
        decRejPretre = CreerDeclencheurDebutDeMetier(0.002, metier.Pretre.NOM, 0.05)
        selecteur_.ajouterDeclencheur(decRejPretre)

        # Ouvrier
        decRejOuvrier = CreerDeclencheurDebutDeMetier(0.2, metier.Ouvrier.NOM, 0.04)
        selecteur_.ajouterDeclencheur(decRejOuvrier)

        # Politique
        decRejPolitique = CreerDeclencheurDebutDeMetier(0.002, metier.Politique.NOM, 0.05)
        selecteur_.ajouterDeclencheur(decRejPolitique)

        # Forgeron
        decRejForgeron = CreerDeclencheurDebutDeMetier(0.002, metier.Forgeron.NOM, 0.05)
        selecteur_.ajouterDeclencheur(decRejForgeron)

        # Alchimiste
        decRejAlchimiste = CreerDeclencheurDebutDeMetier(0.0001, metier.Alchimiste.NOM, 0.05)
        selecteur_.ajouterDeclencheur(decRejAlchimiste)

        # Medecin
        decRejMedecin = CreerDeclencheurDebutDeMetier(0.0, metier.Medecin.NOM, 0.07)
        selecteur_.ajouterDeclencheur(decRejMedecin)

        # TueurDeMonstres
        decRejTueurDeMonstres = CreerDeclencheurDebutDeMetier(0.0, metier.TueurDeMonstres.NOM, 0.05)
        selecteur_.ajouterDeclencheur(decRejTueurDeMonstres)

        # Architecte
        decRejArchitecte = CreerDeclencheurDebutDeMetier(0.003, metier.Architecte.NOM, 0.05)
        selecteur_.ajouterDeclencheur(decRejArchitecte)

        # Parasite
        prob = proba.Proba(0.003, True)
        AjouterModifDeProbaProressifPourMetier(prob, metier.Parasite.NOM, 0.02)
        prob.ajouterModifProbaViaVals(0.01, estParesseux)
        prob.ajouterModifProbaViaVals(0.03, estSournois)
        prob.ajouterModifProbaViaVals(0.01, aBeaute)
        prob.ajouterModifProbaViaVals(0.02, aCharme)
        decRejParasite = declencheur.Declencheur(prob, "decRejParasite")
        decRejParasite.AjouterCondition(aPasDeMetier)
        decRejParasite.AjouterCondition(univFinie)
        selecteur_.ajouterDeclencheur(decRejParasite)

        # Guerrier
        decRejGuerrier = CreerDeclencheurDebutDeMetier(0.002, metier.Guerrier.NOM, 0.05)
        selecteur_.ajouterDeclencheur(decRejGuerrier)

        # Chauffeur
        decRejChauffeur = CreerDeclencheurDebutDeMetier(0.02, metier.Chauffeur.NOM, 0.05)
        selecteur_.ajouterDeclencheur(decRejChauffeur)

        # Pilote
        decRejPilote = CreerDeclencheurDebutDeMetier(0.0, metier.Pilote.NOM, 0.05)
        selecteur_.ajouterDeclencheur(decRejPilote)

        # Chevalier
        decRejChevalier = CreerDeclencheurDebutDeMetier(0.0, metier.Chevalier.NOM, 0.05)
        selecteur_.ajouterDeclencheur(decRejChevalier)

        # Informaticien
        decRejInformaticien = CreerDeclencheurDebutDeMetier(0.0, metier.Informaticien.NOM, 0.06)
        selecteur_.ajouterDeclencheur(decRejInformaticien)

        # Cyberneticien
        decRejCyberneticien = CreerDeclencheurDebutDeMetier(0.0, metier.Cyberneticien.NOM, 0.06)
        selecteur_.ajouterDeclencheur(decRejCyberneticien)

        # Geneticien
        decRejGeneticien = CreerDeclencheurDebutDeMetier(0.0, metier.Geneticien.NOM, 0.06)
        selecteur_.ajouterDeclencheur(decRejGeneticien)

        # Commercial
        decRejCommercial = CreerDeclencheurDebutDeMetier(0.03, metier.Commercial.NOM, 0.05)
        selecteur_.ajouterDeclencheur(decRejCommercial)

        # Policier
        decRejPolicier = CreerDeclencheurDebutDeMetier(0.1, metier.Policier.NOM, 0.05)
        selecteur_.ajouterDeclencheur(decRejPolicier)

        # Vigile
        decRejVigile = CreerDeclencheurDebutDeMetier(0.01, metier.Vigile.NOM, 0.04)
        selecteur_.ajouterDeclencheur(decRejVigile)

        # Banquier
        decRejBanquier = CreerDeclencheurDebutDeMetier(0.01, metier.Banquier.NOM, 0.05)
        selecteur_.ajouterDeclencheur(decRejBanquier)

        # GardeDuCorps
        decRejGardeDuCorps = CreerDeclencheurDebutDeMetier(0.002, metier.GardeDuCorps.NOM, 0.04)
        selecteur_.ajouterDeclencheur(decRejGardeDuCorps)

        # Aventurier
        decRejAventurier = CreerDeclencheurDebutDeMetier( 0.002, metier.Aventurier.NOM, 0.04)
        selecteur_.ajouterDeclencheur(decRejAventurier)

        # Chasseur
        decRejChasseur = CreerDeclencheurDebutDeMetier(0.002,  metier.Chasseur.NOM, 0.01)
        selecteur_.ajouterDeclencheur(decRejChasseur)

        # Marin
        decRejMarin = CreerDeclencheurDebutDeMetier(0.04, metier.Marin.NOM, 0.05)
        selecteur_.ajouterDeclencheur(decRejMarin)

    def AjouterModifDeProbaProressifPourMetier(prob, nomMetier, facteur):
        """
        Modifie la proba selon le niveau du personnage dans le métier "nomMetier" en ajoutant "facteur" proba pour chaque niveau possédé pas le joueur
         - les niveaux vont de 1 (notions) à 10 (maître légendaire)
         - le facteur classique est 0.05. Plus le métier est spécialisé et demande de la formation plus ce facteur devrait monter, surtout si le métier est courant
        """
        condNiv1 = condition.Condition(nomMetier, 1, condition.Condition.SUPERIEUR_EGAL)
        prob.ajouterModifProbaViaVals(facteur, condNiv1)
        condNiv2 = condition.Condition(nomMetier, 2, condition.Condition.SUPERIEUR_EGAL)
        prob.ajouterModifProbaViaVals(facteur, condNiv2)
        condNiv3 = condition.Condition(nomMetier, 3, condition.Condition.SUPERIEUR_EGAL)
        prob.ajouterModifProbaViaVals(facteur, condNiv3)
        condNiv4 = condition.Condition(nomMetier, 4, condition.Condition.SUPERIEUR_EGAL)
        prob.ajouterModifProbaViaVals(facteur, condNiv4)
        condNiv5 = condition.Condition(nomMetier, 5, condition.Condition.SUPERIEUR_EGAL)
        prob.ajouterModifProbaViaVals(facteur, condNiv5)
        condNiv6 = condition.Condition(nomMetier, 6, condition.Condition.SUPERIEUR_EGAL)
        prob.ajouterModifProbaViaVals(facteur, condNiv6)
        condNiv7 = condition.Condition(nomMetier, 7, condition.Condition.SUPERIEUR_EGAL)
        prob.ajouterModifProbaViaVals(facteur, condNiv7)
        condNiv8 = condition.Condition(nomMetier, 8, condition.Condition.SUPERIEUR_EGAL)
        prob.ajouterModifProbaViaVals(facteur, condNiv8)
        condNiv9 = condition.Condition(nomMetier, 9, condition.Condition.SUPERIEUR_EGAL)
        prob.ajouterModifProbaViaVals(facteur, condNiv9)
        condNiv10 = condition.Condition(nomMetier, 10, condition.Condition.SUPERIEUR_EGAL)
        prob.ajouterModifProbaViaVals(facteur, condNiv10)

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

label decRejChasseur:
    # devient Chasseur
    "Vous êtes maintenant un Chasseur."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Chasseur.NOM)
    jump fin_cycle

label decRejAventurier:
    # devient Aventurier
    "Vous êtes maintenant un Aventurier."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Aventurier.NOM)
    jump fin_cycle

label decRejMarin:
    # devient Marin
    "Vous êtes maintenant un marin."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Marin.NOM)
    jump fin_cycle

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

label decRejChauffeur:
    # devient Chauffeur
    "Vous êtes maintenant un Chauffeur."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Chauffeur.NOM)
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
