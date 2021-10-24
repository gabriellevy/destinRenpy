class SautVersNoeud:
    """
    Classe gérant le passage du noeud courant vers le noeud suivant et les différents modes liés :
    - go to un effet
    - go to un evt (premier effet ou effet précisé)
    - sélectionneur de noeud selon une liste de possibilités et de probas associés
    """

    def __init__(self):
        self._m_GoToEffetId = "go to effet id"
        self._m_GoToEvtId = "go to evt id"
        # TODO MATHIEU : sélectionneur de do to selon proba (SelectionneurDeNoeud)

    def _get_m_GoToEffetId(self):
        return  self._m_GoToEffetId
    def _get_m_GoToEvtId(self):
        return  self._m_GoToEvtId

    def __getattr__(self, nom):
        """Si Python ne trouve pas l'attribut nommé nom, il appelle
             cette méthode. On affiche une alerte"""
        print("Alerte ! Il n'y a pas d'attribut '{}' dans l'objet '{}' !".format(nom, self))

    # Les SautVersNoeud sont (intégralement?) non mutables
    m_GoToEffetId = property(_get_m_GoToEffetId)
    m_GoToEvtId = property(_get_m_GoToEvtId)