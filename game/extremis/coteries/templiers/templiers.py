from extremis.coteries import coterie
from abs.humanite import metier
from abs.humanite import trait
from extremis.geographie import quartier
import random

class Templiers(coterie.Coterie):

    NOM = u"Ordre du Temple"
    ID = u"templiers"

    C_RICHESSE = "Richesse du temple" # tous les templiers ont renoncé aux biens matériels, ils ont tous cette richesse (basse)
    RICHESSE_TEMPLE = -4 # richesse de départ du temple, et peu de chance de beaucoup bouger
    C_EPEE_SACREE = u"Épée sacrée"

    def __init__(self):
        self.nom_ = Templiers.NOM
        self.id_ = Templiers.ID
        self.quartier_ = quartier.SaintDenis.NOM

    def getLabelUniversite(self):
        return "univTempliers"

    def GetTraitsCompatibles(self):
        """
        si le perso a ces caracs il a plus de chances de vouloir rejoindre cette coterie
        """
        return [ \
            trait.Spiritualite.NOM, \
            trait.Honorabilite.NOM, \
            trait.Violence.NOM, \
            trait.Ascetisme.NOM, \
            trait.Altruisme.NOM, \
            trait.Franchise.NOM, \
            ]

    def GetMetiersCompatibles(self):
        """
        si le perso a des compétences dans ces métiers il a plus de chances de vouloir rejoindre cette coterie où ils sont souvent pratiqués
        """
        return [ \
            metier.Pretre.NOM, \
            metier.TueurDeMonstres.NOM, \
            metier.Guerrier.NOM, \
            metier.Chevalier.NOM, \
            metier.Policier.NOM, \
            metier.Vigile.NOM, \
            metier.Dessinateur.NOM, \
            metier.Bibliothecaire.NOM, \
            metier.GardeDuCorps.NOM \
            ]

    def GetTraitsIncompatibles(self):
        """
        si le perso a ces caracs il a moins de chances de ne pas vouloir rejoindre cette coterie
        """
        return [ \
            trait.Cupidite.NOM, \
            trait.Opportunisme.NOM, \
            trait.Sexualite.NOM \
            ]

    def GetGentile(self, masculin):
        if masculin:
            return "templier"
        else:
            return "templière"

    def GetPoidsDemo(self):
        """
        à quel point cette coterie est nombreuse dans la population
        1.0 = normal
        0.1 = 10 fois moins que la moyenne
        """
        return 0.3

    def CreerNom(self, masculin):
        """
        génère un patronyme correspondant à la coterie en question
        """
        return random.choice(Templiers.NOMS)

    def CreerPrenom(self, masculin):
        """
        génère un patronyme correspondant à la coterie en question
        """
        if masculin:
            return random.choice(Templiers.PRENOMS_M)
        else:
            return random.choice(Templiers.PRENOMS_F)

    def GenererPortraits(self, age, masculin, metObj, portraits, valeursTraits):
        """
        ajoute des portraits correspondants aux caracs en paramtre (et à la coterie courante)
        """
        if masculin:
            if age >= 20:
                if age >= 30:
                    if age >= 50:
                        if age >= 60:
                            portraits.append("images/coteries/templiers/portraits/60+.jpg")
                        portraits.append("images/coteries/templiers/portraits/50+.jpg")
                        portraits.append("images/coteries/templiers/portraits/50+_b.jpg")
                    portraits.append("images/coteries/templiers/portraits/30+.jpg")
                if age <= 40:
                    portraits.append("images/coteries/templiers/portraits/20-40.jpg")
        else:
            if age >= 15:
                if age >= 70:
                    portraits.append("images/coteries/templiers/portraits/femme70+.jpg")
                if age <= 30: # >=15
                    portraits.append("images/coteries/templiers/portraits/femme15_30.jpg")
                if age >= 20:
                    if age <= 40:
                        portraits.append("images/coteries/templiers/portraits/femme20_40.jpg")

        return portraits

    NOMS = [
        u"d'Aiglemont", u"d'Aiguemorte", u"d'Aiguevive", u"d'Aspremont", u"de Beaulieu", u"de Beaupré", u"de Belleforest",
        u"de Bellegarde", u"de Bénévent", u"de Blancmoustier", u"de Boisjoli", u"de Boutefeu", u"de Clairefontaine",
        u"de Clairval", u"de Clochemerle", u"de la Combe-aux-Cerfs", u"de la Combe-aux-Loups", u"de Courtelande",
        u"de Courtepaille", u"d'Engoulevent", u"de Fiercastel", u"de Gardefeu", u"de Hauterive", u"de Hauteroche",
        u"de Hautfort", u"de Hurlevent", u"du Lac de Maisonfort", u"de Mondragon", u"de Montaigu", u"de Montalembert",
        u"de Montardent", u"de Montbard", u"de Montfaucon", u"de Montfleury", u"deMontjoye", u"de Montmirail",
        u"de Montorgueil", u"de Morneplaine", u"de Mortelande", u"de Mortelune", u"de Neuville", u"de Noirmoustier",
        u"de Sautemouton", u"de Sauveterre", u"de Sombretour", u"de Sombreval", u"de Songecreux", u"de Valvert",
        u"le Bel", u"le Bon", u"le Brave", u"le Fier", u"le Franc", u"le Hardi", u"le Jeune", u"le Matois", u"le Preux", u"le Sagace",
        u"le Sage", u"le Taciturne", u"Barberousse", u"Brisefer", u"Coeur-de-Lion", u"Dent-de-Loup", u"Sang-de-Boeuf", u"Taillefer",
        u"Tuemouches", u"Langlois", u"Duchesne", u"Marchand", u"Boulanger", u"le Chauve", u"Courtois", u"Ageorges", u"Aubernard", u"Alamartine",
        u"Fromentin", u"Rabier", u"Coulomb", u"Cabrera", u"Poudevigne", u"Messonnier", u"Métivier", u"Pelletier", u"Larsonneur",
        u"Castagnier", u"Nouet", u"Lebreton", u"Manceau", u"Legros", u"Lenain", u"Sarrazin", u"Chauvin", u"Roux",
        u"Abarnou", u"Abattu", u"Abbadie", u"Abéjean", u"Abellan", u"Abeloos", u"Abijou", u"Abillard", u"Abisseror", u"Abrassart",
        u"Abravanel", u"Abrazard", u"Abribat", u"Abric", u"Abrigeon", u"Abriol", u"Absalon", u"Acharles", u"Acheriteguy", u"Achotte",
        u"Achouline", u"Adélaïde", u"Adelmard" ]

    PRENOMS_M = [
    u"Abbo",u"Abrahil",u"Abram",u"Adalard",u"Adalbert",u"Adalbertus",u"Adaldag",u"Adalgrimus",u"Adalhaid",u"Adalhard",u"Adalolf",u"Adelard",u"Aega",u"Ageric",u"Agilbert",u"Agilfride",u"Agiulf",u"Agobard",u"Aigulf",u"Alberic",u"Aldedramnus",u"Aldgisl",u"Allowin",u"Amalricus",u"Amand",u"Amator",u"Andica",u"Angegisis",u"Angilbart",u"Angilbert",u"Anno",u"Ansegisel",u"Anskar",u"Ansovald",u"Arbitio",u"Arbogast",u"Arbogastes",u"Arculf",u"Aregisel",u"Arnegisel",u"Arnold",u"Arnoul",u"Arnulf",u"Artaud",u"Asselin",u"Atacinus",u"Audoen",u"Audomar",u"Audoneus",u"Audovald",u"Audramnus",u"Austregisel",u"Avremarus",u"Badegisel",u"Balderic",u"Baldrick",u"Baudry",u"Baugulf",u"Bauto",u"Bavo",u"Benild",u"Berchar",u"Berengar",u"Berenger",u"Bernard",u"Bernardus",u"Bernhard",u"Berno",u"Bero",u"Bertelis",u"Berthaire",u"Berthefried",u"Bertin",u"Bertlinus",u"Bertram",u"Bertramnus",u"Bertulf",u"Besso",u"Birinus",u"Blutmund",u"Boso",u"Bovo",u"Brice",u"Britius",u"Brocard",u"Bruno",u"Burchard",u"Butilin",u"Carloman",u"Cassyon",u"Ceslinus",u"Ceufroy",u"Chararic",u"Charibert",u"Charles",u"Cheldric",u"Childebert",u"Childebrand",u"Childeric",u"Chilperic",u"Chlodion",u"Chlodmer",u"Chlodomer",u"Chlodowig",u"Chlodwig",u"Chlotar",u"Chramnesind",u"Chrodegang",u"Clodio",u"Clodomir",u"Clotaire",u"Clothair",u"Cloud",u"Clovis",u"Conrad",u"Corbinian",u"Corbus",u"Creatus",u"Cyr",u"Cyricus",u"Dado",u"Dagaric",u"Dagobert",u"Dalfin",u"Dietrich",u"Dodo",u"Dreux",u"Drogo",u"Drogon",u"Dudon",u"Durand",u"Ebbo",u"Eberhard",u"Eberulf",u"Ebregisel",u"Ebroin",u"Ebrulf",u"Egide",u"Einhard",u"Electeus",u"Electus",u"Emme",u"Emmeran",u"Emmon",u"Engelbert",u"Engilbert",u"Enguerrand",u"Enurchus",u"Eracle",u"Erard",u"Erchinoald",u"Erenfried",u"Eudes",u"Euric",u"Evrard",u"Evroul",u"Evroult",u"Farabert",u"Fardulf",u"Faro",u"Faroardus",u"Faroinus",u"Feremundus",u"Feroardus",u"Flodoard",u"Floribert",u"Folcard",u"Folmar",u"Foroenus",u"Fredegar",u"Fridolin",u"Fridugis",u"Frobertus",u"Frothardus",u"Frotlaicus",u"Fulbert",u"Fulcaire",u"Fulk",u"Fulrad",u"Gararic",u"Garivald",u"Gaudulfus",u"Gaujoinus",u"Gausbertus",u"Gausboldus",u"Gautmarus",u"Gedalbertus",u"Gedalcaus",u"Gerbert",u"Gereon",u"Gerold",u"Gifemund",u"Gilbert",u"Giselbert",u"Giseler",u"Gislevertus",u"Giso",u"Godalbertus",u"Godobald",u"Godomar",u"Godun",u"Goisfrid",u"Gondulph",u"Goscelin",u"Gouzlim",u"Gozbert",u"Gozolon",u"Griffon",u"Grifo",u"Grimald",u"Grimbald",u"Grimoald",u"Guadulfus",u"Guido",u"Gundobad",u"Gundovald",u"Gunthar",u"Guntram",u"Guntramn",u"Hagen",u"Haldemarus",u"Halinard",u"Hartgard",u"Hartmut",u"Hartnid",u"Helinand",u"Helisachar",u"Heribert",u"Hildebald",u"Hildebold",u"Hildeboldus",u"Hildegaudus",u"Hildeprand",u"Hildevoldus",u"Hildoinus",u"Hilduin",u"Hincmar",u"Hlodver",u"Hrodbert",u"Hubert",u"Huebald",u"Humbert",u"Hunald",u"Imbert",u"Imnachar",u"Imninon",u"Ingalbertus",u"Ingelram",u"Ingomer",u"Ingund",u"Jocelin",u"Karlmann",u"Lambert",u"Lanfranc",u"Lantbertus",u"Laudus",u"Lebuin",u"Ledger",u"Leger",u"Leodegar",u"Letard",u"Leudast",u"Leufred",u"Leufroy",u"Leutfrid",u"Leuthard",u"Leuthere",u"Liudger",u"Liudhard",u"Liudolf",u"Lo",u"Lothar",u"Ludger",u"Lul",u"Lull",u"Magnachar",u"Magneric",u"Maiuel",u"Maixent",u"Majorian",u"Malaric",u"Mallobaudes",u"Mansuetus",u"Marachar",u"Maraulf",u"Marcomir",u"Marcoul",u"Marellus",u"Martinus",u"Matfrid",u"Mauger",u"Maurifius",u"Medard",u"Meginhard",u"Merobaudes",u"Merovech",u"Monulph",u"Munderic",u"Nevelung",u"Nibelung",u"Nithard",u"Norbert",u"Nordbert",u"Notger",u"Notker",u"Odger",u"Odilo",u"Odilon",u"Odo",u"Odulf",u"Omer",u"Orderic",u"Otbert",u"Otker",u"Otto",u"Otton",u"Ouen",u"Ouus",u"Pacatian",u"Pair",u"Pancras",u"Panteleon",u"Paschal",u"Pepin",u"Philibert",u"Piligrim",u"Pippin",u"Poppo",u"Priarios",u"Puvis",u"Radbod",u"Radigis",u"Ragenard",u"Ragenardus",u"Ragenaus",u"Ragnachar",u"Ragnfred",u"Ragno",u"Ramnulf",u"Rathar",u"Rathier",u"Ratold",u"Razo",u"Reginald",u"Reginar",u"Reginard",u"Remacle",u"Remi",u"Reolus",u"Ricbodo",u"Ricchar",u"Ricfried",u"Richer",u"Richomer",u"Richomeres",u"Rigunth",u"Riquier",u"Rothad",u"Samo",u"Samson",u"Sergius",u"Sichar",u"Sicho",u"Siclandus",u"Sicleardus",u"Siclevoldus",u"Siegfried",u"Sigebert",u"Sigefroy",u"Sigeric",u"Sigibert",u"Sigismund",u"Sinopus",u"Suger",u"Suidbert",u"Suidger",u"Sunnegisil",u"Sunno",u"Syagrius",u"Tassilo",u"Taurin",u"Tescelin",u"Thankmar",u"Thegan",u"Theodard",u"Theodebert",u"Theodemir",u"Theodon",u"Theodore",u"Theodoric",u"Theodulf",u"Theodulph",u"Theodwin",u"Theoto",u"Theudebald",u"Theudebert",u"Theuderic",u"Theutgaud",u"Thierry",u"Thietmar",u"Trutgaudus",u"Turpin",u"Unroch",u"Vedast",u"Vicelin",u"Vigor",u"Vulmar",u"Waiofar",u"Wala",u"Walaric",u"Walcaud",u"Waldolanus",u"Waleran",u"Waltgaud",u"Wandregisel",u"Wandregisilus",u"Wandrille",u"Warmann",u"Wazo",u"Welf",u"Werinbert",u"Wibert",u"Wichmann",u"Wido",u"Willehad",u"Willibald",u"Willibrord",u"Willichar",u"Wolbodo",u"Wulfhard",u"Wulfram",u"Zwentibold",
    u"Alphonse", u"Amédée", u"Arnaud", u"Arthur", u"udoin", u"Baudoin", u"Baudouin",
    u"Aalongue", u"Abbaud", u"Abbon", u"Abelène", u"Abran", u"Abzal", u"Acelin", u"Achaire",
    u"Achard", u"Acheric", u"Adalard", u"Adalbaud", u"Adalbéron", u"Adalbert", u"Adalelme",
    u"Adalgaire", u"Adalgise", u"Adalicaire", u"Adalman", u"Adalric", u"Adebran", u"Adélard",
    u"Adelbert", u"Adelin", u"Adenet", u"Adhémar", u"Adier", u"Adinot", u"Adolbert", u"Adon",
    u"Adoul", u"Adrier", u"Adson", u"Agambert", u"Aganon", u"Agebert", u"Agelmar", u"Agelric",
    u"Agenulf", u"Agerad", u"Ageran", u"Agilbert", u"Agilmar", u"Aglebert", u"Agmer", u"Agnebert", u"Agrestin", u"Agrève",
    u"Aibert", u"Aicard", u"Aimbaud", u"Aimin", u"Aimoin", u"Airard", u"Airy", u"Alard", u"Albalde", u"Albaud", u"Albéron",
    u"Alboin", u"Albuson", u"Alchaire", u"Alchas", u"Alcuin", u"Alleaume", u"Amanieu", u"Amat", u"Amblard", u"Anaclet",
    u"Ansbert", u"Anselin", u"Ansoald", u"Archambaud", u"Arembert", u"Arnat", u"Artaud", u"Aubry", u"Authaire", u"Avold",
    u"Ayoul", u"Barnoin", u"Barral", u"Baudri", u"Bérard", u"Bérenger", u"Bernon", u"Bettolin", u"Betton", u"Brunon",
    u"Burchard", u"Caribert", u"Centule", u"Childebert", u"Chilpéric", u"Cillien", u"Clodomir", u"Clotaire", u"Cloud",
    u"Colomban", u"Conan", u"Conrad", u"Cybard", u"Dacien", u"Dadon", u"Dalmace", u"Dambert", u"Dioclétien", u"Doat",
    u"Drogon", u"Durand", u"Eadwin", u"Ebbon", u"Ebehard", u"Eddo", u"Edwin", u"Egfroi", u"Égilon", u"Eilbert", u"Einold",
    u"Éon", u"Ermenfred", u"Ermengaud", u"Ernée", u"Ernold", u"Ernoul", u"Eumène", u"Eunuce", u"Euric", u"Eustaise", u"Euverte",
    u"Evroult", u"Fleuret", u"Flocel", u"Flodoard", u"Flouard", u"Flour", u"Floxel", u"Folquet", u"Fortunat", u"Foulque",
    u"Frajou", u"Frambault", u"Frambourg", u"Frameric", u"Francaire", u"Fulbert", u"Gailhart", u"Gaillon", u"Garréjade",
    u"Gaubert", u"Gerbert", u"Giboin", u"Gildric", u"Gislebert", u"Godomer", u"Gossuin", u"Guéthenoc", u"Guibin", u"Guiscard",
    u"Hatton", u"Haynhard", u"Héribert", u"Herlebald", u"Herlebauld", u"Herlemond", u"Hildebald", u"Hildebrand",
    u"Hilduin", u"Hoel", u"Honfroi", u"Hugon", u"Humbaud", u"Isembert", u"Ithier", u"Jacquemin", u"Jacut", u"Lagier", u"Lambert",
    u"Lancelin", u"Léothéric", u"Lidoire", u"Lisiard", u"Lothaire", u"Lubin", u"Maïeul", u"Malulf", u"Marcuard", u"Maric",
    u"Materne", u"Matfrid", u"Matifas", u"Maur", u"Mauront", u"Mesmin", u"Milon", u"Odo", u"Oldaric", u"Orderic", u"Oricle",
    u"Premon", u"Rachio", u"Radoald", u"Radulf", u"Raginard", u"Raimbaut", u"Raimbert", u"Rainier", u"Rainon", u"Ramnulf",
    u"Ranulfe", u"Rataud", u"Rodron", u"Romary", u"Roscelin", u"Rostang", u"Salvin", u"Savaric", u"Savary", u"Sébaste",
    u"Senoc", u"Sicard", u"Siegebert", u"Sifard", u"Sigebert", u"Taillefer", u"Taurin", u"Théodebert", u"Théodemar",
    u"Theoderich", u"Théodran", u"Thérouanne", u"Thiégaud", u"Ursicin", u"Ursion", u"Vantelme", u"Volusien", u"Warin",
    u"Wigeric", u"Willibert", u"Wulfoald", u"Wulgrin",
    u"Acelin", u"Amaury", u"Anselme", u"Anthiaume", u"Arthaud", u"Aubert", u"Audibert", u"Aymeric", u"Aymon", u"Barthélémi",
    u"Benoît", u"Bérard", u"Bernier", u"Bertrand", u"Bohémond", u"Edmond", u"Enguerrand", u"Ernaut", u"Eudes", u"Galaad",
    u"Garin", u"Garnier", u"Gauthier", u"Gauvain", u"Gibouin", u"Gilemer", u"Girart", u"Godefroy", u"Gontran",
    u"Gonzagues", u"Grégoire", u"Guerri", u"Guilhem", u"Hardouin", u"Herbert", u"Herchambaut", u"Hubert", u"Hugues",
    u"Huon", u"Jehan", u"Lancelot", u"Merlin", u"Perceval", u"Philibert", u"Raoul", u"Raymond", u"Renaud", u"Robert",
    u"Roland", u"Savari", u"Sigismond", u"Tancrède", u"Thibaut", u"Tristan", u"Urbain", u"Ybert", u"Yvain", u"Abélard", u"Mathieu", u"Dominique" ]

    PRENOMS_F = [
    u"Ada",u"Adala",u"Adalberta",u"Adalind",u"Adalindis",u"Adallind",u"Adallinda",u"Adalmut",u"Adalrada",u"Adaltrude",u"Adaltrutis",u"Adaluuidis",u"Adalwif",u"Adda",u"Addela",u"Adela",u"Adelaidis",u"Adele",u"Adelhaid",u"Adelheid",u"Adeltrudis",u"Adhela",u"Adwala",u"Aebbe",u"Agatha",u"Agentrudis",u"Agglethrudis",u"Albelenda",u"Albofleda",u"Albruga",u"Alburch",u"Alburg",u"Aldguda",u"Aldgudana",u"Aldruth",u"Alfgarda",u"Alfild",u"Alflent",u"Alpaida",u"Alpaide",u"Alpais",u"Amabilia",u"Amalberga",u"Amalbirga",u"Amoltrud",u"Amulberga",u"Anselda",u"Ansgard",u"Anstruda",u"Aregund",u"Athalia",u"Athela",u"Atula",u"Aua",u"Auacyn",u"Aubirge",u"Aude",u"Audofleda",u"Audovera",u"Auekin",u"Auin",u"Auina",u"Auriana",u"Austrechild",u"Ava",u"Avacyn",u"Avekin",u"Avin",u"Baldechildis",u"Baltelda",u"Balthechildis",u"Balthildis",u"Basina",u"Bauin",u"Bava",u"Bavacin",u"Bave",u"Bavin",u"Begga",u"Belegardis",u"Benedicta",u"Berchildis",u"Berehta",u"Berenga",u"Beretrude",u"Bergard",u"Bergundis",u"Berhta",u"Beriungis",u"Berna",u"Bernewief",u"Bernewif",u"Berta",u"Bertaida",u"Bertha",u"Berthe",u"Berthefled",u"Berthefried",u"Berthegund",u"Berthildis",u"Berthlenda",u"Bertildis",u"Bertliana",u"Bertoane",u"Bertrada",u"Bertruda",u"Bertswinda",u"Bettin",u"Bilichildis",u"Blesinde",u"Blitekin",u"Boltiarda",u"Bova",u"Boviardis",u"Brunhild",u"Brunhilda",u"Burgundefara",u"Childebertana",u"Chlodeswinthe",u"Chlodosind",u"Chlothsinda",u"Chrodechildis",u"Chrodtrude",u"Chunsina",u"Cilia",u"Clodauuiua",u"Clothild",u"Clotild",u"Clotilde",u"Clotrada",u"Conegont",u"Conegundis",u"Conegunt",u"Crapahildis",u"Cunegonde",u"Cunegund ",u"Cunegundis",u"Dadin",u"Dagarada",u"Danburga",u"Deuteria",u"Doda",u"Dodda",u"Duda",u"Eadgithu",u"Ealswid",u"Ebertana",u"Edeberga",u"Edeborg",u"Ega",u"Egecin",u"Egeluuara",u"Egesburga",u"Egesloga",u"Ehgelhild",u"Ehgeluuara",u"Ellinrat",u"Emecin",u"Emma",u"Engelberga",u"Engelberge",u"Engelgard",u"Engelsuit",u"Engeltrude",u"Engeluuara",u"Engelwara",u"Enna",u"Erchembrog",u"Eremburgis",u"Ereprad",u"Erkembrog",u"Erkenbrog",u"Erkenburoc",u"Erkenrad",u"Ermecin",u"Ermegardis",u"Ermenberga",u"Ermengard",u"Ermengarda",u"Ermengarde",u"Ermengardis",u"Ermentrudis",u"Ermeswindis",u"Ermina",u"Erpsuid",u"Errictruda",u"Ethelchif",u"Ethelgard",u"Ethelgarda",u"Euerloga",u"Everelda",u"Evereldis",u"Faileuba",u"Fara",u"Fastrada",u"Flouerana",u"Folclind",u"Folclinda",u"Folcrada",u"Folcuuara",u"Folgarda",u"Folsuindis",u"Folsuuendis",u"Fordola",u"Fortlifh",u"Foy",u"Frauuara",u"Fredeburgis",u"Fredegunde",u"Frederada",u"Fredeuuara",u"Frethegard",u"Frethesuinda",u"Frethesuindis",u"Fridesuenda",u"Fridewiga",u"Frisburgis",u"Frithelinda",u"Frouuin",u"Frouuina",u"Galswinth",u"Geila",u"Gelduuara",u"Geneva",u"Genofeva",u"Gerberga",u"Geretrudis",u"Gerlent",u"Gerlinda",u"Gersenda",u"Gersuenda",u"Gersuinda",u"Gersvinda",u"Gertruda",u"Geruuara",u"Geua",u"Geva",u"Gisela",u"Gisla",u"Glismodis",u"Godalinda",u"Godeca",u"Godecin",u"Godelda",u"Godelinda",u"Godildis",u"Goduuara",u"Goiswinth",u"Gomatrudis",u"Gothuuera",u"Grimuuara",u"Gudula",u"Gudule",u"Gundrada",u"Gundrade",u"Gundradis",u"Guntheuc",u"Gunza",u"Guodhelda",u"Guodlia",u"Hadaken",u"Hamesindis",u"Harwara",u"Hatilde",u"Hazeca",u"Heilewif",u"Heilswinda",u"Heldeburga",u"Heletradana",u"Heleuuidis",u"Helinda",u"Heltrada",u"Hengelsenda",u"Herden",u"Herdin",u"Herenborg",u"Herenfrida",u"Herleva",u"Herlinda",u"Hermengarda",u"Hildberta",u"Hildborg",u"Hildcardis",u"Hildeberga",u"Hildeburg",u"Hildegard",u"Hildegarde",u"Hildegardis",u"Hildegund",u"Hildelana",u"Hildemunda",u"Hildeswindis",u"Hildeuuara",u"Hildeuuif",u"Hildewara",u"Hildewif",u"Hildrada",u"Hildwara",u"Hiltrude",u"Himiltrud",u"Hirmenlind",u"Hodierna",u"Hostaruuara",u"Hruodgarda",u"Hruotberta",u"Hruothraud",u"Ida",u"Idasgarda",u"Ideslef",u"Idesuuif",u"Ideswif",u"Idisiardis",u"Imicina",u"Imma",u"Ingela",u"Ingelburga",u"Ingelswindis",u"Ingeltrud",u"Ingeltrude",u"Ingeltrudis",u"Ingeluuara",u"Ingelwara",u"Ingitrude",u"Ingoberg",u"Ingunde",u"Iodberta",u"Iolitha",u"Irmengard",u"Irmenhild",u"Irmenlind",u"Irmgard",u"Irmingard",u"Isa",u"Isburch",u"Itta",u"Joveta",u"Kunegund",u"Landburuga",u"Landgarda",u"Landrada",u"Lanthechilde",u"Lanthildis",u"Lantuuara",u"Lebdrudis",u"Leddinga",u"Leubast",u"Leubovera",u"Leuekin",u"Leuuich",u"Liaueld",u"Lidiardis",u"Liedrada",u"Liefhun",u"Lieftet",u"Lietgarda",u"Lietgardis",u"Lietuuif",u"Lieuuara",u"Lifgarda",u"Liobsynde",u"Liodburga",u"Liodgard",u"Liodrada",u"Litburh",u"Litgardis",u"Litiardis",u"Liutgarde",u"Luitgarde",u"Machtildis",u"Madelgarda",u"Madelgarde",u"Madelrada",u"Madhalberta",u"Magnatrude",u"Magthildis",u"Magtildis",u"Marcatrude",u"Marcovefa",u"Markuuara",u"Mathildis",u"Mauriana",u"Mechtild",u"Megenberta",u"Megendrod",u"Megenhelda",u"Megenlind",u"Megenlioba",u"Megensind",u"Megensinda",u"Megenuuara",u"Meinburg",u"Meinnelda",u"Meinsent",u"Meinswindis",u"Menborch",u"Merofled",u"Merwig",u"Methdin",u"Moschia",u"Murina",u"Nantechildis",u"Nidlebis",u"Nordrada",u"Oda",u"Odburga",u"Odela",u"Odgiva",u"Odguda",u"Odgudana",u"Odlenda",u"Odriana",u"Ogiva",u"Olburgis",u"Olga",u"Osgarda",u"Osgiua",u"Otberta",u"Otgiua",u"Otgiva",u"Oydela",u"Pharahildis",u"Plectrudis",u"Radborg",u"Radburg",u"Radburgis",u"Radegund",u"Radeken",u"Radgert",u"Radlia",u"Radogund",u"Radsuinda",u"Ragnachilde",u"Rainilda",u"Rainildis",u"Ramburga",u"Regana",u"Regenburuga",u"Regenelda",u"Regenlind",u"Regenset",u"Reginsuint",u"Regintrude",u"Regnetrudis",u"Regneuuig",u"Reinewif",u"Reingard",u"Reingardis",u"Reingart",u"Reingaud",u"Reingod",u"Reinsuent",u"Renburgis",u"Rennewief",u"Riberta",u"Richelda",u"Richildis",u"Riclindis",u"Ricsuinda",u"Rigunth",u"Rikildis",u"Rinelt",u"Rinilda",u"Rodburga",u"Rodgarda",u"Rodgardae",u"Rofsind",u"Rosamund",u"Rotburga",u"Rothaide",u"Rothin",u"Rotlenda",u"Rotrud",u"Rotrude",u"Rotrudis",u"Ruodhaid",u"Ruothild",u"Ruothilde",u"Seburg",u"Seburga",u"Siborch",u"Siburg",u"Sigarda",u"Sigberta",u"Sigeberta",u"Sigeburgis",u"Sigethrod",u"Sigiburgis",u"Snelburch",u"Stenburch",u"Stilleuuara",u"Strilleburg",u"Suitburgis",u"Susanna",u"Swanahilde",u"Syardis",u"Teudsindis",u"Teutberga",u"Thancuuara",u"Theaduuara",u"Thedela",u"Theodelinda",u"Theoderada",u"Theodrada",u"Theodrade",u"Theudechild",u"Theudelinde",u"Theutberga",u"Thidela",u"Thieda",u"Thietgarda",u"Thietuuich",u"Thietwara",u"Thiodsind",u"Thiodsuinda",u"Thiutuuara",u"Thrasborg",u"Thrudberga",u"Ticekin",u"Tietlenda",u"Tietza",u"Trhutborgana",u"Trudlinde",u"Trutilda",u"UUaldburg",u"UUaldethruda",u"UUeremund",u"UUerenburoc",u"UUiburgis",u"UUindborog",u"UUinebarga",u"UUireda",u"UUlgarda",u"Uda",u"Ultrogotha",u"Uoldolberta",u"Veneranda",u"Vrowecin",u"Vualdberta",u"Vualdedruda",u"Vualdetruda",u"Vuifken",u"Vuinetberta",u"Vuiuechin",u"Vuldretrada",u"Vulfegundis",u"Waldrada",u"Wavin",u"Wiburgis",u"Wihted",u"Wilberga",u"Wilgeva",u"Willelda",u"Willesuindis",u"Wisigard",u"Wivecin",u"Wivin",u"Wlbergis",u"Wlbgis",u"Wlfildis",u"Wlgert",
    u"ADELAIDE", u"AGNES", u"ALIENOR", u"ANASTASE", u"ANASTASIE", u"ASTRID", u"AUDE", u"AURE",
    u"Aalis", u"Ada", u"Adalarde", u"Adalasinde", u"Adalburge", u"Adalinde", u"Adalsende", u"Adalsinde", u"Ade",
    u"Adélaïde", u"Adelberge", u"Adèle", u"Adelheit", u"Adeline", u"Adelsinde", u"Adnette", u"Adrehilde", u"Advise", u"Aélais",
    u"Aelidis", u"Aelis", u"Aélith", u"Aénor", u"Agarde", u"Agathe", u"Agelberte", u"Ageruchia", u"Agnoflède", u"Aiga", u"Aïn",
    u"Alaine", u"Alaison", u"Alaiseta", u"Alaizie", u"Alarèse", u"Alayde", u"Alazaïs", u"Albérade", u"Albereda", u"Albérée",
    u"Alberte", u"Albine", u"Alboflède", u"Alchima", u"Alcima", u"Aldeberge", u"Aléide", u"Aliénor", u"Aliète", u"Aliote",
    u"Alix", u"Almodis", u"Ameline", u"Aneglie", u"Ansgarde", u"Arambour", u"Aremburge", u"Arlette", u"Asceline",
    u"Assalid", u"Attala", u"Audeburge", u"Audefledis", u"Audovère", u"Aubrée", u"Auge", u"Austreberthe", u"Azelaïs",
    u"Barbe", u"Balde", u"Bathilde", u"Bayonne", u"Béatrix", u"Bénigne", u"Berthe", u"Betton", u"Boussarde", u"Brunehaut",
    u"Brunissende", u"Carensa", u"Carétène", u"Clervie", u"Clotsende", u"Clotsinde", u"Dangerosa", u"Déda", u"Dies",
    u"Elbore", u"Eliette", u"Elvide", u"Emillane", u"Emma", u"Erembourg", u"Ermelne", u"Ermengarde", u"Ermenjart",
    u"Ermentrude", u"Ermesinde", u"Etiennette", u"Eudoxie", u"Eusébie", u"Fleur", u"Floberte", u"Flodoberte",
    u"Flor", u"Flore", u"Foi", u"Framehilde", u"Franchilde", u"Gabrielle", u"Gausle", u"Gebétrude", u"Gerberge",
    u"Gerberte", u"Gerloc", u"Gersinde", u"Gillete", u"Gillote", u"Gisla", u"Glossinde", u"Gontrade", u"Guen",
    u"Guillemette", u"Guiraude", u"Hélits", u"Hermine", u"Hersent", u"Hildegarde", u"Huguette", u"Hugonette",
    u"Hylde", u"Ide", u"Inde", u"Ingonde", u"Jutta", u"Lampagia", u"Léceline", u"Leudeberte", u"Liutgarde", u"Mahaud",
    u"Mahaut", u"Malorsie", u"Marguerite", u"Mathe", u"Mathie", u"Mathilde", u"Mechtilde", u"Mélie", u"Métronie", u"Mode",
    u"Nantechilde", u"Ode", u"Odete", u"Odile", u"Odonette", u"Opportune", u"Ostrogotho", u"Pétronille", u"Phébalde",
    u"Placidina", u"Plectrude", u"Poppa", u"Praetoria", u"Pulcelle", u"Ragnachilde", u"Régina", u"Renaude", u"Richilde",
    u"Rictrude", u"Rixende", u"Robresse", u"Rodheid", u"Rosemonde", u"Rothaïde", u"Rotrude", u"Sanche", u"Sancie", u"Sara",
    u"Sédeleude", u"Sénégonde", u"Sichède", u"Souveraine", u"Thelchilde", u"Théodechilde", u"Théodora", u"Théodrade",
    u"Théophanie", u"Waldrade", u"Yolande", u"Yselda", u"Ysoir",
    u"Aalais", u"Aliénor", u"Alix", u"Anthéa", u"Aremburge", u"Artémise", u"Astride", u"Aude", u"Barbe", u"Barberine", u"Béatrix",
    u"Berthe", u"Blanche", u"Blancheflor", u"Bradamante", u"Brunehaut", u"Cathau", u"Diane", u"Ermessende", u"Gallendis",
    u"Geneviève", u"Grisélidis", u"Gudule", u"Guenièvre", u"Hélix", u"Héloïse", u"Hermeline", u"Hersende", u"Hildegarde",
    u"Iseult", u"Léonor", u"Letgarde", u"Mahaut", u"Mélissande", u"Mélusine", u"Milesende", u"Morgane", u"Ursule", u"Viviane"]

    # condition : être chrétien
