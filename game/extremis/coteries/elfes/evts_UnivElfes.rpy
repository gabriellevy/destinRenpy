init -5 python:
    import random

    def evtUnivElfesSuivant():
        global situation_

        evts = ["univElfes_evt1", "univElfes_evt2", "univElfes_evt3",
        "univElfes_evt4", "univElfes_evt5", "univElfes_evt6",
        "univElfes_evt7", "univElfes_evt8", "univElfes_evt9",
        "univElfes_evt10", "univElfes_evt11", "univElfes_evt12" ]

        renpy.jump( random.choice(evts))

label univElfes:
    scene bg univ_elfes

    $ situation_.RetirerACarac(coterie.Coterie.NB_MOIS_UNIV_A_FAIRE, 1)

    $ numMoisRestants = situation_.GetValCaracInt(coterie.Coterie.NB_MOIS_UNIV_A_FAIRE)
    if numMoisRestants < 1:
        jump decUnivCoterie
    else:
        $ situation_.TourSuivant()
        $ evtUnivElfesSuivant()
    jump fin_cycle

label univElfes_evt1:
    "univElfes_evt1"
    jump univElfes
label univElfes_evt2:
    "univElfes_evt2"
    jump univElfes
label univElfes_evt3:
    "univElfes_evt3"
    jump univElfes
label univElfes_evt4:
    "univElfes_evt4"
    jump univElfes
label univElfes_evt5:
    "univElfes_evt5"
    jump univElfes
label univElfes_evt6:
    "univElfes_evt6"
    jump univElfes
label univElfes_evt7:
    "univElfes_evt7"
    jump univElfes
label univElfes_evt8:
    "univElfes_evt8"
    jump univElfes
label univElfes_evt9:
    "univElfes_evt9"
    jump univElfes
label univElfes_evt10:
    "univElfes_evt10"
    jump univElfes
label univElfes_evt11:
    "univElfes_evt11"
    jump univElfes
label univElfes_evt12:
    "univElfes_evt12"
    jump univElfes
