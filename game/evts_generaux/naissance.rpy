# fichier où sont générés les phrases d'ambiance à afficher quand il ne se passe rien durant un mois particulier

init -5 python:
    import random
    from despin.gen_vie import declencheur
    from despin.gen_vie import selecteur
    from despin.gen_vie import proba
    from despin.abs import condition
    from extremis.humanite import trait
    from extremis.constitution import temps

    def genererDateNaissance(situation):
        # le jeu commence quand le personnage a 16 and et donc éligible pour ses quatre années d'univesrsité coteries
        # avant sa majorité idéologique de 20 ans
        # donc la date de naissance est l'actuelle moins 16 ans pile :
        nbJoursDateNaissance = situation[temps.Date.DATE] - 365*18
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

        # situation[u"Pilotage"] = 1 # tmp A FAIRE : ajouter un événement (passage de permis) pour gagner ce trait à peu près sûr entre 18 et 25 ans)

        # A FAIRE Mathieu : génération de la famille
        # Famille::GenererParents(effetNarrationVide);

        # TODO : générer ces données aléatoirement quand la bdd de noms sera ajoutée
        situation[u"Nom"] = "Deharbe"
        situation[u"Prenom"] = "Mathieu"

        # A FAIRE : génération classe sociale :
        # QString clas = ClasseSociale::GetClasseSocialeAleatoire();
        # effetNarrationVide->AjouterChangeurDeCarac(ClasseSociale::C_CLASSE_SOCIALE, clas);
        return

label naissance:
    $ genererDateNaissance(situation_)
    $ genererTraits(situation_, traits_)
    jump debut_cycle
