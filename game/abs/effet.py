from abs.noeudNarration import NoeudNarration
from abs.evt import *
from abs.lancerDe import *

class Effet(NoeudNarration):
    """
    élément de base pour raconter une histoire
    conteneur de choix avec fonctions d'accès/modification surchargées pour ça
    """

    compteurId = 0

    def __init__(self, evt, texte, id, titre):
        if (isinstance(evt, Evt)) != True:
            raise TypeError( \
                "Impossible de créer un effet avec comme 'evt' un objet qui n'est pas un événement mais un : '{0}'".format( \
                    type(evt)))
        self.m_Evt = evt
        NoeudNarration.__init__(self, id, texte)
        self.m_IdChoix = []  # Liste contenant nos "clés" de la liste de choix
        self.m_Choix = list()
        self.m_LancerDe = None
        self.m_Titre = titre

    def AjouterLancerDe(self, nbDes, callback, params):
        self.m_LancerDe = LancerDe(nbDes, callback, params)

    def __repr__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        return "Effet {}-{}".format(self.m_Id, self.m_Texte)

    def __str__(self):
        txt = ""
        if ( self.m_Titre != "" ):
            txt = "------------------ " + self.m_Titre + " --------------------\n"
        return txt + self.m_Texte

    def ParcourirChoix(self):
        """ pseudo itérateur des choix de l'effet """
        for choix in self.m_Choix:
            yield choix

    def __getitem__(self, cle):
        """Renvoie la valeur correspondant à la clé si elle existe, lève
        une exception KeyError sinon"""

        if cle not in self.m_IdChoix:
            raise KeyError( \
                "La clé {0} ne se trouve pas dans le dictionnaire".format( \
                    cle))
        else:
            indice = self.m_IdChoix.index(cle)
            return self.m_Choix[indice]

    def __setitem__(self, cle, valeur):
        """Méthode spéciale appelée quand on cherche à modifier une clé
        présente dans le dictionnaire. Si la clé n'est pas présente, on l'ajoute
        à la fin du dictionnaire"""

        if cle in self.m_IdChoix:
            indice = self.m_IdChoix.index(cle)
            self.m_Choix[indice] = valeur
        else:
            self.m_IdChoix.append(cle)
            self.m_Choix.append(valeur)

    def __delitem__(self, cle):
        """Méthode appelée quand on souhaite supprimer une clé"""
        if cle not in self.m_IdChoix:
            raise KeyError( \
                "La clé {0} ne se trouve pas dans le dictionnaire".format( \
                    cle))
        else:
            indice = self.m_IdChoix.index(cle)
            del self.m_IdChoix[indice]
            del self.m_Choix[indice]

    def __contains__(self, cle):
        """Renvoie True si la clé est dans la liste des clés ou des valeurs, False sinon"""
        if (isinstance(cle, Choix)) == True:
            return cle in self.m_Choix
        else:
            return cle in self.m_IdChoix

    def __len__(self):
        """"""
        return self.m_Choix.__len__()

    def __iter__(self):
        """"""
        return iter(self.m_IdChoix)

    def items(self):
        """Renvoie un générateur contenant les couples (cle, valeur)"""
        for i, cle in enumerate(self.m_IdChoix):
            valeur = self.m_Choix[i]
            yield (cle, valeur)

    def keys(self):
        """Cette méthode renvoie la liste des clés"""
        return list(self.m_IdChoix)

    def values(self):
        """Cette méthode renvoie la liste des valeurs"""
        return list(self.m_Choix)
