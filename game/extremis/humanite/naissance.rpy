# fichier où sont générés les phrases d'ambiance à afficher quand il ne se passe rien durant un mois particulier

init -5 python:
    import random
    from despin.gen_vie import declencheur
    from despin.gen_vie import selecteur
    from despin.gen_vie import proba
    from despin.abs import condition
    from extremis.humanite import trait
    from extremis.humanite import pnj
    from extremis.constitution import temps
    from extremis.geographie import quartier
    from extremis.coteries.elfes import elfes
    from extremis.coteries.orks import orks
    from extremis.coteries import coterie
    from extremis.humanite import identite
    from extremis.techno import bionique

    def genererDateNaissance(situation, ageActuel=16):
        # le jeu commence quand le personnage a 16 and et donc éligible pour ses quatre années d'univesrsité coteries
        # avant sa majorité idéologique de 20 ans
        # donc la date de naissance est l'actuelle moins 16 ans pile :
        nbJoursDateNaissance = situation[temps.Date.DATE] - 365*ageActuel
        situation[temps.Date.DATE_NAISSANCE] = nbJoursDateNaissance

    def genererTraits(situation, tousLesTraits):
        # sélectionne aléatoirement les traits principaux du personnage à la naissance
        nbTraits = 3 + random.randint(0,6)
        m_Traits = []
        while nbTraits > 0:
            trait = tousLesTraits.getTraitAleatoire()
            if trait.PeutEtrePrisALaNaissance():
                situation[trait.eTrait_] = trait.GetValeurALaNaissance()
                nbTraits = nbTraits - 1

        quartierDeDepart = situation.collectionQuartiers.getQuartierAleatoire(True)
        situation.SetCarac(quartier.Quartier.C_QUARTIER, quartierDeDepart.nom_)

        # A FAIRE : générer nom et prénom

        # A FAIRE : génération classe sociale :
        # QString clas = ClasseSociale::GetClasseSocialeAleatoire();
        # effetNarrationVide->AjouterChangeurDeCarac(ClasseSociale::C_CLASSE_SOCIALE, clas);
        return

    def genererTruand(situation, tousLesTraits):
        """
        création d'un perso qui a de très fortes chances de mal tourner
        """
        situation[trait.Sexualite.NOM] = 11
        situation[trait.Richesse.NOM] = -13
        situation[trait.Sincerite.NOM] = -13
        situation[trait.Honorabilite.NOM] = -13
        situation[trait.Industrie.NOM] = -13
        situation[trait.Franchise.NOM] = -13
        situation[trait.Prudence.NOM] = -13
        situation[trait.Altruisme.NOM] = -13
        situation[trait.Cupidite.NOM] = 11
        situation[trait.Opportunisme.NOM] = 11
        situation[trait.Violence.NOM] = 11
        # A FAIRE Mathieu : génération de la famille
        # Famille::GenererParents(effetNarrationVide);

        # TODO : générer ces données aléatoirement quand la bdd de noms sera ajoutée
        situation[u"Nom"] = "Deharbe"
        situation[u"Prénom"] = "Mathieu"

        # A FAIRE : génération classe sociale :
        # QString clas = ClasseSociale::GetClasseSocialeAleatoire();
        # effetNarrationVide->AjouterChangeurDeCarac(ClasseSociale::C_CLASSE_SOCIALE, clas);
        return

    def genererElfePotentiel(situation, tousLesTraits):
        """
        création d'un perso qui a de très fortes chances de devenir elfe
        """
        situation[trait.Nature.NOM] = 11
        situation[trait.Artiste.NOM] = 11
        situation[trait.Serenite.NOM] = 11
        situation[trait.Sensibilite.NOM] = 11
        situation[trait.Violence.NOM] = -13
        situation[trait.Cupidite.NOM] = -13
        situation[trait.Ambition.NOM] = -13
        return

    def genererElfe(situation, tousLesTraits):
        elfesCot = situation.collectionCoteries[elfes.Elfes.ID]
        elfesCot.RejoindreCoterie(situation)
        situation.SetValCarac(coterie.Coterie.Carac_NB_UNIV, coterie.Coterie.Carac_NB_UNIV)
        return genererTraits(situation, tousLesTraits)

    def genererOrk(situation, tousLesTraits):
        orksCot = situation.collectionCoteries[orks.Orks.ID]
        orksCot.RejoindreCoterie(situation)
        situation.SetValCarac(coterie.Coterie.Carac_NB_UNIV, coterie.Coterie.Carac_NB_UNIV)
        situation[trait.Constitution.NOM] = 3
        return genererTraits(situation, tousLesTraits)

    def genererAventurier(situation, tousLesTraits):
        """
        création d'un perso qui a de très fortes chances de devenir aventurier, conquistador,
        bandit peut-être
        """
        situation[trait.Ambition.NOM] = 11
        situation[trait.Opportunisme.NOM] = 11
        situation[trait.Cupidite.NOM] = 11
        situation[trait.Constitution.NOM] = 11
        situation[trait.Pragmatisme.NOM] = 11
        situation[trait.Violence.NOM] = 11
        situation[trait.Prudence.NOM] = -13
        situation[trait.Altruisme.NOM] = -13
        situation[trait.Industrie.NOM] = -13
        situation[trait.Sexualite.NOM] = -13
        situation[trait.Poids.NOM] = -13
        situation[trait.Richesse.NOM] = -13

        quartierDeDepart = situation.collectionQuartiers.getQuartierAleatoire(True)
        situation.SetCarac(quartier.Quartier.C_QUARTIER, quartierDeDepart.nom_)

        return

    def genererParents(situation):
        global coteries_
        pere = pnj.GenererPNJPapa(situation)
        situation.SetValCarac(pnj.Pnj.C_PERE, pere)
        mere = pnj.GenererPNJMaman(situation)
        situation.SetValCarac(pnj.Pnj.C_MERE, mere)

        # genererGenererNomDeDepart du perso principal
        # nom de son père
        nomStr = pere.nom_

        # si pas de nom, nom de sa mère
        if nomStr == "":
            nomStr = mere.nom_

        # prénom de la coterie de sa mère
        prenomStr = "rien"
        if mere.coterie_ != "":
            coterieObj = coteries_[mere.coterie_]
            prenomStr = coterieObj.CreerPrenom(True)

        situation.SetValCarac(identite.Identite.C_PRENOM, prenomStr)
        situation.SetValCarac(identite.Identite.C_NOM, nomStr)

label naissance:
    $ genererDateNaissance(situation_, 15)
    $ genererTraits(situation_, traits_)
    # $ genererOrk(situation_, traits_)
    # $ genererTruand(situation_, traits_) # génération de traits pour un perso typé truand agressif
    # $ genererAventurier(situation_, traits_) # génération de traits pour un perso typé truand agressif
    $ genererParents(situation_)
    # $ situation_[bionique.BioniqueLongevite.NOM] = 10 # gross amélioration de longévité
    jump debut_cycle
