init -5 python:
    import random
    from extremis.coteries.elfes import elfes
    from extremis.socio_eco.metiers import metier
    from extremis.religions import religion

    def AjouterEvtsUnivElfes():
        """
        Quand on s'enrôle dans une université on doit accomplir un certain nombre de modules
        """
        global selecteur_
        conditionDansUniv = condition.Condition(coterie.Coterie.Carac_UNIV_COURANTE, elfes.Elfes.NOM, condition.Condition.EGAL)

        # très forte chance (proba absolue) de suivre des modules tant qu'on n'en a pas fait 6
        univElfes = declencheur.Declencheur(proba.Proba(0.6, False), "univElfes")
        univElfes.AjouterCondition(conditionDansUniv)
        selecteur_.ajouterDeclencheur(univElfes)

    def evtUnivElfesSuivant():
        global situation_

        evts = ["univElfes_evt1", "univElfes_evt2", "univElfes_evt3",
        "univElfes_evt4", "univElfes_evt5", "univElfes_evt6",
        "univElfes_evt7", "univElfes_evt8", "univElfes_evt9",
        "univElfes_evt10", "univElfes_evt11", "univElfes_evt12" ]

        prochainEvt = random.choice(evts)
        while situation_.GetValCaracInt(prochainEvt) == 1:
            prochainEvt = random.choice(evts)

        situation_.SetValCarac(prochainEvt, 1)
        renpy.jump( prochainEvt)

label univElfes:
    scene bg univ_elfes

    $ situation_.SetCarac(coterie.Coterie.Carac_UNIV_COURANTE, elfes.Elfes.NOM)
    $ numMoisRestants = situation_.GetValCaracInt(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE)
    if numMoisRestants == coterie.Coterie.NB_MOIS_UNIV_TOTAL_A_FAIRE:
        # intro :
        "intro univ elfes PAS FAITE. "

    $ numMoisRestants = situation_.GetValCaracInt(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE)
    if numMoisRestants < 1:
        # fin d'université
        $ situation_.SetCarac(coterie.Coterie.Carac_UNIV_COURANTE, "")
        jump decUnivCoterie
    else:
        $ situation_.RetirerACarac(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE, 1)
        $ situation_.TourSuivant()
        $ evtUnivElfesSuivant()
    jump fin_cycle

label univElfes_evt1:
    # est rendu plus beau
    $ beaute = situation_.GetValCaracInt(trait.Beaute.NOM)
    if beaute < 1 :
        "Votre laideur offense tellement vos maître qu'ils font une priorité de vous rendre présentable."
    else:
        "La beauté est primordiale pour les elfes et ils font en sorte que votre médiocrité ne soit pas un frein pour vous intégrer et vous sentir l'un des leurs. "
    "Pour cela ils utilisent une myriades d'outils et d'objets merveilleux. Des pommades, des bains, des amulettes et même des potions enchantées."
    "Le résultat est stupéfiant. "
    $ situation_.AjouterACarac(trait.Beaute.NOM, 2)
    jump fin_cycle

label univElfes_evt2:
    # effet devient artiste
    "Tous les elfes doivent être artistes, sinon ils redeviennent lentement de simples humains. "
    "L'université se doit de consacrer un grand nombre d'heures à rendre votre esprit ouvert à l'art et à la beauté."
    $ situation_.AjouterACarac(trait.Artiste.NOM, 2)
    jump fin_cycle

label univElfes_evt3:
    # effet frustration sexuelle
    "Vous êtes fasciné et tout émoustillé par la quantité incroyable de jeunes beautés que vous rencontrez à l'université elfique. "
    "Malheureusement elles n'ont que mérpis et moquerie pour vous et votre physique médiocre."
    $ resProba = random.uniform(0, 1.0)
    if resProba < 0.6:
        "Vous en intériosez une forte angoisse sur votre propre valeur."
        $ situation_.RetirerACarac(trait.Serenite.NOM, 1)
    elif resProba < 0.75:
        "Vous trouvez ça injuste et vous sentez profondément énervé contre elles et contre la société en général."
        $ situation_.AjouterACarac(trait.Violence.NOM, 1)
    else:
        "Vous décidez de vous concentrer sur votre propre amélioration et enrichissement pour un jour avoir votre chance avec une femme aussi belle"
        $ situation_.AjouterACarac(trait.Ambition.NOM, 1)
    jump fin_cycle

label univElfes_evt4:
    # effet devient Musicien
    scene bg musicien
    if situation_.GetValCarac(trait.Artiste.NOM) < 1:
        jump univElfes_evt2
    "Vu votre potentiel d'artiste les elfes trouvent indispensable de vous former à la musique, le plus noble de tous les arts."
    $ situation_.AjouterACarac(metier.Musicien.NOM, 1)
    jump fin_cycle

label univElfes_evt5:
    # effet devient Poète
    scene bg poesie
    if situation_.GetValCarac(trait.Artiste.NOM) < 1:
        jump univElfes_evt2
    "Vu votre poentiel d'artiste les elfes trouvent indispensable de vous former à la poésie, la pierre angulaire de la sensibilité elfique."
    $ situation_.AjouterACarac(metier.Poete.NOM, 1)
    jump fin_cycle

label univElfes_evt6:
    # effet devient Alchimiste
    scene bg alchimiste
    "La fabrication de potions, de filtres, de pommades est une composante essentielle de l'art elfique. "
    "Leurs usages sont innombrables et vont de potions de soins aux meilleurs produits de beauté du monde. "
    "Un maître herboriste détecte un certain potentiel chez vous et décide de vous apprendre les bases."
    $ situation_.AjouterACarac(metier.Alchimiste.NOM, 1)
    jump fin_cycle

label univElfes_evt7:
    "univElfes_evt7 PAS FAIT"
    jump fin_cycle
label univElfes_evt8:
    "univElfes_evt8 PAS FAIT"
    jump fin_cycle
label univElfes_evt9:
    "univElfes_evt9 PAS FAIT"
    jump fin_cycle
label univElfes_evt10:
    "univElfes_evt10 PAS FAIT"
    jump fin_cycle
label univElfes_evt11:
    "univElfes_evt11 PAS FAIT"
    jump fin_cycle
label univElfes_evt12:
    "univElfes_evt12 PAS FAIT"
    jump fin_cycle

label ElfesPostule:
    "Postulation aux Elfes : pas fait !"
    jump fin_cycle
