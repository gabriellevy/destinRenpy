init -5 python:
    import random
    from extremis.coteries.conquistadors import conquistadors
    from extremis.socio_eco.metiers import metier
    from extremis.religions import religion

    def AjouterEvtsUnivConquistadors():
        """
        Quand on s'enrôle dans une université on doit accomplir un certain nombre de modules
        """
        global selecteur_
        conditionDansUniv = condition.Condition(coterie.Coterie.Carac_UNIV_COURANTE, conquistadors.Conquistadors.NOM, condition.Condition.EGAL)

        # très forte chance (proba absolue) de suivre des modules tant qu'on n'en a pas fait 6
        univConquistadors = declencheur.Declencheur(proba.Proba(0.6, False), "univConquistadors")
        univConquistadors.AjouterCondition(conditionDansUniv)
        selecteur_.ajouterDeclencheur(univConquistadors)

    def evtUnivConquistadorsSuivant():
        global situation_

        evts = ["univConquistadors_evt1", "univConquistadors_evt2", "univConquistadors_evt3",
        "univConquistadors_evt4", "univConquistadors_evt5", "univConquistadors_evt6",
        "univConquistadors_evt7", "univConquistadors_evt8", "univConquistadors_evt9",
        "univConquistadors_evt10", "univConquistadors_evt11", "univConquistadors_evt12" ]

        prochainEvt = random.choice(evts)
        while situation_.GetValCaracInt(prochainEvt) == 1:
            prochainEvt = random.choice(evts)

        situation_.SetValCarac(prochainEvt, 1)
        renpy.jump( prochainEvt)

label univConquistadors:
    scene bg univ_conquistadors

    $ situation_.SetCarac(coterie.Coterie.Carac_UNIV_COURANTE, conquistadors.Conquistadors.NOM)
    $ numMoisRestants = situation_.GetValCaracInt(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE)
    if numMoisRestants == coterie.Coterie.NB_MOIS_UNIV_TOTAL_A_FAIRE:
        # intro :
        "intro univ conquistadors PAS FAITE. "

    $ numMoisRestants = situation_.GetValCaracInt(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE)
    if numMoisRestants < 1:
        # fin d'université
        $ situation_.SetCarac(coterie.Coterie.Carac_UNIV_COURANTE, "")
        jump decUnivCoterie
    else:
        $ situation_.RetirerACarac(coterie.Coterie.Carac_NB_MOIS_UNIV_A_FAIRE, 1)
        $ situation_.TourSuivant()
        $ evtUnivConquistadorsSuivant()
    jump fin_cycle

label univConquistadors_evt1:
    # formation religieuse
    scene bg conquistadors_priant
    "Un conquistador se doit d'être un fervent catholique confiant dans le destin que Dieu trace devant lui et qui le mènera à la gloire et la richesse. Vous passez des jours entiers à prier dans la dévotion des images saintes à suivre les cours de catéchisme des prêtres catholiques."
    $ religionActuelle = situation_.GetValCarac(religion.Religion.C_RELIGION)
    if religionActuelle != religion.Christianisme.NOM:
        $ conversion = conversionReligieuse(religion.Christianisme.NOM)
        if conversion:
            "Vous vous convertissez au christianisme."
        else:
            "Mais votre propre foi était trop forte, vous restez sourd à celle ci."
    jump fin_cycle

label univConquistadors_evt2:
    # effetCombat
    "Seuls les grands guerriers peuvent espérer devenir des conquistadors et affronter les horreurs des terres désolées. Vous suivez donc un entrainement avec de célèbres maîtres d'armes."
    $ AjouterACarac(metier.Guerrier.NOM, 1)
    jump fin_cycle

label univConquistadors_evt3:
    # effetForgeron
    "Les conquistadors sont des experts de la forge, leurs armures sont les meilleures du monde. De plus il est indispensable qu'en expédition ils soient capables de réparer et entretenir leur matériel donc même les aventuriers se doivent d'avoir des rudiments techniques."
    "Vous êtes donc formé par un maître forgeron pour connaître les bases du métier."
    $ AjouterACarac(metier.Forgeron.NOM, 1) # meilleur forgeron
    jump fin_cycle

label univConquistadors_evt4:
    # effet Musicien
    "Les conquistadors ne sont pas seulement des aventuriers, ce sont aussi des baladins itinérants qui divertissent les hôtes qui veulent bien les accueillir dans leurs nombreuses aventures. Ainsi ils peuvent chanter leurs exploits mais aussi ceux de leurs ancêtres et de leur clan."
    $ AjouterACarac(metier.Musicien.NOM, 1)
    jump fin_cycle

label univConquistadors_evt5:
    # effet Cartographe
    scene bg carte
    "Les conquistadors ont bâti le plus grand empire du monde et sont donc ceux qui le connaissent le mieux depuis la destructions massives causées par la dernière guerre. "
    "Cette connaissance est primordiale et c'est pourquoi comme toutes les jeunes recrues vous êtes formé à la cartographie pour contempler la plus grande gloire de la coterie."
    $ AjouterACarac(metier.Cartographe.NOM, 2)
    jump fin_cycle

label univConquistadors_evt6:
    # effet Marchand
    "Par leur maîtrise des mers et leur occupation de nombreuses contrées étrangères, les conquistadors contrôlent une énorme partie du commerce mondial. De plus par leurs pillages ils doivent savoir estimer rapidement la valeur des objets pour ne pas faire d'erreur. "
    "Jamais une expédition ne part sans au moins un marchand. Votre tuteur décide donc de vous y former pour estimer vos talents en la matière."
    $ AjouterACarac(metier.Marchand.NOM, 1)
    jump fin_cycle

label univConquistadors_evt7:
    # effet survie en milieu hostile
    "La partie la plus périeuse des activités des conquistadors est l'exploration de contrées inconnues et dangereuses. Un conquistador doit pour voir survivre seul dans n'import quel environnement."
    scene bg jungle
    "Cette partie cruciale est traitée avec le proagmatisme droit au but typique des instructeurs conquistadors. Vous êtes envoyé dans un stage d'u mois en pleine forêt tropicale pour apprendre les bases de la survie en milieu hostile et de la chasse."
    # ajouter des risques de maladies ??
    $ AjouterACarac(metier.Aventurier.NOM, 1)
    $ AjouterACarac(metier.Chasseur.NOM, 1)
    jump fin_cycle

label univConquistadors_evt8:
    "Les conquistadors sont les plus grands marins du monde. Depuis leur base de Saint Malo ils envoient leurs vaisseaux et leurs aventuriers vers tous les continents. Quelle que soit votre métier futur, si vous êtes conquistador vous naviguerez."
    "Vous faites plusieurs croisières pendant votre année d'université et êtes fortement encouragé à participer et à apprendre les bases de l'art de naviguer."
    $ AjouterACarac(metier.Marin.NOM, 1)
    jump fin_cycle

label univConquistadors_evt9:
    "univConquistadors_evt9 PAS FAIT"
    jump fin_cycle

label univConquistadors_evt10:
    "univConquistadors_evt10 PAS FAIT"
    jump fin_cycle

label univConquistadors_evt11:
    "univConquistadors_evt11 PAS FAIT"
    jump fin_cycle

label univConquistadors_evt12:
    "univConquistadors_evt12 PAS FAIT"
    jump fin_cycle
