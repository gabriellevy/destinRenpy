import random

class Coterie:
    """
    classe de base de toutes les coteries
    """

    NB_UNIV = "Nombre d'universités terminées" # nombre d'universités de coteries terminées
    NB_MOIS_UNIV_A_FAIRE = "Nombre de mois à faire dans l'université actuelle"

    def __init__(self):
        self.nom_ = "pas de nom, à overrider" # enum Trait qui servira à identifier le trait pour lui affecter des caracs secondaires

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

    def Compatibilite(self, situation, aleatoire):
        proba = 0.5
        """
        plus le personnage est compatible avec la coterie, plus le résultat est élevé
        ---
        if ( aleatoire)
            proba = Aleatoire::GetAl()->Entre0Et1();

        for ( shared_ptr<Condition> cond : this->m_TraitsCompatible) {
            if ( cond->Tester()) {
                proba += 0.2;
            }
        }
        for ( shared_ptr<Condition> cond : this->m_TraitsIncompatible) {
            if ( cond->Tester()) {
                proba -= 0.2;
            }
        }
        for (QString idMetier: this->m_MetiersAssocies) {
            if ( hum->GetValeurCarac(Coterie::C_COTERIE) == idMetier) {
                proba += 0.3;
            }
        }

        // baisse de compatibilité si déjà dans une coterie :
        if ( hum->GetValeurCarac(Coterie::C_COTERIE) != "")
           proba -= 0.1;
        """
        return proba

    def GetMusique(self):
        return ""

    def getLabelUniversite(self):
        return "à overrider avec le label de l'université de la coterie"

    def RejoindreCoterie(self, situation):
        """
        hum->SetValeurACaracId(Coterie::C_COTERIE, GetId());
        QString nom = this->CreerPatronyme();
        hum->MajNom(nom);
        eff->m_Texte += "\nVous rejoignez la coterie : " + GetNom() + ". Vous vous appelez maintenant " + nom + ".";
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
        return True

    def Initialisation(self):
        """
        GenererTraitCompatibles();
        m_Quartier = this->GenererQuartier();
        """
        return True
