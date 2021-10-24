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
    from abs.religions import religion
    from extremis.geographie import quartier
    from abs.humanite import identite

label orksPostule:
    scene bg poissy
    "orksPostule PAS FAIT"
    jump orksRejoindre # tmp

label orksRejoindre:
    scene bg poissy
    "Vous avez accompli les épreuves, vous avez gagné le droit de boire le sérum de l'orkitude qui fera de vous un vrai Ork, si vous tenez le coup comme un vrai ork le ferait, bien sûr."
    $ coterieOrks = coteries_[orks.Orks.ID]
    $ coterieOrks.RejoindreCoterie(situation_)

    # orkitude, transformation en ork
    $ scoreTransformation = random.uniform(0, 1.0)
    # $ print("1. scoreTransformation : {}".format(scoreTransformation))
    if situation_.GetValCaracInt(trait.Franchise.NOM) > 0:
        $ scoreTransformation = scoreTransformation + 0.01
    if situation_.GetValCaracInt(trait.Force.NOM) > 0:
        $ scoreTransformation = scoreTransformation + 0.05
    elif situation_.GetValCaracInt(trait.Force.NOM) < 0:
        $ scoreTransformation = scoreTransformation - 0.03
    if situation_.GetValCaracInt(trait.Assurance.NOM) > trait.Trait.SEUIL_A:
        $ scoreTransformation = scoreTransformation + 0.05
    elif situation_.GetValCaracInt(trait.Assurance.NOM) < trait.Trait.SEUIL_A_PAS:
        $ scoreTransformation = scoreTransformation - 0.05
    if situation_.GetValCaracInt(trait.Constitution.NOM) > 0:
        $ scoreTransformation = scoreTransformation + 0.05
    elif situation_.GetValCaracInt(trait.Constitution.NOM) < 0:
        $ scoreTransformation = scoreTransformation - 0.03
    if situation_.GetValCaracInt(trait.Violence.NOM) > 0:
        $ scoreTransformation = scoreTransformation + 0.05
    if situation_.GetValCaracInt(trait.Industrie.NOM) > 0:
        $ scoreTransformation = scoreTransformation - 0.02
    if situation_.GetValCaracInt(trait.Intelligence.NOM) > 0:
        $ scoreTransformation = scoreTransformation - 0.02
    if situation_.GetValCaracInt(trait.Serenite.NOM) < 0:
        $ scoreTransformation = scoreTransformation - 0.02
    if situation_.GetValCaracInt(trait.Intellectualisme.NOM) > 0:
        $ scoreTransformation = scoreTransformation - 0.02
    # $ print("2. scoreTransformation : {}".format(scoreTransformation))

    if scoreTransformation < 0:
        "Malheureusement le résultat est catastrophique. Votre faible volonté ou juste la malchance font de vous un simple gretchin. Esclave pitoyable des ork que vous rêviez d'être."
        $ situation_.SetValCaracSiSuperieur(trait.Taille.NOM, trait.Trait.SEUIL_A_PAS_EXTREME)
        $ situation_.SetValCaracSiSuperieur(trait.Constitution.NOM, trait.Trait.SEUIL_A_PAS)
        $ situation_.SetValCaracSiSuperieur(trait.Force.NOM, trait.Trait.SEUIL_A_PAS)
    elif scoreTransformation > 1:
        "Le résultat dépasse toutes vos espérances. Vous devenez un gros et errible nob. Un chef né tout en muscle à la mesure des orks."
        $ AjouterACarac(trait.Force.NOM, 1)
        $ AjouterACarac(trait.Constitution.NOM, 5)
        $ AjouterACarac(trait.Taille.NOM, 1)
    else:
        "Cela marche à merveille. Vous sentez votre corps se renforcer, votre esprit se libérer. Vous êtes maintenant un ork !"
        $ AjouterACarac(trait.Constitution.NOM, 3)

    $ SetValCarac(trait.Serenite.NOM, 0)
    $ situation_.SetValCaracSiInferieur(trait.Violence.NOM, 1)
    $ situation_.SetValCaracSiSuperieur(trait.Beaute.NOM, trait.Trait.SEUIL_A_PAS)

    # guérison potentielle des blessures par l'orkitude :

    python:
        for blessureK in blessures_.lBlessures_.keys():
            # si le perso a cette blessure :
            if situation_.GetValCarac(blessureK) != u"":
                scoreGuerison = random.uniform(0, 1.0)
                if scoreGuerison >= 0.3:
                    texteSoin = blessures_.SoignerBlessure(blessureK, situation_)
                    renpy.say("", "L'incroyable pouvoir de régénération du sérum ork régénère votre corps.")
                    renpy.say("", texteSoin)

    $ prenom = situation_[identite.Identite.C_PRENOM]
    "Dorénavant vous vous appellerez [prenom]."

    "Vous vous installez dans le quartier des orks à Poissy."
    $ situation_.SetValCarac(quartier.Quartier.C_QUARTIER, coterieOrks.quartier_)
    jump fin_cycle
