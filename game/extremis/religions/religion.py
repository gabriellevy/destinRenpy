import random

class Religion:

    # caracs liées :
    C_RELIGION = u"Religion" # carac à laquelle on applique le nom de la religion
    C_FOI = u"Foi" # niveau de foi dans sa religion (1 à 10)
    C_MIRACLE = u"Faiseur de miracles" # capacité à créer des miracles (1 à 10)

    # caracs de "voeux" religieux
    C_VOEU_CHASTETE = u"Voeu de chasteté"
    C_VOEU_PAUVRETE = u"Voeu de pauvreté" # sa richesse ne doit plus pouvoir bouger, elle est fixe

    def __init__(self):
       self.nom_ = "pas de nom de religion, doit être overridé"


class Christianisme(Religion):

    NOM = u"Christianisme"

    EVEQUE = u"Évèque"

    def __init__(self):
       self.nom_ = Christianisme.NOM

#  différent de pas de religion car l'athée a développé une aversion à la religion, il sera plus dur à reconvertir
class Atheisme(Religion):

    NOM = u"Athéisme"

    def __init__(self):
       self.nom_ = Atheisme.NOM
