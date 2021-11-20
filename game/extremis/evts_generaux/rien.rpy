# fichier où sont générés les phrases d'ambiance à afficher quand il ne se passe rien durant un mois particulier

init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import metier
    from abs.humanite import trait
    from extremis.coteries import coterie
    from extremis.coteries.templiers import templiers
    from abs.religions import religion
    from extremis.geographie import quartier

    def AjouterEvtsRien():
        global selecteur_, situation_
        selecteurDEvenementVide = declencheur.Declencheur(1.0, "selecteurDEvenementVide")
        selecteur_.ajouterDeclencheur(selecteurDEvenementVide)

    def LancerEvtVide(situation):
        sceneParDefaut = ""
        # régénère les événements compatibles avec la situation
        evtsVides_ = ["evtRien1", "evtRien2", "evtRien3" ] # note : peut-être n'utiliser ces événements bidons que si on n'en a aps de plus intéressants ?

        # ------------------ EN PRISON -------------
        if situation_.GetValCarac(justice.Justice.C_LIBERTE) == justice.Justice.PRISON:
            evtsVides_.append("evtRien_Prison_1")
            evtsVides_.append("evtRien_Prison_2")
            evtsVides_.append("evtRien_Prison_3")
            evtsVides_.append("evtRien_Prison_4")
        else:
            # --------LIBRE
            if situation_.GetValCaracInt(metier.Metier.ADMINISTRATIF) > 0:
                evtsVides_.append("evtRien_Administratif1")

            # ------------- METIER ------------------
            # --- capacités
            if situation_.GetValCaracInt(metier.Chauffeur.NOM) > 0:
                evtsVides_.append("evtRien_Conduite")
            # --- métier principal du perso
            if situation_.GetValCarac(metier.Metier.C_METIER) == metier.Parasite.NOM:
                evtsVides_.append("evtRien_Parasite_1")
                evtsVides_.append("evtRien_Parasite_2")
            elif situation_.GetValCarac(metier.Metier.C_METIER) == metier.Paysan.NOM:
                evtsVides_.append("evtRien_Paysan_1")
                evtsVides_.append("evtRien_Paysan_2")
                evtsVides_.append("evtRien_Paysan_3")
                evtsVides_.append("evtRien_Paysan_4")
                evtsVides_.append("evtRien_Paysan_5")
                evtsVides_.append("evtRien_Paysan_6")
                evtsVides_.append("evtRien_Paysan_7")
                evtsVides_.append("evtRien_Paysan_8")
                evtsVides_.append("evtRien_Paysan_9")
                evtsVides_.append("evtRien_Paysan_10")
                evtsVides_.append("evtRien_Paysan_11")
                evtsVides_.append("evtRien_Paysan_12")

            # ----------------------------------------- selon coterie
            nomCoterie = situation_.GetValCarac(coterie.Coterie.C_COTERIE)
            nomCoterieUniv = situation_.GetValCarac(coterie.Coterie.Carac_UNIV_COURANTE)
            if nomCoterie ==  templiers.Templiers.ID or nomCoterieUniv == templiers.Templiers.ID:
                evtsVides_.append("evtRien_Templiers_1")
                evtsVides_.append("evtRien_Templiers_2")
                evtsVides_.append("evtRien_Templiers_3")
                evtsVides_.append("evtRien_Templiers_4")
                evtsVides_.append("evtRien_Templiers_5")
                evtsVides_.append("evtRien_Templiers_6")
                evtsVides_.append("evtRien_Templiers_7")
                evtsVides_.append("evtRien_Templiers_8")
                evtsVides_.append("evtRien_Templiers_9")
                evtsVides_.append("evtRien_Templiers_10")
                evtsVides_.append("evtRien_Templiers_11")
                evtsVides_.append("evtRien_Templiers_12")

            if nomCoterie ==  zaporogues.Zaporogues.ID or nomCoterieUniv == zaporogues.Zaporogues.ID:
                evtsVides_.append("evtRien_Zaporogues_1")

            # selon richesse
            valRichesse = situation_.GetValCaracInt(trait.Richesse.NOM)
            if valRichesse <= trait.Trait.SEUIL_A_PAS_EXTREME:
                # misérable
                evtsVides_.append("evtRien_Miserable_1")
                evtsVides_.append("evtRien_Miserable_2")
            elif valRichesse <= trait.Trait.SEUIL_A_PAS:
                # pauvre
                evtsVides_.append("evtRien_Pauvre_1")
                evtsVides_.append("evtRien_Pauvre_2")
            elif valRichesse < trait.Trait.SEUIL_A:
                # normal
                evtsVides_.append("evtRien_RichesseNormale_1")
            # elif valRichesse >= trait.Trait.SEUIL_A_EXTREME:
                # ultra riche
                # evtsVides_.append("evtRien_Richissime_1")
            # else:
                # riche
                # evtsVides_.append("evtRien_Riche_1")

        # selon religion
        religionActuelle = situation_.GetValCarac(religion.Religion.C_RELIGION)
        if religionActuelle == religion.Christianisme.NOM:
            evtsVides_.append("evtRien_saints")
            evtsVides_.append("evtRien_Christianisme_1")

        # fond selon quartier
        if sceneParDefaut == "":
            quartierCourant = situation.GetQuartier()
            if quartierCourant is not None:
                sceneParDefaut = quartierCourant.imageDeFond_

        if sceneParDefaut == "":
            sceneParDefaut = "bg rue_haussmann"

        # fond
        if sceneParDefaut != "":
            renpy.scene()
            renpy.show(sceneParDefaut)
        # en lance un au hasard
        renpy.jump(random.choice(evtsVides_))

label selecteurDEvenementVide:
    $ LancerEvtVide(situation_)

label evtRien_Conduite:
    scene bg route_campagne
    with Dissolve(.5)
    "Rien de tel qu'une bonne petit promenade à la campagne."
    jump fin_cycle

label evtRien1:
    with Dissolve(.5)
    "Et encore une journée de plus."
    jump fin_cycle

label evtRien2:
    with Dissolve(.5)
    "Les jours se suivent et se ressemblent."
    jump fin_cycle

label evtRien3:
    with Dissolve(.5)
    "Un jour c'est sûr quelque chose vous arrivera."
    jump fin_cycle

label evtRien_Administratif1:
    scene bg bureau
    with Dissolve(.5)
    "La vie de bureau suit son cours."
    jump fin_cycle
