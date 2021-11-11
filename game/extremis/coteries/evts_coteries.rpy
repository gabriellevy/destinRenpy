init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from extremis.socio_eco.metiers import metier
    from abs.reglages import filtres_action
    from abs.humanite import trait
    from extremis.constitution import temps
    from extremis.coteries import coterie

    aAgeDeRecrutement = condition.Condition(temps.Date.AGE_ANNEES, 20, condition.Condition.SUPERIEUR_EGAL) # peut être recruté apr des coterie (univ finie)
    conditionPasUniv = condition.Condition(coterie.Coterie.Carac_UNIV_COURANTE, "", condition.Condition.EGAL)
    def AjouterEvtsCoteries():
        global selecteur_
        conditionAgeCoterieDeb = condition.Condition(temps.Date.AGE_ANNEES, 16, condition.Condition.SUPERIEUR_EGAL)
        conditionAgeCoterieFin = condition.Condition(temps.Date.AGE_ANNEES, 25, condition.Condition.INFERIEUR_EGAL)
        conditionUnivPasTerminee = condition.Condition(coterie.Coterie.Carac_NB_UNIV, coterie.Coterie.NB_UNIV_TOTAL, condition.Condition.INFERIEUR_EGAL)

        # entre 16 et 25 ans on est OBLIGÉ de s'enrôler dans une université de coterie (au hasard)
        # la proba est donc non relative et hautement probable
        decUnivCoterie = declencheur.Declencheur(proba.Proba(0.8, False), "decUnivCoterie")
        decUnivCoterie.AjouterCondition(conditionAgeCoterieDeb)
        decUnivCoterie.AjouterCondition(conditionAgeCoterieFin)
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
                # print("retire {} (<1)".format(cle))
                indexCoteries.pop(cle)

        # trier les autres par ordre décroissant
        coterieChoisie = ""
        plusHautRes = 0
        for cle in indexCoteries.keys():
            if indexCoteries[cle] > plusHautRes:
                plusHautRes = indexCoteries[cle]
                coterieChoisie = cle

        # print("coterieChoisie {}".format(coterieChoisie))
        return coterieChoisie


label decUnivCoterie:
    $ numUnivCoteries = situation_.GetValCaracInt(coterie.Coterie.Carac_NB_UNIV)
    if numUnivCoteries < 1:
        "Ça y est vous avez l'âge de rejoindre les universités des coteries."
        $ metierObj = metiers_[metier.Etudiant.NOM]
        $ metierObj.Rejoindre(situation_)
    else:
        if numUnivCoteries >= coterie.Coterie.NB_UNIV_TOTAL:
            "Vous avez accompli vos années d'université légales. Il est temps de se lancer dans la vie active."
            "Choix éventuel PAS FAIT"
            $ situation_.SetValCarac(coterie.Coterie.Carac_UNIV_COURANTE, "fini")
            $ situation_.SetValCarac(metier.Metier.C_METIER, "")
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
