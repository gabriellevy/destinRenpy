from despin.abs import condition

class ModifProba:
    """
    Probabilité à appliquer à un déclencheur
    """

    def __init__(self, poidsProba, condition):
        self.poidsProba_ = poidsProba
        self.condition_ = condition

    def testerCondition(self, situation):
        return self.condition_.tester(situation)
