import random

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

    def GenererPortraits(self, age, masculin, metier, portraits):
        """
        ajoute des portraits correspondants aux caracs en parametre
        A OVERRIDER
        """
        return portraits

class Paysan(Metier):
    NOM = u"Paysan"
    def __init__(self):
        self.nom_ = Paysan.NOM

class Musicien(Metier):
    NOM = u"Musicien"
    def __init__(self):
        self.nom_ = Musicien.NOM

class Dessinateur(Metier):
    NOM = u"Dessinateur"
    def __init__(self):
        self.nom_ = Dessinateur.NOM

class Bibliothecaire(Metier):
    NOM = u"Bibliothécaire"
    def __init__(self):
        self.nom_ = Bibliothecaire.NOM

class Poete(Metier):
    NOM = u"Poète"
    def __init__(self):
        self.nom_ = Poete.NOM

class Cartographe(Metier):
    NOM = u"Cartographe"
    def __init__(self):
        self.nom_ = Cartographe.NOM

class Marchand(Metier):
    NOM = u"Marchand"
    def __init__(self):
        self.nom_ = Marchand.NOM

class Mineur(Metier):
    NOM = u"Mineur"
    def __init__(self):
        self.nom_ = Mineur.NOM

class Pretre(Metier):
    NOM = u"Prêtre"
    def __init__(self):
        self.nom_ = Pretre.NOM

class Ouvrier(Metier):
    NOM = u"Ouvrier"
    def __init__(self):
        self.nom_ = Ouvrier.NOM

class Politique(Metier):
    NOM = u"Politique"
    def __init__(self):
        self.nom_ = Politique.NOM

class Forgeron(Metier):
    NOM = u"Forgeron"
    def __init__(self):
        self.nom_ = Forgeron.NOM

class Alchimiste(Metier):
    NOM = u"Alchimiste"
    def __init__(self):
        self.nom_ = Alchimiste.NOM

class Medecin(Metier):
    NOM = u"Médecin"
    def __init__(self):
        self.nom_ = Medecin.NOM

class TueurDeMonstres(Metier):
    NOM = u"Tueur de monstres"
    def __init__(self):
        self.nom_ = TueurDeMonstres.NOM

class Architecte(Metier):
    NOM = u"Architecte"
    def __init__(self):
        self.nom_ = Architecte.NOM

class Parasite(Metier):
    NOM = u"Parasite"
    def __init__(self):
        self.nom_ = Parasite.NOM

class Guerrier(Metier):
    NOM = u"Guerrier"
    def __init__(self):
        self.nom_ = Guerrier.NOM

class Conducteur(Metier):
    NOM = u"Conducteur"
    def __init__(self):
        self.nom_ = Conducteur.NOM

class Pilote(Metier):
    NOM = u"Pilote"
    def __init__(self):
        self.nom_ = Pilote.NOM

class Chevalier(Metier):
    NOM = u"Chevalier"
    def __init__(self):
        self.nom_ = Chevalier.NOM

class Informaticien(Metier):
    NOM = u"Informaticien"
    def __init__(self):
        self.nom_ = Informaticien.NOM

    def estDeBureau(self, strMetier):
        return True

class Cyberneticien(Metier):
    NOM = u"Cybernéticien"
    def __init__(self):
        self.nom_ = Cyberneticien.NOM

    def GenererPortraits(self, age, masculin, metier, portraits):
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

    def GenererPortraits(self, age, masculin, metier, portraits):
        """
        ajoute des portraits correspondants aux caracs en parametre
        """
        if masculin:
            if age > 60:
                portraits.append("images/metiers/cyberneticien/portraits/60+.jpg")
        return portraits

class Commercial(Metier):
    NOM = u"Commercial"
    def __init__(self):
        self.nom_ = Commercial.NOM

class Policier(Metier):
    NOM = u"Policier"
    def __init__(self):
        self.nom_ = Policier.NOM

class Vigile(Metier):
    NOM = u"Vigile"
    def __init__(self):
        self.nom_ = Vigile.NOM

class Banquier(Metier):
    NOM = u"Banquier"
    def __init__(self):
        self.nom_ = Banquier.NOM

    def estDeBureau(self, strMetier):
        return True

class GardeDuCorps(Metier):
    NOM = u"Garde du corps"
    def __init__(self):
        self.nom_ = GardeDuCorps.NOM

class CollectionMetiers:

    def __init__(self):
        self.lMetiers_ = dict()

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

        conducteur = Conducteur()
        self.SetMetier(Conducteur.NOM, conducteur)

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

    def getMetierAleatoire(self):
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
