import random
from abs.humanite import metier
from extremis.coteries import coterie
from abs.humanite import portrait

class PortraitDestin(portrait.Portrait):

    def DeterminerPortraitPersoPrincipal(self, situation, masculin):
        """
        retourne l'adresse du portrait à afficher pour le perso courant
        """
        ageAnnees = situation.AgeEnAnnees()
        cotObj = situation.GetCoterie()
        metObj = situation.GetMetier()
        traitsPerso = situation.GetDicoTraits()

        return self.DeterminerPortraits(situation, ageAnnees, cotObj, metObj, traitsPerso, masculin)

    def DeterminerPortraits(self, situation, ageAnnees, cotObj, metObj, valeursTraits, masculin):
        """
        retourne l'adresse du portrait à afficher pour le perso courant
        valeursTraits : dico contenant en clé le nom des traits possédés par le personnage et en valeur leur niveau
        """
        portraits = []
        portraitCourant = situation.GetValCarac(portrait.Portrait.C_PORTRAIT)

        if cotObj is not None:
            portraits = cotObj.GenererPortraits(ageAnnees, masculin, metObj, portraits, valeursTraits)

        if metObj is not None:
            portraits = metObj.GenererPortraits(ageAnnees, masculin, portraits, valeursTraits)

        if len(portraits) == 0:
            # portrait neutres indépendants du métier et de la coterie
            if masculin:
                if ageAnnees >= 8:
                    if ageAnnees >= 14:
                        if ageAnnees <= 40:
                            portraits.append("images/portraits/portrait_15-40.jpg")
                            portraits.append("images/portraits/portrait_15-40_b.jpg")
                            portraits.append("images/portraits/portrait15-35.png")
                        if ageAnnees >= 20:
                            if ageAnnees >= 40:
                                portraits.append("images/portraits/portrait40+.png")
                                if ageAnnees >= 60:
                                    portraits.append("images/portraits/portrait_forgeron_60+.jpg")
                                    portraits.append("images/portraits/portrait60+_miserable.png")
                                if ageAnnees <= 60:
                                    portraits.append("images/portraits/portrait40-60.png")
                            if ageAnnees <= 60:
                                portraits.append("images/portraits/portrait_bucheron_20-60.jpg")
                                if ageAnnees <= 50:
                                    if ageAnnees <= 40: # 20 à 40
                                        portraits.append("images/portraits/portrait20-40.png")
                                        portraits.append("images/portraits/portrait20-40_2.png")
                                        portraits.append("images/portraits/20-40.jpg")
                                    portraits.append("images/portraits/portrait_20-50.jpg")
                                    portraits.append("images/portraits/portrait20-50_2.png")
                                    portraits.append("images/portraits/portrait20-50_3.png")
                                    portraits.append("images/portraits/portrait20-50_4.png")
                    if ageAnnees <= 15:
                        portraits.append("images/portraits/8-15.jpg")
            else:
                # femmes
                if ageAnnees >= 14:
                    if ageAnnees >= 20:
                        if ageAnnees <= 40:# entre 20 et 40
                            portraits.append("images/portraits/F13-20.jpg")
                        if ageAnnees >= 30:
                            if ageAnnees <= 50:
                                portraits.append("images/portraits/femme30_50.jpg")
                    # age >= 14
                    if ageAnnees <= 40:
                        if ageAnnees <= 20:# entre 14 et 20
                            portraits.append("images/portraits/F13-20.jpg")
                        portraits.append("images/portraits/Fportrait14-40.png")

        if len(portraits) == 0:
            portraits = ["images/portraits/inconnu.jpg"]

        if portraits.count(portraitCourant) == 0:
            portraitCourant = random.choice(portraits)

        return portraitCourant
