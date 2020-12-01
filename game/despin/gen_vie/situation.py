

class Situation:
    """
    Situation de jeu
    Etat d'une partie à un instant t avec toutes les informations nécessaires pour la sauvegarder et la recharger
    en particulier la liste intégrale des caractéristiques du perso (qui sont une sous catégorie de la situation de jeu)

    !!!! cette classe est peut-être à surclasser pour ajouter des effets particuliers à certaines caracs (dans SetCarac par exemple)
    """

    def __init__(self):
        self.caracs_ = dict() # dictionnaire contenant toutes les caracs courantes de la partie
        self.valsMin_ = dict() # facultatif : dictionnaire contenant l'éventuelle valeur min de la carac en clé
        self.valsMax_ = dict()# facultatif : dictionnaire contenant l'éventuelle valeur max de la carac en clé

    def __getitem__(self, key):
        return self.caracs_[key]

    def __getattr__(self, nom):
        """Si Python ne trouve pas l'attribut nommé nom, il appelle
             cette méthode. On affiche une alerte"""
        print("Alerte ! Il n'y a pas d'attribut '{}' dans l'objet '{}' !".format(nom, self))

    def AjouterCarac(self, idCarac, val):
        self.caracs_[idCarac] = val

    def CreerCarac(self, idCarac, valCarac, valeurMin = "", valeurMax = ""):
        self.AjouterCarac(idCarac, valCarac)
        if valeurMin != "":
            self.valsMin_[idCarac] = valeurMin
        if valeurMax != "":
            self.valsMax_[idCarac] = valeurMax

    def SetCarac(self, idCarac, valCarac, valeurMin = "", valeurMax = ""):
        # si la carac n'existe pas encore, la créer
        if not idCarac in self.caracs_:
            self.CreerCarac(idCarac, valCarac, valeurMin, valeurMax)

        self.caracs_[idCarac] = valCarac
        if valeurMin != "":
            self.valsMin_[idCarac] = valeurMin
        if valeurMax != "":
            self.valsMax_[idCarac] = valeurMax

    def AjouterACarac(self, idCarac, valCarac):
        finalVal = self.caracs_[idCarac] + valCarac
        if idCarac in self.valsMax_ and finalVal > self.valsMax_[idCarac]:
            finalVal = self.valsMax_[idCarac]
        self.SetCarac(idCarac, finalVal)

    def RetirerACarac(self, idCarac, valCarac):
        finalVal = self.caracs_[idCarac].m_Valeur - valCarac
        if idCarac in self.valsMin_ and finalVal < self.valsMin_[idCarac]:
            finalVal = self.valsMin_[idCarac]
        self.SetCarac(idCarac, finalVal)

    def GetValCarac(self, idCarac):
        if ( idCarac not in self.caracs_):
            return ""
        return self.caracs_[idCarac]
