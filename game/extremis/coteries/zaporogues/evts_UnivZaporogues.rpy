# musiques
define audio.principale_zapos = "musique/zaporogues/01-10-Brahms_Hungarian_Dance_No_10_In_F-LLS.mp3"

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
    # risque d'alcolisme
    $ resProba = random.uniform(0, 1.0)
    if resProba <= 0.3:
        "Malheureusement les beuveries constantes qui accompagnent ces soirées ne vous laissent pas indemne. Vous devenez très largement dépendant de l'alcool."
        $ maladie = maladies_.TomberMaladeStr(situation_, pbsante.Alcoolisme.NOM)
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
    # Animiste
    $ religionActuelle = situation_.GetValCarac(religion.Religion.C_RELIGION)
    "Votre maître vous initie à sa religion animiste."
    "Un jour, durant un de vos voyages dans la steppe, il invoque vos ancêtres pour qu'ils vous reconnaissent et déterminent votre animal totem."
    $ nomAnimalTotem = determinerAnimalTotem()
    $ situation_.SetValCarac(religion.Animisme.NOM_TOTEM, nomAnimalTotem)
    "Quand vous sortez de la transe tout est clair dans votre esprit : vous avez trouvé votre animal totem et dans la steppe vous serez appelé ''[nomAnimalTotem]''"
    if religionActuelle != religion.Animisme.NOM:
        $ conversion = conversionReligieuse(religion.Animisme.NOM)
        if conversion:
            "Profondément marqué par l'expérience, vous vous convertissez à l'animisme Tengri."
        else:
            "Même si vous avez été profondément marqué par cette expérience vous ne prenez pas cette étrange religion au sérieux."
            "Votre maître ne vous en tient pas rigueur. Tolérant comme tous les zaporogues, il estime que la communion vous a rapproché de l'esprit de son peuple et que c'est l'essentiel."
    jump fin_cycle

label univZaporogues_evt6:
    # banquet avec animisme :
    # TODO : pas vraiment un événement d'université, pourrait être extrait
    $ zapoCot = situation_.collectionCoteries[zaporogues.Zaporogues.ID]
    $ nomTribu = zapoCot.nomTribu()
    "Une délégation de la tribu [nomTribu] est venu en visite dans la capitale pour vendre ses fourrures sibériennes."
    "Ils sont accueillis par un banquet monumental à la manière zaporogue, en plein bois de Boulogne."
    "Un des [nomTribu] est un chamane qui repère en vous un non initié aux mystères de l'animisme. Ils vous oriente vers des boissons et vapeurs spécifiques pour tenter de vous faire entrer en transe."
    $ test = testDeCarac.TestDeCarac(trait.Constitution.NOM, 3, situation_)
    menu:
        "Ces intoxication mettent votre corps à rude épreuve [test.affichage_]":
            pass

    $ reussi = test.TesterDifficulte(situation_)
    if reussi:
        "Vos perception se troublent et le reste de la nuit devient flou dans votre mémoire. Vous avez l'impression d'avoir vécu des milliers d'années et voyagé des milliers de kilomètres en une nuit."
        $ AjouterACarac(trait.Spiritualite.NOM, 2)
    else:
        "Sous l'effet des fumées toxiques qu'il vous souffle au visage vbous vous mettez à tousser puis à vomir. Le chaman ne s'excuse même pas. Vous n'êtes qu'un faible indigne de son enseignement juge-t'il."
        "Vous passez le reste de la nuit et la journée du lendemain en bien piètre état mais finissez par vous en remettre."

    jump fin_cycle

label univZaporogues_evt7:
    # sensibilité poésie théâtre
    "Les zaporogues ont tous la sensibilité à fleur de peau et ne peuvent concevoir la vie sans art, théâtre et poésie."
    "Vous passez un mois entier dans une troupe de théâtre vagabonde qui vous emploie comme homme à tout faire corvéable et vous pousse à vous exprimer et faire le figurant de temps à autre."
    "Cette ambiance effervescente vous affecte plus que de raison, vous en revenez profondément changé."
    $ AjouterACarac(trait.Artiste.NOM, 1)
    $ AjouterACarac(trait.Sensibilite.NOM, 1)
    $ AjouterACarac(metier.Poete.NOM, 1)
    $ AjouterACarac(metier.Acteur.NOM, 1)
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
