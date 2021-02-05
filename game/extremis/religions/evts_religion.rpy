

init -5 python:
    import random
    from extremis.religions import religion

    def devientAthee():
        """
        Applique tous les changements liées au fait de quitter sa religion
        return False si le perso n'avait aps de religion
        """
        global situation_
        religion = situation_.GetValCarac(religion.Religion.C_RELIGION)
        if religion == "" or religion == religion.Atheisme.NOM:
            situation_.SetCarac(religion.Religion.C_RELIGION,  religion.Atheisme.NOM)
            situation_.SetCarac(religion.Religion.C_FOI,  0)
            situation_.SetCarac(religion.Religion.C_MIRACLE,  0)
            return True
        return False

    def conversionReligieuse(p_religion, forceConversion=False):
        """
        forceConversion : si True le perso est immédiatement converti, sinon il a des chances de ne aps l'être si il a déjà une religion
        """
        global situation_

        religionCaracStr = religion.Religion.C_RELIGION
        religionActuelle = situation_.GetValCarac(religionCaracStr)
        if religionActuelle == "":
            # pas de religion
            situation_.SetValCarac(religion.Religion.C_RELIGION, p_religion)
            return True
        elif religionActuelle == p_religion:
            # déjà de cette religion
            return False
        else:
            randVal = random.uniform(0, 1.0)
            # conversion pas 100% sûr
            if randVal < 0.7:
                situation_.SetValCarac(religion.Religion.C_RELIGION, p_religion)
                return True
            else:
                return False
