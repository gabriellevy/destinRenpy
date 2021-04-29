import random

class TestDeCarac:
    """
    Classe modélisant un unique test de carac que le joueur doit effectuer

    self.caracs_ : caracs du test. Par exemple le niveau en métier ou en traits.
    Peut être une string ou un tableau de string

    self.difficulte_ : difficulté du test

    Difficulté va de 1 à 10 :
    1 : enfantin
    2 : tâche de base pour un amateur
    3 : tâche de base pour un travailleur/connaisseur de base
    4 : tâche de base pour un travailleur/connaisseur un mauvais jour
    5 : tâche pour un expérimenté
    6 : tâche pour un expert
    7 :
    8 : difficulté héroïque
    9 : difficulté surhumaine
    10 : difficulté divine
    la valeur de carac va de -20 à 16
    """

    def __init__(self, caracs, difficulte, situation):
        self.caracs_ = caracs
        self.difficulte_ = difficulte
        self.affichage_ = self.Affichage(situation) # cet affichage est stocké pour mermettre l'affichage plus facile dans les balises [] de renpy

    def Affichage(self, situation):
        affichageCarac = self.caracs_
        if isinstance(self.caracs_, list):
            affichageCarac = ""
            for carac in self.caracs_:
                affichageCarac = "{}, {}".format(affichageCarac, carac)
        return " ({}% en {})".format(self.CalculerPourcentageReussite(situation), affichageCarac)

    def CalculerPourcentageReussite(self, situation):
        """
        retourne le pourcentage de change que l'action réussisse étant donné  la valeur de la carac donnée chez le joueur
        et la difficulté de la tâche à accomplir
        """
        valCarac = 0
        if isinstance(self.caracs_, list):
            for carac in self.caracs_:
                val = situation.GetValCaracInt(carac)
                valCarac = valCarac + val
            valCarac = valCarac / len(carac)
        else:
            valCarac = situation.GetValCaracInt(self.caracs_)

        diff = [
        [ 80,  40,   0,   0,   0,   0,   0,  0,  0,  0], # -20 très handicapé
        [ 81,  42,   0,   0,   0,   0,   0,  0,  0,  0], # très handicapé
        [ 82,  44,   0,   0,   0,   0,   0,  0,  0,  0], # très handicapé
        [ 83,  46,   0,   0,   0,   0,   0,  0,  0,  0], # très handicapé
        [ 84,  48,   0,   0,   0,   0,   0,  0,  0,  0], # très handicapé
        [ 85,  50,   0,   0,   0,   0,   0,  0,  0,  0], # -15 handicapé
        [ 86,  52,   0,   0,   0,   0,   0,  0,  0,  0], # handicapé
        [ 87,  54,   0,   0,   0,   0,   0,  0,  0,  0], # handicapé
        [ 88,  56,   0,   0,   0,   0,   0,  0,  0,  0], # handicapé
        [ 89,  58,   0,   0,   0,   0,   0,  0,  0,  0], # handicapé
        [ 90,  60,   5,   0,   0,   0,   0,  0,  0,  0], # -10 personne faible, diminuée
        [ 91,  62,  10,   0,   0,   0,   0,  0,  0,  0], # personne faible, diminuée
        [ 91,  64,  20,  10,   0,   0,   0,  0,  0,  0], # personne faible, diminuée
        [ 92,  66,  30,  15,   0,   0,   0,  0,  0,  0], # personne faible, diminuée
        [ 92,  68,  40,  20,   0,   0,   0,  0,  0,  0], # personne faible, diminuée
        [ 93,  70,  45,  25,   0,   0,   0,  0,  0,  0], # -5 personne faible, diminuée
        [ 93,  72,  50,  30,   5,   1,   0,  0,  0,  0], # personne normale
        [ 94,  74,  55,  35,  10,   2,   0,  0,  0,  0], # personne normale
        [ 94,  76,  60,  40,  20,   3,   0,  0,  0,  0], # personne normale
        [ 95,  78,  65,  45,  30,   4,   0,  0,  0,  0], # personne normale
        [ 95,  85,  70,  50,  40,   5,   0,  0,  0,  0], # 0 : le seuil entre 0 (ne connaît rien à rien) et 1 (initié) est volontairement assez tranché
        [100,  95,  90,  70,  55,  20,  10,  0,  0,  0], # débutant, connaît
        [100,  98,  92,  75,  60,  25,  16,  0,  0,  0], # débutant, connaît
        [100, 100,  95,  80,  65,  30,  22,  0,  0,  0], # débutant, connaît
        [100, 100,  97,  85,  70,  35,  28,  0,  0,  0], # débutant, connaît
        [100, 100, 100,  90,  75,  40,  34,  5,  0,  0], # 5 très avancé
        [100, 100, 100,  92,  80,  45,  40, 10,  0,  0], # très avancé
        [100, 100, 100,  95,  85,  50,  46, 20,  0,  0], # très avancé
        [100, 100, 100, 100,  90,  55,  52, 30,  0,  0], # très avancé
        [100, 100, 100, 100,  95,  60,  58, 40, 10,  5], # héros
        [100, 100, 100, 100, 100,  65,  64, 45, 20, 10], # 10 héros
        [100, 100, 100, 100, 100,  75,  70, 50, 30, 15], # héros
        [100, 100, 100, 100, 100,  85,  76, 55, 40, 20], # 12 héros
        [100, 100, 100, 100, 100,  95,  82, 60, 50, 30], # surhumain
        [100, 100, 100, 100, 100, 100,  88, 65, 60, 40], # surhumain
        [100, 100, 100, 100, 100, 100,  94, 75, 70, 45], #15 surhumain
        [100, 100, 100, 100, 100, 100, 100, 85, 80, 50] #16 dieu
        ]
        return diff[valCarac+20][self.difficulte_-1]

    def TesterDifficulte(self, situation):
        """
        retourne True si le joueur réussit la tâche de difficulté demandée avec sa valeur en carac idCarac
        False sinon
        """
        return random.randint(1,100) <= self.CalculerPourcentageReussite(situation)

    def TesterDegreReussite(self, situation):
        """
        retourne un chiffre entre -5 et 5 qui est une note de réussite d'un test de difficulté demandée avec sa valeur en carac idCarac
        -4 échec catastrophique
        0 échec passable
        1 réussite médiocre
        5 réussite exceptionnelle
        """
        scorePourcent = random.randint(0,100)
        pourcentageReussi = self.CalculerPourcentageReussite(situation)
        degreReussite = 1
        if scorePourcent <= pourcentageReussi:
            # réussite
            degreReussite = ( pourcentageReussi - scorePourcent )/20 + 1
        else:
            # échec
            degreReussite = ( pourcentageReussi - scorePourcent )/15

        return degreReussite
