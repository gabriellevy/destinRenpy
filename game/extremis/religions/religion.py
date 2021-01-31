import random

class Religion:

    # caracs liées :
    C_RELIGION = "Religion" # carac à laquelle on applique le nom de la religion
    C_FOI = "Foi" # niveau de foi dans sa religion (1 à 10)
    C_MIRACLE = "Faiseur de miracles" # capacité à créer des miracles (1 à 10)

    def __init__(self):
       self.nom_ = "pas de nom de religion, doit être overridé"


class Christianisme(Religion):

    NOM = u"Christianisme"

    def __init__(self):
       self.nom_ = Christianisme.NOM

#  différent de pas de religion car l'athée a développé une aversion à la religion, il sera plus dur à reconvertir
class Atheisme(Religion):

    NOM = u"Athéisme"

    def __init__(self):
       self.nom_ = Atheisme.NOM
