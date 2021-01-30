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
        global erreur_
        probaCompleteRel = 0 # total des probas relatives
        probaCompleteAbs = 0 # total des probas absolues
        probaTmp = 0
        for declencheur in self.declencheurs_:
            proba = declencheur.calculerProba(situation)
            if declencheur.proba_.relative_:
                probaCompleteRel = probaCompleteRel + proba
            else:
                probaCompleteAbs = probaCompleteAbs + proba

        # proba absolues (où le total des proba absolues ne peut pas dépasser 1.0 car une proba de 0.5 est VRAIMENT une proba de 50%
        resProba = random.uniform(0, 1.0)
        if resProba <= probaCompleteAbs:
            print(probaCompleteAbs)
            if probaCompleteAbs > 1.0:
                return "probaAbsoluesSup100"
            for declencheur in self.declencheurs_:
                if not declencheur.proba_.relative_:
                    proba = declencheur.calculerProba(situation)
                    if proba > 0:
                        probaTmp = probaTmp + proba
                        if resProba <= probaTmp:
                            return declencheur.executer()

        # si pas de proba absolue validée, on passe aux relatives :
        # probas relatives
        resProba = random.uniform(0, probaCompleteRel)

        # déterminer évt final
        for declencheur in self.declencheurs_:
            if declencheur.proba_.relative_:
                proba = declencheur.calculerProba(situation)
                if proba > 0:
                    probaTmp = probaTmp + proba
                    if resProba <= probaTmp:
                        return declencheur.executer()

        return "pas_evt_trouve"
