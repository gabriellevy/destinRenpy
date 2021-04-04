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
    from extremis.humanite.amour import relationAmoureuse

    def AjouterCetteAmoureuse(situation, amoureuse):
        amoureuses = situation.GetValCarac(relationAmoureuse.RelationAmoureuse.C_AMOUREUSES)
        amoureuses.append(amoureuse)
        situation.SetValCarac(relationAmoureuse.RelationAmoureuse.C_AMOUREUSES, amoureuses)

    def AjouterEvtsRencontresAmoureuses():
        global selecteur_
        probaRencontre = proba.Proba(10.01)
        # conditioChetif = condition.Condition(trait.Constitution.NOM, -2, condition.Condition.INFERIEUR_EGAL)
        # probaMaladie.ajouterModifProbaViaVals(0.02, conditioChetif)
        # conditionResistant = condition.Condition(trait.Constitution.NOM, 3, condition.Condition.SUPERIEUR_EGAL)
        # probaMaladie.ajouterModifProbaViaVals(-0.005, conditionResistant)

        # à 16 ans on est OBLIGÉ de s'enrôler dans une université de coterie (au hasard)
        decRencontre = declencheur.Declencheur(probaRencontre, "decRencontre")
        selecteur_.ajouterDeclencheur(decRencontre)

label decRencontre:
    "decRencontre"
    $ amoureuse = pnj.GenererRelationAmoureuse(situation_)
    $ AjouterCetteAmoureuse(situation_, amoureuse)
    "Vous avez rencontré [amoureuse.prenom_]"

    jump fin_cycle
