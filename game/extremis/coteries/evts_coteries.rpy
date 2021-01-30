init -5 python:
    import random
    from despin.gen_vie import declencheur
    from despin.gen_vie import selecteur
    from despin.gen_vie import proba
    from despin.abs import condition
    from extremis.socio_eco import metier
    from despin.reglages import filtres_action
    from extremis.humanite import trait
    from extremis.constitution import temps


    def AjouterEvtsCoteries():
        global selecteur_
        conditionAgeCoterie = condition.Condition(temps.Date.AGE_ANNEES, 16, condition.Condition.SUPERIEUR_EGAL)

        decUnivCoterie = declencheur.Declencheur(proba.Proba(1.0, False), "decUnivCoterie") # proba stricte ?
        decUnivCoterie.AjouterCondition(conditionAgeCoterie)
        selecteur_.ajouterDeclencheur(decUnivCoterie)

label decUnivCoterie:
    "Ça y est vous avez l'âge de rejoindre les universités des coteries."
    jump fin_cycle
