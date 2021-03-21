
define audio.principale_conquistadors = "musique/conquistadors/01-06-Lemminkainen_Suite_Op_22_IV_Lemminkainen-LLS.mp3"

init -5 python:
    import random
    from extremis.coteries.conquistadors import conquistadors
    from extremis.socio_eco.metiers import metier
    from extremis.humanite import identite
    from extremis.religions import religion
    from extremis.geographie import quartier

label conquistadorsPostule:
    "POSTULER CONQUISTADORS TEST PAS FAIT."

label conquistadorsRejoindre:
    "REJOINDRE CONQUISTADORS PAS FAIT."
    play music principale_conquistadors
    ordo "Lisez le serment de l'Ordre."
    $ coterieConquistadors = coteries_[conquistadors.Conquistadors.ID]
    $ coterieConquistadors.RejoindreCoterie(situation_)
    $ prenom = situation_[identite.Identite.C_PRENOM]
    $ nom = situation_[identite.Identite.C_NOM]
    ordo "Dorénavant vous vous appellerez [prenom] [nom]."

    "Vous vous installez dans le quartier du Temple à Saint Denis"
    $ situation_.SetValCarac(quartier.Quartier.C_QUARTIER, coterieConquistadors.quartier_)
    jump fin_cycle
