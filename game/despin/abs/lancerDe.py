from random import randint

class LancerDe:
    """
    simule un lancer de dé
    est forcément partie d'un noeud narratif. Après l'affichage du texte mais avant les éventuels choix.
    Il demande validation pour lancer m_NbDes, exécute sa fonction callback (en fonction du résultat de dé en général) puis lexécution du noeud continue
    """
    def __init__(self, nbDes, callback = None):
        """
        :param nbDes: nombre de dés à lancer
        :param callback: fonction qui sera appelée après lancement des dés
        """
        self.m_NbDes = nbDes
        self.m_Callback = callback
        # self.m_CallbackParams = callbackParams
        txt = ""
        if (nbDes > 1):
            txt = "s"
        self.m_MessageLancerDe = "Validez pour lancer {} dé{}".format(nbDes, txt)

    def CalculerResDe(self):
        listeRes = self.GetListeResDes()
        resTotal = 0
        for resDe in listeRes:
            resTotal += resDe
        return resTotal

    def GetListeResDes(self):
        res = list()
        i = 0
        while i < self.m_NbDes:
            res.append(randint(1,6))
            i+=1
        return res

    def LancerDe(self, effetActuel, input):
        """
        Lancement d'un dé au cours d'un effet
        :param effetActuel:
        :return: True si l'exécution est terminée, False si il faut lancer les dés une nouvelle fois en restant dans son effet actuel
        """
        if ( self.m_Callback is not None):
            listeRes = self.GetListeResDes()
            print("Résultat des dés : {}".format(listeRes))
            self.m_Callback(listeRes)
        return True
