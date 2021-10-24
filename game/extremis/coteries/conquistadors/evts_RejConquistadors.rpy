image officierConquistador = "coteries/conquistadors/officier.png"
define inst = Character('Instructeur', color="#e30909")

define audio.principale_conquistadors = "musique/conquistadors/01-06-Lemminkainen_Suite_Op_22_IV_Lemminkainen-LLS.mp3"

init -5 python:
    import random
    from extremis.coteries.conquistadors import conquistadors
    from extremis.socio_eco.metiers import metier
    from abs.religions import religion
    from extremis.geographie import quartier
    from abs.humanite import identite
    from abs.humanite import trait
    from abs import testDeCarac

label conquistadorsPostule:
    $note = 0 # points marqués durant l'épreuve (peut passer en négatif)
    "Vous avez demandé à rejoindre la coterie des conquistadors."
    "Bien que les conquistadors soient toujours fiers d'être choisis, leur coterie est très dangereuse et pas recommandée pourle premier postulant fragile qui se présente."
    "Ils font donc subir des épreuves pour éviter de recruter quelqu'un qui risquerait de vite mourir en mission."
    scene bg marais
    show officierConquistador at right
    with moveinright
    inst "La survie en milieu hostile est la base du métier de conquistador."
    inst "Si vous n'êtes pas capable de survivre par vous même dans ce marais vous ne serez bon à rien parmi nous."
    inst "Il y a tout ce qu'il faut pour survivre ici si on ouvre les yeux et qu'on a une bonne constitution."
    inst "Je viendrai vous chercher dans une semaine. Si il y a quelque chose à venir chercher."
    hide officierConquistador
    with moveoutright
    $ testAventurier = testDeCarac.TestDeCarac([trait.Constitution.NOM, metier.Aventurier.NOM], 3, situation_)
    "Hum difficile de croire qu'ils vous abandonneraient réellement mais enfin, de toute façon, la perspective de se débrouiller seul dans ce marais froid et fétide n'est pas réjouissante."
    menu:
        "Inspectez votre sac à dos. [testAventurier.affichage_]":
            jump conquistadorsPostule_phase2

    label conquistadorsPostule_phase2:
        $ reussi = testAventurier.TesterDifficulte(situation_)
        if reussi:
            "Vous parvenez vite à dresser un feu de camps avec le matériel qu'on vous a confié. Vous constatez que votre sac contient le nécessaire pour survivre ici, mais en quantité faible."
            "Il va falloir se rationner."
            $ note = note + 1
            jump conquistadorsPostule_phase3
        else:
            $ note = note - 1
            "Vous passez péniblement les premières heures à chercher un endroit sec et pas trop exposé au vent glacé pour pouvoir inspecter le matériel qu'on vous a confié."
            "Après ces quelques efforts vous êtes soulagé de voir qu'ils vous ont confié le nécessaire pour vos besoins de base. Mais en si peu de temps vous vous sentez déjà fatigué et fiévreux."
            jump conquistadorsPostule_phase3

label conquistadorsPostule_phase3:
    "Il vous faut maintenant trouver de quoi manger. Si vous entamez déjà les provisions qu'ils vous ont confié les conquistadors vous mépriseront, vous devez vous nourrir par vous même."

    $ testChasseur = testDeCarac.TestDeCarac([metier.Chasseur.NOM], 3, situation_)
    $ testAventurier = testDeCarac.TestDeCarac([metier.Aventurier.NOM], 4, situation_)
    menu:
        "Si vous chassez. [testChasseur.affichage_]":
            jump conquistadorsPostule_phase3_chasse
        "Si vous cherchez des végétaux. [testAventurier.affichage_]":
            jump conquistadorsPostule_phase3_cueille

    label conquistadorsPostule_phase3_chasse:
        $ reussi = testChasseur.TesterDifficulte(situation_)
        if reussi:
            "Grâce à un fusil de chasse de mauvaise qualité qu'on vous a donné, mais surtout grâce à vos compétences de chasseur, vous parvenez à abattre un canard, puis à le préparer et le faire cuire sur votre feu."
            $ note = note + 1
            jump conquistadorsPostule_phase4
        else:
            $ note = note - 1
            "Après des heures de tentatives vous croyez avoir réussi à abattre un canard mais impossible de trouver son corps."
            "Finalement vous renoncez et entamez les provisions qu'on vous a confié, c'est à dire un vilain pain sec."
            jump conquistadorsPostule_phase4

    label conquistadorsPostule_phase3_cueille:
        $ reussi = testAventurier.TesterDifficulte(situation_)
        if reussi:
            "Vous parvenez à trouver des champignons et des racines comestibles. C'est loin d'être le festin de vos rêves mais comparé à l'ignoble pain sec qu'on vous a confié c'est le luxe."
            "Et surtout vous êtes persuadé que c'est ainsi que vous serez respecté et accepté dans la coterie."
            $ note = note + 1
            jump conquistadorsPostule_phase4
        else:
            $ note = note - 1
            "Après des heures de tentatives c'est tout juste si vous avez trouvé quelques baies douteuses et un immonde champignon."
            "Finalement vous renoncez et entamez les provisions qu'on vous a confié, c'est à dire un vilain pain sec."
            jump conquistadorsPostule_phase4

label conquistadorsPostule_phase4:
    "Même si tout ne se passe pas à la perfection vous sentez que vous allez pouvoir tenir la semaine, que ce soit au niveau de la nourriture ou du froid."
    "Mais le confort est catastrophique. Vous êtes mouillé en permanence et d'autant plus gelé par le vent. Vous n'avez même pas une vraie tente mais juste une toile tendue pour couvrir le haut de votre corps."
    "De plus vous êtes surpris de la difficulté que vous avez à rester absolument seul dans le noir dans ce marais plein de bruits étrangers et effrayants."

    $ testNuit = testDeCarac.TestDeCarac([trait.Ascetisme.NOM, trait.Courage.NOM], 5, situation_)
    menu:
        "Il va falloir faire preuvre de courage et de ténacité. [testNuit.affichage_]":
            jump conquistadorsPostule_phase4_b

    label conquistadorsPostule_phase4_b:
        $ reussi = testNuit.TesterDifficulte(situation_)
        if reussi:
            "Vous surmontez vos doutes et parvenez à vous débrouillez sans aucune assistance extérieure et sans fléchir jusqu'au retour de l'instructeur."
            $ note = note + 1
            jump conquistadorsPostule_phase5
        else:
            $ note = note - 1
            "Vous avez des tremblements continuels, vous ne dormez péniblement que quelques heures par nuit. Et chaque journée est pire que la précédente."
            "Une semaine plus tard quand l'instructeur vient vous rechercher vous êtes épuisé, fiévreux et tremblotant."
            jump conquistadorsPostule_phase5

label conquistadorsPostule_phase5:
    "conquistadorsPostule_phase3 ! note : [note]"
    show officierConquistador at right
    with moveinright
    if note <= 0:
        inst "C'était courageux d'essayer petit, mais tu n'as juste pas ce qu'il faut pour devenir un conquistador."
        inst "On s'occuper de toi le temps que tu récupères mais ensuite je ne veux pas te revoir."
        jump fin_cycle
    elif note <= 2:
        inst "Pas mal du tout. Avec une petit formation complémentaire tu seras digne d'être l'un des nôtres. Bienvenue."
        jump conquistadorsRejoindre
    else:
        inst "Bravo tu as un gros potentiel. Je suis fier que tu deviennes l'un des nôtres. Bienvenue."
        $ AjouterACarac(trait.Assurance.NOM, 1)
        jump conquistadorsRejoindre

label conquistadorsRejoindre:
    play music principale_conquistadors
    inst "Vous êtes maintenant un conquistador."
    $ coterieConquistadors = coteries_[conquistadors.Conquistadors.ID]
    $ coterieConquistadors.RejoindreCoterie(situation_)
    $ prenom = situation_[identite.Identite.C_PRENOM]
    $ nom = situation_[identite.Identite.C_NOM]
    inst "Dorénavant vous vous appellerez [prenom] [nom]."

    "Vous allez vous installer dans le grand port de Saint Malo, la base principale de votre nouvelle coterie."
    $ situation_.SetValCarac(quartier.Quartier.C_QUARTIER, coterieConquistadors.quartier_)
    jump fin_cycle
