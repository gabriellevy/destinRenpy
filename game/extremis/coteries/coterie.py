import random
from extremis.humanite import identite

class Coterie:
    """
    classe de base de toutes les coteries
    """

    C_COTERIE = "Coterie"

    # UNIVERSITE
    Carac_NB_UNIV = "Nombre d'universités terminées" # nombre d'universités de coteries terminées
    NB_UNIV_TOTAL = 3 #nombre total d'université que doit suivre un personnage

    Carac_NB_MOIS_UNIV_A_FAIRE = "Nombre de mois à faire dans l'université actuelle"
    NB_MOIS_UNIV_TOTAL_A_FAIRE = 6 # nombre de "modules" obligatoires à suivre quand on rejoint une université de coterie

    Carac_UNIV_COURANTE = "Université actuelle"

    def __init__(self):
        self.nom_ = "pas de nom, à overrider"
        self.id_ = "pas de id, à overrider"

    def __repr__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        return "Coterie : {}".format(self.nom_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        return "{}".format(self.nom_)

    def GenererQuartier(self):
        """
        retourne l'objet Quartier qui est le quartier principal de la coterie
        """
        # return m_Quartier
        return ""

    def GetGentile(self, masculin):
        if masculin:
            return "pas de gentilé masculin, à overrider !"
        else:
            return "pas de gentilé féminin, à overrider !"

    def GetPoidsDemo(self):
        """
        à quel point cette coterie est nombreuse dans la population
        1.0 = normal
        0.1 = 10 fois moins que la moyenne
        """
        return 1.0

    def GetTraitsCompatibles(self):
        """
        si le perso a ces caracs il a plus de chances de vouloir rejoindre cette coterie
        """
        return "doit être overridée"

    def GetMetiersCompatibles(self):
        """
        si le perso a des compétences dans ces métiers il a plus de chances de vouloir rejoindre cette coterie où ils sont souvent pratiqués
        """
        return "GetMetiersCompatibles doit être overridée"

    def GetTraitsIncompatibles(self):
        """
        si le perso a ces caracs il a plus de chances de ne pas vouloir rejoindre cette coterie
        """
        return "doit être overridée"


    def CalculerAffinite(self, situation, aleatoire = False):
        affinite = 0.5
        """
        plus le personnage est compatible avec la coterie, plus le résultat est élevé
        """
        #if ( aleatoire)
        #    proba = Aleatoire::GetAl()->Entre0Et1();

        # un score d'affinité est calculé selon les traits compatibles ou incompatibles du personnage avec la coterie
        CaracsCompatibles = self.GetTraitsCompatibles()
        CaracsInCompatibles = self.GetTraitsIncompatibles()
        # les deux coeffs suivants servent à rééquilibrer le score final en donnant plus de valeurs aux côté qui contient le moins de traits
        coeffCompatibles = len(CaracsInCompatibles)
        coeffIncompatibles = len(CaracsCompatibles)
        affinite = 0

        for idCarac in CaracsCompatibles:
            if situation[idCarac] != "":
                val = situation.GetValCaracInt(idCarac)
                bonus = 1
                if val > 5:
                    bonus = 2
                    if val > 10:
                        bonus = 3
                elif val < 0:
                    bonus = -1
                    if val < -5:
                        bonus = -2
                        if val < -10:
                            bonus = -3
                affinite = affinite + bonus * coeffCompatibles

        for idCarac in CaracsInCompatibles:
            if situation[idCarac] != "":
                val = situation.GetValCaracInt(idCarac)
                bonus = 1
                if val > 5:
                    bonus = 2
                    if val > 10:
                        bonus = 3
                elif val < 0:
                    bonus = -1
                    if val < -5:
                        bonus = -2
                        if val < -10:
                            bonus = -3
                affinite = affinite - bonus * coeffIncompatibles

        # bonus pour les métiers liés
        metiersCompatibles = self.GetMetiersCompatibles()
        for idMetier in metiersCompatibles:
            if situation[idMetier] != "":
                val = situation.GetValCaracInt(idCarac)
                affinite = affinite + val

        # petit malus de rééquilibrage au cas où il y abeaucoup de métiers liés :
        valEquilibre = len(metiersCompatibles)%3
        affinite = affinite - valEquilibre


        # baisse de compatibilité si déjà dans une coterie :
        #if ( hum->GetValeurCarac(Coterie::C_COTERIE) != "")
        #   proba -= 0.1;

        print (u"Coterie {} affinité {}".format(self.nom_, affinite))

        return affinite

    def GenererPortraits(self, age, masculin, metier, portraits):
        """
        ajoute des portraits correspondants aux caracs en paramtre (et à la coterie courante)
        A OVERRIDER
        """
        return portraits

    def GetMusique(self):
        return ""

    def getLabelUniversite(self):
        return "à overrider avec le label de l'université de la coterie"

    def RejoindreCoterie(self, situation):
        """
        QString musique = GetMusique();
        if ( musique != "") {
            eff->m_Son = musique;
        }
        // déménagement dans le quartier de la coterie ?
        if ( hum->EstLibre()) {
            double proba = Aleatoire::GetAl()->Entre0Et1();
            if ( proba >= 0.3) {
                eff->m_Texte += "\nVous décidez de déménager dans " + m_Quartier->m_Nom + ", le quartier de votre nouvelle coterie.";
                hum->SetValeurACaracId(QuartierEffets::C_QUARTIER_HABITE,
                                                           m_Quartier->m_Nom);
                hum->SetValeurACaracId(QuartierEffets::C_QUARTIER_ACTUEL,
                                                           m_Quartier->m_Nom);
                hum->SetValeurACaracId(EconomieEvt::C_NIVEAU_ECONOMIQUE,
                     hum->GetValeurCaracAsInt(EconomieEvt::C_NIVEAU_ECONOMIQUE) - 1);
            }
        }
        """
        situation[Coterie.C_COTERIE] = self.id_
        situation[identite.Identite.C_PRENOM] = self.CreerPrenom(True)
        situation[identite.Identite.C_NOM] = self.CreerNom(True)

        return True

    def CreerNom(self, masculin):
        """
        génère un patronyme correspondant à la coterie en question
        """
        return "pas de nom ! à overrider!"

    def CreerPrenom(self, masculin):
        """
        génère un patronyme correspondant à la coterie en question
        """
        return "pas de prénom ! à overrider!"

    def Initialisation(self):
        """
        GenererTraitCompatibles();
        m_Quartier = this->GenererQuartier();
        """
        return True
