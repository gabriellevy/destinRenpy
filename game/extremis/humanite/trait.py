

class Trait:
    """
    ce qui a rapport aux traits descriptif d'un personnage
    Tous ces traits sont définis par des entiers.
    Souvent ils sont binaires par souci de simplification (0 oumoins signifie aps de trait, 1 ou plus signifie possède le trait)
    Certains ont des valeurs qui s'échelonnent de -20 à +16 mais sont encore utilisables en binaires comme ci dessus.
    Ils peuvent aussi bien être psychologiques que physiques.

    TODO : différencier ceux qui sont réellement évolutifs et les acquis à la naissance et presque impossible à gagner.
    """

    def __init__(self, eTrait):
        self._eTrait = eTrait # enum Trait qui servira à identifier le trait pour lui affecter des caracs secondaires
