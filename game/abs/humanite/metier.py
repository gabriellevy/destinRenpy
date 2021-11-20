import random
from abs.humanite import trait

class Metier:
    """
    Classe contenant les fonctions statiques de base liées à tous les métiers
    Comme le métier en tant que carac n'est qu'une String il faut appeler ces fonctions pour avoir les valeurs liées au métier comme par exemple :
     - le salaire
     - si il est de bureau
     - si il est dangereux
     - etc
    """

    C_METIER = u"Métier"
    C_COMPETENCE_METIER  = u"Compétence Métier"
    C_TITRE = u"Titre"

    # types de métiers
    ADMINISTRATIF = u"MétierAdministratif"

    def __init__(self):
        """
         le membre 'nom_' sert à la fois :
         -  d'identifiant du métier en étant la valeur de la carac 'C_METIER'
         - de niveau de compétence dans ce métier en étant l'identifiant d'une carac chiffré correspondant à ce niveau
         """
        self.nom_ = "pas de nom de métier, doit être overridé"

    def __repr__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        return "Métier : {}".format(self.nom_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        return "{}".format(self.nom_)

    def estDeBureau(self, strMetier):
        """
        renvoie true si le métier en question se passe essentiellement dans un bureau
        """
        return False

    def regenererCaracsMetier(self, situation):
        if not aUnMetier(situation):
            # pas de métier
            return
        nomMetier = situation[Metier.C_METIER]
        situation[Metier.C_COMPETENCE_METIER] = situation[nomMetier]
        if self.estDeBureau(nomMetier):
            situation[Metier.ADMINISTRATIF] = 1
        else:
            situation[Metier.ADMINISTRATIF] = ""

    def GetNiveauRichesse(self):
        """
        niveau de richesse associé à ce métier, 0 étant la classe moyenne
        Va de
        -5 : fouilleur de poubelles
        à
        +5 : PDG de multinationale
        à overrider quand émtier non moyen
        """
        return 0

    def Rejoindre(self, situation):
        """
        effet quand le joueur fait de ce métier son métier principal (suclassable si nécessaire)
        """
        # changement de la richesse selon métier d'avant et le nouveau
        ancienMetier = situation.GetMetier()
        if ancienMetier is not None:
            situation.RetirerACarac(trait.Richesse.NOM, ancienMetier.GetNiveauRichesse())

        situation.SetValCarac(Metier.C_METIER, self.nom_)
        nouveauMetier = situation.GetMetier()
        situation.AjouterACarac(trait.Richesse.NOM, nouveauMetier.GetNiveauRichesse())

        self.regenererCaracsMetier(situation)


    def GenererPortraits(self, age, masculin, portraits, valeursTraits):
        """
        ajoute des portraits correspondants aux caracs en parametre
        A OVERRIDER
        """
        return portraits

    def GetPoidsDemo(self, masculin, coterieObj):
        """
        à quel point ce métier est pratiqué par une grande partie de la population
        1.0 = normal (employé de bureau, enseignant...)
        0.1 = 10 fois moins que la moyenne (Musicien,
        0.01 = très rare (généticien, roboticien)
        """
        poids = 1.0
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

    def GetDiscipline(self):
        """
        renvoie le nom de la discipline principale liée à ce métier
        à surclasser
        """
        return u""

    def GetTexteCompetence(self, niveauComp):
        """
        renvoie le niveau de compétence dans ce métier du perso rapport à la valeur en paramètre
        éventuellement surclassable pour être plus précis
        """
        txtCompetence = u"Notions"
        if niveauComp > 1:
            txtCompetence = u"Apprenti"
            if niveauComp > 3:
                txtCompetence = u"Expérimenté"
                if niveauComp > 5:
                    txtCompetence = u"Élite"
                    if niveauComp > 8:
                        txtCompetence = u"Maître"
        return txtCompetence

class Paysan(Metier):
    NOM = u"Paysan"
    def __init__(self):
        self.nom_ = Paysan.NOM

    def GetDiscipline(self):
        return u"Agriculture"

    def GenererPortraits(self, age, masculin, portraits, valeursTraits):
        """
        ajoute des portraits correspondants aux caracs en parametre
        """
        if masculin:
            if age >= 60:
                portraits.append("images/metiers/paysan/portraits/paysan60+.jpg")
        else:
            if age >= 15:
                if age >= 60:
                    portraits.append("images/metiers/paysan/portraits/femme60+.jpg")
                if age <= 30:
                        portraits.append("images/metiers/paysan/portraits/femme15_30.jpg")
                        portraits.append("images/metiers/paysan/portraits/femme15_30_b.jpg")
                # >= 15
                if age >= 20:
                    if age <= 50:
                        portraits.append("images/metiers/paysan/portraits/femme20_50.jpg")
                        portraits.append("images/metiers/paysan/portraits/femme20_50_b.jpg")
                        portraits.append("images/metiers/paysan/portraits/femme20_50_c.jpg")

        return portraits

class Robotique(Metier):
    NOM = u"Roboticien"
    def __init__(self):
        self.nom_ = Robotique.NOM

    def GetNiveauRichesse(self):
        return 4

    def GetDiscipline(self):
        return u"Robotique"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.01
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.2
        return poids

class Roi(Metier):
    NOM = u"Roi des francs"
    def __init__(self):
        self.nom_ = Roi.NOM

    def GetNiveauRichesse(self):
        return 9

    def GetDiscipline(self):
        return u"Royauté"

    def GetPoidsDemo(self, masculin, coterieObj):
        return 0


class Berger(Metier):
    NOM = u"Berger"
    def __init__(self):
        self.nom_ = Berger.NOM

    def GetNiveauRichesse(self):
        return -1

    def GetDiscipline(self):
        return u"Élevage"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.01
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.4
        return poids

class Stratege(Metier):
    NOM = u"Général"
    def __init__(self):
        self.nom_ = Stratege.NOM

    def GetNiveauRichesse(self):
        return 6

    def GetDiscipline(self):
        return u"Stratégie"

    def GetPoidsDemo(self, masculin, coterieObj):
        return 0

class Danseur(Metier):
    NOM = u"Danseur"
    def __init__(self):
        self.nom_ = Danseur.NOM

    def GetDiscipline(self):
        return u"Danse"

    def GetNiveauRichesse(self):
        return -2

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.002
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.1
        return poids

class Musicien(Metier):
    NOM = u"Musicien"
    def __init__(self):
        self.nom_ = Musicien.NOM

    def GetNiveauRichesse(self):
        return -2

    def GetDiscipline(self):
        return u"Musique"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.1
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

class Cuisinier(Metier):
    NOM = u"Cuisinier"
    def __init__(self):
        self.nom_ = Cuisinier.NOM

    def GetDiscipline(self):
        return u"Cuisine"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 1.0
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

class Acteur(Metier):
    NOM = u"Acteur"
    def __init__(self):
        self.nom_ = Acteur.NOM

    def GetNiveauRichesse(self):
        return -2

    def GetDiscipline(self):
        return u"Comédie"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.1
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.2
        return poids

class Dessinateur(Metier):
    NOM = u"Dessinateur"
    def __init__(self):
        self.nom_ = Dessinateur.NOM

    def GetNiveauRichesse(self):
        return -2

    def GetDiscipline(self):
        return u"Dessin"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.1
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

class Bibliothecaire(Metier):
    NOM = u"Bibliothécaire"
    def __init__(self):
        self.nom_ = Bibliothecaire.NOM

    def GetDiscipline(self):
        return u"Litérature"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.3
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

class Poete(Metier):
    NOM = u"Poète"
    def __init__(self):
        self.nom_ = Poete.NOM

    def GetNiveauRichesse(self):
        return -4

    def GetDiscipline(self):
        return u"Poésie"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.01
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.1
        return poids

class Cartographe(Metier):
    NOM = u"Cartographe"
    def __init__(self):
        self.nom_ = Cartographe.NOM

    def GetDiscipline(self):
        return u"Cathographie"

    def GetNiveauRichesse(self):
        return 2

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.01
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.2
        return poids

class Marchand(Metier):
    NOM = u"Marchand"
    def __init__(self):
        self.nom_ = Marchand.NOM

    def GetNiveauRichesse(self):
        return 3

    def GetDiscipline(self):
        return u"Commerce"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.3
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

    def GenererPortraits(self, age, masculin, portraits, valeursTraits):
        """
        ajoute des portraits correspondants aux caracs en parametre et au métier
        """
        if masculin:
            if age > 15:
                if age > 50:
                    portraits.append("images/metiers/marchand/portraits/portrait_marchand_50+.jpg")
                if age < 50:
                    portraits.append("images/metiers/marchand/portraits/portrait_marchand_15-50.jpg")
        return portraits

class Mineur(Metier):
    NOM = u"Mineur"
    def __init__(self):
        self.nom_ = Mineur.NOM

    def GetNiveauRichesse(self):
        return -4

    def GetDiscipline(self):
        return u"Minage"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.3
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

class Pretre(Metier):
    NOM = u"Prêtre"
    def __init__(self):
        self.nom_ = Pretre.NOM

    def GetDiscipline(self):
        return u"Prêtrise"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.02
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

class Ouvrier(Metier):
    NOM = u"Ouvrier"
    def __init__(self):
        self.nom_ = Ouvrier.NOM

    def GetNiveauRichesse(self):
        return -4

    def GetDiscipline(self):
        return u"Manutention"

class Politique(Metier):
    NOM = u"Politicien"
    def __init__(self):
        self.nom_ = Politique.NOM

    def GetNiveauRichesse(self):
        return 2

    def GetDiscipline(self):
        return u"Politique"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.02
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.2
        return poids

class Forgeron(Metier):
    NOM = u"Forgeron"
    def __init__(self):
        self.nom_ = Forgeron.NOM

    def GetNiveauRichesse(self):
        return 2

    def GetDiscipline(self):
        return u"Forge"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.1
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

class Alchimiste(Metier):
    NOM = u"Alchimiste"
    def __init__(self):
        self.nom_ = Alchimiste.NOM

    def GetNiveauRichesse(self):
        return 3

    def GetDiscipline(self):
        return u"Alchimie"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.0
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

class Medecin(Metier):
    NOM = u"Médecin"
    def __init__(self):
        self.nom_ = Medecin.NOM

    def GetNiveauRichesse(self):
        return 4

    def GetDiscipline(self):
        return u"Médecine"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.2
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

class TueurDeMonstres(Metier):
    NOM = u"Tueur de monstres"
    def __init__(self):
        self.nom_ = TueurDeMonstres.NOM

    def GetNiveauRichesse(self):
        return -2

    def GetDiscipline(self):
        return u"Traque de monstre"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

class Architecte(Metier):
    NOM = u"Architecte"
    def __init__(self):
        self.nom_ = Architecte.NOM

    def GetNiveauRichesse(self):
        return 4

    def GetDiscipline(self):
        return u"Architecture"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.2
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

class Parasite(Metier):
    NOM = u"Parasite"
    def __init__(self):
        self.nom_ = Parasite.NOM

    def GetDiscipline(self):
        return u"Parasitage"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.1
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

class Guerrier(Metier):
    NOM = u"Guerrier"
    def __init__(self):
        self.nom_ = Guerrier.NOM

    def GetNiveauRichesse(self):
        return -1

    def GetDiscipline(self):
        return u"Combat"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.1
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

    def GetTexteCompetence(self, niveauComp):
        """
        renvoie le niveau de compétence dans ce métier du perso rapport à la valeur en paramètre
        éventuellement surclassable pour être plus précis
        """
        txtCompetence = u"Apprenti"
        if niveauComp > 1:
            txtCompetence = u"Combattant"
            if niveauComp > 3:
                txtCompetence = u"Élite"
                if niveauComp > 5:
                    txtCompetence = u"Champion"
                    if niveauComp > 8:
                        txtCompetence = u"Maître"
                        if niveauComp > 10:
                            txtCompetence = u"Maître légendaire"
        return txtCompetence

class Chauffeur(Metier):
    """
    Savoir conduire les voiture (et dans une moindre mesure les motos)
    """
    NOM = u"Conducteur de véhicules moteurs"
    def __init__(self):
        self.nom_ = Chauffeur.NOM

    def GetDiscipline(self):
        return u"Conduite"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.5
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

class Pilote(Metier):
    """
    Savoir conduire les aéronefs
    """
    NOM = u"Pilote d'aéronef"
    def __init__(self):
        self.nom_ = Pilote.NOM

    def GetNiveauRichesse(self):
        return 3

    def GetDiscipline(self):
        return u"Pilotage"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.01
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

class Mecanicien(Metier):
    NOM = u"Mécanicien"
    def __init__(self):
        self.nom_ = Mecanicien.NOM

    def GetNiveauRichesse(self):
        return 3

    def GetDiscipline(self):
        return u"Mécanique"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.05
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

class Chevalier(Metier):
    NOM = u"Chevalier"
    def __init__(self):
        self.nom_ = Chevalier.NOM

    def GetDiscipline(self):
        return u"Chevalerie"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.5
        return poids

class Informaticien(Metier):
    NOM = u"Informaticien"
    def __init__(self):
        self.nom_ = Informaticien.NOM

    def GetNiveauRichesse(self):
        return 3

    def GetDiscipline(self):
        return u"Informatique"

    def estDeBureau(self, strMetier):
        return True

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.4
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

class Cyberneticien(Metier):
    """
    améliorations cybernétiques sur le corps, bionique compris
    """
    NOM = u"Cybernéticien"
    def __init__(self):
        self.nom_ = Cyberneticien.NOM

    def GetNiveauRichesse(self):
        return 5

    def GetDiscipline(self):
        return u"Cybernétique"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

    def GenererPortraits(self, age, masculin, portraits, valeursTraits):
        """
        ajoute des portraits correspondants aux caracs en parametre
        """
        if masculin:
            if age > 60:
                portraits.append("images/metiers/cyberneticien/portraits/60+.jpg")
        return portraits

class Geneticien(Metier):
    NOM = u"Généticien"
    def __init__(self):
        self.nom_ = Geneticien.NOM

    def GetNiveauRichesse(self):
        return 5

    def GetDiscipline(self):
        return u"Génétique"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

    def GenererPortraits(self, age, masculin, portraits, valeursTraits):
        if masculin:
            if age > 60:
                portraits.append("images/metiers/cyberneticien/portraits/60+.jpg")
        return portraits

class Commercial(Metier):
    NOM = u"Commercial"
    def __init__(self):
        self.nom_ = Commercial.NOM

    def GetNiveauRichesse(self):
        return 2

    def GetDiscipline(self):
        return u"Vente"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.4
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

class Policier(Metier):
    NOM = u"Policier"
    def __init__(self):
        self.nom_ = Policier.NOM

    def GetDiscipline(self):
        return u"Police"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.3
        if masculin:
            poids = 1.5
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

    def GenererPortraits(self, age, masculin, portraits, valeursTraits):
        if masculin:
            pass
        else:
            if age >= 20:
                if age <= 30:
                    portraits.append("images/metiers/policier/portraits/femme20_30.jpg")
        return portraits

class Vigile(Metier):
    NOM = u"Vigile"
    def __init__(self):
        self.nom_ = Vigile.NOM

    def GetDiscipline(self):
        return u"Surveillance"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.4
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

class Banquier(Metier):
    NOM = u"Banquier"
    def __init__(self):
        self.nom_ = Banquier.NOM

    def GetNiveauRichesse(self):
        return 4

    def GetDiscipline(self):
        return u"Banque"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.3
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

    def estDeBureau(self, strMetier):
        return True

class GardeDuCorps(Metier):
    NOM = u"Garde du corps"
    def __init__(self):
        self.nom_ = GardeDuCorps.NOM

    def GetNiveauRichesse(self):
        return 1

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.04
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

class Electronique(Metier):
    NOM = u"Électronicien"
    def __init__(self):
        self.nom_ = Electronique.NOM

    def GetNiveauRichesse(self):
        return 3

    def GetDiscipline(self):
        return u"Électronique"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.1
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.3
        return poids

class Chasseur(Metier):
    NOM = u"Chasseur"
    def __init__(self):
        self.nom_ = Chasseur.NOM

    def GetDiscipline(self):
        return u"Chasse"

    def GetNiveauRichesse(self):
        return -2

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.02
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.4
        return poids

class Marin(Metier):
    NOM = u"Marin"
    def __init__(self):
        self.nom_ = Marin.NOM

    def GetNiveauRichesse(self):
        return -1

    def GetDiscipline(self):
        return u"Navigation"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.1
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.4
        return poids

class Etudiant(Metier):
    NOM = u"Étudiant"
    def __init__(self):
        self.nom_ = Etudiant.NOM

    def GetNiveauRichesse(self):
        return -5

    def GetDiscipline(self):
        return u"Études"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.2
        return poids

class Aventurier(Metier):
    NOM = u"Aventurier"
    def __init__(self):
        self.nom_ = Aventurier.NOM

    def GetNiveauRichesse(self):
        return -4

    def GetDiscipline(self):
        return u"Aventure"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.001
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.4
        return poids

class Journaliste(Metier):
    NOM = u"Journaliste"
    def __init__(self):
        self.nom_ = Journaliste.NOM

    def GetNiveauRichesse(self):
        return -1

    def GetDiscipline(self):
        return u"Journalisme"

    def GetPoidsDemo(self, masculin, coterieObj):
        poids = 0.5
        if self.nom_ in coterieObj.GetMetiersCompatibles():
            poids = poids + 0.5
        return poids

    def GenererPortraits(self, age, masculin, portraits, valeursTraits):
        """
        ajoute des portraits correspondants aux caracs en parametre
        """
        if masculin:
            if age > 25:
                if age < 50:
                    portraits.append("images/coteries/transhumanistes/portraits/journaliste25-50.jpg")
        return portraits

class CollectionMetiers:

    def __init__(self):
        self.lMetiers_ = dict()

        mecanicien = Mecanicien()
        self.SetMetier(Mecanicien.NOM, mecanicien)

        danseur = Danseur()
        self.SetMetier(Danseur.NOM, danseur)

        roi = Roi()
        self.SetMetier(Roi.NOM, roi)

        stratege = Stratege()
        self.SetMetier(Stratege.NOM, stratege)

        acteur = Acteur()
        self.SetMetier(Acteur.NOM, acteur)

        cuisinier = Cuisinier()
        self.SetMetier(Cuisinier.NOM, cuisinier)

        etudiant = Etudiant()
        self.SetMetier(Etudiant.NOM, etudiant)

        journaliste = Journaliste()
        self.SetMetier(Journaliste.NOM, journaliste)

        berger = Berger()
        self.SetMetier(Berger.NOM, berger)

        electronique = Electronique()
        self.SetMetier(Electronique.NOM, electronique)

        robotique = Robotique()
        self.SetMetier(Robotique.NOM, robotique)

        paysan = Paysan()
        self.SetMetier(Paysan.NOM, paysan)

        bibliothecaire = Bibliothecaire()
        self.SetMetier(Bibliothecaire.NOM, bibliothecaire)

        dessinateur = Dessinateur()
        self.SetMetier(Dessinateur.NOM, dessinateur)

        musicien = Musicien()
        self.SetMetier(Musicien.NOM, musicien)

        cartographe = Cartographe()
        self.SetMetier(Cartographe.NOM, cartographe)

        marchand = Marchand()
        self.SetMetier(Marchand.NOM, marchand)

        poete = Poete()
        self.SetMetier(Poete.NOM, poete)

        mineur = Mineur()
        self.SetMetier(Mineur.NOM, mineur)

        pretre = Pretre()
        self.SetMetier(Pretre.NOM, pretre)

        ouvrier = Ouvrier()
        self.SetMetier(Ouvrier.NOM, ouvrier)

        politique = Politique()
        self.SetMetier(Politique.NOM, politique)

        forgeron = Forgeron()
        self.SetMetier(Forgeron.NOM, forgeron)

        alchimiste = Alchimiste()
        self.SetMetier(Alchimiste.NOM, alchimiste)

        medecin = Medecin()
        self.SetMetier(Medecin.NOM, medecin)

        tueurDeMonstres = TueurDeMonstres()
        self.SetMetier(TueurDeMonstres.NOM, tueurDeMonstres)

        architecte = Architecte()
        self.SetMetier(Architecte.NOM, architecte)

        parasite = Parasite()
        self.SetMetier(Parasite.NOM, parasite)

        guerrier = Guerrier()
        self.SetMetier(Guerrier.NOM, guerrier)

        chauffeur = Chauffeur()
        self.SetMetier(Chauffeur.NOM, chauffeur)

        pilote = Pilote()
        self.SetMetier(Pilote.NOM, pilote)

        chevalier = Chevalier()
        self.SetMetier(Chevalier.NOM, chevalier)

        informaticien = Informaticien()
        self.SetMetier(Informaticien.NOM, informaticien)

        cyberneticien = Cyberneticien()
        self.SetMetier(Cyberneticien.NOM, cyberneticien)

        geneticien = Geneticien()
        self.SetMetier(Geneticien.NOM, geneticien)

        commercial = Commercial()
        self.SetMetier(Commercial.NOM, commercial)

        policier = Policier()
        self.SetMetier(Policier.NOM, policier)

        vigile = Vigile()
        self.SetMetier(Vigile.NOM, vigile)

        banquier = Banquier()
        self.SetMetier(Banquier.NOM, banquier)

        gardeDuCorps = GardeDuCorps()
        self.SetMetier(GardeDuCorps.NOM, gardeDuCorps)

        aventurier = Aventurier()
        self.SetMetier(Aventurier.NOM, aventurier)

        chasseur = Chasseur()
        self.SetMetier(Chasseur.NOM, chasseur)

        marin = Marin()
        self.SetMetier(Marin.NOM, marin)

    def getMetierAleatoire(self, selonDemographie, masculin, cotObj):
        """
        selonDemographie : si True le métier est sélectionné en fonction de la proportion de gens qui le pratiquent dans la vie
        masculin : si True la démographie utilisée sera celle des hommes
        """
        if selonDemographie:
            poidsDemoTotal = 0
            for idMetier in self.lMetiers_:
                poidsDemoTotal = poidsDemoTotal + self.lMetiers_[idMetier].GetPoidsDemo(masculin, cotObj)

            alPoidsDemo = random.uniform(0, poidsDemoTotal)

            for idMetier in self.lMetiers_:
                alPoidsDemo = alPoidsDemo - self.lMetiers_[idMetier].GetPoidsDemo(masculin, cotObj)
                if alPoidsDemo <= 0:
                    return self.lMetiers_[idMetier]

        return random.choice(list(self.lMetiers_.values()))

    def __getitem__(self, idMetier):
        if not idMetier in self.lMetiers_:
            print("ce métier n'existe pas ! : {}".format(idMetier))
        return self.lMetiers_[idMetier]

    def __setitem__(self, idMetier, metier):
        self.SetMetier(idMetier, metier)

    def SetMetier(self, idMetier, metier):
        self.lMetiers_[idMetier] = metier

    def __len__(self):
        return len(self.lMetiers_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        if len(self.lMetiers_) == 0:
            return "Aucun métier."
        str = u"Liste de tous les métiers : "
        for metier in self.lMetiers_:
            str = str + metier + ","
        return str

def aUnMetier(situation):
    return situation[Metier.C_METIER] != ""
