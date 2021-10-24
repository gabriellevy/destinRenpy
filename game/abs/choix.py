from abs.noeudNarration import NoeudNarration
from abs.effet import *

class Choix(NoeudNarration):
    """
    dérive des noeuds narration tout comme les effets mais est un bouton et a comme principale particularité que l'exécution des actions n'est
    faite que quand on appuie sur le bouton de même que la transition. Ils sont donc complètement désolidarisés de l'affichage contrairement
    à la plupart des noeuds
    """

    compteurId = 0

    def __init__(self, effet, texte, id):
        if (isinstance(effet, Effet)) != True:
            raise TypeError( \
                "Impossible de créer un choix avec comme 'effet' un objet qui n'est pas un effet mais un : '{0}'".format( \
                    type(effet)))
        self.m_Effet = effet
        NoeudNarration.__init__(self, id, texte)

    def __repr__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        return "Choix {}-{}".format(self.m_Id, self.m_Texte)

    def __str__(self):
        return self.m_Texte

