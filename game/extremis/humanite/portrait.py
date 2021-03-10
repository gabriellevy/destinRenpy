import random
from extremis.socio_eco.metiers import metier
from extremis.coteries import coterie

class Portrait:

    C_PORTRAIT = u"Portrait"

    def DeterminerPortraits(self, situation, masculin):
        """
        retourne l'adresse du portrait à afficher pour le perso courant
        """
        portraits = []
        portraitCourant = situation.GetValCarac(Portrait.C_PORTRAIT)
        age = situation.AgeEnAnnees()
        cot = situation.GetCoterie()
        met = situation.GetMetier()
        traitsPerso = situation.GetTraits()

        if cot != None:
            portraits = cot.GenererPortraits(age, masculin, met, portraits)

        if met != None:
            portraits = met.GenererPortraits(age, masculin, met, portraits)

        if len(portraits) == 0:
            # portrait neutres indépendants du métier et de la coterie
            if masculin:
                if age >= 8:
                    if age >= 14:
                        if age <= 40:
                            portraits.append("images/portraits/portrait_15-40.jpg")
                            portraits.append("images/portraits/portrait_15-40_b.jpg")
                            portraits.append("images/portraits/portrait15-35.png")
                        if age >= 20:
                            if age >= 40:
                                portraits.append("images/portraits/portrait40+.png")
                                if age >= 60:
                                    portraits.append("images/portraits/portrait_forgeron_60+.jpg")
                                    portraits.append("images/portraits/portrait60+_miserable.png")
                                if age <= 60:
                                    portraits.append("images/portraits/portrait40-60.png")
                            if age <= 60:
                                portraits.append("images/portraits/portrait_bucheron_20-60.jpg")
                                if age <= 50:
                                    if age <= 40: # 20 à 40
                                        portraits.append("images/portraits/portrait20-40.png")
                                        portraits.append("images/portraits/portrait20-40_2.png")
                                        portraits.append("images/portraits/20-40.jpg")
                                    portraits.append("images/portraits/portrait_20-50.jpg")
                                    portraits.append("images/portraits/portrait20-50_2.png")
                                    portraits.append("images/portraits/portrait20-50_3.png")
                                    portraits.append("images/portraits/portrait20-50_4.png")
                    if age <= 15:
                        portraits.append("images/portraits/8-15.jpg")
            else:
                if age >= 14:
                    if age >= 20:
                        if age <= 40:
                            portraits.append("images/portraits/F13-20.jpg")
                    if age <= 40:
                        if age <= 20:# entre 14 et 20
                            portraits.append("images/portraits/F13-20.jpg")
                        portraits.append("images/portraits/Fportrait14-40.png")

        if len(portraits) == 0:
            portraits = ["images/portraits/inconnu.jpg"]

        if portraits.count(portraitCourant) == 0:
            portraitCourant = random.choice(portraits)

        return portraitCourant
