init -5 python:
    import random
    from extremis.coteries.elfes import elfes
    from abs import condition

    # condition de niveau d'elfitude :
    demiElfe = condition.Condition(elfes.Elfes.ASCENSION, 5, condition.Condition.SUPERIEUR_EGAL)
    elfeParfait = condition.Condition(elfes.Elfes.ASCENSION, 10, condition.Condition.SUPERIEUR_EGAL)

    def CalcElfitude(situation):
        """
        retourne une note du niveau d'elfitude du personnage
        de 1 à 10 avec un fort aléatoire
        """
        testElfitude = random.randint(1,10)

        estCriminel = GetValCarac(crime.Crime.C_CRIMINEL)
        if estCriminel != "":
            testElfitude = testElfitude - 1
        amoureuses = situation.GetValCarac(relationAmoureuse.RelA.C_AMOUREUSES)
        if len(amoureuses) > 1:
            # plein de maîtresses n'est pas elfique
            testElfitude = testElfitude - 1 # pb : compte les simple amoureuses mais non amantes
        elif len(amoureuses) == 1:
            # si c'est une épouse :
            if amoureuses[0].typeRelation_ == relationAmoureuse.RelA.MARIAGE:
                testElfitude = testElfitude + 1

        valMetierStr = situation.GetValCarac(metier.Metier.C_METIER)
        coterieElfe = situation.collectionCoteries[elfes.Elfes.ID]
        if valMetierStr in coterieElfe.GetMetiersCompatibles():
            # a un métier d'elfe
            testElfitude = testElfitude + 1

        # maîtrise à haut niveau les disciplines elfes ?
        metiersCompatibles = coterieElfe.GetMetiersCompatibles()
        for idMetier in metiersCompatibles:
            compMetier = situation.GetValCaracInt(idMetier)
            if compMetier > 4:
                testElfitude = testElfitude + 1

        return testElfitude


label testElfitude:
    $ elfitude = CalcElfitude(situation_)

    if elfitude >=7:
        jump ascensionElfique
    else:
        "Le temps passe et vous n'êtes toujours pas accepté comme un elfe à part entière."
        jump effetVieillir

label ascensionElfique:
    "Vous vous sentez de plus en plus elfe. Vos oreilles poussent lentement. Mais surtout : "
    $ nbEffets = random.randint(1, 3)
    # +1 en niveau elfique puis des bonus divers :
    $ AjouterACarac(elfes.Elfes.ASCENSION, 1)
    label effetAscensionElfique:
        while nbEffets > 0:
            $ indexEffet = random.randint(0, 13)

            if indexEffet == 0:
                "Vous êtes de plus en plus beau."
                $ AjouterACarac(trait.Beaute.NOM, 1)
                $ nbEffets = nbEffets - 1
                jump effetAscensionElfique
            elif indexEffet == 1:
                "Vous atteignez un nouveau stade de sérénité."
                $ AjouterACarac(trait.Serenite.NOM, 1)
                $ nbEffets = nbEffets - 1
                jump effetAscensionElfique
            elif indexEffet == 2:
                # pas petit
                $ val = situation_.GetValCaracInt(trait.Taille.NOM)
                if val >= 1:
                    jump effetAscensionElfique
                else:
                    "Vous devenez plus grand."
                    $ AjouterACarac(trait.Taille.NOM, 1)
                    $ nbEffets = nbEffets - 1
                    jump effetAscensionElfique
            elif indexEffet == 3:
                # pas gros
                $ val = situation_.GetValCaracInt(trait.Poids.NOM)
                if val <= 0:
                    jump effetAscensionElfique
                else:
                    "Vous devenez plus fin."
                    $ RetirerACarac(trait.Taille.NOM, 1)
                    $ nbEffets = nbEffets - 1
                    jump effetAscensionElfique
            elif indexEffet == 4:
                "Vous êtes de plus en plus inspiré par la beauté du monde."
                $ AjouterACarac(trait.Artiste.NOM, 1)
                $ nbEffets = nbEffets - 1
                jump effetAscensionElfique
            elif indexEffet == 5:
                # moins violent
                $ val = situation_.GetValCaracInt(trait.Violence.NOM)
                if val <= 0:
                    jump effetAscensionElfique
                else:
                    "Vous devenez plus calme et moins colérique."
                    $ RetirerACarac(trait.Violence.NOM, 1)
                    $ nbEffets = nbEffets - 1
                    jump effetAscensionElfique
            elif indexEffet == 6:
                "Vous êtes de plus en plus adroit de vos mains."
                $ AjouterACarac(trait.Habilete.NOM, 1)
                $ nbEffets = nbEffets - 1
                jump effetAscensionElfique
            elif indexEffet == 7:
                "Vous êtes de plus en plus charmeur et sociable."
                $ AjouterACarac(trait.Charme.NOM, 1)
                $ nbEffets = nbEffets - 1
                jump effetAscensionElfique
            elif indexEffet == 8:
                "Vous êtes de plus en plus sensible."
                $ AjouterACarac(trait.Sensibilite.NOM, 1)
                $ nbEffets = nbEffets - 1
                jump effetAscensionElfique
            elif indexEffet == 9:
                # moins cupide
                $ val = situation_.GetValCaracInt(trait.Cupidite.NOM)
                if val <= 0:
                    jump effetAscensionElfique
                else:
                    "Vous êtes de moins en moins attiré par les possessions matérielles."
                    $ RetirerACarac(trait.Cupidite.NOM, 1)
                    $ nbEffets = nbEffets - 1
                    jump effetAscensionElfique
            elif indexEffet == 10:
                # moins opportuniste
                $ val = situation_.GetValCaracInt(trait.Opportunisme.NOM)
                if val <= 0:
                    jump effetAscensionElfique
                else:
                    "Vous vous contentez de ce que vous avez. Votre envie diminue."
                    $ RetirerACarac(trait.Opportunisme.NOM, 1)
                    $ nbEffets = nbEffets - 1
                    jump effetAscensionElfique
            elif indexEffet == 11:
                # au moins un peu honorable
                $ val = situation_.GetValCaracInt(trait.Honorabilite.NOM)
                if val >= 1:
                    jump effetAscensionElfique
                else:
                    "Vous ne trahissez plus votre parole."
                    $ AjouterACarac(trait.Honorabilite.NOM, 1)
                    $ nbEffets = nbEffets - 1
                    jump effetAscensionElfique
            elif indexEffet == 12:
                # au moins un peu ascète
                $ val = situation_.GetValCaracInt(trait.Ascetisme.NOM)
                if val >= 1:
                    jump effetAscensionElfique
                else:
                    "Votre goût pour le luxe disparaît."
                    $ AjouterACarac(trait.Ascetisme.NOM, 1)
                    $ nbEffets = nbEffets - 1
                    jump effetAscensionElfique
            elif indexEffet == 13:
                # au moins un peu courageux
                $ val = situation_.GetValCaracInt(trait.Courage.NOM)
                if val >= 1:
                    jump effetAscensionElfique
                else:
                    "Vous ne serez plus jamais un lâche."
                    $ AjouterACarac(trait.Courage.NOM, 1)
                    $ nbEffets = nbEffets - 1
                    jump effetAscensionElfique

        jump fin_cycle
    jump fin_cycle
