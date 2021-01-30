from extremis.coteries import coterie

class Elfes(coterie.Coterie):

    NOM = u"Elfes"

    def __init__(self):
        self.nom_ = Elfes.NOM

    def getLabelUniversite(self):
        return "univElfes"
