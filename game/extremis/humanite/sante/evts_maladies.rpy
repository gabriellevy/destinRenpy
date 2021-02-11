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

    def AjouterEvtsMaladies():
        global selecteur_
        # conditionAgeCoterie = condition.Condition(temps.Date.AGE_ANNEES, 16, condition.Condition.SUPERIEUR_EGAL)
        probaMaladie = proba.Proba(0.01)
        conditioChetif = condition.Condition(trait.Constitution.NOM, -2, condition.Condition.INFERIEUR_EGAL)
        probaMaladie.ajouterModifProbaViaVals(0.02, conditioChetif)
        conditionResistant = condition.Condition(trait.Constitution.NOM, 3, condition.Condition.SUPERIEUR_EGAL)
        probaMaladie.ajouterModifProbaViaVals(-0.005, conditionResistant)

        # à 16 ans on est OBLIGÉ de s'enrôler dans une université de coterie (au hasard)
        decTombeMalade = declencheur.Declencheur(probaMaladie, "decTombeMalade")
        selecteur_.ajouterDeclencheur(decTombeMalade)

label decTombeMalade:
    $ maladie = maladies_.TomberMaladeAleatoirement(situation_)
    $ texteMaladie = maladie.GetDescriptionRecu()
    "[texteMaladie]"

    jump fin_cycle
