
class Theme:

    def __init__(self):
        self.themes_ = dict() # dictionnaire contenant toutes les caracs courantes de la partie

    def __getitem__(self, key):
        if key not in self.themes_:
            self.themes_[key] = ""
        return self.themes_[key]

    def __setitem__(self, key, val):
        self.themes_[key] = val

class FiltreAction:
    """
    Filtres des Actions qui seront proposées au joueur durant la partie.
    Ils peuvent être réglés par le joueur pour que certains événements soient proposés alors qu'ils ne seraient pas en temps normal.
    Ils ont aussi pour effet de faire arriver certains événements plus souvent si leurs thèmes correspondants ont été sélectionnés
    """

    # liste des filtres disponibles :
    RECOLTE_PREPARATION = "Récolte et préparation" # artisanat, alchimie, cuisisine etc...
    VOL = "Vol"
    ANIMAUX = "Animaux" #approvoisement etc..."
    MAGIE = "Magie"
    ART = "Art"
    DESTRUCTION = "Destruction" # Actions vraiment nihiliste gratuites
    VIOLENCE = "Violence"
    AMOUR = "Amour"

    def __init__(self):
        self.themes_ = Theme()
        self.themes_[FiltreAction.VOL] = 1
        self.themes_[FiltreAction.AMOUR] = 1