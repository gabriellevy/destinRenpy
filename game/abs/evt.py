from abs.noeudNarration import NoeudNarration

class Evt(NoeudNarration):
    """
    sorte de chapitre groupant les effets
    Comme c'est avant tout un conteneur d'effets définis par un id l'Evt est une forme de dictionnaire ordonné d'effets et ses fonctions d'itération sont remplacées.
    """

    compteurId = 0

    def __init__(self, id):
        NoeudNarration.__init__(self, id, "")
        #les deux objets suivants doivent toujours être ordonnés de la même manière : m_IdEffets permettra d'accéder à m_Effets
        self.m_IdEffets = []  # Liste contenant nos "clés" de la liste d'effets
        self.m_Effets = list()

    def __repr__(self):
        """Représentation d'un événement"""
        chaine = "\n   {"
        premier_passage = True
        for cle, valeur in self.items():
            if not premier_passage:
                chaine += ",\n   "  # On ajoute la virgule comme séparateur
            else:
                premier_passage = False
            chaine += repr(cle) + ": " + str(valeur)
        chaine += "}"
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

        if cle not in self.m_IdEffets:
            raise KeyError( \
                "La clé {0} ne se trouve pas dans le dictionnaire".format( \
                    cle))
        else:
            indice = self.m_IdEffets.index(cle)
            return self.m_Effets[indice]

    def __setitem__(self, cle, valeur):
        """Méthode spéciale appelée quand on cherche à modifier une clé
        présente dans le dictionnaire. Si la clé n'est pas présente, on l'ajoute
        à la fin du dictionnaire"""

        if cle in self.m_IdEffets:
            indice = self.m_IdEffets.index(cle)
            self.m_Effets[indice] = valeur
        else:
            self.m_IdEffets.append(cle)
            self.m_Effets.append(valeur)

    def __delitem__(self, cle):
        """Méthode appelée quand on souhaite supprimer une clé"""
        if cle not in self.m_IdEffets:
            raise KeyError( \
                "La clé {0} ne se trouve pas dans le dictionnaire".format( \
                    cle))
        else:
            indice = self.m_IdEffets.index(cle)
            del self.m_IdEffets[indice]
            del self.m_Effets[indice]

    def __contains__(self, cle):
        """Renvoie True si la clé est dans la liste des clés ou des valeurs, False sinon"""
        if (isinstance(cle, Effet)) == True:
            return cle in self.m_Effets
        else:
            return cle in self.m_IdEffets

    def __len__(self):
        """Comme histoire est essentiellement un conteneur d'effets ses fonctions d'accès sont surchargés par commodité"""
        return self.m_Effets.__len__()

    def EffetSuivant(self, idEffetActuel):
        indice = self.m_IdEffets.index(idEffetActuel)
        indice = indice + 1
        if ( indice >= len(self.m_IdEffets)):
            return None
        return  self.m_Effets[indice]

    def ParcourirEffets(self):
        """pseudo itérateur des effets de l'événement"""
        for effet in self.m_Effets:
            yield effet

    def __iter__(self):
        """Méthode de parcours de l'objet. On renvoie l'itérateur des clés"""
        return iter(self.m_IdEffets)

    def items(self):
        """Renvoie un générateur contenant les couples (cle, valeur)"""
        for i, cle in enumerate(self.m_IdEffets):
            valeur = self.m_Effets[i]
            yield (cle, valeur)

    def keys(self):
        """Cette méthode renvoie la liste des clés"""
        return list(self.m_IdEffets)

    def values(self):
        """Cette méthode renvoie la liste des valeurs"""
        return list(self.m_Effets)

# stupides tests
'''print("------tests Evt")'''