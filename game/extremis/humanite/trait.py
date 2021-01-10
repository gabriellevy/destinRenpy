import random

class Trait:
    """
    ce qui a rapport aux traits descriptif d'un personnage
    Tous ces traits sont définis par des entiers.
    Souvent ils sont binaires par souci de simplification (0 oumoins signifie pas de trait, 1 ou plus signifie possède le trait)
    Certains ont des valeurs qui s'échelonnent de -20 à +16 mais sont encore utilisables en binaires comme ci dessus.
    Ils peuvent aussi bien être psychologiques que physiques.

    TODO : différencier ceux qui sont réellement évolutifs et les acquis à la naissance et presque impossible à gagner.
    """

    SEUIL_A = 1 # valeur à partir de laquelle (et au dessus) on est considéré comme ayant le trait
    SEUIL_A_EXTREME = 11 # valeur à partir de laquelle (et au dessus) on est considéré comme ayant le trait à un niveau héroïque
    SEUIL_A_PAS = -3 # valeur à partir de laquelle (et en dessous) on est considéré comme ayant le trait en négatif
    SEUIL_A_PAS_EXTREME = -13 # valeur à partir de laquelle (et en dessous) on est considéré comme ayant le trait en très très négatif

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
        return "Valeur de description non trouvée pour : Trait : {}. Valeur : {}".format(self.eTrait_, val)


    def __repr__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        print("__repr__ de Trait")
        return "Trait : {}".format(self.eTrait_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        # print("__str__ de Trait")
        return "{}".format(self.eTrait_)

class TraitBinaire(Trait):

    NOM = u"TraitBinaire"

    def GetDescription(self, situation):
        """
        Mot décrivant le personnage dans ce trait particulier
        """
        return u"Description TraitBinaire" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode

class TraitTernaire(Trait):

    NOM = u"TraitTernaire"

    def GetDescription(self, situation):
        """
        Mot décrivant le personnage dans ce trait particulier
        """
        return u"Description TraitTernaire" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode

class TraitGraduel(Trait):

    NOM = u"TraitGraduel"

    def GetDescription(self, situation):
        """
        Mot décrivant le personnage dans ce trait particulier
        """
        return u"Description TraitGraduel" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode

class Cupidite(TraitTernaire):

    NOM = u"Cupidité"

    def __init__(self):
        self.eTrait_ = Cupidite.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            return u"Prodigue"
        elif val >= Trait.SEUIL_A:
            return u"Cupide" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode
        else:
            return u""

class Franchise(TraitTernaire):

    NOM = u"Franchise"

    def __init__(self):
        self.eTrait_ = Franchise.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            return u"Sournois"
        elif val >= Trait.SEUIL_A:
            return u"Franc" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode
        else:
            return u""

# simple, // pas forcément idiot mais a peu tendace à utiliser son intelligence de manière abstraite : plutôt terre à terre
# intellectuel, // intelligent à priori mais a surtout tendance à intellectualiser tout, à conceptualiser, à aimer l'abstrait et la discussion
class Intellectualisme(TraitTernaire):

    NOM = u"Intellectualisme"

    def __init__(self):
        self.eTrait_ = Intellectualisme.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            return u"Simple"
        elif val >= Trait.SEUIL_A:
            return u"Intellectuel" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode
        else:
            return u""

class Pragmatisme(TraitTernaire):

    NOM = u"Pragmatisme"

    def __init__(self):
        self.eTrait_ = Pragmatisme.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            return u"Idéaliste"
        elif val >= Trait.SEUIL_A:
            return u"Pragmatique" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode
        else:
            return u""

class Prudence(TraitTernaire):

    NOM = u"Prudence"

    def __init__(self):
        self.eTrait_ = Prudence.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            return u"Aventureux"
        elif val >= Trait.SEUIL_A:
            return u"Prudent" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode
        else:
            return u""


class Opportunisme(TraitBinaire):

    NOM = u"Opportunisme"

    def __init__(self):
        self.eTrait_ = Opportunisme.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val >= Trait.SEUIL_A:
            return u"Opportuniste"
        else:
            return ""

# prends très au sérieux sa réputation, ne ment jamais, respecte ses pairs et sa famille...
# inclut aussi la sincérité vs l'hypocrisie etc
class Sincerite(TraitGraduel):

    NOM = u"Sincérité"

    def __init__(self):
        self.eTrait_ = Sincerite.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Mythomane"
            return u"Menteur"
        elif val >= Trait.SEUIL_A:
            return u"Sincère"
        else:
            return ""

class Intelligence(TraitGraduel):

    NOM = u"Intelligence"

    def __init__(self):
        self.eTrait_ = Intelligence.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Stupide"
            return u"Bête"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Très intelligent"
            return u"Intelligent"
        else:
            return ""

class Altruisme(TraitGraduel):

    NOM = u"Altruisme"

    def __init__(self):
        self.eTrait_ = Altruisme.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Cruel"
            return u"Méchant"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Altruiste"
            return u"Gentil"
        else:
            return ""


# industrieux == travailleur, aime produire...
class Industrie(TraitGraduel):

    NOM = u"Industrie"

    def __init__(self):
        self.eTrait_ = Industrie.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            return u"Paresseux"
        elif val >= Trait.SEUIL_A:
            return u"Industrieux"
        else:
            return ""

class Sensibilite(TraitGraduel):

    NOM = u"Sensibilité"

    def __init__(self):
        self.eTrait_ = Sensibilite.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Indifférent"
            return u"Insensible"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Ultrasensible"
            return u"Sensible"
        else:
            return ""


class Violence(TraitGraduel):

    NOM = u"Violence"

    def __init__(self):
        self.eTrait_ = Violence.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Pacifique"
            return u"Doux"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Ultraviolent"
            return u"Violent"
        else:
            return ""

class Ascetisme(TraitGraduel):

    NOM = u"Ascétisme"

    def __init__(self):
        self.eTrait_ = Ascetisme.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Sybarite"
            return u"Jouisseur"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Ascète"
            return u"Abstinent"
        else:
            return ""

class Rancune(TraitGraduel):

    NOM = u"Rancune"

    def __init__(self):
        self.eTrait_ = Rancune.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Magnanime"
            return u"Oublieux"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Magnanime"
            return u"Rancunier"
        else:
            return ""

class Ambition(TraitGraduel):

    NOM = u"Ambition"

    def __init__(self):
        self.eTrait_ = Ambition.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            return u"Désintéressé"
        elif val >= Trait.SEUIL_A:
            return u"Ambitieux"
        else:
            return ""


class CollectionTraits:

    def __init__(self):
        self.lTraits_ = dict()
        cupidite = Cupidite()
        self.SetTrait(Cupidite.NOM, cupidite)
        honorabilite = Sincerite()
        self.SetTrait(Sincerite.NOM, honorabilite)
        opp = Opportunisme()
        self.SetTrait(Opportunisme.NOM, opp)
        ind = Industrie()
        self.SetTrait(Industrie.NOM, ind)
        franch = Franchise()
        self.SetTrait(Franchise.NOM, franch)
        violence = Violence()
        self.SetTrait(Violence.NOM, violence)
        prag = Pragmatisme()
        self.SetTrait(Pragmatisme.NOM, prag)
        intel = Intellectualisme()
        self.SetTrait(Intellectualisme.NOM, intel)
        intelligence = Intelligence()
        self.SetTrait(Intelligence.NOM, intelligence)
        sensi = Sensibilite()
        self.SetTrait(Sensibilite.NOM, sensi)
        ascetisme = Ascetisme()
        self.SetTrait(Ascetisme.NOM, ascetisme)
        ambition = Ambition()
        self.SetTrait(Ambition.NOM, ambition)
        prud = Prudence()
        self.SetTrait(Prudence.NOM, prud)
        altruisme = Altruisme()
        self.SetTrait(Altruisme.NOM, altruisme)
        rancune = Rancune()
        self.SetTrait(Rancune.NOM, rancune)

    def getTraitAleatoire(self):
        return random.choice(list(self.lTraits_.values()))

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

    def __len__(self):
        return len(self.lTraits_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        if len(self.lTraits_) == 0:
            return "Aucun trait."
        str = u"Liste de tous les traits : "
        for trait in self.lTraits_:
            str = str + trait + ","
        return str
