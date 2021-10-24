from abs.evt import Evt
from abs.effet import Effet

class Hist:
    """
    Cette classe est une pure structure de données. Elle fait le lien entre GenHistoire qui la créée et ExecHistoire qui l'exécute
    elle est donc tout aussi indépendante de la manière dont elle est générée ou exécutée
    Comme c'est avant tout un conteneur d'événements définis par un id elle est une forme de dictionnaire ordonné d'événements et ses fonctions d'itération sont remplacées.
    """

    def __init__(self, titre):
        self.m_Titre = titre
        self.m_Perso = None

        #les deux objets suivants doivent toujours être ordonnés de la même manière : m_IdEvts permettra d'accéder à m_Evts
        self.m_IdEvts = []  # Liste contenant nos "clés" de la liste d'événements
        self.m_Evts = list();

        self.m_MessageVictoire = "Vous avez gagné"
        self.m_MessageDefaite = "Vous avez perdu"

    def __repr__(self):
        """Représentation de l'histoire en abrégé"""

        chaine = self.m_Titre + "\n{\n"
        premier_passage = True
        for cle, valeur in self.items():
            if not premier_passage:
                chaine += ",\n"  # On ajoute la virgule comme séparateur
            else:
                premier_passage = False
            chaine += repr(cle) + ": " + repr(valeur)
        chaine += "\n}"
        return chaine

    def __str__(self):
        """Fonction appelée quand on souhaite afficher le dictionnaire grâce
        à la fonction 'print' ou le convertir en chaîne grâce au constructeur
        'str'. On redirige sur __repr__"""
        return repr(self)

    def __getattr__(self, nom):
        """Si Python ne trouve pas l'attribut nommé nom, il appelle
             cette méthode. On affiche une alerte"""
        print("Alerte ! Il n'y a pas d'attribut '{}' dans l'objet '{}' !".format(nom, self))

    def __getitem__(self, cle):
        """Renvoie la valeur correspondant à la clé si elle existe, lève
        une exception KeyError sinon"""

        if cle not in self.m_IdEvts:
            raise KeyError( \
                "La clé {0} ne se trouve pas dans le dictionnaire".format( \
                    cle))
        else:
            indice = self.m_IdEvts.index(cle)
            return self.m_Evts[indice]

    def __setitem__(self, cle, valeur):
        """Méthode spéciale appelée quand on cherche à modifier une clé
        présente dans le dictionnaire. Si la clé n'est pas présente, on l'ajoute
        à la fin du dictionnaire"""

        if cle in self.m_IdEvts:
            indice = self.m_IdEvts.index(cle)
            self.m_Evts[indice] = valeur
        else:
            self.m_IdEvts.append(cle)
            self.m_Evts.append(valeur)

    def __delitem__(self, cle):
        """Méthode appelée quand on souhaite supprimer une clé"""
        if cle not in self.m_IdEvts:
            raise KeyError( \
                "La clé {0} ne se trouve pas dans le dictionnaire".format( \
                    cle))
        else:
            indice = self.m_IdEvts.index(cle)
            del self.m_IdEvts[indice]
            del self.m_Evts[indice]

    def __contains__(self, cle):
        """Renvoie True si la clé est dans la liste des clés ou des valeurs, False sinon"""
        if (isinstance(cle, Evt)) == True:
            return cle in self.m_Evts
        else:
            return cle in self.m_IdEvts

    def __len__(self):
        """Comme histoire est essentiellement un conteneur d'événements ses fonctions d'accès sont surchargés par commodité"""
        return self.m_Evts.__len__()

    def ParcourirEvts(self):
        """pseudo itérateur des événements de l'histoire"""
        for evt in self.m_Evts:
            yield evt

    def __iter__(self):
        """Méthode de parcours de l'objet. On renvoie l'itérateur des clés"""
        return iter(self.m_IdEvts)

    def items(self):
        """Renvoie un générateur contenant les couples (cle, valeur)"""
        for i, cle in enumerate(self.m_IdEvts):
            valeur = self.m_Evts[i]
            yield (cle, valeur)

    def keys(self):
        """Cette méthode renvoie la liste des clés"""
        return list(self.m_IdEvts)

    def values(self):
        """Cette méthode renvoie la liste des valeurs"""
        return list(self.m_Evts)


# stupides tests
'''print("------tests HISTOIRE")'''