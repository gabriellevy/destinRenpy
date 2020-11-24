from enum import Enum
from exec.situation import *

class ModifCaracType(Enum):
    SET = 0
    AJOUTE = 1
    RETIRE = 2

class SetCarac:
    """
    Système de mise à jour de carac
    """

    def __init__(self, caracId, modifCaracType, valeur):
        """Constructeur"""
        self.m_CaracId = caracId
        self.m_ModifCaracType = modifCaracType
        self.m_Valeur = valeur
        self.m_IdValeurCaracCopie = None # quand la valeur du set carac est égale à la valeur d'une autre carac au moment de la modification

    def Appliquer(self):
        situation = Situation()
        if self.m_ModifCaracType == ModifCaracType.SET:
            situation.SetCarac(self.m_CaracId, self.m_Valeur)
        elif self.m_ModifCaracType == ModifCaracType.AJOUTE:
            situation.AjouterACarac(self.m_CaracId, self.m_Valeur)
        elif self.m_ModifCaracType == ModifCaracType.RETIRE:
            situation.RetirerACarac(self.m_CaracId, self.m_Valeur)
