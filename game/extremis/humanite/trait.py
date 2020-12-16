

class CollectionTraits:

    def __init__(self):
        self.traits_ = dict()

    def __getitem__(self, traitStr):
        if traitStr not in self.traits_:
            self.traits_[traitStr] = Trait(traitStr)
        return self.traits_[traitStr]

    def __setitem__(self, traitStr, val):
        self.caracs_[traitStr] = val

class Trait:
    """
    ce qui a rapport aux traits descriptif d'un personnage
    Tous ces traits sont définis par des entiers.
    Souvent ils sont binaires par souci de simplification (0 oumoins signifie aps de trait, 1 ou plus signifie possède le trait)
    Certains ont des valeurs qui s'échelonnent de -20 à +16 mais sont encore utilisables en binaires comme ci dessus.
    Ils peuvent aussi bien être psychologiques que physiques.

    TODO : différencier ceux qui sont réellement évolutifs et les acquis à la naissance et presque impossible à gagner.
    """

    TOUS_LES_TRAITS = CollectionTraits()

    CUPIDE = "Cupide"

    def __init__(self, eTrait):
        self.eTrait_ = eTrait # enum Trait qui servira à identifier le trait pour lui affecter des caracs secondaires

    def GetTxt(self):
        switcher = {
            CUPIDE: "Cupide"
        }
        return switcher.get(self.eTrait_, "Ce trait n'a pas de string correspondante : {}".format(self.eTrait_))

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        return "{}".format(GetTxt(self))
