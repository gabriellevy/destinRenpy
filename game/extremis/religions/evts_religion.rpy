

init -5 python:
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
