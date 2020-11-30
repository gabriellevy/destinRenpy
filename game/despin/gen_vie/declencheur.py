

class Declencheur:
    """
    Classe gérant le déclenchement d'événement particulier via leurs conditions et probas,
    calculs en fonction des caracs de la situation actuelle
    """

    conditions_ = list()
    proba_ = None # float d'abord puis proba composée avec des modificateurs de proba
    labelGoTo_ = "labelGoTo_pasFait"

    def __init__(self, proba, labelGoTo):
        self.proba_ = proba
        self.labelGoTo_ = labelGoTo

    def calculerProba(self):
        #  compléter bien sûr, en attendant :
        return self.proba_

    def executer(self):
        return self.labelGoTo_
