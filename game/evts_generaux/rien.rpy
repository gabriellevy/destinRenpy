# fichier où sont générés les phrases d'ambiance à afficher quand il ne se passe rien durant un mois particulier

init -5 python:
    import random
    from despin.gen_vie import declencheur
    from despin.gen_vie import selecteur
    from despin.gen_vie import proba
    from despin.abs import condition
    from extremis.socio_eco import metier

    def AjouterEvtsRien():
        global selecteur_, situation_
        selecteurDEvenementVide = declencheur.Declencheur(1.0, "selecteurDEvenementVide")
        selecteur_.ajouterDeclencheur(selecteurDEvenementVide)

    def LancerEvtVide(situation):
        # régénère les événements compatibles avec la situation
        evtsVides_ = ["evtRien1", "evtRien2", "evtRien3" ]

        if situation[metier.Metier.ADMINISTRATIF] > 0:
            evtsVides_.append("evtRien_Administratif1")

        # en lance un au hasard
        renpy.jump(random.choice(evtsVides_))

label selecteurDEvenementVide:
    $ LancerEvtVide(situation_)

label evtRien1:
    "Et encore une journée de plus."
    jump debut_cycle

label evtRien2:
    "Les jours se suivent et se ressemblent."
    jump debut_cycle

label evtRien3:
    "Un jour c'est sûr quelque chose vous arrivera."
    jump debut_cycle

label evtRien_Administratif1:
    "La vie de bureau suit son cours."
    jump debut_cycle
