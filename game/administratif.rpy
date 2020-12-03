
init -5 python:
    import random
    from despin.gen_vie import declencheur
    from despin.gen_vie import selecteur
    from despin.gen_vie import proba
    from despin.abs import condition
    from despin.extremis import metier

    def AjouterEvtsAdministratif():
        global selecteur_
        conditionAdministratif = condition.Condition(metier.Metier.ADMINISTRATIF, 1, condition.Condition.EGAL)
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
        selecteur_.ajouterDeclencheur(testBidonAdministratif)

        testBidonAdministratif2 = declencheur.Declencheur(0.5, "testBidonAdministratif2")
        selecteur_.ajouterDeclencheur(testBidonAdministratif2)

    # attention des actions sont à exécuter au début et à al fin de chaque événement administratif :
    def actionDebutAdministratif():
        global situation_
        metier.regenererCaracsMetier(situation_)

    # attention des actions sont à exécuter au début et à al fin de chaque événement administratif :
    def actionFinAdministratif():
        global situation_
        metier.regenererCaracsMetier(situation_)


label decVisiteInvestisseurs:
    $ actionDebutAdministratif()
    "Déclenchement de decVisiteInvestisseurs."
    $ actionFinAdministratif()
    jump debut_cycle

label decVisiteInvestisseurs_Mathieu:
    $ actionDebutAdministratif()
    "Déclenchement de decVisiteInvestisseurs. Surtout si Mathieu !!!"
    $ actionFinAdministratif()
    jump debut_cycle

label testBidonAdministratif:
    $ actionDebutAdministratif()
    "Test bidon à virer un de ces jours. 1"
    $ actionFinAdministratif()
    jump debut_cycle

label testBidonAdministratif2:
    $ actionDebutAdministratif()
    "Test bidon à virer un de ces jours. 2"
    $ actionFinAdministratif()
    jump debut_cycle
