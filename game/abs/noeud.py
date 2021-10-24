from abs.condition import Condition
from abs.setCarac import *

class Noeud:
    """
    Structure de base du système destin.
    Contient essentiellement des valeurs d'affichage et est héritée par toute les briques principales de structure d'affichage/histoire
    """

    def __init__(self, id):
        """Constructeur"""
        self._m_Id = id
        # TODO MATHIEU : changeur de perso
        self.m_Conditions = list()
        self.m_Parcouru = False # est-ce que ce noeud a déjà été parcouru ? (que sa condition ait ou non autorisé son exécution, il compte quand même comme parcouru)
        self.m_GoToEvtId = None
        self.m_GoToEffetId = None
        self.m_SetsCaracs = list()
        self.m_ChangementPhaseHistoire = None

    def _get_m_Id(self):
        return self._m_Id

    # L'identifiant ne peut jamais être modifié après création
    m_Id = property(_get_m_Id)

    def __getattr__(self, nom):
        """Si Python ne trouve pas l'attribut nommé nom, il appelle
             cette méthode. On affiche une alerte"""
        print("Alerte ! Il n'y a pas d'attribut '{}' dans l'objet '{}' !".format(nom, self))

    def AjouterCondition(self, caracId, valeur, comparateur):
        condition = Condition(caracId, valeur, comparateur)
        self.m_Conditions.append(condition)

    def AjouterRetireurACarac( id, valeur):
        setCarac = SetCarac(id, ModifCaracType.RETIRE, valeur)
        self.m_SetsCaracs.append(setCarac)
"""
{
    std::shared_ptr<SetCarac> set_carac = make_shared<SetCarac>(ModifCaracType::RetireDeCarac, id, QString::number(valeur));
    m_SetCaracs.append(set_carac);
    return set_carac;
}

std::shared_ptr<SetCarac> Noeud::AjouterRetireurACarac(QString id, QString valeur)
{
    std::shared_ptr<SetCarac> set_carac = make_shared<SetCarac>(ModifCaracType::RetireDeCarac, id, valeur);
    m_SetCaracs.append(set_carac);
    return set_carac;
}

std::shared_ptr<SetCarac> Noeud::AjouterAjouteurACarac(QString id, QString valeur)
{
    std::shared_ptr<SetCarac> set_carac = make_shared<SetCarac>(ModifCaracType::AddToCarac, id, valeur);
    m_SetCaracs.append(set_carac);
    return set_carac;
}
"""