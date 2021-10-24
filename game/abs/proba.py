from abs import modifProba

class Proba:
    """
    Probabilité à appliquer à un déclencheur
    """

    def __init__(self, poidsProba, relative = True):
        self.modifsProba_ = []
        # si relative_ est à True la proba dépend du poids des autres proba dans le sélecteur
        # Sinon elle est absolue et poidsProba devient une proba de type pourcentage (entre 0 (=> jamais) et 1(=>toujours))
        self.poidsProba_ = poidsProba
        self.relative_ = relative

    def ajouterModifProba(self, modifProba):
        # TODO : tester le type d'objet en paramètre avec isInstance ou je ne sais quoi
        self.modifsProba_.append(modifProba)

    def ajouterModifProbaViaVals(self, poidsProba, condition):
        lModifProba = modifProba.ModifProba(poidsProba, condition)
        self.ajouterModifProba(lModifProba)

    def calculer(self, situation):
        probaFinale = self.poidsProba_
        for modifProba in self.modifsProba_:
            if modifProba.testerCondition(situation):
                probaFinale = probaFinale + modifProba.poidsProba_
            pass

        if probaFinale < 0:
            probaFinale = 0
        return probaFinale
