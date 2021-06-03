
from extremis.socio_eco.metiers import metier
from extremis.coteries import coterie
from extremis.coteries.templiers import templiers
from extremis.religions import religion
from extremis.humanite.sante import pbsante
from extremis.constitution import temps
from extremis.geographie import quartier
from extremis.humanite import portrait
from extremis.socio_eco.crime import crime
from extremis.socio_eco.crime import justice
from extremis.humanite import pnj
from extremis.humanite import trait
from extremis.humanite import identite
from affichage import affichagePortrait
from extremis.humanite.amour import relationAmoureuse
import random

class Situation:
    """
    Situation de jeu
    Etat d'une partie à un instant t avec toutes les informations nécessaires pour la sauvegarder et la recharger
    en particulier la liste intégrale des caractéristiques du perso (qui sont une sous catégorie de la situation de jeu)

    !!!! cette classe est peut-être à surclasser pour ajouter des effets particuliers à certaines caracs (dans SetCarac par exemple)
    """

    def __init__(self):
        self.caracs_ = dict() # dictionnaire contenant toutes les caracs courantes de la partie
        self.valsMin_ = dict() # facultatif : dictionnaire contenant l'éventuelle valeur min de la carac en clé
        self.valsMax_ = dict() # facultatif : dictionnaire contenant l'éventuelle valeur max de la carac en clé
        date = temps.Date()
        self.caracs_[temps.Date.DATE] = date.nbJours_
        self.caracs_[temps.Date.AGE_ANNEES] = 0
        self.collectionMetiers = None
        self.collectionTraits = None
        self.collectionCoteries = None
        self.collectionBlessures = None
        self.collectionMaladies = None
        self.collectionQuartiers = None
        self.collectionCrimes = None
        self.collectionPnjs = {}

    def DeterminerPortrait(self):
        """
        récupérer une liste de portraits selon les caracs du perso et en choisir un aléatoirement
        celui est choisi est stocké dans une carac mais en cas de changement important (âge, métier, coterie...) on en recalcule un
        """
        portr = portrait.Portrait()
        portraitStr = portr.DeterminerPortraitPersoPrincipal(self, True)
        self.SetCarac(portrait.Portrait.C_PORTRAIT, portraitStr)
        print("portrait str : {}".format(self.GetValCarac(portrait.Portrait.C_PORTRAIT)))
        return self.GetValCarac(portrait.Portrait.C_PORTRAIT)

    def __getitem__(self, key):
        if key not in self.caracs_:
            self.caracs_[key] = ""
        return self.caracs_[key]

    def __setitem__(self, key, val):
        #self.caracs_[key] = val
        self.SetCarac(key, val)

    def __format__(self, format):
        # if(format == 'age'):
        #     return '23'
        return str(self)

    def __getattr__(self, nom):
        """Si Python ne trouve pas l'attribut nommé nom, il appelle
             cette méthode. On affiche une alerte"""
        print("Alerte ! Il n'y a pas d'attribut '{}' dans l'objet '{}' !".format(nom, self))

    def AjouterCarac(self, idCarac, val):
        self.caracs_[idCarac] = val

    def CreerCarac(self, idCarac, valCarac, valeurMin = "", valeurMax = ""):
        self.AjouterCarac(idCarac, valCarac)
        if valeurMin != "":
            self.valsMin_[idCarac] = valeurMin
        if valeurMax != "":
            self.valsMax_[idCarac] = valeurMax

    def SetCarac(self, idCarac, valCarac, valeurMin = "", valeurMax = ""):
        # si la carac n'existe pas encore, la créer
        if not idCarac in self.caracs_:
            self.CreerCarac(idCarac, valCarac, valeurMin, valeurMax)

        self.caracs_[idCarac] = valCarac
        if valeurMin != "":
            self.valsMin_[idCarac] = valeurMin
        if valeurMax != "":
            self.valsMax_[idCarac] = valeurMax

        # modifier certaines caracs peut impliquer des changements implicites à d'autres :
        if idCarac == metier.Metier.C_METIER:
            metierStr = valCarac
            if metierStr != "":
                metierCourant = self.collectionMetiers[metierStr]
                metierCourant.regenererCaracsMetier(self)

    def SetValCaracSiInferieur(self, idCarac, valCarac, valeurMin = "", valeurMax = ""):
        """
        ne modifie la valeur de carac que si elle était précédemment inférieur à la valeur qu'on veut lui donner
        """
        if not idCarac in self.caracs_:
            self.SetValCarac(idCarac, valCarac, valeurMin, valeurMax)
        else:
            valCourante = self.GetValCaracInt(idCarac)
            if valCourante > valCarac:
                return

        self.SetCarac(idCarac, valCarac, valeurMin, valeurMax)

    def SetValCaracSiSuperieur(self, idCarac, valCarac, valeurMin = "", valeurMax = ""):
        """
        ne modifie la valeur de carac que si elle était précédemment inférieur à la valeur qu'on veut lui donner
        """
        if not idCarac in self.caracs_:
            self.SetValCarac(idCarac, valCarac, valeurMin, valeurMax)
        else:
            valCourante = self.GetValCaracInt(idCarac)
            if valCourante < valCarac:
                return

        self.SetCarac(idCarac, valCarac, valeurMin, valeurMax)

    def SetValCarac(self, idCarac, valCarac, valeurMin = "", valeurMax = ""):
        self.SetCarac(idCarac, valCarac, valeurMin, valeurMax)

    def AjouterACarac(self, idCarac, valCarac):
        # si la carac n'existe pas encore, la créer
        if not idCarac in self.caracs_:
            self.CreerCarac(idCarac, 0)

        finalVal = self.caracs_[idCarac] + valCarac
        if idCarac in self.valsMax_ and finalVal > self.valsMax_[idCarac]:
            finalVal = self.valsMax_[idCarac]
        self.SetCarac(idCarac, finalVal)

    def RetirerACarac(self, idCarac, valCarac):
        # si la carac n'existe pas encore, la créer
        if not idCarac in self.caracs_:
            self.CreerCarac(idCarac, 0)

        finalVal = self.caracs_[idCarac] - valCarac
        if idCarac in self.valsMin_ and finalVal < self.valsMin_[idCarac]:
            finalVal = self.valsMin_[idCarac]
        self.SetCarac(idCarac, finalVal)

    def GetValCarac(self, idCarac):
        if ( idCarac not in self.caracs_):
            if idCarac == relationAmoureuse.RelA.C_AMOUREUSES:
                self.caracs_[idCarac] = []
            else:
                self.caracs_[idCarac] = ""
        return self.caracs_[idCarac]

    def GetValCaracInt(self, idCarac):
        if ( idCarac not in self.caracs_):
            self.caracs_[idCarac] = 0
        elif self.caracs_[idCarac] == "":
            self.caracs_[idCarac] = 0
        return self.caracs_[idCarac]

    # get objets tirés des caracs du perso
    def GetQuartier(self):
        valQuartierStr = self.GetValCarac(quartier.Quartier.C_QUARTIER)
        if valQuartierStr == "":
            return None
        return self.collectionQuartiers[valQuartierStr]

    def GetMetier(self):
        valMetierStr = self.GetValCarac(metier.Metier.C_METIER)
        if valMetierStr == "":
            return None
        return self.collectionMetiers[valMetierStr]

    def GetCoterie(self):
        valCoterieStr = self.GetValCarac(coterie.Coterie.C_COTERIE)
        if valCoterieStr == "":
            return None
        cot = self.collectionCoteries[valCoterieStr]
        return cot

    def GetTraits(self):
        """
        renvoi la liste des traits du perso sous forme de 'Trait'
        """
        traitsPerso = []
        for traitK in self.collectionTraits.lTraits_.keys():
            valTrait = self.GetValCarac(traitK)
            if valTrait != "" and valTrait != 0:
                traitsPerso.append(self.collectionTraits[traitK])
        return traitsPerso

    def GetDicoTraits(self):
        """
        renvoi la liste des traits du perso sous forme d'un dico avec comme clé l'id du trait et comme valeur son contenu
        les traits à "" ou 0 ne sont pas renvoyés
        """
        traitsPerso = {}
        for traitK in self.collectionTraits.lTraits_.keys():
            valTrait = self.GetValCarac(traitK)
            if valTrait != "" and valTrait != 0:
                trait = self.collectionTraits[traitK]
                traitsPerso[trait.eTrait_] = valTrait
        return traitsPerso

    # ---------------------------------- affichage des caracs dans l'interface
    def DescriptionTraits(self, traits):
        """
        Description des traits
        """
        str = u""
        for traitK in traits.lTraits_.keys():
            # A FAIRE : cacher trait.Richesse.NOM
            trait = traits[traitK]
            descr = u"{}".format(trait.GetDescription(self))
            if descr != "":
                if str != "":
                    str = u"{}\n".format(str)
                # str = u"{}{} ({})".format(str, descr, trait.eTrait_) # activer pour plus de détails sur els traits
                str = u"{}{}".format(str, descr)
        return str

    def DescriptionBlessuresEtMaladies(self, blessures, maladies):
        """
        Description des blessures et maladies actuelles actuelles du personnage
        """
        str = u""
        # affichage des blessures
        for blessureK in blessures.lBlessures_.keys():
            blessure = blessures[blessureK]
            if self.GetValCarac(blessureK) != u"":
                str = u"{}\n{}".format(str, blessure.nom_)

        # affichage des maladies
        for maladieK in maladies.lMaladies_.keys():
            maladie = maladies[maladieK]
            if self.GetValCarac(maladieK) != u"":
                str = u"{}\n{}".format(str, maladie.nom_)

        # affichage des jours de convalescence
        nbJoursConvalescence = self.GetValCaracInt(pbsante.PbSante.C_JOURS_DHOPITAL)
        if nbJoursConvalescence > 0:
            str = u"{}\nJours de convalescence : {}".format(str, nbJoursConvalescence)

        if str == "":
            str = "Sain"
        return str

    def AffichageAge(self):
        nbJoursVecus = temps.Date(self.caracs_[temps.Date.DATE]).nbJours_ - temps.Date(self.caracs_[temps.Date.DATE_NAISSANCE]).nbJours_
        if isinstance(nbJoursVecus, int):
            nbAnnees = nbJoursVecus/365
            nbJoursPasses = nbJoursVecus%365
            nbMois = nbJoursPasses/30
            return "{} ans, {} mois".format(nbAnnees, nbMois)
        return "??? nbJoursVecus pas int : {}".format(nbJoursVecus)

    def AgeEnAnnees(self):
        if isinstance(self.caracs_[temps.Date.DATE_NAISSANCE], int):
            nbJoursVecus = temps.Date(self.caracs_[temps.Date.DATE]).nbJours_ - temps.Date(self.caracs_[temps.Date.DATE_NAISSANCE]).nbJours_
            nbAnnees = nbJoursVecus/365
            return nbAnnees
        return 0

    def AffichageMetier(self):
        strMetier = u""
        if ( metier.Metier.C_METIER not in self.caracs_):
            strMetier = u"Sans emploi"
        strMetier = self.caracs_[metier.Metier.C_METIER]
        if strMetier == "":
            strMetier = u"Sans emploi"

        # afficher les compétences :
        strComp = u""
        for metierK in self.collectionMetiers.lMetiers_.keys():
            valMetier = self.GetValCaracInt(metierK)
            if valMetier != "" and valMetier != 0:
                txtDiscipline = self.collectionMetiers.lMetiers_[metierK].GetDiscipline()
                if txtDiscipline == "":
                    txtDiscipline = metierK

                txtCompetence = self.collectionMetiers.lMetiers_[metierK].GetTexteCompetence(valMetier)
                strComp = u"{}\n - {} ({})".format(strComp, txtDiscipline, txtCompetence)

        if strComp != "":
            strMetier = u"{}\n\nCompétences : {}".format(strMetier, strComp)

        return strMetier

    def AffichagePortraitPere(self):
        # père
        str = u""
        pere = self.GetValCarac(pnj.Pnj.C_PERE)
        if isinstance(pere, pnj.Pnj) :
            return pere.portraitStr_
        return ""

    def AffichagePortraitMere(self):
        # mère
        str = u""
        mere = self.GetValCarac(pnj.Pnj.C_MERE)
        if isinstance(mere, pnj.Pnj) :
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
                if isinstance(amoureuses[0], pnj.Pnj) :
                    for amoureuse in amoureuses:
                        affichage = affichagePortrait.AffichagePortrait(amoureuse)
                        affichageAmoureuses.append(affichage)
        return affichageAmoureuses

    def AffichagePere(self):
        # père
        str = u""
        pere = self.GetValCarac(pnj.Pnj.C_PERE)
        if isinstance(pere, pnj.Pnj) :
            str = u"{}".format(pere)
        return str

    def AffichageMere(self):
        # mère
        str = u""
        mere = self.GetValCarac(pnj.Pnj.C_MERE)
        if isinstance(mere, pnj.Pnj) :
            str = u"{}".format(mere)
        return str

    def AffichageRichesse(self):
        if ( trait.Richesse.NOM not in self.caracs_):
            return u"Classe moyenne"
        strRichesse = self.collectionTraits[trait.Richesse.NOM].GetDescription(self)
        if strRichesse == "":
            strRichesse = u"Classe moyenne"
        return strRichesse

    def AffichagePossessions(self):
        strPossession = u""
        if ( templiers.Templiers.C_EPEE_SACREE in self.caracs_):
            strPossession = u"{}\n{}".format(strPossession, self.GetValCarac(templiers.Templiers.C_EPEE_SACREE))

        if strPossession == "":
            strPossession = u"Aucune possession"
        return strPossession

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

    def AffichageReligion(self):
        if ( religion.Religion.C_RELIGION not in self.caracs_):
            return "Sans religion"
        return self.caracs_[religion.Religion.C_RELIGION]

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

    def GetDateDuJour(self):
        nbJours = self.caracs_[temps.Date.DATE]
        return temps.Date(nbJours)

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

    # FONCTIONS GENERIQUES
    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        if len(self.caracs_) == 0:
            return u"Aucune carac."
        str = u"Situation actuelle : "
        for carac in self.caracs_.keys():
            str = "{} {} ({}), ".format(str, self.caracs_[carac], carac)
        return str
