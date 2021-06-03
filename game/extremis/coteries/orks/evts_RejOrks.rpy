 # persos
# image ordonnateur = "coteries/templiers/ordonnateur.png"
# define ordo = Character('Ordonnateur', color="#e30909")

# musiques
# define audio.principale_temple = "musique/templiers/principale.mp3"
# define audio.rejoindre_temple = "musique/templiers/rejoindre_doux_spirituel.mp3"

init -5 python:
    import random
    from extremis.coteries.orks import orks
    from extremis.socio_eco.metiers import metier
    from extremis.religions import religion
    from extremis.geographie import quartier
    from extremis.humanite import identite

label orksPostule:
    scene bg poissy
    "orksPostule PAS FAIT"
    jump orksRejoindre # tmp

label orksRejoindre:
    scene bg poissy
    "orksRejoindre PAS FAIT."
    $ coterieOrks = coteries_[orks.Orks.ID]
    $ coterieOrks.RejoindreCoterie(situation_)
    $ prenom = situation_[identite.Identite.C_PRENOM]
    "Dorénavant vous vous appellerez [prenom]."

    "Vous vous installez dans le quartier des orks à Poissy."
    $ situation_.SetValCarac(quartier.Quartier.C_QUARTIER, coterieOrks.quartier_)
    jump fin_cycle
