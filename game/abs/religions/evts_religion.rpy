define audio.sanctus = "musique/templiers/sanctus.mp3"
define audio.turexgloriae = "musique/templiers/turexgloriae.mp3"

init -5 python:
    import random
    from abs.religions import religion

    estAthee = condition.Condition(religion.Religion.C_RELIGION, religion.Atheisme.NOM, condition.Condition.EGAL)
    estPasAthee = condition.Condition(religion.Religion.C_RELIGION, religion.Atheisme.NOM, condition.Condition.DIFFERENT)
    estChretien = condition.Condition(religion.Religion.C_RELIGION, religion.Christianisme.NOM, condition.Condition.EGAL)
    estPasChretien = condition.Condition(religion.Religion.C_RELIGION, religion.Christianisme.NOM, condition.Condition.DIFFERENT)
    estAnimiste = condition.Condition(religion.Religion.C_RELIGION, religion.Animisme.NOM, condition.Condition.EGAL)
    estPasAnimiste = condition.Condition(religion.Religion.C_RELIGION, religion.Animisme.NOM, condition.Condition.DIFFERENT)
    aPasDeReligion = condition.Condition(religion.Religion.C_RELIGION, "", condition.Condition.EGAL)
    aUneReligion = condition.Condition(religion.Religion.C_RELIGION, "", condition.Condition.DIFFERENT)
    # traits
    estCruel = condition.Condition(trait.Altruisme.NOM, -13, condition.Condition.INFERIEUR_EGAL)
    estEgoiste = condition.Condition(trait.Altruisme.NOM, -3, condition.Condition.INFERIEUR_EGAL)
    estGenereux = condition.Condition(trait.Altruisme.NOM, 1, condition.Condition.SUPERIEUR_EGAL)
    estAltruiste = condition.Condition(trait.Altruisme.NOM, 11, condition.Condition.SUPERIEUR_EGAL)

    def devientAthee():
        """
        Applique tous les changements liées au fait de quitter sa religion
        return False si le perso n'avait aps de religion
        """
        global situation_
        religionCourante = situation_.GetValCarac(religion.Religion.C_RELIGION)
        if religionCourante == "" or religionCourante == religion.Atheisme.NOM:
            situation_.SetCarac(religion.Religion.C_RELIGION,  religion.Atheisme.NOM)
            situation_.SetCarac(religion.Religion.C_FOI,  0)
            situation_.SetCarac(religion.Religion.C_MIRACLE,  0)
            return True
        return False

    def conversionReligieuse(p_religion, forceConversion=False):
        """
        forceConversion : si True le perso est immédiatement converti, sinon il a des chances de ne aps l'être si il a déjà une religion
        """
        global situation_

        religionCaracStr = religion.Religion.C_RELIGION
        religionActuelle = situation_.GetValCarac(religionCaracStr)
        if religionActuelle == "":
            # pas de religion
            situation_.SetValCarac(religion.Religion.C_RELIGION, p_religion)
            return True
        elif religionActuelle == p_religion:
            # déjà de cette religion
            return False
        else:
            randVal = random.uniform(0, 1.0)
            # conversion pas 100% sûr
            if randVal < 0.7:
                situation_.SetValCarac(religion.Religion.C_RELIGION, p_religion)
                return True
            else:
                return False

    def AjouterEvtsChretiens():
        global selecteur_
        estPretreNiv5 = condition.Condition(metier.Pretre.NOM, 5, condition.Condition.SUPERIEUR_EGAL)
        estPasEveque = condition.Condition(metier.Metier.C_TITRE, religion.Christianisme.EVEQUE, condition.Condition.DIFFERENT)

        # très forte chance (proba absolue) de suivre des modules tant qu'on n'en a pas fait 6
        nominationEveque = declencheur.Declencheur(proba.Proba(0.01, True), "nominationEveque")
        nominationEveque.AjouterCondition(estChretien)
        nominationEveque.AjouterCondition(estPretreNiv5)
        nominationEveque.AjouterCondition(estPasEveque)
        selecteur_.ajouterDeclencheur(nominationEveque)

        # Don aux pauvres
        prob = proba.Proba(0.003, True)
        prob.ajouterModifProbaViaVals(0.01, estGenereux)
        prob.ajouterModifProbaViaVals(0.02, estAltruiste)
        prob.ajouterModifProbaViaVals(-0.003, estEgoiste)
        donAuxPauvres = declencheur.Declencheur(prob, "donAuxPauvres")
        donAuxPauvres.AjouterCondition(estChretien)
        selecteur_.ajouterDeclencheur(donAuxPauvres)

label donAuxPauvres:
    # Don aux pauvres
    play music turexgloriae noloop
    "Vous donnez une grande partie de votre argent pour soutenir les pauvres."
    $ situation_.RetirerACarac(trait.Richesse.NOM, 1)
    jump fin_cycle

label nominationEveque:
    # Nomination comme évèque";
    play music sanctus noloop
    "Pour vos fortes compétences et votre ancienneté, et pour votre foi bien sûr, vous êtes nommé évèque."
    $ situation_.SetCarac(metier.Metier.C_TITRE, religion.Religion.EVEQUE)
    jump fin_cycle
