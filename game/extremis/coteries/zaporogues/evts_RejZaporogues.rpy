# persos
# image ordonnateur = "coteries/templiers/ordonnateur.png"
# define ordo = Character('Ordonnateur', color="#e30909")

# musiques
define audio.rejoindre_zapos = "musique/zaporogues/Hymne_National_De_L'URSS.mp3"

init -5 python:
    import random
    from extremis.coteries.zaporogues import zaporogues
    from abs.humanite import metier
    from abs.religions import religion
    from extremis.geographie import quartier
    from abs.humanite import identite

label zaporoguesPostule:
    menu:
        "PAS FAIT postuler LES Zaporogues."
        "ok":
            pass
    jump zaporoguesRejoindre
    jump fin_cycle

label zaporoguesRejoindre:
    "PAS FAIT REJOINDRE LES Zaporogues."
    # scene bg univ_zaporogues
    # show ordonnateur at right
    # with moveinright
    play music rejoindre_zapos noloop
    $ coterieZaporogues = coteries_[zaporogues.Zaporogues.ID]
    $ coterieZaporogues.RejoindreCoterie(situation_)
    $ prenom = situation_[identite.Identite.C_PRENOM]
    $ nom = situation_[identite.Identite.C_NOM]
    ordo "Dorénavant vous vous appellerez [prenom] [nom]."
    $ situation_.SetValCarac(quartier.Quartier.C_QUARTIER, coterieZaporogues.quartier_)
    jump fin_cycle
