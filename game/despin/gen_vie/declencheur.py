

class Declencheur:
    """
    Classe gérant le déclenchement d'événement particulier via leurs conditions et probas,
    calculs en fonction des caracs de la situation actuelle
    """

    def __init__(self, proba, labelGoTo):
        self.conditions_ = []
        self.proba_ = proba # float d'abord puis proba composée avec des modificateurs de proba
        self.labelGoTo_ = labelGoTo

    def calculerProba(self, situation):
        for condition in self.conditions_:
            resTest = condition.Tester(situation)
            print("condition : {}".format(condition))
            print("resTest : {}".format(resTest))
            if not resTest:
                return 0. # si une des conditions n'est pas vérifiée alors la proba est égale à 0
            pass

        print("fin calculerProba")
        #  compléter bien sûr, en attendant :
        return self.proba_

    def executer(self):
        return self.labelGoTo_

    def AjouterCondition(self, conditionAdministratif):
        self.conditions_.append(conditionAdministratif)
