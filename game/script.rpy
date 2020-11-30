# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Persos
define narrator = Character(color="#fafad8", what_italic=True)


# Le jeu commence ici
label start:
    "Lancement du jeu"

    $ DeterminerPerso()

label debut_cycle:
    "Début d'un cycle."

    # $ DeterminationEvtCourant()

    "Fin d'un cycle."

    if situation_["Santé"] != "Mort":
        jump debut_cycle

    "Fin de vie."
    return
