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
    from extremis.coteries import coterie

    def AjouterEvtsCoteries():
        global selecteur_
        conditionAgeCoterie = condition.Condition(temps.Date.AGE_ANNEES, 16, condition.Condition.SUPERIEUR_EGAL)

        decUnivCoterie = declencheur.Declencheur(proba.Proba(1.0, False), "decUnivCoterie") # proba stricte ?
        decUnivCoterie.AjouterCondition(conditionAgeCoterie)
        selecteur_.ajouterDeclencheur(decUnivCoterie)

label decUnivCoterie:
    $ numUnivCoteries = situation_.GetValCaracInt(coterie.Coterie.NB_UNIV)
    if numUnivCoteries < 1:
        "Ça y est vous avez l'âge de rejoindre les universités des coteries."
    else:
        "Cette année d'université se termine, place à la suivante."
    $ situation_.SetCarac(coterie.Coterie.NB_MOIS_UNIV_A_FAIRE, 12)
    $ situation_.AjouterACarac(coterie.Coterie.NB_UNIV, 1)
    $ univ = coteries_.DebuterProchaineUniversite()
    $ renpy.jump(univ)
