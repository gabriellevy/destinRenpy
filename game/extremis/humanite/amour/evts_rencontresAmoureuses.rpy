init -5 python:
    import random
    from despin.gen_vie import declencheur
    from despin.gen_vie import selecteur
    from despin.gen_vie import proba
    from despin.abs import condition
    from extremis.socio_eco.metiers import metier
    from despin.reglages import filtres_action
    from extremis.humanite import trait
    from extremis.constitution import temps
    from extremis.coteries import coterie
    from extremis.humanite.sante import pbsante
    from extremis.humanite.amour import relationAmoureuse

    def AjouterCetteAmoureuse(situation, amoureuse):
        amoureuses = situation.GetValCarac(relationAmoureuse.RelationAmoureuse.C_AMOUREUSES)
        amoureuses.append(amoureuse)
        situation.SetValCarac(relationAmoureuse.RelationAmoureuse.C_AMOUREUSES, amoureuses)

    estAbstinentAscete = condition.Condition(trait.Ascetisme.NOM, trait.Trait.SEUIL_A, condition.Condition.SUPERIEUR_EGAL)
    estJouisseur = condition.Condition(trait.Ascetisme.NOM, trait.Trait.SEUIL_A_PAS, condition.Condition.INFERIEUR_EGAL)
    estObsedeSexuel = condition.Condition(trait.Sexualite.NOM, trait.Trait.SEUIL_A, condition.Condition.SUPERIEUR_EGAL)
    estPerversSexuel = condition.Condition(trait.Sexualite.NOM, trait.Trait.SEUIL_A_EXTREME, condition.Condition.SUPERIEUR_EGAL)
    estPeuSexuel = condition.Condition(trait.Sexualite.NOM, trait.Trait.SEUIL_A_PAS, condition.Condition.INFERIEUR_EGAL)
    estAbstinentSexuel = condition.Condition(trait.Sexualite.NOM, trait.Trait.SEUIL_A_PAS_EXTREME, condition.Condition.INFERIEUR_EGAL)

    estBeau = condition.Condition(trait.Beaute.NOM, trait.Trait.SEUIL_A, condition.Condition.SUPERIEUR_EGAL)
    estApollon = condition.Condition(trait.Beaute.NOM, trait.Trait.SEUIL_A_EXTREME, condition.Condition.SUPERIEUR_EGAL)
    estLaid = condition.Condition(trait.Beaute.NOM, trait.Trait.SEUIL_A_PAS, condition.Condition.INFERIEUR_EGAL)
    estHideux = condition.Condition(trait.Beaute.NOM, trait.Trait.SEUIL_A_PAS_EXTREME, condition.Condition.INFERIEUR_EGAL)

    estCharmant = condition.Condition(trait.Charme.NOM, trait.Trait.SEUIL_A, condition.Condition.SUPERIEUR_EGAL)
    estTresCharmant = condition.Condition(trait.Charme.NOM, trait.Trait.SEUIL_A_EXTREME, condition.Condition.SUPERIEUR_EGAL)
    estDeplaisant = condition.Condition(trait.Charme.NOM, trait.Trait.SEUIL_A_PAS, condition.Condition.INFERIEUR_EGAL)
    estTresDeplaisant = condition.Condition(trait.Charme.NOM, trait.Trait.SEUIL_A_PAS_EXTREME, condition.Condition.INFERIEUR_EGAL)

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

label decRencontre:
    $ amoureuse = pnj.GenererRelationAmoureuse(situation_)
    $ AjouterCetteAmoureuse(situation_, amoureuse)
    "Vous avez rencontré [amoureuse.prenom_]."

    jump fin_cycle

label decJoueurTombeAmoureux:
    $ amoureuse = pnj.GenererRelationAmoureuse(situation_)
    $ AjouterCetteAmoureuse(situation_, amoureuse)
    "[amoureuse.prenom_] vous fait complètement craquer."

label decPnjTombeAmoureuse:
    $ amoureuse = pnj.GenererRelationAmoureuse(situation_)
    $ AjouterCetteAmoureuse(situation_, amoureuse)
    "Cette [amoureuse.prenom_] semble avoir un faible pour vous."

    jump fin_cycle
