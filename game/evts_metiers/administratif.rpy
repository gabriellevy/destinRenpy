
image superieur_hierarchique = "administration/homme_elegant_barbu.png"
image investisseur = "coteries/victorien/jeune_monocle.png"

define ch = Character('Chef', who_outlines=[(2, "#894646",1,1)], color="#580404")
define inv = Character('M. Maxwell', color="#e30909")

init -5 python:
    import random
    from despin.gen_vie import declencheur
    from despin.gen_vie import selecteur
    from despin.gen_vie import proba
    from despin.abs import condition
    from despin.extremis import metier

    def AjouterEvtsAdministratif():
        global selecteur_
        conditionAdministratif = condition.Condition(metier.Metier.ADMINISTRATIF, 1, condition.Condition.EGAL)

        decVisiteInvestisseurs = declencheur.Declencheur(400.02, "decVisiteInvestisseurs")
        decVisiteInvestisseurs.AjouterCondition(conditionAdministratif)
        selecteur_.ajouterDeclencheur(decVisiteInvestisseurs)

    # attention des actions sont à exécuter au début et à al fin de chaque événement administratif :
    def actionDebutAdministratif():
        global situation_
        renpy.transition(dissolve)
        renpy.scene()
        renpy.show("bg bureau")
        # metier.regenererCaracsMetier(situation_)

    # attention des actions sont à exécuter au début et à al fin de chaque événement administratif :
    def actionFinAdministratif():
        global situation_
        # metier.regenererCaracsMetier(situation_)


label decVisiteInvestisseurs:
    $ actionDebutAdministratif()
    "On dit qu'une délégation de très importants investisseurs Victoriens va visiter les bureaux aujourd'hui."
    "Votre chef fait le tour du personnel. Il semble très tendu."
    show superieur_hierarchique at left
    with moveinleft
    ch "Bonjour [situation_[Prénom]]. Aujourd'hui est un jour très important. Je compte sur vous pour faire bonne impression."
    ch "Contentez vous bien bien travailler ou au moins d'en avoir l'air et restez discret."
    "Avant que vous puissiez répondre un homme apparaît."
    show investisseur at right
    with moveinright
    inv "Bonjour. Votre secrétaire m'a permis d'entrer pour vous retrouver et observer les locaux."
    inv "J'espère que vous ne m'en voulez pas de ne pas vous avoir attendu à l'entrée."
    ch "Non vous avez bien fait. Suivez moi dans la salle de réunion, nous ferons le tour des bureaux après la présentation de 9h."
    menu:
        "En profiter pour vous faire remarquer en vantant votre travail.":
             jump decVisiteInvestisseurs_frime
        "Flatter votre directeur pour vous faire bien voir.":
             jump decVisiteInvestisseurs_flatterie
        "Travailler sérieusement et discrètement.":
             jump decVisiteInvestisseurs_discret

    label decVisiteInvestisseurs_discret:
        "Vous préférez rester discret comme le souhaitait votre chef."
        "Le chef semble satisfait de comment s'est déroulé la visite et lLa journée se passe tranquillement sans événement notable."
    $ actionFinAdministratif()
    jump debut_cycle
