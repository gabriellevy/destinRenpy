from extremis.coteries import coterie

class Transhumanistes(coterie.Coterie):

    NOM = u"Transhumanistes"

    def __init__(self):
        self.nom_ = Transhumanistes.NOM

    def getLabelUniversite(self):
        return "univTranshumanistes"
