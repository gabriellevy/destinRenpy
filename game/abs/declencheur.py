from abs import proba
from abs import modifProba
from abs import condition

class Declencheur:
    """
    Classe gérant le déclenchement d'événement particulier via leurs conditions et probas,
    calculs en fonction des caracs de la situation actuelle
    """

    def __init__(self, aproba, labelGoTo):
        """
        aproba peut être une proba complète déclarée ou juste un float dans ce cas il sera convertie en proba déclarée dans ce constructeur
        """
        self.conditions_ = []
        if isinstance(aproba, proba.Proba):
            self.proba_ = aproba
        else:
            # la proba est un simple nombre flottant (sans modif de proba)
            self.proba_ = proba.Proba(aproba)
        self.labelGoTo_ = labelGoTo

    def calculerProba(self, situation):
        for condition in self.conditions_:
            resTest = condition.tester(situation)
            if not resTest:
                return 0. # si une des conditions n'est pas vérifiée alors la proba est égale à 0
            pass

        return self.proba_.calculer(situation)

    def executer(self):
        return self.labelGoTo_

    def AjouterCondition(self, condition):
        self.conditions_.append(condition)

    def AjouterConditions(self, conditions):
        """
        tableau de conditions ajoutées une à une
        """
        for condObj in conditions:
            self.conditions_.append(condObj)


class DeclencheurU(Declencheur):
    """
    U signifie 'Unique' => l'événement auquel on applique ce déclencheur ne peut s'exécuter qu'une fois maximum
    """

    def __init__(self, aproba, labelGoTo):
        """
        identique à la version historique amis ne se déclenche qu'une fois maximum quoiqu'il arrive
        """
        Declencheur.__init__(self, aproba, labelGoTo)

    def executer(self):
        # cette exécution ne doit plus jamais arriver : on lui met une proba à 0 :
        # self.proba_ = proba.Proba(0)
        if self.selecteur_ is not None:
            self.selecteur_.declencheurs_.remove(self)
        return self.labelGoTo_
