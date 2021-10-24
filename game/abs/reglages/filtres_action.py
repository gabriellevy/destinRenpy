
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
    Filtres de préférences du joueur qui s'appliquent aux Actions qui seront proposées durant la partie.

    Ils peuvent être réglés par le joueur pour que certains événements soient proposés alors qu'ils ne seraient pas en temps normal.
    Ils ont aussi pour effet de faire arriver certains événements plus souvent si leurs thèmes correspondants ont été sélectionnés.

    A FAIRE : à terme il devrait y avoir une interface affichée au joueur au lancement de la partie pour lui permettre de choisir ces filtres pour personnaliser sa partie
    """

    # liste des thèmes disponibles :
    RECOLTE_PREPARATION = "Récolte et préparation" # artisanat, alchimie, cuisisine etc...
    VOL = "Vol"
    ANIMAUX = "Animaux" #approvoisement etc..."
    MAGIE = "Magie"
    ART = "Art"
    DESTRUCTION = "Destruction" # Actions vraiment nihiliste gratuites
    VIOLENCE = "Violence"
    AMOUR = "Amour"
    # Importance des choix affichés (valeurs applicables à self.importanceChoix_)
    TOUS_LES_CHOIX = 0 # cette option affiche tous les choix même les plus insignifiants comme quels vêtements porter
    CHOIX_IMPORTANTS = 1 # choix qui ont de fortes chances d'avoir des effets long termes
    CHOIX_PRIMORDIAUX = 2 # choix qui auront sans le moindre doute des effets long terme (mariage, études, carrière...)
    AUCUN_CHOIX = 3 # aucun choix n'est proposé
    # Complexité des choix acceptés (valeurs applicables à self.complexiteChoix_)
    # à suppose que le choix passe le filtre "importance" ci dessus il faut encore qu'il soit d'une complexité acceptée par le joueur:
    CHOIX_SIMPLES = 0 # n'accepte que les choix "unique" avec un seul choix puis un redémarrage "automatique" de l'aventure
    MINI_HISTOIRES = 1 # accepte les sections d'histoires impliquant plusieurs choix menant au maximum à une petite histoire de 30 minutes
    AVENTURES = 2 # accepte les éventuelles aventures très longues (des heures) qui pourraient se trouver dans la partie (il n'y en a aucun pour l'instant)


    def __init__(self):
        self.themes_ = Theme()
        self.themes_[FiltreAction.VOL] = 1
        self.themes_[FiltreAction.AMOUR] = 1
        self.importanceChoix_ = FiltreAction.CHOIX_IMPORTANTS
        self.complexiteChoix_ = FiltreAction.AVENTURES
