label evtRien_saints:
    menu:
        "hop"
        "youpi":
            pass
    $ dateDuJour = situation_.GetDateDuJour()
    $ jour = dateDuJour.numJourGregorien
    $ mois = dateDuJour.numMoisGregorien
    "Vous êtes le [jour] [mois]."
    if dateDuJour.numMoisGregorien == 4:
        # avril
        if dateDuJour.numJourGregorien == 13:
            scene bg saint_ermenegilde
            "Aujourd'hui vous fêtez Saint Erménégilde. Prince wisigoth fils du roi d'espagne il fut élevé dans la foi arienne."
            "Il épousa la princesse catholique Ingonde et se convertit. Emprisonné, il fut décapité après aoir refusé la communion offerte par un prêtre arrien."
            jump fin_cycle
    if dateDuJour.numMoisGregorien == 10:
        # octobre
        if dateDuJour.numJourGregorien == 24:
            "Aujourd'hui vous fêtez Saint Florentin. C'est un fils du roi d'Écosse qui a émigré à Bonnet dans la Meuse. Il y est devenu un guérisseur miraculeux dont le gisant provoque aujourd'hui encore des guérisons spontanées des troubles mentaux."
            jump fin_cycle





    "PAS FAIT"
    jump fin_cycle
