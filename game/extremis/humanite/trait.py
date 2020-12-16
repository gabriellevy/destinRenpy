

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

    CUPIDE = u"Cupide"

    def __init__(self, eTrait):
        # print("__init__ de Trait")
        self.eTrait_ = eTrait # enum Trait qui servira à identifier le trait pour lui affecter des caracs secondaires
        # print("fin de __init__ de Trait")

    def GetTxt(self):
        """
        Mot définissant le trait lui-même (pas le personnage qui l'a)
        """
        # print("GetTxt de Trait")
        switcher = {
            Trait.CUPIDE: "Cupide"
        }
        # print("eTrait : {}".format(self.eTrait_))
        return switcher.get(self.eTrait_, "Ce trait n'a pas de string correspondante : {}".format(self.eTrait_))

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
            if val < -3:
                return "Prodigue"
            elif val > 0:
                return "Cupide"
            else:
                return u"Équilibré" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode

        return "Valeur de description non trouvée pour : Trait : {}. Valeur : {}".format(self.eTrait_, val)


    def __repr__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        print("__repr__ de Trait")
        return "Trait : {}".format(self.GetTxt())

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        # print("__str__ de Trait")
        return "{}".format(self.GetTxt())
