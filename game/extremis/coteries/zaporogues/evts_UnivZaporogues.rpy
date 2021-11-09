# musiques
# define audio.principale_temple = "musique/templiers/principale.mp3"

init -5 python:
    import random
    from extremis.coteries.zaporogues import zaporogues
    from extremis.socio_eco.metiers import metier
    from abs.religions import religion

    def AjouterEvtsUnivZaporogues():
        """
        Quand on s'enrôle dans une université on doit accomplir un certain nombre de modules
        """
        global selecteur_
        conditionDansUniv = condition.Condition(coterie.Coterie.Carac_UNIV_COURANTE, zaporogues.Zaporogues.ID, condition.Condition.EGAL)

        # très forte chance (proba absolue) de suivre des modules tant qu'on n'en a pas fait 6
        univZaporogues = declencheur.Declencheur(proba.Proba(0.6, False), "univZaporogues")
        univZaporogues.AjouterCondition(conditionDansUniv)
        selecteur_.ajouterDeclencheur(univZaporogues)

    def evtUnivZaporoguesSuivant():
        global situation_

        evts = ["univZaporogues_evt1", "univZaporogues_evt2", "univZaporogues_evt3",
        "univZaporogues_evt4", "univZaporogues_evt5", "univZaporogues_evt6",
        "univZaporogues_evt7", "univZaporogues_evt8", "univZaporogues_evt9",
        "univZaporogues_evt10", "univZaporogues_evt11", "univZaporogues_evt12"  ]

        prochainEvt = random.choice(evts)
        while situation_.GetValCaracInt(prochainEvt) == 1:
            prochainEvt = random.choice(evts)

        situation_.SetValCarac(prochainEvt, 1)
        renpy.jump( prochainEvt)

label univZaporogues:
    scene bg univ_zaporogues
    $ situation_.SetCarac(coterie.Coterie.Carac_UNIV_COURANTE, zaporogues.Zaporogues.ID)
    $ numMoisRestants = situation_.GetValCaracInt(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE)
    if numMoisRestants == coterie.Coterie.NB_MOIS_UNIV_TOTAL_A_FAIRE:
        # intro :
        # play music principale_temple
        "Vous allez passer cette année d'études dans la coterie dez zaporogues, les nomades coriaces et bons vivants des plaines de l'Est."
        "Les zaporogues n'ont pas à proprement parler d'université car l'apprentissage de leur mdoe de vie se fait nécessairement dans les grandes steppes asiatiques qui sont leur vraie maison."
        "Vous êtes néanmoins accueilli dans un bâtiment ancien de leur petit quartier de Suresne où vous entamerez votre instruction avant votre départ."

    $ numMoisRestants = situation_.GetValCaracInt(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE)
    if numMoisRestants < 1:
        # fin d'université
        $ situation_.SetCarac(coterie.Coterie.Carac_UNIV_COURANTE, "")
        jump decUnivCoterie
    else:
        $ situation_.RetirerACarac(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE, 1)
        $ situation_.TourSuivant()
        $ evtUnivZaporoguesSuivant()
    jump fin_cycle

label univZaporogues_evt1:
    # musique et danse
    "La musique, en particulier le chant et le violon, font partie intégrante de la vie des zaporogues. Elle rythme leurs journées, leur joies, leurs peines, et bien sûr leurs veillées au clair de lune."
    "Impossible de leur dire non, vous êtes entrainé jour après jour dans leurs danses endiabliées qui durent parfois jusqu'au lever du soleil."
    "Quelques mois de ce régime et vous avez toutes les bases pour briller au bal ou dans une chorale."
    $ AjouterACarac(metier.Musicien.NOM, 1)
    $ AjouterACarac(metier.Danseur.NOM, 2)
    jump fin_cycle

label univZaporogues_evt2:
    # chasse et survie dans la steppe
    "Dans la steppe immense il faut toujours avoir un plan de secours. Votre instructeur vous y entraîne en vous exerçant pendant un bon mois à vous nourrir, vous déplacer et vous vêtir en trouvant tout le nécessaire dans votre environnement."
    $ AjouterACarac(metier.Chasseur.NOM, 1)
    $ AjouterACarac(metier.Aventurier.NOM, 2)
    jump fin_cycle

label univZaporogues_evt3:
    # éleveur nomade
    "L'élevage est la première source de subsistance des zaporogues. Pour la nourriture, le transport, le couvert et le commerce, leurs gigantesques troupeaux sont indispensables pour les tribus."
    "Vous apprenez les bases du métier de berger parmi les moutons, les chèvres les chevaux et les vaches."
    $ AjouterACarac(metier.Berger.NOM, 2)
    jump fin_cycle

label univZaporogues_evt4:
    # périple
    "L'apprentissage de la vie zaporogue se fait inévitablement aux quatre coins du gigantesque territoire eurasiatique dans lequel les zaporogues se déplacent en permanence."
    "Durant ces voyages variés et souvent difficiles vous apprenez l'essentiel de ce qui fait le mode de vie zaporogue : la liberté et la vie à la dure."
    $ AjouterACarac(metier.Aventurier.NOM, 1)
    $ AjouterACarac(trait.Constitution.NOM, 1)
    $ AjouterACarac(trait.Liberte.NOM, 2)
    jump fin_cycle

label univZaporogues_evt5:
    "PAS FAIT univZaporogues_evt5"
    jump fin_cycle

label univZaporogues_evt6:
    "PAS FAIT univZaporogues_evt6"
    jump fin_cycle

label univZaporogues_evt7:
    "PAS FAIT univZaporogues_evt7"
    jump fin_cycle

label univZaporogues_evt8:
    "PAS FAIT univZaporogues_evt8"
    jump fin_cycle

label univZaporogues_evt9:
    "PAS FAIT univZaporogues_evt9"
    jump fin_cycle

label univZaporogues_evt10:
    "PAS FAIT univZaporogues_evt10"
    jump fin_cycle

label univZaporogues_evt11:
    "PAS FAIT univZaporogues_evt11"
    jump fin_cycle

label univZaporogues_evt12:
    "PAS FAIT univZaporogues_evt12"
    jump fin_cycle
