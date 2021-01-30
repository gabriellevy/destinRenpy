init -5 python:
    import random

    def evtUnivTranshumanistesSuivant():
        global situation_

        evts = ["univTranshumanistes_evt1", "univTranshumanistes_evt2", "univTranshumanistes_evt3",
        "univTranshumanistes_evt4", "univTranshumanistes_evt5", "univTranshumanistes_evt6",
        "univTranshumanistes_evt7", "univTranshumanistes_evt8", "univTranshumanistes_evt9",
        "univTranshumanistes_evt10", "univTranshumanistes_evt11", "univTranshumanistes_evt12" ]

        renpy.jump( random.choice(evts))

label univTranshumanistes:
    scene bg univ_transhumanistes

    $ situation_.RetirerACarac(coterie.Coterie.NB_MOIS_UNIV_A_FAIRE, 1)

    $ numMoisRestants = situation_.GetValCaracInt(coterie.Coterie.NB_MOIS_UNIV_A_FAIRE)
    if numMoisRestants < 1:
        jump decUnivCoterie
    else:
        $ situation_.TourSuivant()
        $ evtUnivTranshumanistesSuivant()
    jump fin_cycle

label univTranshumanistes_evt1:
    "univTranshumanistes_evt1"
    jump univTranshumanistes
label univTranshumanistes_evt2:
    "univTranshumanistes_evt2"
    jump univTranshumanistes
label univTranshumanistes_evt3:
    "univTranshumanistes_evt3"
    jump univTranshumanistes
label univTranshumanistes_evt4:
    "univTranshumanistes_evt4"
    jump univTranshumanistes
label univTranshumanistes_evt5:
    "univTranshumanistes_evt5"
    jump univTranshumanistes
label univTranshumanistes_evt6:
    "univTranshumanistes_evt6"
    jump univTranshumanistes
label univTranshumanistes_evt7:
    "univTranshumanistes_evt7"
    jump univTranshumanistes
label univTranshumanistes_evt8:
    "univTranshumanistes_evt8"
    jump univTranshumanistes
label univTranshumanistes_evt9:
    "univTranshumanistes_evt9"
    jump univTranshumanistes
label univTranshumanistes_evt10:
    "univTranshumanistes_evt10"
    jump univTranshumanistes
label univTranshumanistes_evt11:
    "univTranshumanistes_evt11"
    jump univTranshumanistes
label univTranshumanistes_evt12:
    "univTranshumanistes_evt12"
    jump univTranshumanistes
