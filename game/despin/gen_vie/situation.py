from extremis.socio_eco import metier
from extremis.constitution import temps
import random

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
        self.valsMax_ = dict() # facultatif : dictionnaire contenant l'éventuelle valeur max de la carac en clé
        date = temps.Date()
        self.caracs_[temps.Date.DATE] = date.nbJours_
        self.caracs_[temps.Date.AGE_ANNEES] = 0

    def __getitem__(self, key):
        if key not in self.caracs_:
            self.caracs_[key] = ""
        return self.caracs_[key]

    def __setitem__(self, key, val):
        #self.caracs_[key] = val
        self.SetCarac(key, val)

    def __format__(self, format):
        # if(format == 'age'):
        #     return '23'
        return str(self)

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

        # modifier certaines caracs peut impliquer des changements implicites à d'autres :
        if idCarac == metier.Metier.METIER:
            metier.regenererCaracsMetier(self)

    def AjouterACarac(self, idCarac, valCarac):
        # si la carac n'existe pas encore, la créer
        if not idCarac in self.caracs_:
            self.CreerCarac(idCarac, 0)

        finalVal = self.caracs_[idCarac] + valCarac
        if idCarac in self.valsMax_ and finalVal > self.valsMax_[idCarac]:
            finalVal = self.valsMax_[idCarac]
        self.SetCarac(idCarac, finalVal)

    def RetirerACarac(self, idCarac, valCarac):
        # si la carac n'existe pas encore, la créer
        if not idCarac in self.caracs_:
            self.CreerCarac(idCarac, 0)

        finalVal = self.caracs_[idCarac] - valCarac
        if idCarac in self.valsMin_ and finalVal < self.valsMin_[idCarac]:
            finalVal = self.valsMin_[idCarac]
        self.SetCarac(idCarac, finalVal)

    def GetValCarac(self, idCarac):
        if ( idCarac not in self.caracs_):
            return ""
        return self.caracs_[idCarac]

    def GetValCaracInt(self, idCarac):
        if ( idCarac not in self.caracs_):
            return 0
        return self.caracs_[idCarac]

    def DescriptionTraits(self, traits):
        """
        Description des traits
        """
        str = u""
        for traitK in traits.lTraits_.keys():
            trait = traits[traitK]
            descr = u"{}".format(trait.GetDescription(self))
            if descr != "":
                if str != "":
                    str = u"{}\n".format(str)
                str = u"{}{} ({})".format(str, descr, trait.eTrait_)
        return str

    def AffichageAge(self):
        nbJoursVecus = temps.Date(self.caracs_[temps.Date.DATE]).nbJours_ - temps.Date(self.caracs_[temps.Date.DATE_NAISSANCE]).nbJours_
        if isinstance(nbJoursVecus, int):
            nbAnnees = nbJoursVecus/365
            nbJoursPasses = nbJoursVecus%365
            nbMois = nbJoursPasses/30
            return "{} ans, {} mois".format(nbAnnees, nbMois)
        return "??? nbJoursVecus pas int : {}".format(nbJoursVecus)

    def AgeEnAnnees(self):
        if isinstance(self.caracs_[temps.Date.DATE_NAISSANCE], int):
            nbJoursVecus = temps.Date(self.caracs_[temps.Date.DATE]).nbJours_ - temps.Date(self.caracs_[temps.Date.DATE_NAISSANCE]).nbJours_
            nbAnnees = nbJoursVecus/365
            return nbAnnees
        return 0

    def AffichageDate(self):
        return temps.Date(self.caracs_[temps.Date.DATE])

    def TourSuivant(self):
        """
        Passage au "tour" suivant dans un destin extermis c'est à dire grosso modo à un mois un peu randomisé
        """
        nbJoursPasses = 20 + random.randint(0, 20)
        nouvelleDate = self.caracs_[temps.Date.DATE] + nbJoursPasses
        self.caracs_[temps.Date.DATE] = nouvelleDate
        self.caracs_[temps.Date.AGE_ANNEES] = self.AgeEnAnnees()

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        if len(self.caracs_) == 0:
            return u"Aucune carac."
        str = u"Situation actuelle : "
        for carac in self.caracs_.keys():
            str = "{} {} ({}), ".format(str, self.caracs_[carac], carac)
        return str

    def TesterDifficulte(self, idCarac, difficulte):
        """
        retourne True si le joueur réussit la tâche de difficulté demandée avec sa valeur en carac idCarac
        False sinon
        """
        return random.randint(1,100) <= self.CalculerPourcentageReussite(idCarac, difficulte)

    def TesterDegreReussite(self, idCarac, difficulte):
        """
        retourne un chiffre entre -5 et 5 qui est une note de réussite d'un test de difficulté demandée avec sa valeur en carac idCarac
        -4 échec catastrophique
        0 échec passable
        1 réussite médiocre
        5 réussite exceptionnelle
        """
        scorePourcent = random.randint(0,100)
        pourcentageReussi = self.CalculerPourcentageReussite(idCarac, difficulte)
        degreReussite = 1
        if scorePourcent <= pourcentageReussi:
            # réussite
            degreReussite = ( pourcentageReussi - scorePourcent )/20 + 1
        else:
            # échec
            degreReussite = ( pourcentageReussi - scorePourcent )/15

        return degreReussite

    def AffichagePourcentageReussite(self, idCarac, difficulte):
        affichageCarac = idCarac
        if isinstance(idCarac, list):
            affichageCarac = ""
            for carac in idCarac:
                affichageCarac = "{}, {}".format(affichageCarac, carac)
        return " ({}% en {})".format(self.CalculerPourcentageReussite(idCarac, difficulte), affichageCarac)

    def CalculerPourcentageReussite(self, idCarac, difficulte):
        """
        retourne le pourcentage de change que l'action réussisse étant donné  la valeur de la carac donnée chez le joueur
        et la difficulté de la tâche à accomplir

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
        valCarac = 0
        if isinstance(idCarac, list):
            for carac in idCarac:
                valCarac = valCarac + self.GetValCarac(carac)
            valCarac = valCarac / len(carac)
        else:
            valCarac = self.GetValCarac(idCarac)

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
        return diff[valCarac+20][difficulte-1]
