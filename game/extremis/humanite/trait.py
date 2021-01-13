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

    def PeutEtrePrisALaNaissance(self):
        """
        Renvoie true si il s'agit d'un trait qui peut être choisi dès la crréation du personnage
        Renvoie false si c'est un trait uniquement 'acquis'
        """
        return True

    def GetValeurALaNaissance(self):
        """
        Doit être overridée
        """
        return -99999

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

    def GetValeurALaNaissance(self):
        return 1

class TraitTernaire(Trait):

    NOM = u"TraitTernaire"

    def GetDescription(self, situation):
        """
        Mot décrivant le personnage dans ce trait particulier
        """
        return u"Description TraitTernaire" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode

    def GetValeurALaNaissance(self):
        """
        50% de chance en négatif, 50% de chance en positif
        """
        if random.randint(0,1) == 0:
            return Trait.SEUIL_A_PAS
        else:
            return Trait.SEUIL_A

class TraitGraduel(Trait):

    NOM = u"TraitGraduel"

    def GetDescription(self, situation):
        """
        Mot décrivant le personnage dans ce trait particulier
        """
        return u"Description TraitGraduel" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode

    def GetValeurALaNaissance(self):
        """
        50% de chance en négatif, 50% de chance en positif
        """
        val = random.randint(0,100)
        if val <= 15:
            return Trait.SEUIL_A_PAS_EXTREME
        elif val <= 35:
            return Trait.SEUIL_A_PAS
        elif val <= 85:
            return Trait.SEUIL_A
        else:
            return Trait.SEUIL_A_EXTREME

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

class Patriarcat(TraitTernaire):

    NOM = u"Rapport entre les sexes"

    def __init__(self):
        self.eTrait_ = Patriarcat.NOM

    def PeutEtrePrisALaNaissance(self):
        return False

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            return u"Matriarcal"
        elif val >= Trait.SEUIL_A:
            return u"Patriarcal" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode
        else:
            return u""

class Serenite(TraitTernaire):

    NOM = u"Sérénité"

    def __init__(self):
        self.eTrait_ = Serenite.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            return u"Angoissé"
        elif val >= Trait.SEUIL_A:
            return u"Serein" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode
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

class Observation(TraitTernaire):

    NOM = u"Sens de l'observation"

    def __init__(self):
        self.eTrait_ = Observation.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            return u"Distrait"
        elif val >= Trait.SEUIL_A:
            return u"Observateur" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode
        else:
            return u""

class Spiritualite(TraitTernaire):

    NOM = u"Spiritualité"

    def __init__(self):
        self.eTrait_ = Spiritualite.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            return u"Matérialiste"
        elif val >= Trait.SEUIL_A:
            return u"Spirituel" # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode
        else:
            return u""

class Nature(TraitTernaire):

    NOM = u"Nature"

    def __init__(self):
        self.eTrait_ = Nature.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            return u"Antinaturaliste "
        elif val >= Trait.SEUIL_A:
            return u"Naturophile " # ATTENTION ACCENTS : mettre 'u' devant les string à accents pour utiliser le mode unicode
        else:
            return u""

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
            return u"Égoïste"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Altruiste"
            return u"Désintéressé"
        else:
            return ""

# Est-ce que le personnage est indivisualiste ou est-ce qu'il aime agir en groupe
# estt-ce qu'il est prêt à se sacrifier pour les autres ?..
class Individualisme(TraitGraduel):

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
                return u"Sens du sacrifice"
            return u"Collectisme"
        elif val >= Trait.SEUIL_A:
            return u"Individualisme"
        else:
            return ""

class Sexualite(TraitGraduel):

    NOM = u"Sexualité"

    def __init__(self):
        self.eTrait_ = Sexualite.NOM

    def PeutEtrePrisALaNaissance(self):
        """
        Renvoie true si il s'agit d'un trait qui peut être choisi dès la crréation du personnage
        Renvoie false si c'est un trait uniquement 'acquis'
        """
        return False

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Abstinent"
            return u"Indifférent"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Pervers"
            return u"Obsédé"
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

class Force(TraitGraduel):

    NOM = u"Force"

    def __init__(self):
        self.eTrait_ = Force.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Anémique"
            return u"Faible"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Herculéen"
            return u"Fort"
        else:
            return ""

class Resistance(TraitGraduel):

    NOM = u"Résistance"

    def __init__(self):
        self.eTrait_ = Resistance.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Chétif"
            return u"Fragile"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Indestructible"
            return u"Résistant"
        else:
            return ""

class Poids(TraitGraduel):

    NOM = u"Poids"

    def __init__(self):
        self.eTrait_ = Poids.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Obèse"
            return u"Gros"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Famélique"
            return u"Maigre"
        else:
            return ""

class Taille(TraitGraduel):

    NOM = u"Taille"

    def __init__(self):
        self.eTrait_ = Taille.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Nain"
            return u"Petit"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Géant"
            return u"Grand"
        else:
            return ""

class Beaute(TraitGraduel):

    NOM = u"Beauté"

    def __init__(self):
        self.eTrait_ = Beaute.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Hideux"
            return u"Laid"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Apollon"
            return u"Beau"
        else:
            return ""

class Habilete(TraitGraduel):

    NOM = u"Habileté"

    def __init__(self):
        self.eTrait_ = Habilete.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Très Maladroit"
            return u"Maladroit"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Très Habile"
            return u"Habile"
        else:
            return ""

class Charme(TraitGraduel):

    NOM = u"Charme"

    def __init__(self):
        self.eTrait_ = Charme.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Très Déplaisant"
            return u"Déplaisant"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Très Charmant"
            return u"Charmant"
        else:
            return ""

class Artiste(TraitGraduel):

    NOM = u"Artiste"

    def __init__(self):
        self.eTrait_ = Artiste.NOM

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            # if val <= Trait.SEUIL_A_PAS_EXTREME:
            #    return u"Très Déplaisant"
            return u"Vulgaire"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Grand Artiste"
            return u"Artiste"
        else:
            return ""

class Pilotage(TraitGraduel):

    NOM = u"Pilotage"

    def __init__(self):
        self.eTrait_ = Pilotage.NOM

    def PeutEtrePrisALaNaissance(self):
        return False

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            # if val <= Trait.SEUIL_A_PAS_EXTREME:
            #    return u"Très Déplaisant"
            return u"Ne sais pas conduire"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Pilote de course"
            return u"A son permis"
        else:
            return ""

class Richesse(TraitGraduel):

    NOM = u"Richesse"

    def __init__(self):
        self.eTrait_ = Richesse.NOM

    def PeutEtrePrisALaNaissance(self):
        return True

    def GetDescription(self, situation):
        val = situation[self.eTrait_]
        if val == "":
            val = 0
            situation[self.eTrait_] = val
        if not isinstance(val, int):
            assert "Ce trait n'a pas comme valeur un int. Trait : {}. Valeur : {}".format(self.eTrait_, val)

        if val <= Trait.SEUIL_A_PAS:
            if val <= Trait.SEUIL_A_PAS_EXTREME:
                return u"Misérable"
            return u"Pauvre"
        elif val >= Trait.SEUIL_A:
            if val >= Trait.SEUIL_A_EXTREME:
                return u"Richissime"
            return u"Aisé"
        else:
            return ""

class CollectionTraits:

    def __init__(self):
        self.lTraits_ = dict()
        richesse = Richesse()
        self.SetTrait(Richesse.NOM, richesse)
        pilotage = Pilotage()
        self.SetTrait(Pilotage.NOM, pilotage)
        artiste = Artiste()
        self.SetTrait(Artiste.NOM, artiste)
        spiritualite = Spiritualite()
        self.SetTrait(Spiritualite.NOM, spiritualite)
        charme = Charme()
        self.SetTrait(Charme.NOM, charme)
        observation = Observation()
        self.SetTrait(Observation.NOM, observation)
        habilete = Habilete()
        self.SetTrait(Habilete.NOM, habilete)
        beaute = Beaute()
        self.SetTrait(Beaute.NOM, beaute)
        taille = Taille()
        self.SetTrait(Taille.NOM, taille)
        poids = Poids()
        self.SetTrait(Poids.NOM, poids)
        resistance = Resistance()
        self.SetTrait(Resistance.NOM, resistance)
        force = Force()
        self.SetTrait(Force.NOM, force)
        patriarcat = Patriarcat()
        self.SetTrait(Patriarcat.NOM, patriarcat)
        sexualite = Sexualite()
        self.SetTrait(Sexualite.NOM, sexualite)
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
        serenite = Serenite()
        self.SetTrait(Serenite.NOM, serenite)

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
