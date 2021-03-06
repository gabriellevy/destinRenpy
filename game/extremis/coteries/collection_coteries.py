from extremis.coteries.templiers import templiers
from extremis.coteries.elfes import elfes
from extremis.coteries.orks import orks
from extremis.coteries.conquistadors import conquistadors
from extremis.coteries.transhumanistes import transhumanistes
from extremis.geographie import quartier
import random

class CollectionCoteries:

    def __init__(self):
        self.lCoteries_ = dict()

        templier = templiers.Templiers()
        self.SetCoterie(templiers.Templiers.ID, templier)

        transhumaniste = transhumanistes.Transhumanistes()
        self.SetCoterie(transhumanistes.Transhumanistes.ID, transhumaniste)

        elfe = elfes.Elfes()
        self.SetCoterie(elfes.Elfes.ID, elfe)

        ork = orks.Orks()
        self.SetCoterie(orks.Orks.ID, ork)

        conqu = conquistadors.Conquistadors()
        self.SetCoterie(conquistadors.Conquistadors.ID, conqu)

    def getCoterieAleatoire(self, selonDemographie):
        if selonDemographie:
            poidsDemoTotal = 0
            for idCoterie in self.lCoteries_:
                poidsDemoTotal = poidsDemoTotal + self.lCoteries_[idCoterie].GetPoidsDemo()

            alPoidsDemo = random.uniform(0, poidsDemoTotal)

            for idCoterie in self.lCoteries_:
                alPoidsDemo = alPoidsDemo - self.lCoteries_[idCoterie].GetPoidsDemo()
                if alPoidsDemo <= 0:
                    return self.lCoteries_[idCoterie]

        else:
            return random.choice(list(self.lCoteries_.values()))

    def DebuterProchaineUniversite(self, situation):
        coterie = self.getCoterieAleatoire(False)
        labelProchainEvt = coterie.getLabelUniversite()

        while situation.GetValCaracInt(labelProchainEvt) == 1: # détection de si cette coterie a déjà été effectuée par le personnage
            coterie = self.getCoterieAleatoire(False)
            labelProchainEvt = coterie.getLabelUniversite()

        situation.SetValCarac(quartier.Quartier.C_QUARTIER, coterie.quartier_)
        situation.SetValCarac(labelProchainEvt, 1)

        return labelProchainEvt

    def __getitem__(self, idCoterie):
        if not idCoterie in self.lCoteries_:
            erreur = u"Pas de coterie d'id '{}'".format(idCoterie)
            print(erreur)
            assert erreur # pas sûr que ça marche ça !
            return erreur
        return self.lCoteries_[idCoterie]

    def __setitem__(self, idCoterie, coterie):
        self.SetCoterie(idCoterie, coterie)

    def SetCoterie(self, idCoterie, coterie):
        self.lCoteries_[idCoterie] = coterie

    def __len__(self):
        return len(self.lCoteries_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        if len(self.lCoteries_) == 0:
            return "Aucune Coterie."
        str = u"Liste de toutes les Coteries : "
        for coterie in self.lCoteries_:
            str = str + coterie + ","
        return str

    def GetCoterieAleatoire(self, critereCoterie):
        """
        switch (critereCoterie) {
        case cc_Demographie : {
            double poidsDemoTotal = 0;
            for ( shared_ptr<Coterie> cot: Extremis::COTERIES) {
                poidsDemoTotal += cot->GetPoidsDemo();
            }

            double alPoidsDemo = Aleatoire::GetAl()->Entre0Et1() * poidsDemoTotal;

            for ( shared_ptr<Coterie> cot: Extremis::COTERIES) {
                alPoidsDemo -= cot->GetPoidsDemo();
                if ( alPoidsDemo <= 0)
                    return cot;
            }
        }break;
        case cc_Aleatoire :
            return Extremis::COTERIES[Aleatoire::GetAl()->EntierInferieurA(Extremis::COTERIES.size())];
        case cc_Seduction : {
            double poidsTotal = 0;
            for ( shared_ptr<Coterie> cot: Extremis::COTERIES) {
                poidsTotal += cot->GetCoeffSeduction();
            }

            double alPoidsDemo = Aleatoire::GetAl()->Entre0Et1() * poidsTotal;

            for ( shared_ptr<Coterie> cot: Extremis::COTERIES) {
                alPoidsDemo -= cot->GetCoeffSeduction();
                if ( alPoidsDemo <= 0)
                    return cot;
            }
        }break;
        }
        return nullptr;
        """
        return "truc"

    def GetNRandomCoteries(self, nombre, critereCoterie):
        """
        QVector<shared_ptr<Coterie>> m_Coteries = {};

        while (n > 0) {
            shared_ptr<Coterie> coterie = GetCoterieAleatoire(critereCoterie);

            if ( m_Coteries.indexOf(coterie) == -1) {
                m_Coteries.push_back(coterie);
                n--;
            }
        }

        return m_Coteries
        """
        return "truc"
