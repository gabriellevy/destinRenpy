# Vous pouvez placer le script de votre jeu dans ce fichier.

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

# Le jeu commence ici
label start:
    "Lancement du jeu"

    $ DeterminerPerso()

label debut_cycle:
    "Début d'un cycle."

    $ prochainEvt = determinationEvtCourant(situation_)
    $ renpy.jump(prochainEvt)

    "Fin d'un cycle."

    if situation_["Santé"] != "Mort":
        jump debut_cycle

    "Fin de vie."
    return

label labelGoTo_pasFait:
    "Ce sélecteur d'énévement n'a pas de label go to on dirait"

label pas_evt_trouve:
    " ERREUR : pas d'événement trouvé à ce cycle"
