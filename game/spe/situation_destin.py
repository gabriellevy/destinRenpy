from extremis.socio_eco.metiers import metier
from extremis.coteries import coterie
from extremis.coteries.templiers import templiers
from abs.religions import religion
from abs.humanite.sante import pbsante
from extremis.constitution import temps
from extremis.geographie import quartier
from spe.humanite import portrait_destin
from abs.humanite import portrait
from extremis.socio_eco.crime import crime
from extremis.socio_eco.crime import justice
from spe.humanite import pnj_destin
from abs.humanite import pnj
from abs.humanite import trait
from abs.humanite import identite
from abs.humanite.amour import relationAmoureuse
from abs import situation
from abs.affichage import affichagePortrait
import random

class SituationDestin(situation.Situation):

    def __init__(self):
        situation.Situation.__init__(self, 0)
        self.collectionCoteries = None
        self.collectionBioniques = None
        self.collectionQuartiers = None
        self.collectionCrimes = None
        self.collectionPnjs = {}

    def DeterminerPortrait(self):
        """
        récupérer une liste de portraits selon les caracs du perso et en choisir un aléatoirement
        celui est choisi est stocké dans une carac mais en cas de changement important (âge, métier, coterie...) on en recalcule un
        """
        portr = portrait_destin.PortraitDestin()
        portraitStr = portr.DeterminerPortraitPersoPrincipal(self, True)
        self.SetCarac(portrait.Portrait.C_PORTRAIT, portraitStr)
        return self.GetValCarac(portrait.Portrait.C_PORTRAIT)

    # get objets tirés des caracs du perso
    def GetQuartier(self):
        valQuartierStr = self.GetValCarac(quartier.Quartier.C_QUARTIER)
        if valQuartierStr == "":
            return None
        return self.collectionQuartiers[valQuartierStr]

    def GetCoterie(self):
        valCoterieStr = self.GetValCarac(coterie.Coterie.C_COTERIE)
        if valCoterieStr == "":
            return None
        cot = self.collectionCoteries[valCoterieStr]
        return cot

    # ---------------------------------- affichage des caracs dans l'interface

    def AffichageQuartier(self):
        if ( quartier.Quartier.C_QUARTIER not in self.caracs_):
            return u"Pas d'habitation !!"
        return self.caracs_[quartier.Quartier.C_QUARTIER]

    def AffichageCrime(self, crimes):
        str = u"{}".format(self.GetValCarac(crime.Crime.C_CRIMINEL))

        # affichage des crimes dans le détail
        for crimeK in crimes.lCrimes_.keys():
            crimeCarac = crimes[crimeK]
            descr = u"{}".format(crimeCarac.GetDescription(self))
            if descr != "":
                if str != "":
                    str = u"{}\n".format(str)
                str = u"{}{}".format(str, descr)
        if str != "":
            str = u"{}\n".format(str)
        str = u"{}{}".format(str, self.GetValCarac(justice.Justice.C_LIBERTE))
        if str != "":
            str = u"{}\n".format(str)
        nbJoursPrison = self.GetValCaracInt(justice.Justice.C_JOURS_PRISON)
        if nbJoursPrison > 0:
            str = u"{}{} mois de prison".format(str, nbJoursPrison/30 + 1)
        if str == "":
            str =u"Casier vierge"
        return str

    def AffichageCoterie(self):
        if ( coterie.Coterie.C_COTERIE not in self.caracs_):
            return ""
        cot = self.GetCoterie()
        if cot is None:
            return ""
        return cot.AffichageSituationDansCoterie(self)

    def AffichagePatronyme(self):
        if ( identite.Identite.C_PRENOM not in self.caracs_):
            return "!!! Pas de nom !!!!"
        return u"{} {}".format(self.caracs_[identite.Identite.C_PRENOM], self.caracs_[identite.Identite.C_NOM])

    # DATES ET TEMPS QUI PASSE-----------------------------------------------------------------------------------------------------------
    def AffichageDate(self):
        nbJours = self.caracs_[temps.Date.DATE]
        dateDuJour = temps.Date(nbJours)
        dateStr = "{}\n{}".format(dateDuJour.formatConstitution(), dateDuJour.formatGregorien())
        return dateStr

    def AvanceDeXJours(self, nbJoursPasses):
        nouvelleDate = self.caracs_[temps.Date.DATE] + nbJoursPasses
        self.caracs_[temps.Date.DATE] = nouvelleDate
        self.caracs_[temps.Date.AGE_ANNEES] = self.AgeEnAnnees()

        # application des jours passés aux pnjs :
        for pnjObj in self.collectionPnjs.values():
            nbAnneesAvant = pnjObj.nbJours_/360
            pnjObj.nbJours_ = pnjObj.nbJours_ + nbJoursPasses
            nbAnneesApres = pnjObj.nbJours_/360
            # si le perso a pris une année et que la nouvelle année est un multiple de 5 on lui change de portrait
            if nbAnneesApres > nbAnneesAvant:
                if nbAnneesAvant%5 == 0:
                    pnjObj.MajPortrait(self)

        # avancée des caracs de jours qui passent :
        # jours de convalescence :
        nbJoursConvalescence = self.GetValCaracInt(pbsante.PbSante.C_JOURS_DHOPITAL)
        if nbJoursConvalescence > 0:
            nbJoursConvalescence = nbJoursConvalescence - nbJoursPasses
            if nbJoursConvalescence < 0:
                nbJoursConvalescence = 0
            self.caracs_[pbsante.PbSante.C_JOURS_DHOPITAL] = nbJoursConvalescence
        # prison
        nbJoursPrison = self.GetValCaracInt(justice.Justice.C_JOURS_PRISON)
        if nbJoursPrison > 0:
            nbJoursPrison = nbJoursPrison - nbJoursPasses
            if nbJoursPrison < 0:
                nbJoursPrison = 0
            self.caracs_[justice.Justice.C_JOURS_PRISON] = nbJoursPrison

    def TourSuivant(self):
        """
        Passage au "tour" suivant dans un destin extermis c'est à dire grosso modo à un mois un peu randomisé
        """
        nbJoursPasses = 20 + random.randint(0, 20)
        self.AvanceDeXJours(nbJoursPasses)

    # PNJ

    def AffichagePortraitPere(self):
        # père
        str = u""
        pere = self.GetValCarac(pnj.Pnj.C_PERE)
        if isinstance(pere, pnj_destin.PnjDestin) :
            return pere.portraitStr_
        return ""

    def AffichagePortraitMere(self):
        # mère
        str = u""
        mere = self.GetValCarac(pnj.Pnj.C_MERE)
        if isinstance(mere, pnj_destin.PnjDestin) :
            return mere.portraitStr_
        return ""

    def AffichageAmoureuses(self):
        """
        génère un tableau qui contient les éléments affichables du pnj
        """
        amoureuses = self.GetValCarac(relationAmoureuse.RelA.C_AMOUREUSES)
        affichageAmoureuses = []
        if isinstance(amoureuses, list) :
            if len(amoureuses) > 0:
                if isinstance(amoureuses[0], pnj_destin.PnjDestin) :
                    for amoureuse in amoureuses:
                        affichage = affichagePortrait.AffichagePortrait(amoureuse)
                        affichageAmoureuses.append(affichage)
        return affichageAmoureuses

    def AffichagePere(self):
        # père
        str = u""
        pere = self.GetValCarac(pnj.Pnj.C_PERE)
        if isinstance(pere, pnj_destin.PnjDestin) :
            str = u"{}".format(pere)
        return str

    def AffichageMere(self):
        # mère
        str = u""
        mere = self.GetValCarac(pnj.Pnj.C_MERE)
        if isinstance(mere, pnj_destin.PnjDestin) :
            str = u"{}".format(mere)
        return str

    # FONCTIONS GENERIQUES
    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        if len(self.caracs_) == 0:
            return u"Aucune carac."
        str = u"Situation actuelle : "
        for carac in self.caracs_.keys():
            str = "{} {} ({}), ".format(str, self.caracs_[carac], carac)
        return str
