init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.reglages import filtres_action
    from abs.humanite import trait
    from abs.univers import temps
    from abs.humanite.sante import pbsante
    from abs.humanite.amour import relationAmoureuse

    def AjouterCetteAmoureuse(situation, amoureuse):
        amoureuses = situation.GetValCarac(relationAmoureuse.RelA.C_AMOUREUSES)
        amoureuses.append(amoureuse)
        situation.SetValCarac(relationAmoureuse.RelA.C_AMOUREUSES, amoureuses)

    estAbstinentAscete = condition.Condition(trait.Ascetisme.NOM, trait.Trait.SEUIL_A, condition.Condition.SUPERIEUR_EGAL)
    estJouisseur = condition.Condition(trait.Ascetisme.NOM, trait.Trait.SEUIL_A_PAS, condition.Condition.INFERIEUR_EGAL)
    estObsedeSexuel = condition.Condition(trait.Sexualite.NOM, trait.Trait.SEUIL_A, condition.Condition.SUPERIEUR_EGAL)
    estPerversSexuel = condition.Condition(trait.Sexualite.NOM, trait.Trait.SEUIL_A_EXTREME, condition.Condition.SUPERIEUR_EGAL)
    estPeuSexuel = condition.Condition(trait.Sexualite.NOM, trait.Trait.SEUIL_A_PAS, condition.Condition.INFERIEUR_EGAL)
    estAbstinentSexuel = condition.Condition(trait.Sexualite.NOM, trait.Trait.SEUIL_A_PAS_EXTREME, condition.Condition.INFERIEUR_EGAL)

    estCelebre = condition.Condition(trait.Celebrite.NOM, trait.Trait.SEUIL_A, condition.Condition.SUPERIEUR_EGAL)
    estGlorieux = condition.Condition(trait.Celebrite.NOM, trait.Trait.SEUIL_A_EXTREME, condition.Condition.SUPERIEUR_EGAL)

    estBeau = condition.Condition(trait.Beaute.NOM, trait.Trait.SEUIL_A, condition.Condition.SUPERIEUR_EGAL)
    estApollon = condition.Condition(trait.Beaute.NOM, trait.Trait.SEUIL_A_EXTREME, condition.Condition.SUPERIEUR_EGAL)
    estLaid = condition.Condition(trait.Beaute.NOM, trait.Trait.SEUIL_A_PAS, condition.Condition.INFERIEUR_EGAL)
    estHideux = condition.Condition(trait.Beaute.NOM, trait.Trait.SEUIL_A_PAS_EXTREME, condition.Condition.INFERIEUR_EGAL)

    estCharmant = condition.Condition(trait.Charme.NOM, trait.Trait.SEUIL_A, condition.Condition.SUPERIEUR_EGAL)
    estTresCharmant = condition.Condition(trait.Charme.NOM, trait.Trait.SEUIL_A_EXTREME, condition.Condition.SUPERIEUR_EGAL)
    estDeplaisant = condition.Condition(trait.Charme.NOM, trait.Trait.SEUIL_A_PAS, condition.Condition.INFERIEUR_EGAL)
    estTresDeplaisant = condition.Condition(trait.Charme.NOM, trait.Trait.SEUIL_A_PAS_EXTREME, condition.Condition.INFERIEUR_EGAL)

    # état affectif et sexuel :
    aAuMoinsUnePnjEnSeduction = condition.Condition(relationAmoureuse.RelA.C_NB_PNJ_EN_SEDUCTION, 1, condition.Condition.SUPERIEUR_EGAL)
    aAuMoinsUnePnjQuiLuiPlait = condition.Condition(relationAmoureuse.RelA.C_NB_PNJ_EN_SEDUCTION_SUP_5, 1, condition.Condition.SUPERIEUR_EGAL)
    aRelationsSexuellesRegulieres = condition.Condition(relationAmoureuse.RelA.C_RELATIONS_SEXUELLES_REGULIERES, 1, condition.Condition.SUPERIEUR_EGAL)

    def AppliquerModifProbaSiSeduisible(proba):
        """
        applique des modifictaurs de proba à la proba en param pour qu'elle ait plus de chances d'arriver si le perso est
        du genre à tomber amoureux/en arrêt à tout bout de champs
        """
        proba.ajouterModifProbaViaVals(0.01, estObsedeSexuel)
        proba.ajouterModifProbaViaVals(0.01, estPerversSexuel)
        proba.ajouterModifProbaViaVals(0.01, estJouisseur)
        proba.ajouterModifProbaViaVals(-0.005, estPeuSexuel)
        proba.ajouterModifProbaViaVals(-0.005, estAbstinentSexuel)
        proba.ajouterModifProbaViaVals(-0.005, estAbstinentAscete)

    def AppliquerModifProbaSiSeduisant(proba):
        """
        applique des modifictaurs de proba à la proba en param pour qu'elle ait plus de chances d'arriver si le perso est séduisant
        """
        proba.ajouterModifProbaViaVals(0.01, estBeau)
        proba.ajouterModifProbaViaVals(0.01, estApollon)
        proba.ajouterModifProbaViaVals(-0.005, estLaid)
        proba.ajouterModifProbaViaVals(-0.005, estHideux)
        proba.ajouterModifProbaViaVals(0.01, estCharmant)
        proba.ajouterModifProbaViaVals(0.01, estTresCharmant)
        proba.ajouterModifProbaViaVals(-0.005, estDeplaisant)
        proba.ajouterModifProbaViaVals(-0.005, estTresDeplaisant)
        proba.ajouterModifProbaViaVals(0.01, estCelebre)
        proba.ajouterModifProbaViaVals(0.01, estGlorieux)

    def AjouterEvtsRencontresAmoureuses():
        global selecteur_
        # rencontre "mutuelle" où les deux se sont au moins un peu remarqués
        probaRencontre = proba.Proba(0.01)
        AppliquerModifProbaSiSeduisant(probaRencontre)
        AppliquerModifProbaSiSeduisible(probaRencontre)
        decRencontre = declencheur.Declencheur(probaRencontre, "decRencontre")
        selecteur_.ajouterDeclencheur(decRencontre)

        # rencontre où le personnage joueur est le seul à être tombé amoureux
        probaJoueurTombeAmoureux = proba.Proba(0.01)
        AppliquerModifProbaSiSeduisible(probaJoueurTombeAmoureux)
        decJoueurTombeAmoureux = declencheur.Declencheur(probaJoueurTombeAmoureux, "decJoueurTombeAmoureux")
        selecteur_.ajouterDeclencheur(decJoueurTombeAmoureux)

        # rencontre où une pnj est la seule à être tombé amoureuse
        probaPnjTombeAmoureuse = proba.Proba(0.01)
        AppliquerModifProbaSiSeduisant(probaPnjTombeAmoureuse)
        decPnjTombeAmoureuse = declencheur.Declencheur(probaPnjTombeAmoureuse, "decPnjTombeAmoureuse")
        selecteur_.ajouterDeclencheur(decPnjTombeAmoureuse)

        # -------------> passage de phase séduction à lui faire la cour
        probaFaireLaCour = proba.Proba(0.1)
        # à faire : aumenter cette proba si victorien
        decFaireLaCour = declencheur.Declencheur(probaFaireLaCour, "decFaireLaCour")
        decFaireLaCour.AjouterCondition(aAuMoinsUnePnjQuiLuiPlait)
        selecteur_.ajouterDeclencheur(decFaireLaCour)

    def MAJCaracsRelationsAmoureuses(situation):
        """
        met à jour les caracs de relation amoureuses qui servent de conditions aux événements
        (essentiellement déduites de la liste des relations amoureuses)
        """
        nbPnjEnSeduction = 0
        nbPnjEnSeductionQuiLuiPlait = 0
        aDesRelationsSexuellesRegulieres = 0
        amoureuses = situation.GetValCarac(relationAmoureuse.RelA.C_AMOUREUSES)
        for amoureuse in amoureuses:
            typeRelation = amoureuse.relationAmoureuse_.typeRelation_
            if typeRelation == relationAmoureuse.RelA.SEDUCTION:
                nbPnjEnSeduction = nbPnjEnSeduction + 1
                if amoureuse.relationAmoureuse_.interetJoueurEnversPnj_ >= 2 : # tmp : devrait être 5 mais c'est pour tester tmp !!!
                    nbPnjEnSeductionQuiLuiPlait = nbPnjEnSeductionQuiLuiPlait + 1
            if typeRelation == relationAmoureuse.RelA.OCCASIONNEL \
            or typeRelation == relationAmoureuse.RelA.MARIAGE \
            or typeRelation == relationAmoureuse.RelA.COHABITATION: \
                aDesRelationsSexuellesRegulieres = 1

        situation.SetValCarac(relationAmoureuse.RelA.C_NB_PNJ_EN_SEDUCTION , nbPnjEnSeduction)
        situation.SetValCarac(relationAmoureuse.RelA.C_NB_PNJ_EN_SEDUCTION_SUP_5 , nbPnjEnSeductionQuiLuiPlait)
        situation.SetValCarac(relationAmoureuse.RelA.C_RELATIONS_SEXUELLES_REGULIERES , aDesRelationsSexuellesRegulieres)

label decFaireLaCour:
    $ amoureuse = relationAmoureuse.GetUneAmoureuseEnSeduction(situation_) # A FAIRE : ne récupérez qu'une amoureuse d'un certain niveau ?
    if amoureuse is not None:
        "[amoureuse.nom_] vous plaît tellement que vous tentez de la séduire par tous les moyens."
        $ relationAmoureuse.FaitLaCour(situation_, amoureuse)
    $ MAJCaracsRelationsAmoureuses(situation_)

label decRencontre:
    $ amoureuse = pnj_destin.GenererRelationAmoureuseDestin(situation_) # Destin ajouté en attendant de trouver un meilleur système
    $ AjouterCetteAmoureuse(situation_, amoureuse)
    "Vous avez rencontré [amoureuse.nom_]."
    $ MAJCaracsRelationsAmoureuses(situation_)
    jump fin_cycle

label decJoueurTombeAmoureux:
    $ amoureuse = pnj_destin.GenererRelationAmoureuseDestin(situation_) # Destin ajouté en attendant de trouver un meilleur système
    $ AjouterCetteAmoureuse(situation_, amoureuse)
    "[amoureuse.nom_] vous fait complètement craquer."
    $ MAJCaracsRelationsAmoureuses(situation_)
    jump fin_cycle

label decPnjTombeAmoureuse:
    $ amoureuse = pnj_destin.GenererRelationAmoureuseDestin(situation_) # Destin ajouté en attendant de trouver un meilleur système
    $ AjouterCetteAmoureuse(situation_, amoureuse)
    "Cette [amoureuse.nom_] semble avoir un faible pour vous."
    $ MAJCaracsRelationsAmoureuses(situation_)
    jump fin_cycle
