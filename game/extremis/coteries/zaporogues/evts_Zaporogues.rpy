
# define audio.tedonimum = "musique/templiers/tedonimum.mp3"

init -5 python:
    import random
    from extremis.coteries.zaporogues import zaporogues
    from abs.humanite import metier
    from abs.religions import religion
    from extremis.socio_eco.crime import justice

    estZaporogue = condition.Condition(coterie.Coterie.C_COTERIE, zaporogues.Zaporogues.ID, condition.Condition.EGAL)
    estPasZaporogue = condition.Condition(coterie.Coterie.C_COTERIE, zaporogues.Zaporogues.ID, condition.Condition.DIFFERENT)
    estDansQuartierZaporogue = condition.Condition(quartier.Quartier.C_QUARTIER, quartier.Suresnes.NOM, condition.Condition.EGAL)

    def AjouterEvtsZaporogues():
        """
        événements génériques qui concernent les Zaporogues
        """
        global selecteur_

        # a faire : recutement zaporogue en cours de vie
        # recrutementZaporogues = declencheur.Declencheur(proba.Proba(0.1, True), "recrutementZaporogues")
        # recrutementZaporogues.AjouterCondition(estPasZaporogue)
        # recrutementZaporogues.AjouterCondition(aAgeDeRecrutement)
        # recrutementZaporogues.AjouterCondition(conditionPasUniv)
        # selecteur_.ajouterDeclencheur(recrutementZaporogues)
