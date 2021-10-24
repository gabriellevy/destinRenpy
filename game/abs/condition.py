class Condition:
    """
    Système de condition par comparaison d'une carac avec une valeur
    """

    # pas d'eum dans cette version de python on dirait donc hop bricolage :
    INFERIEUR = -2
    INFERIEUR_EGAL = -1
    EGAL = 0
    SUPERIEUR_EGAL = 1
    SUPERIEUR = 2
    DIFFERENT = -99

    def __init__(self, caracId, valeur, comparateur):
        self._m_CaracId = caracId
        self._m_Valeur = valeur
        self._m_Comparateur = comparateur

    def tester(self, situation):
        """
        renvoit true si la condition est vérifiée
        """
        valCarac = situation.GetValCarac(self._m_CaracId)
        if (self._m_Comparateur == Condition.EGAL):
            return str(self._m_Valeur) == str(valCarac)
        if (self._m_Comparateur == Condition.DIFFERENT):
            return str(self._m_Valeur) != str(valCarac)
        else:
            # test de valeurs forcément arithmétiques :
            assert isinstance(valCarac, int), "Test de valeur arithmétique sur une valeur de carac ({}) qui n'est pas arithmétique : '{}'".format(self._m_CaracId, valCarac)
            valCarac = situation.GetValCaracInt(self._m_CaracId)
            if (self._m_Comparateur == Condition.INFERIEUR_EGAL):
                return valCarac <= float(self._m_Valeur)
            elif (self._m_Comparateur == Condition.INFERIEUR):
                return valCarac < float(self._m_Valeur)
            elif (self._m_Comparateur == Condition.SUPERIEUR):
                return valCarac > float(self._m_Valeur)
            elif (self._m_Comparateur == Condition.SUPERIEUR_EGAL):
                return valCarac >= float(self._m_Valeur)
        assert False, "Condition intestable (pas de COmparateur) : {}".format(self)


    def __repr__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        return "Condition {}-{}-{}".format(self._m_CaracId, self._m_Comparateur, self._m_Valeur)

    def __str__(self):
        return self.__repr__()

    # def _get_m_CaracId(self):
    #     return  self._m_CaracId
    # def _get_m_Valeur(self):
    #     return  self._m_Valeur

    # Les conditions sont (intégralement?) non mutables
    # m_CaracId = property(_get_m_CaracId)
    # m_Valeur = property(_get_m_Valeur)
