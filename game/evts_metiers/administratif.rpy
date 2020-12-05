
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

        decVisiteInvestisseurs = declencheur.Declencheur(400.02, "decVisiteInvestisseurs")
        decVisiteInvestisseurs.AjouterCondition(conditionAdministratif)
        selecteur_.ajouterDeclencheur(decVisiteInvestisseurs)

    # attention des actions sont à exécuter au début et à al fin de chaque événement administratif :
    def actionDebutAdministratif():
        global situation_
        renpy.transition(dissolve)
        renpy.scene()
        renpy.show("bg bureau")
        # metier.regenererCaracsMetier(situation_)

    # attention des actions sont à exécuter au début et à al fin de chaque événement administratif :
    def actionFinAdministratif():
        global situation_
        # metier.regenererCaracsMetier(situation_)


label decVisiteInvestisseurs:
    $ actionDebutAdministratif()
    "Visite d'investisseurs. A FAIRE"
    $ actionFinAdministratif()
    jump debut_cycle
