# define audio.sanctus = "musique/templiers/sanctus.mp3"

init -5 python:
    import random
    from abs.religions import religion

    def determinerAnimalTotem():
        """
        forceConversion : si True le perso est immédiatement converti, sinon il a des chances de ne aps l'être si il a déjà une religion
        """
        global situation_
        animalTotemStr = ""
        adjectifStr = ""
        valAbsMax = 0

        # animal :
        valsAnimalTotem = {"abeille" : 0, "aigle" : 0,
        "Araignée": 0,
        "Canard": 0,
        "cerf": 0,
        "chat": 0,
        "cheval": 0,
        "coccinelle": 0,
        "colibri": 0,
        "corbeau": 0,
        "Coyotte": 0,
        "Éléphant": 0,
        "giraffe": 0,
        "hibou": 0,
        "libellule": 0,
        "lion": 0,
        "loup": 0,
        "mouton": 0,
        "ours": 0,
        "panda": 0,
        "papillon": 0,
        "pieuvre": 0,
        "Renard": 0,
        "serpent": 0,
        "tigre": 0,
        "Tortue": 0,
        "vautour": 0}

        # Liberte
        valsAnimalTotem["aigle"] = valsAnimalTotem["aigle"] + situation_.GetValCaracInt(trait.Liberte.NOM)
        valsAnimalTotem["chat"] = valsAnimalTotem["chat"] + situation_.GetValCaracInt(trait.Liberte.NOM)
        valsAnimalTotem["colibri"] = valsAnimalTotem["colibri"] + situation_.GetValCaracInt(trait.Liberte.NOM)
        # Assurance
        valsAnimalTotem["aigle"] = valsAnimalTotem["aigle"] + situation_.GetValCaracInt(trait.Assurance.NOM)
        valsAnimalTotem["lion"] = valsAnimalTotem["lion"] + situation_.GetValCaracInt(trait.Assurance.NOM)
        valsAnimalTotem["tigre"] = valsAnimalTotem["tigre"] + situation_.GetValCaracInt(trait.Assurance.NOM)
        valsAnimalTotem["loup"] = valsAnimalTotem["loup"] + situation_.GetValCaracInt(trait.Assurance.NOM)
        valsAnimalTotem["mouton"] = valsAnimalTotem["mouton"] - situation_.GetValCaracInt(trait.Assurance.NOM)
        # Richesse
        # Artiste
        valsAnimalTotem["Araignée"] = valsAnimalTotem["Araignée"] + situation_.GetValCaracInt(trait.Artiste.NOM)
        # Spiritualite
        # Charme
        valsAnimalTotem["chat"] = valsAnimalTotem["chat"] + situation_.GetValCaracInt(trait.Charme.NOM)
        valsAnimalTotem["coccinelle"] = valsAnimalTotem["coccinelle"] + situation_.GetValCaracInt(trait.Charme.NOM)
        valsAnimalTotem["libellule"] = valsAnimalTotem["libellule"] + situation_.GetValCaracInt(trait.Charme.NOM)
        valsAnimalTotem["panda"] = valsAnimalTotem["panda"] + situation_.GetValCaracInt(trait.Charme.NOM)
        # Observation
        valsAnimalTotem["aigle"] = valsAnimalTotem["aigle"] + situation_.GetValCaracInt(trait.Observation.NOM)
        valsAnimalTotem["vautour"] = valsAnimalTotem["vautour"] + situation_.GetValCaracInt(trait.Observation.NOM)
        # Habilete
        valsAnimalTotem["Araignée"] = valsAnimalTotem["Araignée"] + situation_.GetValCaracInt(trait.Habilete.NOM)
        valsAnimalTotem["chat"] = valsAnimalTotem["chat"] + situation_.GetValCaracInt(trait.Habilete.NOM)
        # Beaute
        valsAnimalTotem["cerf"] = valsAnimalTotem["cerf"] + situation_.GetValCaracInt(trait.Beaute.NOM)
        valsAnimalTotem["cheval"] = valsAnimalTotem["cheval"] + situation_.GetValCaracInt(trait.Beaute.NOM)
        # Taille
        valsAnimalTotem["giraffe"] = valsAnimalTotem["giraffe"] + situation_.GetValCaracInt(trait.Taille.NOM)
        valsAnimalTotem["ours"] = valsAnimalTotem["ours"] + situation_.GetValCaracInt(trait.Taille.NOM)
        valsAnimalTotem["Éléphant"] = valsAnimalTotem["Éléphant"] + situation_.GetValCaracInt(trait.Taille.NOM)
        # Poids
        valsAnimalTotem["Éléphant"] = valsAnimalTotem["Éléphant"] + situation_.GetValCaracInt(trait.Poids.NOM)
        valsAnimalTotem["ours"] = valsAnimalTotem["ours"] + situation_.GetValCaracInt(trait.Poids.NOM)
        valsAnimalTotem["panda"] = valsAnimalTotem["panda"] + situation_.GetValCaracInt(trait.Poids.NOM)
        valsAnimalTotem["libellule"] = valsAnimalTotem["libellule"] - situation_.GetValCaracInt(trait.Poids.NOM)
        # Constitution
        valsAnimalTotem["Coyotte"] = valsAnimalTotem["Coyotte"] + situation_.GetValCaracInt(trait.Constitution.NOM)
        valsAnimalTotem["Tortue"] = valsAnimalTotem["Tortue"] + situation_.GetValCaracInt(trait.Constitution.NOM)
        valsAnimalTotem["papillon"] = valsAnimalTotem["papillon"] - situation_.GetValCaracInt(trait.Constitution.NOM)
        # Force
        valsAnimalTotem["Éléphant"] = valsAnimalTotem["Éléphant"] + situation_.GetValCaracInt(trait.Force.NOM)
        valsAnimalTotem["lion"] = valsAnimalTotem["lion"] + situation_.GetValCaracInt(trait.Force.NOM)
        valsAnimalTotem["ours"] = valsAnimalTotem["ours"] + situation_.GetValCaracInt(trait.Force.NOM)
        # Patriarcat
        # Sexualite
        valsAnimalTotem["Canard"] = valsAnimalTotem["Canard"] + situation_.GetValCaracInt(trait.Sexualite.NOM)
        # Cupidite
        valsAnimalTotem["Renard"] = valsAnimalTotem["Renard"] + situation_.GetValCaracInt(trait.Cupidite.NOM)
        # Sincerite
        valsAnimalTotem["mouton"] = valsAnimalTotem["mouton"] + situation_.GetValCaracInt(trait.Sincerite.NOM)
        # Honorabilite
        valsAnimalTotem["abeille"] = valsAnimalTotem["abeille"] + situation_.GetValCaracInt(trait.Honorabilite.NOM)
        valsAnimalTotem["cerf"] = valsAnimalTotem["cerf"] + situation_.GetValCaracInt(trait.Honorabilite.NOM)
        valsAnimalTotem["hibou"] = valsAnimalTotem["hibou"] + situation_.GetValCaracInt(trait.Honorabilite.NOM)
        valsAnimalTotem["lion"] = valsAnimalTotem["lion"] + situation_.GetValCaracInt(trait.Honorabilite.NOM)
        valsAnimalTotem["Éléphant"] = valsAnimalTotem["Éléphant"] + situation_.GetValCaracInt(trait.Honorabilite.NOM)
        valsAnimalTotem["Renard"] = valsAnimalTotem["Renard"] - situation_.GetValCaracInt(trait.Honorabilite.NOM)
        valsAnimalTotem["chat"] = valsAnimalTotem["chat"] - situation_.GetValCaracInt(trait.Honorabilite.NOM)
        # Opportunisme
        valsAnimalTotem["Renard"] = valsAnimalTotem["Renard"] + situation_.GetValCaracInt(trait.Opportunisme.NOM)
        # Industrie
        valsAnimalTotem["abeille"] = valsAnimalTotem["abeille"] + situation_.GetValCaracInt(trait.Industrie.NOM)
        valsAnimalTotem["Araignée"] = valsAnimalTotem["Araignée"] + situation_.GetValCaracInt(trait.Industrie.NOM)
        # Franchise
        valsAnimalTotem["chat"] = valsAnimalTotem["chat"] - situation_.GetValCaracInt(trait.Franchise.NOM)
        valsAnimalTotem["Renard"] = valsAnimalTotem["Renard"] - situation_.GetValCaracInt(trait.Franchise.NOM)
        valsAnimalTotem["serpent"] = valsAnimalTotem["serpent"] - situation_.GetValCaracInt(trait.Franchise.NOM)
        # Violence
        valsAnimalTotem["lion"] = valsAnimalTotem["lion"] - situation_.GetValCaracInt(trait.Violence.NOM)
        valsAnimalTotem["ours"] = valsAnimalTotem["ours"] - situation_.GetValCaracInt(trait.Violence.NOM)
        valsAnimalTotem["tigre"] = valsAnimalTotem["tigre"] - situation_.GetValCaracInt(trait.Violence.NOM)
        # Pragmatisme
        valsAnimalTotem["abeille"] = valsAnimalTotem["abeille"] + situation_.GetValCaracInt(trait.Pragmatisme.NOM)
        valsAnimalTotem["Araignée"] = valsAnimalTotem["Araignée"] + situation_.GetValCaracInt(trait.Pragmatisme.NOM)
        valsAnimalTotem["vautour"] = valsAnimalTotem["vautour"] + situation_.GetValCaracInt(trait.Pragmatisme.NOM)
        valsAnimalTotem["corbeau"] = valsAnimalTotem["corbeau"] + situation_.GetValCaracInt(trait.Pragmatisme.NOM)
        valsAnimalTotem["serpent"] = valsAnimalTotem["serpent"] + situation_.GetValCaracInt(trait.Pragmatisme.NOM)
        valsAnimalTotem["Tortue"] = valsAnimalTotem["Tortue"] + situation_.GetValCaracInt(trait.Pragmatisme.NOM)
        # Intellectualisme
        valsAnimalTotem["hibou"] = valsAnimalTotem["hibou"] + situation_.GetValCaracInt(trait.Intellectualisme.NOM)
        # Intelligence
        valsAnimalTotem["Éléphant"] = valsAnimalTotem["Éléphant"] + situation_.GetValCaracInt(trait.Intelligence.NOM)
        valsAnimalTotem["corbeau"] = valsAnimalTotem["corbeau"] + situation_.GetValCaracInt(trait.Intelligence.NOM)
        valsAnimalTotem["pieuvre"] = valsAnimalTotem["pieuvre"] + situation_.GetValCaracInt(trait.Intelligence.NOM)
        valsAnimalTotem["Renard"] = valsAnimalTotem["Renard"] + situation_.GetValCaracInt(trait.Intelligence.NOM)
        valsAnimalTotem["Coyotte"] = valsAnimalTotem["Coyotte"] + situation_.GetValCaracInt(trait.Intelligence.NOM)
        # Sensibilite
        valsAnimalTotem["coccinelle"] = valsAnimalTotem["coccinelle"] + situation_.GetValCaracInt(trait.Sensibilite.NOM)
        valsAnimalTotem["papillon"] = valsAnimalTotem["papillon"] + situation_.GetValCaracInt(trait.Sensibilite.NOM)
        # Ascetisme
        valsAnimalTotem["Tortue"] = valsAnimalTotem["Tortue"] + situation_.GetValCaracInt(trait.Ascetisme.NOM)
        valsAnimalTotem["serpent"] = valsAnimalTotem["serpent"] + situation_.GetValCaracInt(trait.Ascetisme.NOM)
        valsAnimalTotem["Coyotte"] = valsAnimalTotem["Coyotte"] + situation_.GetValCaracInt(trait.Ascetisme.NOM)
        valsAnimalTotem["serpent"] = valsAnimalTotem["serpent"] + situation_.GetValCaracInt(trait.Ascetisme.NOM)
        # Courage
        valsAnimalTotem["lion"] = valsAnimalTotem["lion"] + situation_.GetValCaracInt(trait.Courage.NOM)
        # Ambition
        valsAnimalTotem["lion"] = valsAnimalTotem["lion"] + situation_.GetValCaracInt(trait.Ambition.NOM)
        valsAnimalTotem["mouton"] = valsAnimalTotem["mouton"] - situation_.GetValCaracInt(trait.Ambition.NOM)
        valsAnimalTotem["Renard"] = valsAnimalTotem["Renard"] + situation_.GetValCaracInt(trait.Ambition.NOM)
        # Prudence
        valsAnimalTotem["vautour"] = valsAnimalTotem["vautour"] + situation_.GetValCaracInt(trait.Prudence.NOM)
        valsAnimalTotem["hibou"] = valsAnimalTotem["hibou"] + situation_.GetValCaracInt(trait.Prudence.NOM)
        valsAnimalTotem["serpent"] = valsAnimalTotem["serpent"] + situation_.GetValCaracInt(trait.Prudence.NOM)
        valsAnimalTotem["Tortue"] = valsAnimalTotem["Tortue"] + situation_.GetValCaracInt(trait.Prudence.NOM)
        # Altruisme
        valsAnimalTotem["loup"] = valsAnimalTotem["loup"] - situation_.GetValCaracInt(trait.Altruisme.NOM)
        # Rancune
        valsAnimalTotem["Éléphant"] = valsAnimalTotem["Éléphant"] + situation_.GetValCaracInt(trait.Rancune.NOM)
        valsAnimalTotem["hibou"] = valsAnimalTotem["hibou"] + situation_.GetValCaracInt(trait.Rancune.NOM)
        # Serenite
        valsAnimalTotem["Tortue"] = valsAnimalTotem["Tortue"] + situation_.GetValCaracInt(trait.Serenite.NOM)
        valsAnimalTotem["vautour"] = valsAnimalTotem["vautour"] + situation_.GetValCaracInt(trait.Serenite.NOM)
        valsAnimalTotem["colibri"] = valsAnimalTotem["colibri"] - situation_.GetValCaracInt(trait.Serenite.NOM)
        # Celebrite

        # déterminer animal final :
        valMax = -9999
        for k, v in valsAnimalTotem.items():
            if v > valMax:
                valMax = v
                animalTotemStr = k
        print("Valeur Animal totem : {} {}".format(animalTotemStr, valMax))

        # adjectif :
        valAbsMax = 0
        for traitK in traits_.lTraits_.keys():
            valTrait = situation_.GetValCaracInt(traitK)
            if abs(valTrait) > valAbsMax:
                valMax = abs(valTrait)
                adjectifStr = traits_.lTraits_[traitK].GetDescription(situation_)
        # valCourante = # adjectif du trait le plus élevé en valeur absolue

        print("Animal totem : {} {}".format(animalTotemStr, adjectifStr))

        return "{} {}".format(animalTotemStr, adjectifStr)
