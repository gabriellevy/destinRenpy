from extremis.coteries.templiers import templiers
from extremis.coteries.elfes import elfes
from extremis.coteries.transhumanistes import transhumanistes
import random

class CollectionCoteries:

    def __init__(self):
        self.lCoteries_ = dict()

        templier = templiers.Templiers()
        self.SetCoterie(templiers.Templiers.NOM, templier)

        transhumaniste = transhumanistes.Transhumanistes()
        self.SetCoterie(transhumanistes.Transhumanistes.NOM, transhumaniste)
        
        elfe = elfes.Elfes()
        self.SetCoterie(elfes.Elfes.NOM, elfe)

    def getCoterieAleatoire(self):
        return random.choice(list(self.lCoteries_.values()))

    def __getitem__(self, idCoterie):
        if not idCoterie in self.lCoteries_:
            self.CreerCoterie(idCoterie)
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
