from enum import Enum
from exec.situation import *

class Comparateur(Enum):
    INFERIEUR = -2
    INFERIEUR_EGAL = -1
    EGAL = 0
    SUPERIEUR_EGAL = 1
    SUPERIEUR = 2

class Condition:
    """
    Système de condition par comparaison d'une carac avec une valeur
    """

    def __init__(self, caracId, valeur, comparateur):
        self._m_CaracId = caracId
        self._m_Valeur = valeur
        self._m_Comparateur = comparateur

    def Tester(self):
        """
        renvoit true si la condition est vérifiée
        """
        situation = Situation()
        valCarac = situation.GetValCarac(self.m_CaracId)
        if (self._m_Comparateur == Comparateur.EGAL):
            return str(self._m_Valeur) == str(valCarac)
        else:
            # test de valeurs forcément arithmétiques :
            assert isinstance(valCarac, int), "Test de valeur arithmétique sur une valeur de carac ({}) qui n'est pas arithmétique : '{}'".format(self.m_CaracId, valCarac)
            if (self._m_Comparateur == Comparateur.INFERIEUR_EGAL):
                return valCarac <= self._m_Valeur
            elif (self._m_Comparateur == Comparateur.INFERIEUR):
                return valCarac < self._m_Valeur
            elif (self._m_Comparateur == Comparateur.SUPERIEUR):
                return valCarac > self._m_Valeur
            elif (self._m_Comparateur == Comparateur.SUPERIEUR_EGAL):
                return valCarac >= self._m_Valeur
        assert False, "Condition intestable (pas de COmparateur) : {}".format(self)

    def _get_m_CaracId(self):
        return  self._m_CaracId
    def _get_m_Valeur(self):
        return  self._m_Valeur

    # Les conditions sont (intégralement?) non mutables
    m_CaracId = property(_get_m_CaracId)
    m_Valeur = property(_get_m_Valeur)


# stupides tests
'''
print("------tests Condition")
situation = Situation()
testCarac = "testCarac"
situation.CreerCarac(testCarac, 2)
condition = Condition(testCarac, 4, Comparateur.INFERIEUR)
print(condition.m_Valeur)
print(condition.Tester())
'''