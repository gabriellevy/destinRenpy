
init -5 python:
    import random
    from despin.gen_vie import declencheur
    from despin.gen_vie import selecteur
    from despin.abs import condition

    def AjouterEvtsAdministratif():
        global selecteur_
        conditionAdministratif = condition.Condition("Métier", "Fonctionnaire administratif", condition.Condition.EGAL)
        conditionTmp = condition.Condition("Métier", "Test tmp", condition.Condition.EGAL)

        decVisiteInvestisseurs = declencheur.Declencheur(0.5, "decVisiteInvestisseurs")
        decVisiteInvestisseurs.AjouterCondition(conditionAdministratif)
        selecteur_.ajouterDeclencheur(decVisiteInvestisseurs)

        decVisiteInvestisseurs2 = declencheur.Declencheur(0.5, "decVisiteInvestisseurs2")
        decVisiteInvestisseurs2.AjouterCondition(conditionAdministratif)
        selecteur_.ajouterDeclencheur(decVisiteInvestisseurs2)

        testBidonAdministratif = declencheur.Declencheur(0.5, "testBidonAdministratif")
        testBidonAdministratif.AjouterCondition(conditionTmp)
        selecteur_.ajouterDeclencheur(testBidonAdministratif)

        testBidonAdministratif2 = declencheur.Declencheur(0.5, "testBidonAdministratif2")
        testBidonAdministratif2.AjouterCondition(conditionTmp)
        selecteur_.ajouterDeclencheur(testBidonAdministratif2)

label decVisiteInvestisseurs:
    "Déclenchement de decVisiteInvestisseurs. 1"
    jump debut_cycle

label decVisiteInvestisseurs2:
    "Déclenchement de decVisiteInvestisseurs. 2"
    jump debut_cycle

label testBidonAdministratif:
    "Test bidon à virer un de ces jours. 1"
    jump debut_cycle

label testBidonAdministratif2:
    "Test bidon à virer un de ces jours. 2"
    jump debut_cycle
