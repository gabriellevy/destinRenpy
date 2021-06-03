# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Persos
define narrator = Character(color="#fafad8", what_italic=True)

init -10 python:
    from despin.gen_vie import selecteur
    import random

    selecteur_ = selecteur.Selecteur()
    def determinationEvtCourant(situation):
        global selecteur_
        return selecteur_.determinationEvtCourant(situation)

init -1 python:
    from despin.gen_vie import selecteur
    import random

    # métiers
    AjouterEvtsAdministratif()
    AjouterEvtsRejMetier()
    # crime / loi
    AjouterEvtsCrime()
    AjouterEvtsJustice()
    # vie courante
    AjouterEvtsPilotage()
    AjouterEvtsRien()
    # coteries
    AjouterEvtsCoteries()
    AjouterEvtsUnivTranshumanistes()
    AjouterEvtsTranshumanistes()

    AjouterEvtsUnivTempliers()
    AjouterEvtsTempliers()

    AjouterEvtsUnivElfes()
    AjouterEvtsUnivConquistadors()
    # amour
    AjouterEvtsRencontresAmoureuses()
    # santé
    AjouterEvtsMaladies()
    AjouterEvtsVieillesse()
    # religion
    AjouterEvtsChretiens()

# Le jeu commence ici
label start:
    scene bg rue_haussmann
    $ DeterminerPerso() # attention cette fonction lance un jump

label debut_cycle:
    show screen valeurs_traits
    #show screen fading_text("sniff", 3.0, 400, 300, 600, 600, color="#fff", size=24)
    #"tmp stop" # tmp test

    $ prochainEvt = determinationEvtCourant(situation_)
    $ renpy.jump(prochainEvt)

label fin_cycle:
    # "Fin d'un cycle."
    # jump orksRejoindre # tmp test

    $ situation_.TourSuivant()

    if situation_["Santé"] != "Mort":
        jump debut_cycle

label mort:
    menu:
        "Fin de vie."
        "ok":
            pass
    return

label labelGoTo_pasFait:
    "Ce sélecteur d'énévement n'a pas de label go to on dirait"

label pas_evt_trouve:
    " ERREUR : pas d'événement trouvé à ce cycle"

label probaAbsoluesSup100:
    "Le total des probas absolues dépasse 100%% !"
