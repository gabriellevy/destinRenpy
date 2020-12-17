

class CollectionTraits:

    def __init__(self):
        self.lTraits_ = dict()

    def __getitem__(self, idTrait):
        if not idTrait in self.lTraits_:
            self.CreerTrait(idTrait)
        return self.lTraits_[idTrait]

    def __setitem__(self, idTrait, trait):
        self.SetTrait(idTrait, trait)

    def SetTrait(self, idTrait, trait):
        # si la carac n'existe pas encore, la créer
        if not idTrait in self.lTraits_:
            self.CreerTrait(idTrait)

        self.lTraits_[idTrait] = trait

    def CreerTrait(self, idTrait):
        trait = Trait(idTrait)
        self.lTraits_[idTrait] = trait

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        if len(self.lTraits_) == 0:
            return "Aucun trait."
        str = "Liste de tous les traits : "
        for trait in self.lTraits_:
            str = str + trait + ","
        return str

class Trait:
    """
    ce qui a rapport aux traits descriptif d'un personnage
    Tous ces traits sont définis par des entiers.
    Souvent ils sont binaires par souci de simplification (0 oumoins signifie aps de trait, 1 ou plus signifie possède le trait)
    Certains ont des valeurs qui s'échelonnent de -20 à +16 mais sont encore utilisables en binaires comme ci dessus.
    Ils peuvent aussi bien être psychologiques que physiques.

    TODO : différencier ceux qui sont réellement évolutifs et les acquis à la naissance et presque impossible à gagner.
    """

    SEUIL_A = 1 # valeur à partir de laquelle (et au dessus) on est considéré comme ayant le trait
    SEUIL_A_EXTREME = 11 # valeur à partir de laquelle (et au dessus) on est considéré comme ayant le trait à un niveau héroïque
    SEUIL_A_PAS = -3 # valeur à partir de laquelle (et en dessous) on est considéré comme ayant le trait en négatif
    SEUIL_A_PAS_EXTREME = -13 # valeur à partir de laquelle (et en dessous) on est considéré comme ayant le trait en très très négatif

    CUPIDE = u"Cupidité"
    HONORABILITE = u"Honorabilité" # prends très au sérieux sa réputation, ne ment jamais, respecte ses pairs et sa famille...

    def __init__(self, eTrait):
        self.eTrait_ = eTrait # enum Trait qui servira à identifier le trait pour lui affecter des caracs secondaires

    def GetDescription(self, situation):
        """
        Mot décrivant le personnage dans ce trait particulier
        """
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if self.eTrait_ == Trait.CUPIDE:
            if val <= Trait.SEUIL_A_PAS:
                return u"Prodigue"
            elif val >= Trait.SEUIL_A:
                return u"Cupide"
            else:
                return u"Équilibré" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode
        elif self.eTrait_ == Trait.HONORABILITE:
            if val <= Trait.SEUIL_A_PAS:
                if val <= Trait.SEUIL_A_PAS_EXTREME:
                    return u"Mythomane"
                return u"Menteur"
            elif val >= Trait.SEUIL_A:
                return u"Honorable"
            else:
                return u"Équilibré"

        return "Valeur de description non trouvée pour : Trait : {}. Valeur : {}".format(self.eTrait_, val)


    def __repr__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        print("__repr__ de Trait")
        return "Trait : {}".format(self.eTrait_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        # print("__str__ de Trait")
        return "{}".format(self.eTrait_)
