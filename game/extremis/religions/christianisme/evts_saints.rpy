label evtRien_saints:
    # A FAIRE : ce pourrait être amusant d'ajouter des effets à certains jours des saints selon leur rôle (mais bon en même temps ils arrivent si rarement...)
    $ dateDuJour = situation_.GetDateDuJour()
    $ jour = dateDuJour.numJourGregorien
    $ mois = dateDuJour.numMoisGregorien

    if dateDuJour.numMoisGregorien == 1:
        # janvier
        if dateDuJour.numJourGregorien == 21:
            scene bg sainte_agnes
            "Aujourd'hui vous fêtez Sainte Agnès, vierge et martyre. Elle fut égorgée à douze au cours de la persécution de Dioclétien."
            jump fin_cycle

    if dateDuJour.numMoisGregorien == 2:
        # février
        if dateDuJour.numJourGregorien == 1:
            "Aujourd'hui 1 février vous fêtez Sainte Brigitte d'Irlande. Fondatrice et abesse du monastère de Kildare. Elle changeait l'eau en bière."
            jump fin_cycle
        if dateDuJour.numJourGregorien == 9:
            "Aujourd'hui 9 février vous fêtez Sainte Apolline, diaconesse d'Alexandrie. On lui cassa les dents et la mâchoire lors des persécutions. Elle fut brûlée pour avoir refusé de renier le Christ. Elle est al sainte patronne des dentistes."
            jump fin_cycle
        if dateDuJour.numJourGregorien == 13:
            "Aujourd'hui 9 février vous fêtez les Saintes Fosca et Maure. Fosca appartenait à une famille païenne de Ravenne et Maure était sa nourrice."
            "Quand Fosca se convertit au catholicisme elle convainquit Maure de la suivre. Mais elles furent dénoncées par le père de Fosca pendant les persécutions du 3ème siècle, jugées et décapitées."
            jump fin_cycle
        if dateDuJour.numJourGregorien == 18:
            scene bg fra_angelico
            "Aujourd'hui 18 février vous fêtez le bienheureux Fra Angelico. Alors qu'il était déjà peintre, sa vocation le conduisit au couvent Dominicain de Fiesole, où il prit le nom de Giovanni. Son art fut sa prédication."
            "Il oeuvra en toscane et au Vatican. Il refusa le siège épiscopal de Florence qui lui offfrait le pape. Il est le protecteur des peintres et des artistes en général."
            jump fin_cycle

    if dateDuJour.numMoisGregorien == 3:
        # mars
        if dateDuJour.numJourGregorien == 1:
            "Aujourd'hui vous fêtez Saint Aubin de Verceil qui fit reconstruire la cathédrale de son évéché après les dégâts qu'elle subit lors des combats contre les Goths et les Huns."
            jump fin_cycle
        if dateDuJour.numJourGregorien == 24:
            "Aujourd'hui vous fêtez le bienheureux Diego Joseph de Cadix qui était un grand missionnaire espagnol du XVIIIème siècle."
            jump fin_cycle

    if dateDuJour.numMoisGregorien == 4:
        # avril
        if dateDuJour.numJourGregorien == 2:
            "Aujourd'hui 2 avril vous fêtez Saint François de Paule.Après 3 ans passés au couvent il se retira dans un ermitage où il mena une vie de prière, de jeûne, de travaile t de mortification. De nombreux disciples l'imitèrent et il devint Saint Patron des ermites."
            jump fin_cycle
        if dateDuJour.numJourGregorien == 4:
            "Aujourd'hui 4 avril vous fêtez Saint Isidore de Séville. Né en 560 dans une famille noble de Carthagène il est devenu évèque et a dirigé le diocèse pendant plus de 30 ans. Son ministère a été marqué par la conversion des wisigoths et l'organisation de l'église espagnole."
            jump fin_cycle
        if dateDuJour.numJourGregorien == 11:
            "Aujourd'hui 11 avril vous fêtez Saint Stanislas."
            "Grand prédicateur et homme charitable il eut à combattre les mauvaises moeurs du roi BoleslavII. Après de multiples récidives Stanislas l'excommunia et celui ci se vengea en le tuant alors qu'il célébrait la messe."
            jump fin_cycle
        if dateDuJour.numJourGregorien == 13:
            scene bg saint_ermenegilde
            "Aujourd'hui vous fêtez Saint Erménégilde. Prince wisigoth fils du roi d'espagne il fut élevé dans la foi arienne."
            "Il épousa la princesse catholique Ingonde et se convertit. Emprisonné, il fut décapité après aoir refusé la communion offerte par un prêtre arrien."
            jump fin_cycle

    if dateDuJour.numMoisGregorien == 5:
        # mai
        if dateDuJour.numJourGregorien == 2:
            "Aujourd'hui vous fêtez Saint Job, qui vécu dans le nord de l'arabie vers 1500 avant Jésus-Christ."
            "Parvenu au faîte de la prospérité -il avait 7 files et 3 filles, des champs et des troupeaux-, il faut frappé de malheurs indicibles qui le privèrent de tous ses biens, de ses enfants, et altéran sa santé."
            "Il supporta cette adversité parce qu'il la jugeait dictée par la volonté de Dieu."
            jump fin_cycle
        if dateDuJour.numJourGregorien == 10:
            "Aujourd'hui 2 mai vous fêtez Saint Boris, tsar de Bulgarie. Au IXème siècle se fait instruire dans la religion chrétienne et baptiser avec toute son armée."
            "En 888 il décide de rejoindre un monastère et de laisser le pays à son fils Vladimir. Mais celui ci tente de rétablir le paganisme et Boris doit le destituer par la force pour mettre en place son autre fils Siméon, avant de se retirer définitivement."
            jump fin_cycle
        if dateDuJour.numJourGregorien == 22:
            scene bg presentation_marie
            "Aujourd'hui vous fêtez Sainte Rita de Cascia. Après l'assassinat de son mari ses deux fils voulurent se venger. Comme ils refusaient de pardonner elle pria Dieu de les faire mourir plutôt qu'ils se tâchent les mains de sang."
            "Elle reçut en signe de sa dévotion une stigmate au front telle une épine."
            jump fin_cycle

    if dateDuJour.numMoisGregorien == 6:
        # juin
        if dateDuJour.numJourGregorien == 2:
            "Aujourd'hui vous fêtez Sainte Blandine, une jeune esclave martyr qui fut emprisonnée dans un filet puis jetée à un taureau furieux."
            jump fin_cycle
        if dateDuJour.numJourGregorien == 17:
            "Aujourd'hui vous fêtez Saint Hervé, né aveugle d'une mère ermite séparée de son mari le barde Hyvarnion."
            "Il est élevé par un moine puis part en quête d'un ermitage, guidé apr un loup qu'il avait apprivoisé. Il se fixe à Lanhouarneau. À l'approche de la mort il s'écrie : "
            "{i}\"Je vois le ciel ouvert, le ciel ma patrie. Je veux m'y envoler. Je vois mon père et ma mère dans la gloire et la beauté je vois mes frères, les hommes de mon pays. Des choeurs d'anges portés sur leurs ailes volent autour de leurs têtes, comme autant d'abeilles dans un champs de fleur.\"{/i}"
            jump fin_cycle

    if dateDuJour.numMoisGregorien == 8:
        # août
        if dateDuJour.numJourGregorien == 17:
            "Aujourd'hui 17 août vous fêtez Saint Hyacinthe, le grand missionnaire et apôtre de la Pologne.Il s'illustre par ses nombreux miracles, il traverse notamment la Vistule avec plusieurs de ses frères, sur son manteau répandu à la surface des eaux."
            "Sa prédication le mènera à visiter de nombreux pays -Poméranie, Danemark, Prusse, Norvège, Lithuanie, et jusqu'en Russie- dans lesquels il fonde des monastères. Informé par la vierge de la date de sa mort, ils'éteint dans la foi le 17 août 1257."
            jump fin_cycle
        if dateDuJour.numJourGregorien == 22:
            scene bg vierge_marie
            "Aujourd'hui vous fêtez la bienheureuse Vierge Marie Reine."
            jump fin_cycle
        if dateDuJour.numJourGregorien == 29:
            scene bg saint_jean_baptiste
            "Aujourd'hui vous fêtez Saint Jean-Baptiste. Précurseur de Jésus-Christ il exhorta le peuple à se convertir en attendant la venue du messie, prêchant et baptisant sans relâche."
            "Il dénonçait les moeurs de Hérode Antipas et de sa maîtresse Hérodiade, qui le jettèrent en prison. "
            "Plus tard lors d'un banquet Salomé, fille d'Hérodiade, dansa si merveilleusement que le roi lui accorda un souhait. Elle souhaita la tête de Jean Baptiste qui fut décapité et dont la tête lui fut apportée à sa table."
            jump fin_cycle

    if dateDuJour.numMoisGregorien == 10:
        # octobre
        if dateDuJour.numJourGregorien == 24:
            "Aujourd'hui 24 octobre vous fêtez Saint Florentin. C'est un fils du roi d'Écosse qui a émigré à Bonnet dans la Meuse. Il y est devenu un guérisseur miraculeux dont le gisant provoque aujourd'hui encore des guérisons spontanées des troubles mentaux."
            jump fin_cycle
        if dateDuJour.numJourGregorien == 26:
            "Aujourd'hui 26 octobre vous fêtez Saint Démétrius. Démétrius, élevé dans la foi chrétienne, fut nommé proconsul de macédoine par Maximin et chargé d'éradiquer le christianisme."
            "Mais Démétrius s'empressa au contraire de rendre gloire au christ et d'enseigner la foi. Furieux l'empereur décida d'aller à Thessalonique y massacrer tous les chrétiens. Apprenant cela, Démétrius donna tous ses biens aux pauvres et se prépara au martyr."
            "Maximin le fit arrêter et assassiner."
            jump fin_cycle
        if dateDuJour.numJourGregorien == 28:
            "Aujourd'hui 28 octobre vous fêtez Saint Jude Thadée, apôtre de Jésus."
            jump fin_cycle

    if dateDuJour.numMoisGregorien == 11:
        # novembre
        if dateDuJour.numJourGregorien == 21:
            "Aujourd'hui 21 novembre vous fêtez la présentation de la vierge Marie au Temple de Jérusalem."
            jump fin_cycle

    if dateDuJour.numMoisGregorien == 12:
        # décembre
        if dateDuJour.numJourGregorien == 7:
            scene bg saint_ambroise
            "Aujourd'hui 7 décembre vous fêtez Saint Ambroise. Il fut évêque de Milan et un grand docteur de l'église acclamé par le peuple. C'est le saint protecteur des abeilles, des apiculteurs, et de tous ceux qui travaillent la cire."
            jump fin_cycle
        if dateDuJour.numJourGregorien == 26:
            "Aujourd'hui 26 décembre vous fêtez Saint Étienne. Il fut l'un des sept diacres de Jérusalem nommés par les apôtres. Il fut accusé d'avoir prononcé des paroles blasphématoires contre Moïse et contre Dieu."
            "Grâce à sa profonde connaissance des écritures il mit en lumière comment les juifs résistaient à l'esprit saint et refusaient de reconnaître le messie. Il fut alors lapidé."
            jump fin_cycle

    "fête du saint de ce jour : [jour] [mois] PAS FAIT"

    jump fin_cycle
