init -5 python:
    import random

    def evtUnivTempliersSuivant():
        global situation_

        evts = ["univTempliers_evt1", "univTempliers_evt2", "univTempliers_evt3",
        "univTempliers_evt4", "univTempliers_evt5", "univTempliers_evt6",
        "univTempliers_evt7", "univTempliers_evt8", "univTempliers_evt9",
        "univTempliers_evt10", "univTempliers_evt11", "univTempliers_evt12" ]

        renpy.jump( random.choice(evts))

label univTempliers:
    scene bg univ_templiers

    $ situation_.RetirerACarac(coterie.Coterie.NB_MOIS_UNIV_A_FAIRE, 1)

    $ numMoisRestants = situation_.GetValCaracInt(coterie.Coterie.NB_MOIS_UNIV_A_FAIRE)
    if numMoisRestants < 1:
        jump decUnivCoterie
    else:
        $ situation_.TourSuivant()
        $ evtUnivTempliersSuivant()
    jump fin_cycle

label univTempliers_evt1:
    "univTempliers_evt1"
    jump univTempliers
label univTempliers_evt2:
    "univTempliers_evt2"
    jump univTempliers
label univTempliers_evt3:
    "univTempliers_evt3"
    jump univTempliers
label univTempliers_evt4:
    "univTempliers_evt4"
    jump univTempliers
label univTempliers_evt5:
    "univTempliers_evt5"
    jump univTempliers
label univTempliers_evt6:
    "univTempliers_evt6"
    jump univTempliers
label univTempliers_evt7:
    "univTempliers_evt7"
    jump univTempliers
label univTempliers_evt8:
    "univTempliers_evt8"
    jump univTempliers
label univTempliers_evt9:
    "univTempliers_evt9"
    jump univTempliers
label univTempliers_evt10:
    "univTempliers_evt10"
    jump univTempliers
label univTempliers_evt11:
    "univTempliers_evt11"
    jump univTempliers
label univTempliers_evt12:
    "univTempliers_evt12"
    jump univTempliers
