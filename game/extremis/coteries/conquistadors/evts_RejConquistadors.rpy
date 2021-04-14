image officierConquistador = "coteries/conquistadors/officier.png"
define inst = Character('Instructeur', color="#e30909")

define audio.principale_conquistadors = "musique/conquistadors/01-06-Lemminkainen_Suite_Op_22_IV_Lemminkainen-LLS.mp3"

init -5 python:
    import random
    from extremis.coteries.conquistadors import conquistadors
    from extremis.socio_eco.metiers import metier
    from extremis.religions import religion
    from extremis.geographie import quartier
    from extremis.humanite import pnj

label conquistadorsPostule:
    "Vous avez demandé à rejoindre la coterie des conquistadors."
    "Bien que les conquistadors soient toujours fiers et heureux d'être choisis, il est clair que leur coterie est très dangereuse et pas recommandée pour tout le monde."
    "Ils vont donc vous faire subir des épreuves pour éviter de recruter quelqu'un qui risquerait de vite mourir en mssion."
    scene bg marais
    menu:
        "conquistadorsPostule"
        "youpi":
            pass
    show officierConquistador at right
    with moveinright
    inst "La survie en milieu hostile est la base du métier de conquistador."
    inst "Si vous n'êtes pas capable de survivre par vous même dans ce marais vous ne serez bon à rien parmi nous."
    inst "Il y a tout ce qu'il faut pour survivre ici si on ouvre les yeux et qu'on a une bonne constitution."
    inst "Je viendrai vous chercher dans une semaine si il y a quelque chose à venir chercher."
    hide officierConquistador
    with moveoutright
    jump fin_cycle# tmp

label conquistadorsPostule_reussi:
    show officierConquistador at right
    with moveinright
    "texte postulation conquistadors PAS FAIT"
    jump TempliersRejoindre

label conquistadorsRejoindre:
    "REJOINDRE CONQUISTADORS PAS FAIT."
    play music principale_conquistadors
    ordo "Lisez le serment de l'Ordre."
    $ coterieConquistadors = coteries_[conquistadors.Conquistadors.ID]
    $ coterieConquistadors.RejoindreCoterie(situation_)
    $ prenom = situation_[pnj.Pnj.C_PRENOM]
    $ nom = situation_[pnj.Pnj.C_NOM]
    ordo "Dorénavant vous vous appellerez [prenom] [nom]."

    "Vous allez vous installer dans le grand port de Saint Malo, la abse principale de votre nouvelle coterie."
    $ situation_.SetValCarac(quartier.Quartier.C_QUARTIER, coterieConquistadors.quartier_)
    jump fin_cycle
