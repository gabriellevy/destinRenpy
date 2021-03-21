 # persos
image ordonnateur = "coteries/templiers/ordonnateur.png"
define ordo = Character('Ordonnateur', color="#e30909")

# musiques
define audio.principale_temple = "musique/templiers/principale.mp3"
define audio.rejoindre_temple = "musique/templiers/rejoindre_doux_spirituel.mp3"

init -5 python:
    import random
    from extremis.coteries.templiers import templiers
    from extremis.socio_eco.metiers import metier
    from extremis.humanite import identite
    from extremis.religions import religion
    from extremis.geographie import quartier

label templiersPostule:
    "Vous souhaitez rejoindre l'Ordre du Temple."
    scene bg catacombes
    $ religionActuelle = situation_.GetValCarac(religion.Religion.C_RELIGION)
    if religionActuelle != religion.Christianisme.NOM:
        "Malheureusement seul un chrétien à la foi pure et désintéressée peut entrer dans l'Ordre. Quelles que soient vos protestations les ordonnateurs sentent la faiblesse de votre foi et vous refusent."
    show ordonnateur at right
    with moveinright
    "Vous vous trouvez dans un noir tunnel. Vous et chacun des deux ordonnateurs avez une torche en main qui peine à éclairer à quelques mètres alors que le tunnel semble très long vu la résonnance de vos voix."
    ordo "Nous sommes dans les souterrains de la basilique de Saint Denis, les catacombes du Temple."
    ordo "Nous avons jugé votre demande sincère ; maintenant vous allez devoir prouver votre pureté, votre courage et votre détermination."
    ordo "Votre tâche est simple : suivez le tunnel, ne vous en écartez sous aucun prétexte et vous serez digne de devenir un des nôtres."
    ordo "Que Dieu soit avec vous."
    hide ordonnateur
    with moveoutright
    "Vous suivez le tunnel et réalisez qu'il est infiniment plus long que vous ne le pensiez."
    "Vous dépassez plusieurs croisements mais n'en empruntez aucun."
    "Vous perdez très vite la notion du temps. L'humidité vous gèle, vous vous mettez déjà à avoir faim. Des vapeurs étranges montent depuis les grilles sous vos pieds."
    "Plusieurs fois vous titubez et vous écorchez sur une pierre tant le chemin est plein de trous et votre lumière de plus en plus faible."
    "Vous croyez entendre une musique."
    "Vous voyez de la lumière au loin."
    "Ce n'était pas un rêve. Une salle luxueuse se trouve à votre droite au bout d'un court tunnel. De bonnez odeurs de nourriture en viennent ainsi que des rires."
    $ diffTests = 3
    $ affDiff = situation_.AffichagePourcentageReussite(trait.Ascetisme.NOM, diffTests)
    menu:
        "Si vous vous penchez pour voir un peu.":
            jump TempliersPostule_t1_phase2
        "Si vous continuez. [affDiff]":
            jump TempliersPostule_t1

    label TempliersPostule_t1:
    $ reussi = situation_.TesterDifficulte(trait.Ascetisme.NOM, diffTests)
    if reussi:
        jump TempliersPostule_t2
    else:
        "La curiosité est trop forte, vous vous penchez pour  jeter juste un petit coup d'oeil."
        jump TempliersPostule_t1_phase2

    label TempliersPostule_t1_phase2:
        scene bg banquet
        "Vous apercevez nettement une grande tablée entourée de convives vêtues étrangement et s'amusant beaucoup."
        "La pièce est très sombre comme votre tunnel mais ça ajoute encore à l'ambiance et les convives semblent profiter avec plaisir des coins sombres."
        "Une d'entre elles vous apperçoit. D'abord surprise elle prend vite une attitude accueillante et vous fait signe de la rejoindre."
    menu:
        "Si vous acceptez l'invitation.":
            jump TempliersPostule_t1_rate
        "Si vous continuez. [affDiff]":
            jump TempliersPostule_t1_phase3

    label TempliersPostule_t1_phase3:
    $ reussi = situation_.TesterDifficulte(trait.Ascetisme.NOM, diffTests)
    if reussi:
        jump TempliersPostule_t2
    else:
        "Vous êtes comme hypnotisé par la musique, les odeurs, et le charmant souvenir de la belle inconnue et vous marchez dans la grande salle."
        jump TempliersPostule_t1_rate

    label TempliersPostule_t1_rate:
        "Échouer si rapidement à des instructions si simples. L'Ordre est très déçu, vous aurez peut-être une autre chance un jour..."
        "PAS FAIT : développer cette rencontre pourrait être marrant !"
        jump fin_cycle


    label TempliersPostule_t2:
        scene bg catacombes
        "Votre reprenez votre longue marche pendant Dieu seul sait combien de longues très longues minutes ou heures."
        "Bientôt un large gouffre se trouve devant vous. Aucune issue à droite, aucune issue à gauche. De toute façon vous devez suivre le tunnel jusqu'au bout."
        "Vous pouvez en voir la suite de l'autre côté du trou mais il s'agit d'un saut de plus de 4 mètres à accomplir ! Vous ne voyez pas le fond du trou mais vu la faible portée de votre torche ça ne veut pas dire pour autant qu'il est profond."
        menu:
            "Si vous préférez retourner en arrière.":
                jump TempliersPostule_t2_rate
            "Si vous prenez votre élan pour tenter de sauter de l'autre côté.":
                jump TempliersPostule_t2_saute
            "Si vous marchez droit dans le vide.":
                jump TempliersPostule_t2_marche

    label TempliersPostule_t2_saute:
        $ reussi = situation_.TesterDifficulte(trait.Force.NOM, 6)
        if reussi:
            "C'est à peine croyable mais vous parvenez à bondir de l'autre côté du gouffre sans même vous blesser à l'arrivée."
            jump TempliersPostule_t3
        else:
            "Vous prenez courageusement votre élan mais au moment de suter c'est la catastrophe, vous doutez, perdez pied et tombez dans le gouffre."
            jump TempliersPostule_t2_tombe

    label TempliersPostule_t2_marche:
        $ reussi = situation_.TesterDifficulte(religion.Religion.C_MIRACLE, 2)
        if reussi:
            "C'est un miracle ! Vos pieds restent suspendus en l'air et vous parvenez de l'autre côté du gouffre en marchant doucement sans ressentir aucune peur."
            jump TempliersPostule_t3
        else:
            "Vous avez beau vous concentrer, il n'y a pas de miracle. Votre pied lancé en avant ne rencontre que le vide et vous vous écrasez piteusement au fond du gouffre."
            jump TempliersPostule_t2_tombe


    label TempliersPostule_t2_tombe:
        $ blessure = blessures_.InfligerBlessureAleatoire(situation_, 1, 8)
        $ texteBlessure = blessure.GetDescriptionRecu()
        "Il n'est heureusement pas très profond mais tomber sur des caillous pointus dans le noir est une dure expérience. [texteBlessure]"
        jump TempliersPostule_t2_rate

    label TempliersPostule_t2_rate:
        "Quel triste manque de foi. Vous n'avez pas le coeur d'un templier voilà tout. Vous trouverez votre propre voie un jour."
        jump fin_cycle

    label TempliersPostule_t3:
        "PAS FAIT : seulement deux tests pour l'instant, un de plus ça serait bien !"

    label TempliersPostule_reussi:
        "Vous marchez encore presque une heure dans l'obscurité quandenfin vous appercevez des rayons de lumière du jour."
        "Le tunnel finit en un escalier de métal qui remonte en plein quinzième arrondissement."
        show ordonnateur at right
        with moveinright
        ordo "Bravo mon fils tu as prouvé ta valeur morale et physique. Tu es digne de nous rejoindre dès aujourd'hui"
        jump TempliersRejoindre

    jump fin_cycle

label TempliersRejoindre:
    scene bg univ_templiers
    show ordonnateur at right
    with moveinright
    play music rejoindre_temple
    ordo "Lisez le serment de l'Ordre."
    "Exauce, nous t'en prions, Seigneur, nos prières, de sorte que tu daignes bénir ton serviteur qui ce jour avec ton assentiment a ceint le glaive,"
    "qu'il soit le défenseur contre la cruauté de païens et de tous les méchants, et le protecteur des églises, des veuves, des orphelins, de tous tes serviteurs,"
    "et qu'avec ton aide il soit la terreur et l'épouvante de tous ceux qui rejettent la sainte foi."
    $ coterieTempliers = coteries_[templiers.Templiers.ID]
    $ coterieTempliers.RejoindreCoterie(situation_)
    $ prenom = situation_[identite.Identite.C_PRENOM]
    $ nom = situation_[identite.Identite.C_NOM]
    ordo "Dorénavant vous vous appellerez [prenom] [nom]."
    ordo "Lisez maintenant les voeux."
    "Moi [prenom], je fais profession et je jure chasteté, renoncement à la propriété et obéissance à Dieu, à la bienheureuse Marie et à toi, frère Aldebert, maître de l'Ordre du Temple et à tes successeurs, selon la règle et les institutions de l'ordre du Temple,"
    "et je jure que j'obéirai, à toi et à tes successeurs, jusqu'à la mort."
    $ situation_.SetValCarac(religion.Religion.C_VOEU_CHASTETE, "1")
    $ situation_.SetValCarac(religion.Religion.C_VOEU_PAUVRETE, "1")
    $ situation_.SetValCarac(templiers.Templiers.C_RICHESSE, templiers.Templiers.RICHESSE_TEMPLE)
    $ situation_.SetValCarac(trait.Richesse.NOM, templiers.Templiers.RICHESSE_TEMPLE)
    ordo "Voici votre robe blanche marquée du symbole de l'ordre."
    ordo "Portez cette croix avec fierté et honneur, que tous les hommes qui vous croiseront continuent à y voir un symbole de pureté et de force comme ça a toujours été le cas depuis la fondation de notre Ordre il y a plus de deux mille ans."

    "Vous vous installez dans le quartier du Temple à Saint Denis"
    $ situation_.SetValCarac(quartier.Quartier.C_QUARTIER, coterieTempliers.quartier_)
    jump fin_cycle
