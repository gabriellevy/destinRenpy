
init -5 python:
    import random
    from despin.gen_vie import declencheur
    from despin.gen_vie import selecteur
    from despin.gen_vie import proba
    from despin.abs import condition

    def AjouterEvtsAdministratif():
        global selecteur_
        conditionAdministratif = condition.Condition("Métier", "Fonctionnaire administratif", condition.Condition.EGAL)
        conditionTmp = condition.Condition("Métier", "Test tmp", condition.Condition.EGAL)
        conditionMathieu = condition.Condition("Prénom", "Mathieu", condition.Condition.EGAL)

        decVisiteInvestisseurs = declencheur.Declencheur(0.5, "decVisiteInvestisseurs")
        decVisiteInvestisseurs.AjouterCondition(conditionAdministratif)
        selecteur_.ajouterDeclencheur(decVisiteInvestisseurs)

        probaMathieu = proba.Proba(0.01)
        probaMathieu.ajouterModifProbaViaVals(10., conditionMathieu)
        decVisiteInvestisseurs2 = declencheur.Declencheur(probaMathieu, "decVisiteInvestisseurs_Mathieu")
        decVisiteInvestisseurs2.AjouterCondition(conditionAdministratif)
        selecteur_.ajouterDeclencheur(decVisiteInvestisseurs2)

        testBidonAdministratif = declencheur.Declencheur(0.5, "testBidonAdministratif")
        testBidonAdministratif.AjouterCondition(conditionTmp)
        selecteur_.ajouterDeclencheur(testBidonAdministratif)

        testBidonAdministratif2 = declencheur.Declencheur(0.5, "testBidonAdministratif2")
        testBidonAdministratif2.AjouterCondition(conditionTmp)
        selecteur_.ajouterDeclencheur(testBidonAdministratif2)

label decVisiteInvestisseurs:
    "Déclenchement de decVisiteInvestisseurs."
    jump debut_cycle

label decVisiteInvestisseurs_Mathieu:
    "Déclenchement de decVisiteInvestisseurs. Surtout si Mathieu !!!"
    jump debut_cycle

label testBidonAdministratif:
    "Test bidon à virer un de ces jours. 1"
    jump debut_cycle

label testBidonAdministratif2:
    "Test bidon à virer un de ces jours. 2"
    jump debut_cycle
