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

    def AjouterEvtsCoteries():
        global selecteur_
        conditionAgeCoterie = condition.Condition(temps.Date.AGE_ANNEES, 16, condition.Condition.SUPERIEUR_EGAL)
        conditionPasUniv = condition.Condition(coterie.Coterie.Carac_UNIV_COURANTE, "", condition.Condition.EGAL)
        conditionUnivPasTerminee = condition.Condition(coterie.Coterie.Carac_NB_UNIV, coterie.Coterie.NB_UNIV_TOTAL, condition.Condition.INFERIEUR_EGAL)

        # à 16 ans on est OBLIGÉ de s'enrôler dans une université de coterie (au hasard)
        decUnivCoterie = declencheur.Declencheur(proba.Proba(1.0, False), "decUnivCoterie")
        decUnivCoterie.AjouterCondition(conditionAgeCoterie)
        decUnivCoterie.AjouterCondition(conditionPasUniv)
        decUnivCoterie.AjouterCondition(conditionUnivPasTerminee)
        selecteur_.ajouterDeclencheur(decUnivCoterie)

    def ChoisirCoterie():
        global situation_, coteries_, traits_, metiers_

        # calculer les coefficient d'intérêt du perso pour chaque coterie :
        indexCoteries = dict()
        for idCoterie in coteries_.lCoteries_:
            affinite = coteries_.lCoteries_[idCoterie].CalculerAffinite(situation_)
            indexCoteries[idCoterie] = affinite
            # print("coterie {} -> affinité {}".format(idCoterie, affinite))

        # éliminer les coeff inférieurs à 1
        for cle in indexCoteries.keys():
            resAffinite = indexCoteries[cle]
            if resAffinite < 1:
                print("retire {}".format(cle))
                indexCoteries.pop(cle)

        # trier les autres par ordre décroissant
        coterieChoisie = ""
        plusHautRes = 0
        for cle in indexCoteries.keys():
            if indexCoteries[cle] > plusHautRes:
                plusHautRes = indexCoteries[cle]
                coterieChoisie = cle

        print("coterieChoisie {}".format(coterieChoisie))
        return coterieChoisie


label decUnivCoterie:
    $ numUnivCoteries = situation_.GetValCaracInt(coterie.Coterie.Carac_NB_UNIV)
    if numUnivCoteries < 1:
        "Ça y est vous avez l'âge de rejoindre les universités des coteries."
    else:
        if numUnivCoteries >= coterie.Coterie.NB_UNIV_TOTAL:
            "Vous avez accompli vos années d'université légales. Il est temps de se lancer dans la vie active."
            "Choix éventuel PAS FAIT"
            $ situation_.SetValCarac(coterie.Coterie.Carac_UNIV_COURANTE, "fini")
            jump choixUniv
        else:
            "Cette année d'université se termine, place à la suivante."
    $ situation_.SetCarac(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE, coterie.Coterie.NB_MOIS_UNIV_TOTAL_A_FAIRE)
    $ AjouterACarac(coterie.Coterie.Carac_NB_UNIV, 1)
    $ univ = coteries_.DebuterProchaineUniversite(situation_)
    $ renpy.jump(univ)

label choixUniv:
    # le joueur va éventuellement choisir une université
    $ coterieChoisie = ChoisirCoterie()
    if coterieChoisie == "":
        "Après réflexion aucune coterie ne répond à vos désirs et intérêts profonds. Vous préférez suivre votre propre route pour l'instant."
    else:
        $ labelPostuleCoterie = "{}{}".format(coterieChoisie, "Postule")
        $ renpy.jump(labelPostuleCoterie)

    jump fin_cycle
