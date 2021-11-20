define audio.paso_doble = "musique/conquistadors/01-02-Cantovano_and_His_Orchestra-El_Gato_Mont-LLS.mp3"
define audio.paso_doble_doux = "musique/conquistadors/01-05-Cantovano_and_His_Orchestra-Fiesta_Moren-LLS.mp3"
define audio.paso_doble_guitare = "musique/conquistadors/01-07-Cantovano_and_His_Orchestra-El_Picador-LLS.mp3"
define audio.diablo_rojo = "musique/conquistadors/02-Diablo rojo.mp3"
define audio.tamacun = "musique/conquistadors/01-Tamacun.mp3"
define audio.stairway_gabriella = "musique/conquistadors/06-Stairway to heaven.mp3"
define audio.orion_gabriella = "musique/conquistadors/07-Orion.mp3"

init -5 python:
    import random
    from extremis.coteries.conquistadors import conquistadors
    from abs.humanite import metier
    from abs.religions import religion

    estConquistador = condition.Condition(coterie.Coterie.C_COTERIE, conquistadors.Conquistadors.ID, condition.Condition.EGAL)
    estPasConquistador = condition.Condition(coterie.Coterie.C_COTERIE, conquistadors.Conquistadors.ID, condition.Condition.DIFFERENT)
    estDansQuartierConquistador = condition.Condition(quartier.Quartier.C_QUARTIER, quartier.SaintMalo.NOM, condition.Condition.EGAL)
    def AjouterEvtsConquistadors():
        """
        événements génériques qui concernent les conquistadors
        """
        global selecteur_

        recrutementDesPauvresParConquistadors = declencheur.Declencheur(proba.Proba(0.1, True), "recrutementDesPauvresParConquistadors")
        recrutementDesPauvresParConquistadors.AjouterCondition(estPasConquistador)
        recrutementDesPauvresParConquistadors.AjouterCondition(estPauvre)
        recrutementDesPauvresParConquistadors.AjouterCondition(aAgeDeRecrutement)
        recrutementDesPauvresParConquistadors.AjouterCondition(conditionPasUniv)
        selecteur_.ajouterDeclencheur(recrutementDesPauvresParConquistadors)

label recrutementDesPauvresParConquistadors:
    # Conversion des pauvres
    "Alors que vous êtes au plus bas à déprimer dans un bar vous êtes abordé par un jovial conquistador en armure resplendissante. Il vous vante la vie aventureuse aux confins du monde où vous pourrez avoir une vie aventureuse pleine de combats et de pillages. "
    "Là où la fortune se fait au mérite loin des magouilles politiciennes."
    $ affecte = False # est-ce que le prêche l'a affecté
    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.3:
        $ RetirerACarac(trait.Prudence.NOM, 1)
        $ affecte = True
    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.3:
        $ AjouterACarac(trait.Cupidite.NOM, 1)
        $ affecte = True
    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.3:
        $ AjouterACarac(trait.Opportunisme.NOM, 1)
        $ affecte = True

    $ conquistadorsCot = coteries_[conquistadors.Conquistadors.ID]
    $ affinite = conquistadorsCot.CalculerAffinite(situation_)
    if affinite > 0:
        "Ses arguments vous convainquent de postuler."
        jump conquistadorsPostule
    elif affecte:
        "Quoique son discours vous ait beaucoup affecté, ses arguments ne vous convainquent pas de rejoindre les conquisstadors."
    else:
        "Ca ne suffit néanmoins pas à vous convaincre de devenir un conquistador."

    jump fin_cycle
