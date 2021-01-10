# fichier où sont générés les phrases d'ambiance à afficher quand il ne se passe rien durant un mois particulier

init -5 python:
    import random
    from despin.gen_vie import declencheur
    from despin.gen_vie import selecteur
    from despin.gen_vie import proba
    from despin.abs import condition
    from extremis.humanite import trait

    def genererTraits(situation, tousLesTraits):
        # sélectionne aléatoirement les traits principaux du personnage à la naissance
        nbTraits = 3 + random.randint(0,6)
        m_Traits = []
        while nbTraits > 0:
            trait = tousLesTraits.getTraitAleatoire()
            situation[trait.eTrait_] = random.randint(-10,10)
            nbTraits = nbTraits - 1

        # situation[u"Cupidité"] = 5
        # situation[u"Sincérité"] = -5
        # situation[u"Opportunisme"] = 5

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
    $ genererTraits(situation_, traits_)
    "Post naissance : [situation_]"
    # "Vous êtes un jeune homme de 15 ans."
    # "Vous vous appelez [situation_[Prenom]] [situation_[Nom]]."
    jump debut_cycle
