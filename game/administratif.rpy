
init -5 python:
    import random
    from despin.gen_vie import declencheur
    from despin.gen_vie import selecteur

    def AjouterEvtsAdministratif():
        global selecteur_
        decVisiteInvestisseurs = declencheur.Declencheur(0.5, "decVisiteInvestisseurs")
        selecteur_.ajouterDeclencheur(decVisiteInvestisseurs)
        testBidonAdministratif = declencheur.Declencheur(0.5, "testBidonAdministratif")
        selecteur_.ajouterDeclencheur(testBidonAdministratif)

label decVisiteInvestisseurs:
    "Déclenchement de decVisiteInvestisseurs."
    jump debut_cycle

label testBidonAdministratif:
    "Test bidon à virer un de ces jours."
    jump debut_cycle
