import random

class Selecteur:
    """
    Objet qui contient tous les déclencheurs et le système de sélection selon les proba
    """

    def __init__(self):
        self.declencheurs_ = []

    def ajouterDeclencheur(self, declencheur):
        self.declencheurs_.append(declencheur)

    def determinationEvtCourant(self, situation):
        probaComplete = 0
        probaTmp = 0
        for declencheur in self.declencheurs_:
            proba = declencheur.calculerProba(situation)
            probaComplete = probaComplete + proba

        resProba = random.uniform(0, probaComplete)

        # déterminer évt final
        for declencheur in self.declencheurs_:
            proba = declencheur.calculerProba(situation)
            if proba > 0:
                probaTmp = probaTmp + proba
                if resProba <= probaTmp:
                    return declencheur.executer()

        return "pas_evt_trouve"
