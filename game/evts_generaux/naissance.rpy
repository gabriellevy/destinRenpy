# fichier où sont générés les phrases d'ambiance à afficher quand il ne se passe rien durant un mois particulier

init -5 python:
    import random
    from despin.gen_vie import declencheur
    from despin.gen_vie import selecteur
    from despin.gen_vie import proba
    from despin.abs import condition
    from extremis.humanite import trait

    def genererTraits(situation):
        # sélectionne aléatoirement les traits principaux du personnage à la naissance
        situation[u"Cupidité"] = -5
        situation[u"Sincérité"] = 5
        situation[u"Opportunisme"] = 1

        # TODO : générer ces données aléatoirement quand la bdd de noms sera ajoutée
        situation[u"Nom"] = "Deharbe"
        situation[u"Prenom"] = "Mathieu"
        return

label naissance:
    $ genererTraits(situation_)
    "Post naissance : [situation_]"
    # "Vous êtes un jeune homme de 15 ans."
    # "Vous vous appelez [situation_[Prenom]] [situation_[Nom]]."
    jump debut_cycle
