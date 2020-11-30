import random

class Selecteur:
    """
    Objet qui contient tous les déclencheurs et le système de sélection selon les proba
    """

    declencheurs_ = []

    def __init__(self):
        self.declencheurs_ = []

    def ajouterDeclencheur(self, declencheur):
        self.declencheurs_.append(declencheur)

    def determinationEvtCourant(self):
        probaComplete = 0
        probaTmp = 0
        for declencheur in self.declencheurs_:
            probaComplete = probaComplete + declencheur.calculerProba()

        resProba = random.uniform(0, probaComplete)

        # déterminer évt final
        for declencheur in self.declencheurs_:
            probaTmp = probaTmp + declencheur.calculerProba()
            if resProba < probaTmp:
                return declencheur.executer()

        return "pas_evt_trouve"
