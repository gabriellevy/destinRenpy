
image superieur_hierarchique = "administration/homme_elegant_barbu.png"
image investisseur = "coteries/victorien/jeune_monocle.png"
image investisseuse = "coteries/victorien/belle_jeune_femme.png"

define ch = Character('Chef', who_outlines=[(2, "#894646",1,1)], color="#580404")
define inv = Character('M. Maxwell', color="#e30909")
define inve = Character('Mlle. Dowe', color="#22002c")

init -5 python:
    import random
    from despin.gen_vie import declencheur
    from despin.gen_vie import selecteur
    from despin.gen_vie import proba
    from despin.abs import condition
    from extremis.socio_eco import metier
    from despin.reglages import filtres_action

    def AjouterEvtsAdministratif():
        global selecteur_
        conditionAdministratif = condition.Condition(metier.Metier.ADMINISTRATIF, 1, condition.Condition.EGAL)

        decVisiteInvestisseurs = declencheur.Declencheur(0.02, "decVisiteInvestisseurs")
        decVisiteInvestisseurs.AjouterCondition(conditionAdministratif)
        selecteur_.ajouterDeclencheur(decVisiteInvestisseurs)

        # exemple d'ajout d'événement :
        # conditionExemple = condition.Condition(metier.Metier.ADMINISTRATIF, 1, condition.Condition.EGAL) # condition de base de l'événement
        # probaExemple = proba.Proba(0.02) # faible chance d'arriver
        # conditionDeharbe = condition.Condition("Nom", "Deharbe", condition.Condition.EGAL)
        # probaVisiteInvestisseurs.ajouterModifProbaViaVals(10.0, conditionDeharbe) # sauf si nommé Deharbe : très forte chance d'arriver
        # decExemple = declencheur.Declencheur(0.02, "decExemple") # déclencheur avec en param la proba et le nom du label à suivre
        # decExemple.AjouterCondition(conditionExemple)
        # selecteur_.ajouterDeclencheur(decExemple)

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

# exemple de label d'événement (lié à l'exemple de déclencheur commenté ci dessus)
# label decExemple:
    # $ actionDebutAdministratif()
    # actions etc classiques
    # $ actionFinAdministratif()
    # jump debut_cycle


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
    show investisseuse at center
    with dissolve
    inve "D'accord, tant que nous avons le temps de visiter les installations en détail ensuite."

    menu:
        "En profiter pour vous faire remarquer en vantant votre travail.":
             jump decVisiteInvestisseurs_frime
        "Flatter votre directeur pour vous faire bien voir.":
             jump decVisiteInvestisseurs_flatterie
        "Travailler sérieusement et discrètement.":
             jump decVisiteInvestisseurs_discret
        "Profiter de cette diversion pour voler des choses au bureau." if filtre_.themes_[filtres_action.FiltreAction.VOL] != "":
            jump decVisiteInvestisseurs_vol
        "Tenter de se faire remarquer par Mlle Dowe." if filtre_.themes_[filtres_action.FiltreAction.AMOUR] != "":
            jump decVisiteInvestisseurs_drague

    label decVisiteInvestisseurs_discret:
        hide superieur_hierarchique
        with moveoutleft
        hide investisseuse
        with moveoutright
        hide investisseur
        with moveoutright
        "Vous préférez rester discret comme le souhaitait votre chef."
        "Le chef semble satisfait de comment s'est déroulé la visite et la journée se passe tranquillement sans événement notable."
        show superieur_hierarchique at left
        with moveinleft
        ch "Bonne soirée [situation_[Prénom]]. À demain."
        jump decVisiteInvestisseurs_fin

    label decVisiteInvestisseurs_drague:
        "youpi drague PAS FAIT"
        jump decVisiteInvestisseurs_fin

    label decVisiteInvestisseurs_vol:
        "voler c'est pas cool PAS FAIT"
        jump decVisiteInvestisseurs_fin

    label decVisiteInvestisseurs_fin:

    $ actionFinAdministratif()
    jump debut_cycle























    # tmp
