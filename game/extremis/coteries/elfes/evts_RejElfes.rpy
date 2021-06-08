 # persos
# image ordonnateur = "coteries/templiers/ordonnateur.png"
# define ordo = Character('Ordonnateur', color="#e30909")

# musiques
define audio.principale_elfes = "musique/elfes/principale.mp3"

init -5 python:
    import random
    from extremis.coteries.elfes import elfes
    from extremis.socio_eco.metiers import metier
    from extremis.religions import religion
    from extremis.geographie import quartier
    from extremis.humanite import identite

label elfesPostule:
    # A FAIRE : faire de cette pièce une scène du seigneur des anneaux
    # OU SUREMENT MIEUX : songe d'une nuit d'été de shakespeare avec la musique correspondante de Mendelsshon !!
    "Les elfes n'aiment rien de plus que l'art et vous accueilleront avec joie si vous les distrayez avec talent et élégance."
    "Ils vous mettent donc au défi de monter une pièce de théâtre avec quatre autres postulants."
    $ points = 0
    $ testMusique = testDeCarac.TestDeCarac(metier.Musicien.NOM, 3, situation_)
    $ bTestMusique = False
    $ testAlchimiste = testDeCarac.TestDeCarac(metier.Alchimiste.NOM, 3, situation_)
    $ bTestAlchimiste = False
    $ testPoete = testDeCarac.TestDeCarac(metier.Poete.NOM, 5, situation_)
    $ bTestPoete = False
    $ testDessinateur = testDeCarac.TestDeCarac(metier.Dessinateur.NOM, 4, situation_)
    $ bTestDessinateur = False
    $ testDanseur = testDeCarac.TestDeCarac(metier.Danseur.NOM, 4, situation_)
    $ bTestDanseur = False
    $ tachePreparation = 0
    $ premierRole = False
    $ secondRole = False

    label elfesPostuleChoix:
        menu:
            "En plus de jouer vous pouvez proposer de mettre vos autres talents au service de la pièce : "
            "Si vous proposez de jouer une musique d'introduction à la pièce [testMusique.affichage_]" if not bTestMusique:
                $ bTestMusique = True
                $ tachePreparation = tachePreparation + 1
                "Vous vous entrainez à jouer un air elfique entrainant."
                jump elfesPostuleChoix
            "Si vous proposez d'utiliser vos talents alchimiques pour ajouter des effets de scène [testAlchimiste.affichage_]" if not bTestAlchimiste:
                $ bTestAlchimiste = True
                $ tachePreparation = tachePreparation + 1
                "Vous préparez quelques potions."
                jump elfesPostuleChoix
            "Si vous proposez de créer votre propre pièce [testPoete.affichage_]" if not bTestPoete:
                $ bTestPoete = True
                $ tachePreparation = tachePreparation + 1
                "Vu votre ambition le jury vous accorde un délai supplémentaire. Vous passez plus d'une semaine sur le sujet."
                jump elfesPostuleChoix
            "Si vous proposez de peindre des décors [testDessinateur.affichage_]" if not bTestDessinateur:
                $ bTestDessinateur = True
                $ tachePreparation = tachePreparation + 1
                "Vous faites beaucoup d'effort pour réaliser un fond par acte de la pièce."
                jump elfesPostuleChoix
            "Si vous vous portez volontaire pour le numéro de danse final [testDanseur.affichage_]" if not bTestDanseur:
                $ bTestDanseur = True
                $ tachePreparation = tachePreparation + 1
                "Vous répétez en duo avec la postulante qui joue le rôle de la fée."
                jump elfesPostuleChoix
            "Si vous avez choisi tout ce que désirez faire, il est temps de répéter votre rôle dans la pièce.":
                jump elfesPostuleChoixRole

    label elfesPostuleChoixRole:
        menu:
            "Voulez vous jouer un premier rôle ?"
            "Oui":
                $ premierRole = True
                jump elfesPostuleDebutPiece
            "Non plutôt un second rôle moins difficile.":
                $ secondRole = True
                jump elfesPostuleDebutPiece
            "Vous trouvez que vous avez déjà beaucoup trop de travail pour en plus être acteur" if tachePreparation > 1:
                jump elfesPostuleDebutPiece

    label elfesPostuleDebutPiece:
        "Le jour de la pièce est arrivé. Le public est mince car une troupe d'amateurs postulants intéresse peu de monde, mais il y a une bonne cinquantaine d'elfes tout de même et surtout il y a ceux qui choisiront si vous êtes dignes de devenir un elfe."

        if bTestDessinateur:
            $ reussite = testDessinateur.TesterDegreReussite(situation_)
            if reussite > 2:
                "Dès l'ouverture du rideau vos décors splendides et féériques retiennent toute l'attention."
                $ points = points + 2
            elif reussite > 0:
                "Dès l'ouverture du rideau vos décors sont remarqués et appréciés."
                $ points = points + 1
            else:
                "Dès l'ouverture du rideau le jury juge vos décors de très mauvais goût."
                $ points = points - 2

        $ testAssurance = testDeCarac.TestDeCarac(trait.Assurance.NOM, 4, situation_)
        $ reussi = testAssurance.TesterDifficulte(situation_)
        $ trac = 0
        if not reussi:
            "Vous êtes paralysé par le trac. Votre jeu s'en ressent."
            $ trac = 1

        if bTestMusique:
            "Vous jouez votre musique d'introduction [testMusique.affichage_]"
            $ reussite = testMusique.TesterDegreReussite(situation_)
            if reussite > 2:
                "Cette charmante mélodie satisfait le public."
                $ points = points + 2
            elif reussite > 0:
                "Le public est enchanté par la mélodie et le jury en prend bonne note."
                $ points = points + 1
            else:
                "Votre interprétation est un échec complet. Dès le début une partie du public s'en va."
                $ points = points - 2

        "La pièce commence."
        "Une des postulante joue une fée malicieuse et entre en scène."
        if bTestAlchimiste:
            " C'est là que votre potion doit créer un nuage de fumée colorée. [testAlchimiste.affichage_]"
            $ reussite = testAlchimiste.TesterDegreReussite(situation_)
            if reussite > 2:
                "L'effet est si réussi que le public applaudit et en oublie presque la pièce elle-même."
                $ points = points + 2
            elif reussite > 0:
                "L'effet lumineux ajoute un parfait air mystérieux et magique à la scène."
                $ points = points + 1
            else:
                "La potion crée une fumée noire hideuse qui tâche la combinaison affriolante de l'actrice. Elle est furieuse contre vous. Et même si quelques elfes trouvent ça drôle ce ne sera pas à votre crédit auprès du jury."
                $ points = points - 2

        if bTestPoete:
            $ reussite = testPoete.TesterDegreReussite(situation_)
            if reussite > 2:
                "L'excellent niveau de votre pièce est une surprise our tout l'auditoire. Vos sentez que si vous continuez sur cette lancée vous serez bientôt un elfe."
                $ points = points + 4
            elif reussite > 0:
                "Sans être un chef d'oeuvre votre pièce est bien écrite et appréciée."
                $ points = points + 1
            else:
                "Votre pièce est jugée très médiocre et rend les prestations des acteurs difficiles à juger tant leur texte est peu inspiré. Vous êtes très inquiet."
                $ points = points - 3

        # capacité en tant qu'acteur
        if premierRole or secondRole:

            $ testBeaute = testDeCarac.TestDeCarac(trait.Beaute.NOM, 5, situation_)
            $ reussi = testBeaute.TesterDifficulte(situation_)
            if not reussi:
                "Votre physique ne joue vraiment pas en votre faveur. Mais le public laisse une chance à votre talent de s'exprimer."
                $ points = points - 1

            $ difficulteJeuActeur = 2 + tachePreparation + trac
            if premierRole:
                $ difficulteJeuActeur = difficulteJeuActeur + 2
            $ testActeur = testDeCarac.TestDeCarac(metier.Acteur.NOM, difficulteJeuActeur, situation_)
            $ reussite = testActeur.TesterDegreReussite(situation_)
            if reussite > 2:
                "Votre jeu d'acteur exceptionnel attire tous les regards."
                $ points = points + 2
                if premierRole:
                    $ points = points + 2
            elif reussite > 0:
                "Vous êtes heureux de vous sentir à la hauteur parmi les autres acteurs. Vous n'avez pas à rougir de votre niveau."
                $ points = points + 1
                if premierRole:
                    $ points = points + 1
            else:
                "Non seulement vous jouez mal mais vous oubliez le moitié des répliques. Vous êtes mort de honte."
                $ points = points - 2
                if premierRole:
                    $ points = points - 2

            $ testSensibilite = testDeCarac.TestDeCarac(trait.Sensibilite.NOM, 6, situation_)
            $ reussi = testSensibilite.TesterDifficulte(situation_)
            if reussi:
                "Vous êtes ému aux larmes en récitant les derniers vers. Votre grande sensibilité, qualité elfique par excellence, touche beaucoup le public même si votre jeu s'en ressent."
                $ points = points + 1

        if bTestDanseur:
            "Le spectacle se termine par votre spectacle de danse."
            $ reussite = testDanseur.TesterDegreReussite(situation_)
            if reussite > 2:
                "Pour un non-elfe votre performance est vraiment formidable. Plusieurs elfes ont les larmes aux yeux."
                $ points = points + 2
            elif reussite > 0:
                "Votre ballet à deux est une charmante conclusion à la pièce."
                $ points = points + 1
            else:
                "Votre gaucherie gâche la fin de la pièce. Il est clair que vous vous êtes gravement surestimé et cela va vous être reproché."
                $ points = points - 2

        "points : [points]"
        if points >= 2:
            jump elfesRejoindre
        else:
            "Vous n'êtes malheureusement pas jugé digne d'être elfe. Peut-être quand vous aurez mieux développé votre sensibilité artistique ?"
            jump fin_cycle

label elfesRejoindre:
    scene bg univ_elfes
    "Votre bonne volonté, votre sensibilité et votre talent ont conquis le public. Vous êtes maintenant un membre de la coterie : un apprenti sur la voix de l'elfe."
    $ coterieElfes = coteries_[elfes.Elfes.ID]
    $ coterieElfes.RejoindreCoterie(situation_)
    $ prenom = situation_[identite.Identite.C_PRENOM]
    $ nom = situation_[identite.Identite.C_NOM]
    ordo "Dorénavant vous vous appellerez [prenom] [nom]."

    "Vous vous installez dans le quartier des elfes à Saint Germain en Laye."
    $ situation_.SetValCarac(quartier.Quartier.C_QUARTIER, coterieElfes.quartier_)
    jump fin_cycle
