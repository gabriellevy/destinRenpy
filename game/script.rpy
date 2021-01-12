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

    AjouterEvtsAdministratif()
    AjouterEvtsRien()

# Le jeu commence ici
label start:
    scene bg rue_haussmann
    $ DeterminerPerso() # attention cette fonction lance un jump

label debut_cycle:
    show screen valeurs_traits
    "Début d'un cycle."
    $ res = situation_.CalculerPourcentageReussite(trait.Charme.NOM, 8)
    "res Charme, 8 : [res]"
    $ res = situation_.CalculerPourcentageReussite(trait.Habilete.NOM, 3)
    "res Habilete, 3 : [res]"
    $ res = situation_.CalculerPourcentageReussite(trait.Ambition.NOM, 10)
    "res Ambition, 10 : [res]"
    $ res = situation_.CalculerPourcentageReussite(trait.Taille.NOM, 1)
    "res Taille, 1 : [res]"

    $ prochainEvt = determinationEvtCourant(situation_)
    $ renpy.jump(prochainEvt)

label fin_cycle:
    "Fin d'un cycle."

    if situation_["Santé"] != "Mort":
        jump debut_cycle

    "Fin de vie."
    return

label labelGoTo_pasFait:
    "Ce sélecteur d'énévement n'a pas de label go to on dirait"

label pas_evt_trouve:
    " ERREUR : pas d'événement trouvé à ce cycle"
