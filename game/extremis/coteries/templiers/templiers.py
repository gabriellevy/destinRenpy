from extremis.coteries import coterie
from extremis.socio_eco.metiers import metier
from extremis.humanite import trait
from extremis.geographie import quartier
import random

class Templiers(coterie.Coterie):

    NOM = u"Ordre du Temple"
    ID = u"templiers"

    C_RICHESSE = "Richesse du temple" # tous les templiers ont renoncé aux biens matériels, ils ont tous cette richesse (basse)
    RICHESSE_TEMPLE = -4 # richesse de départ du temple, et peu de chance de beaucoup bouger

    def __init__(self):
        self.nom_ = Templiers.NOM
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
        si le perso a ces caracs il a plus de chances de ne pas vouloir rejoindre cette coterie
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

    NOMS = [
        "d'Aiglemont", "d'Aiguemorte", "d'Aiguevive", "d'Aspremont", "de Beaulieu", "de Beaupré", "de Belleforest",
        "de Bellegarde", "de Bénévent", "de Blancmoustier", "de Boisjoli", "de Boutefeu", "de Clairefontaine",
        "de Clairval", "de Clochemerle", "de la Combe-aux-Cerfs", "de la Combe-aux-Loups", "de Courtelande",
        "de Courtepaille", "d'Engoulevent", "de Fiercastel", "de Gardefeu", "de Hauterive", "de Hauteroche",
        "de Hautfort", "de Hurlevent", "du Lac de Maisonfort", "de Mondragon", "de Montaigu", "de Montalembert",
        "de Montardent", "de Montbard", "de Montfaucon", "de Montfleury", "deMontjoye", "de Montmirail",
        "de Montorgueil", "de Morneplaine", "de Mortelande", "de Mortelune", "de Neuville", "de Noirmoustier",
        "de Sautemouton", "de Sauveterre", "de Sombretour", "de Sombreval", "de Songecreux", "de Valvert",
        "le Bel", "le Bon", "le Brave", "le Fier", "le Franc", "le Hardi", "le Jeune", "le Matois", "le Preux", "le Sagace",
        "le Sage", "le Taciturne", "Barberousse", "Brisefer", "Coeur-de-Lion", "Dent-de-Loup", "Sang-de-Boeuf", "Taillefer",
        "Tuemouches", "Langlois", "Duchesne", "Marchand", "Boulanger", "le Chauve", "Courtois", "Ageorges", "Aubernard", "Alamartine",
        "Fromentin", "Rabier", "Coulomb", "Cabrera", "Poudevigne", "Messonnier", "Métivier", "Pelletier", "Larsonneur",
        "Castagnier", "Nouet", "Lebreton", "Manceau", "Legros", "Lenain", "Sarrazin", "Chauvin", "Roux",
        "Abarnou", "Abattu", "Abbadie", "Abéjean", "Abellan", "Abeloos", "Abijou", "Abillard", "Abisseror", "Abrassart",
        "Abravanel", "Abrazard", "Abribat", "Abric", "Abrigeon", "Abriol", "Absalon", "Acharles", "Acheriteguy", "Achotte",
        "Achouline", "Adélaïde", "Adelmard" ]

    PRENOMS_M = [
    "Abbo","Abrahil","Abram","Adalard","Adalbert","Adalbertus","Adaldag","Adalgrimus","Adalhaid","Adalhard","Adalolf","Adelard","Aega","Ageric","Agilbert","Agilfride","Agiulf","Agobard","Aigulf","Alberic","Aldedramnus","Aldgisl","Allowin","Amalricus","Amand","Amator","Andica","Angegisis","Angilbart","Angilbert","Anno","Ansegisel","Anskar","Ansovald","Arbitio","Arbogast","Arbogastes","Arculf","Aregisel","Arnegisel","Arnold","Arnoul","Arnulf","Artaud","Asselin","Atacinus","Audoen","Audomar","Audoneus","Audovald","Audramnus","Austregisel","Avremarus","Badegisel","Balderic","Baldrick","Baudry","Baugulf","Bauto","Bavo","Benild","Berchar","Berengar","Berenger","Bernard","Bernardus","Bernhard","Berno","Bero","Bertelis","Berthaire","Berthefried","Bertin","Bertlinus","Bertram","Bertramnus","Bertulf","Besso","Birinus","Blutmund","Boso","Bovo","Brice","Britius","Brocard","Bruno","Burchard","Butilin","Carloman","Cassyon","Ceslinus","Ceufroy","Chararic","Charibert","Charles","Cheldric","Childebert","Childebrand","Childeric","Chilperic","Chlodion","Chlodmer","Chlodomer","Chlodowig","Chlodwig","Chlotar","Chramnesind","Chrodegang","Clodio","Clodomir","Clotaire","Clothair","Cloud","Clovis","Conrad","Corbinian","Corbus","Creatus","Cyr","Cyricus","Dado","Dagaric","Dagobert","Dalfin","Dietrich","Dodo","Dreux","Drogo","Drogon","Dudon","Durand","Ebbo","Eberhard","Eberulf","Ebregisel","Ebroin","Ebrulf","Egide","Einhard","Electeus","Electus","Emme","Emmeran","Emmon","Engelbert","Engilbert","Enguerrand","Enurchus","Eracle","Erard","Erchinoald","Erenfried","Eudes","Euric","Evrard","Evroul","Evroult","Farabert","Fardulf","Faro","Faroardus","Faroinus","Feremundus","Feroardus","Flodoard","Floribert","Folcard","Folmar","Foroenus","Fredegar","Fridolin","Fridugis","Frobertus","Frothardus","Frotlaicus","Fulbert","Fulcaire","Fulk","Fulrad","Gararic","Garivald","Gaudulfus","Gaujoinus","Gausbertus","Gausboldus","Gautmarus","Gedalbertus","Gedalcaus","Gerbert","Gereon","Gerold","Gifemund","Gilbert","Giselbert","Giseler","Gislevertus","Giso","Godalbertus","Godobald","Godomar","Godun","Goisfrid","Gondulph","Goscelin","Gouzlim","Gozbert","Gozolon","Griffon","Grifo","Grimald","Grimbald","Grimoald","Guadulfus","Guido","Gundobad","Gundovald","Gunthar","Guntram","Guntramn","Hagen","Haldemarus","Halinard","Hartgard","Hartmut","Hartnid","Helinand","Helisachar","Heribert","Hildebald","Hildebold","Hildeboldus","Hildegaudus","Hildeprand","Hildevoldus","Hildoinus","Hilduin","Hincmar","Hlodver","Hrodbert","Hubert","Huebald","Humbert","Hunald","Imbert","Imnachar","Imninon","Ingalbertus","Ingelram","Ingomer","Ingund","Jocelin","Karlmann","Lambert","Lanfranc","Lantbertus","Laudus","Lebuin","Ledger","Leger","Leodegar","Letard","Leudast","Leufred","Leufroy","Leutfrid","Leuthard","Leuthere","Liudger","Liudhard","Liudolf","Lo","Lothar","Ludger","Lul","Lull","Magnachar","Magneric","Maiuel","Maixent","Majorian","Malaric","Mallobaudes","Mansuetus","Marachar","Maraulf","Marcomir","Marcoul","Marellus","Martinus","Matfrid","Mauger","Maurifius","Medard","Meginhard","Merobaudes","Merovech","Monulph","Munderic","Nevelung","Nibelung","Nithard","Norbert","Nordbert","Notger","Notker","Odger","Odilo","Odilon","Odo","Odulf","Omer","Orderic","Otbert","Otker","Otto","Otton","Ouen","Ouus","Pacatian","Pair","Pancras","Panteleon","Paschal","Pepin","Philibert","Piligrim","Pippin","Poppo","Priarios","Puvis","Radbod","Radigis","Ragenard","Ragenardus","Ragenaus","Ragnachar","Ragnfred","Ragno","Ramnulf","Rathar","Rathier","Ratold","Razo","Reginald","Reginar","Reginard","Remacle","Remi","Reolus","Ricbodo","Ricchar","Ricfried","Richer","Richomer","Richomeres","Rigunth","Riquier","Rothad","Samo","Samson","Sergius","Sichar","Sicho","Siclandus","Sicleardus","Siclevoldus","Siegfried","Sigebert","Sigefroy","Sigeric","Sigibert","Sigismund","Sinopus","Suger","Suidbert","Suidger","Sunnegisil","Sunno","Syagrius","Tassilo","Taurin","Tescelin","Thankmar","Thegan","Theodard","Theodebert","Theodemir","Theodon","Theodore","Theodoric","Theodulf","Theodulph","Theodwin","Theoto","Theudebald","Theudebert","Theuderic","Theutgaud","Thierry","Thietmar","Trutgaudus","Turpin","Unroch","Vedast","Vicelin","Vigor","Vulmar","Waiofar","Wala","Walaric","Walcaud","Waldolanus","Waleran","Waltgaud","Wandregisel","Wandregisilus","Wandrille","Warmann","Wazo","Welf","Werinbert","Wibert","Wichmann","Wido","Willehad","Willibald","Willibrord","Willichar","Wolbodo","Wulfhard","Wulfram","Zwentibold",
    "Alphonse", "Amédée", "Arnaud", "Arthur", "udoin", "Baudoin", "Baudouin",
    "Aalongue", "Abbaud", "Abbon", "Abelène", "Abran", "Abzal", "Acelin", "Achaire",
    "Achard", "Acheric", "Adalard", "Adalbaud", "Adalbéron", "Adalbert", "Adalelme",
    "Adalgaire", "Adalgise", "Adalicaire", "Adalman", "Adalric", "Adebran", "Adélard",
    "Adelbert", "Adelin", "Adenet", "Adhémar", "Adier", "Adinot", "Adolbert", "Adon",
    "Adoul", "Adrier", "Adson", "Agambert", "Aganon", "Agebert", "Agelmar", "Agelric",
    "Agenulf", "Agerad", "Ageran", "Agilbert", "Agilmar", "Aglebert", "Agmer", "Agnebert", "Agrestin", "Agrève",
    "Aibert", "Aicard", "Aimbaud", "Aimin", "Aimoin", "Airard", "Airy", "Alard", "Albalde", "Albaud", "Albéron",
    "Alboin", "Albuson", "Alchaire", "Alchas", "Alcuin", "Alleaume", "Amanieu", "Amat", "Amblard", "Anaclet",
    "Ansbert", "Anselin", "Ansoald", "Archambaud", "Arembert", "Arnat", "Artaud", "Aubry", "Authaire", "Avold",
    "Ayoul", "Barnoin", "Barral", "Baudri", "Bérard", "Bérenger", "Bernon", "Bettolin", "Betton", "Brunon",
    "Burchard", "Caribert", "Centule", "Childebert", "Chilpéric", "Cillien", "Clodomir", "Clotaire", "Cloud",
    "Colomban", "Conan", "Conrad", "Cybard", "Dacien", "Dadon", "Dalmace", "Dambert", "Dioclétien", "Doat",
    "Drogon", "Durand", "Eadwin", "Ebbon", "Ebehard", "Eddo", "Edwin", "Egfroi", "Égilon", "Eilbert", "Einold",
    "Éon", "Ermenfred", "Ermengaud", "Ernée", "Ernold", "Ernoul", "Eumène", "Eunuce", "Euric", "Eustaise", "Euverte",
    "Evroult", "Fleuret", "Flocel", "Flodoard", "Flouard", "Flour", "Floxel", "Folquet", "Fortunat", "Foulque",
    "Frajou", "Frambault", "Frambourg", "Frameric", "Francaire", "Fulbert", "Gailhart", "Gaillon", "Garréjade",
    "Gaubert", "Gerbert", "Giboin", "Gildric", "Gislebert", "Godomer", "Gossuin", "Guéthenoc", "Guibin", "Guiscard",
    "Hatton", "Haynhard", "Héribert", "Herlebald", "Herlebauld", "Herlemond", "Hildebald", "Hildebrand",
    "Hilduin", "Hoel", "Honfroi", "Hugon", "Humbaud", "Isembert", "Ithier", "Jacquemin", "Jacut", "Lagier", "Lambert",
    "Lancelin", u"Léothéric", "Lidoire", "Lisiard", "Lothaire", "Lubin", u"Maïeul", "Malulf", "Marcuard", "Maric",
    "Materne", "Matfrid", "Matifas", "Maur", "Mauront", "Mesmin", "Milon", "Odo", "Oldaric", "Orderic", "Oricle",
    "Premon", "Rachio", "Radoald", "Radulf", "Raginard", "Raimbaut", "Raimbert", "Rainier", "Rainon", "Ramnulf",
    "Ranulfe", "Rataud", "Rodron", "Romary", "Roscelin", "Rostang", "Salvin", "Savaric", "Savary", "Sébaste",
    "Senoc", "Sicard", "Siegebert", "Sifard", "Sigebert", "Taillefer", "Taurin", "Théodebert", "Théodemar",
    "Theoderich", u"Théodran", "Thérouanne", "Thiégaud", "Ursicin", "Ursion", "Vantelme", "Volusien", "Warin",
    "Wigeric", "Willibert", "Wulfoald", "Wulgrin",
    "Acelin", "Amaury", "Anselme", "Anthiaume", "Arthaud", "Aubert", "Audibert", "Aymeric", "Aymon", "Barthélémi",
    "Benoît", "Bérard", "Bernier", "Bertrand", "Bohémond", "Edmond", "Enguerrand", "Ernaut", "Eudes", "Galaad",
    "Garin", "Garnier", "Gauthier", "Gauvain", "Gibouin", "Gilemer", "Girart", "Godefroy", "Gontran",
    "Gonzagues", "Grégoire", "Guerri", "Guilhem", "Hardouin", "Herbert", "Herchambaut", "Hubert", "Hugues",
    "Huon", "Jehan", "Lancelot", "Merlin", "Perceval", "Philibert", "Raoul", "Raymond", "Renaud", "Robert",
    "Roland", "Savari", "Sigismond", u"Tancrède", "Thibaut", "Tristan", "Urbain", "Ybert", "Yvain", u"Abélard", "Mathieu", "Dominique" ]

    PRENOMS_F = [
    "Ada","Adala","Adalberta","Adalind","Adalindis","Adallind","Adallinda","Adalmut","Adalrada","Adaltrude","Adaltrutis","Adaluuidis","Adalwif","Adda","Addela","Adela","Adelaidis","Adele","Adelhaid","Adelheid","Adeltrudis","Adhela","Adwala","Aebbe","Agatha","Agentrudis","Agglethrudis","Albelenda","Albofleda","Albruga","Alburch","Alburg","Aldguda","Aldgudana","Aldruth","Alfgarda","Alfild","Alflent","Alpaida","Alpaide","Alpais","Amabilia","Amalberga","Amalbirga","Amoltrud","Amulberga","Anselda","Ansgard","Anstruda","Aregund","Athalia","Athela","Atula","Aua","Auacyn","Aubirge","Aude","Audofleda","Audovera","Auekin","Auin","Auina","Auriana","Austrechild","Ava","Avacyn","Avekin","Avin","Baldechildis","Baltelda","Balthechildis","Balthildis","Basina","Bauin","Bava","Bavacin","Bave","Bavin","Begga","Belegardis","Benedicta","Berchildis","Berehta","Berenga","Beretrude","Bergard","Bergundis","Berhta","Beriungis","Berna","Bernewief","Bernewif","Berta","Bertaida","Bertha","Berthe","Berthefled","Berthefried","Berthegund","Berthildis","Berthlenda","Bertildis","Bertliana","Bertoane","Bertrada","Bertruda","Bertswinda","Bettin","Bilichildis","Blesinde","Blitekin","Boltiarda","Bova","Boviardis","Brunhild","Brunhilda","Burgundefara","Childebertana","Chlodeswinthe","Chlodosind","Chlothsinda","Chrodechildis","Chrodtrude","Chunsina","Cilia","Clodauuiua","Clothild","Clotild","Clotilde","Clotrada","Conegont","Conegundis","Conegunt","Crapahildis","Cunegonde","Cunegund ","Cunegundis","Dadin","Dagarada","Danburga","Deuteria","Doda","Dodda","Duda","Eadgithu","Ealswid","Ebertana","Edeberga","Edeborg","Ega","Egecin","Egeluuara","Egesburga","Egesloga","Ehgelhild","Ehgeluuara","Ellinrat","Emecin","Emma","Engelberga","Engelberge","Engelgard","Engelsuit","Engeltrude","Engeluuara","Engelwara","Enna","Erchembrog","Eremburgis","Ereprad","Erkembrog","Erkenbrog","Erkenburoc","Erkenrad","Ermecin","Ermegardis","Ermenberga","Ermengard","Ermengarda","Ermengarde","Ermengardis","Ermentrudis","Ermeswindis","Ermina","Erpsuid","Errictruda","Ethelchif","Ethelgard","Ethelgarda","Euerloga","Everelda","Evereldis","Faileuba","Fara","Fastrada","Flouerana","Folclind","Folclinda","Folcrada","Folcuuara","Folgarda","Folsuindis","Folsuuendis","Fordola","Fortlifh","Foy","Frauuara","Fredeburgis","Fredegunde","Frederada","Fredeuuara","Frethegard","Frethesuinda","Frethesuindis","Fridesuenda","Fridewiga","Frisburgis","Frithelinda","Frouuin","Frouuina","Galswinth","Geila","Gelduuara","Geneva","Genofeva","Gerberga","Geretrudis","Gerlent","Gerlinda","Gersenda","Gersuenda","Gersuinda","Gersvinda","Gertruda","Geruuara","Geua","Geva","Gisela","Gisla","Glismodis","Godalinda","Godeca","Godecin","Godelda","Godelinda","Godildis","Goduuara","Goiswinth","Gomatrudis","Gothuuera","Grimuuara","Gudula","Gudule","Gundrada","Gundrade","Gundradis","Guntheuc","Gunza","Guodhelda","Guodlia","Hadaken","Hamesindis","Harwara","Hatilde","Hazeca","Heilewif","Heilswinda","Heldeburga","Heletradana","Heleuuidis","Helinda","Heltrada","Hengelsenda","Herden","Herdin","Herenborg","Herenfrida","Herleva","Herlinda","Hermengarda","Hildberta","Hildborg","Hildcardis","Hildeberga","Hildeburg","Hildegard","Hildegarde","Hildegardis","Hildegund","Hildelana","Hildemunda","Hildeswindis","Hildeuuara","Hildeuuif","Hildewara","Hildewif","Hildrada","Hildwara","Hiltrude","Himiltrud","Hirmenlind","Hodierna","Hostaruuara","Hruodgarda","Hruotberta","Hruothraud","Ida","Idasgarda","Ideslef","Idesuuif","Ideswif","Idisiardis","Imicina","Imma","Ingela","Ingelburga","Ingelswindis","Ingeltrud","Ingeltrude","Ingeltrudis","Ingeluuara","Ingelwara","Ingitrude","Ingoberg","Ingunde","Iodberta","Iolitha","Irmengard","Irmenhild","Irmenlind","Irmgard","Irmingard","Isa","Isburch","Itta","Joveta","Kunegund","Landburuga","Landgarda","Landrada","Lanthechilde","Lanthildis","Lantuuara","Lebdrudis","Leddinga","Leubast","Leubovera","Leuekin","Leuuich","Liaueld","Lidiardis","Liedrada","Liefhun","Lieftet","Lietgarda","Lietgardis","Lietuuif","Lieuuara","Lifgarda","Liobsynde","Liodburga","Liodgard","Liodrada","Litburh","Litgardis","Litiardis","Liutgarde","Luitgarde","Machtildis","Madelgarda","Madelgarde","Madelrada","Madhalberta","Magnatrude","Magthildis","Magtildis","Marcatrude","Marcovefa","Markuuara","Mathildis","Mauriana","Mechtild","Megenberta","Megendrod","Megenhelda","Megenlind","Megenlioba","Megensind","Megensinda","Megenuuara","Meinburg","Meinnelda","Meinsent","Meinswindis","Menborch","Merofled","Merwig","Methdin","Moschia","Murina","Nantechildis","Nidlebis","Nordrada","Oda","Odburga","Odela","Odgiva","Odguda","Odgudana","Odlenda","Odriana","Ogiva","Olburgis","Olga","Osgarda","Osgiua","Otberta","Otgiua","Otgiva","Oydela","Pharahildis","Plectrudis","Radborg","Radburg","Radburgis","Radegund","Radeken","Radgert","Radlia","Radogund","Radsuinda","Ragnachilde","Rainilda","Rainildis","Ramburga","Regana","Regenburuga","Regenelda","Regenlind","Regenset","Reginsuint","Regintrude","Regnetrudis","Regneuuig","Reinewif","Reingard","Reingardis","Reingart","Reingaud","Reingod","Reinsuent","Renburgis","Rennewief","Riberta","Richelda","Richildis","Riclindis","Ricsuinda","Rigunth","Rikildis","Rinelt","Rinilda","Rodburga","Rodgarda","Rodgardae","Rofsind","Rosamund","Rotburga","Rothaide","Rothin","Rotlenda","Rotrud","Rotrude","Rotrudis","Ruodhaid","Ruothild","Ruothilde","Seburg","Seburga","Siborch","Siburg","Sigarda","Sigberta","Sigeberta","Sigeburgis","Sigethrod","Sigiburgis","Snelburch","Stenburch","Stilleuuara","Strilleburg","Suitburgis","Susanna","Swanahilde","Syardis","Teudsindis","Teutberga","Thancuuara","Theaduuara","Thedela","Theodelinda","Theoderada","Theodrada","Theodrade","Theudechild","Theudelinde","Theutberga","Thidela","Thieda","Thietgarda","Thietuuich","Thietwara","Thiodsind","Thiodsuinda","Thiutuuara","Thrasborg","Thrudberga","Ticekin","Tietlenda","Tietza","Trhutborgana","Trudlinde","Trutilda","UUaldburg","UUaldethruda","UUeremund","UUerenburoc","UUiburgis","UUindborog","UUinebarga","UUireda","UUlgarda","Uda","Ultrogotha","Uoldolberta","Veneranda","Vrowecin","Vualdberta","Vualdedruda","Vualdetruda","Vuifken","Vuinetberta","Vuiuechin","Vuldretrada","Vulfegundis","Waldrada","Wavin","Wiburgis","Wihted","Wilberga","Wilgeva","Willelda","Willesuindis","Wisigard","Wivecin","Wivin","Wlbergis","Wlbgis","Wlfildis","Wlgert",
    "ADELAIDE", "AGNES", "ALIENOR", "ANASTASE", "ANASTASIE", "ASTRID", "AUDE", "AURE",
    "Aalis", "Ada", "Adalarde", "Adalasinde", "Adalburge", "Adalinde", "Adalsende", "Adalsinde", "Ade",
    "Adélaïde", "Adelberge", "Adèle", "Adelheit", "Adeline", "Adelsinde", "Adnette", "Adrehilde", "Advise", "Aélais",
    "Aelidis", "Aelis", "Aélith", "Aénor", "Agarde", "Agathe", "Agelberte", "Ageruchia", "Agnoflède", "Aiga", "Aïn",
    "Alaine", "Alaison", "Alaiseta", "Alaizie", "Alarèse", "Alayde", "Alazaïs", "Albérade", "Albereda", "Albérée",
    "Alberte", "Albine", "Alboflède", "Alchima", "Alcima", "Aldeberge", "Aléide", "Aliénor", "Aliète", "Aliote",
    "Alix", "Almodis", "Ameline", "Aneglie", "Ansgarde", "Arambour", "Aremburge", "Arlette", "Asceline",
    "Assalid", "Attala", "Audeburge", "Audefledis", "Audovère", "Aubrée", "Auge", "Austreberthe", "Azelaïs",
    "Barbe", "Balde", "Bathilde", "Bayonne", "Béatrix", "Bénigne", "Berthe", "Betton", "Boussarde", "Brunehaut",
    "Brunissende", "Carensa", "Carétène", "Clervie", "Clotsende", "Clotsinde", "Dangerosa", "Déda", "Dies",
    "Elbore", "Eliette", "Elvide", "Emillane", "Emma", "Erembourg", "Ermelne", "Ermengarde", "Ermenjart",
    "Ermentrude", "Ermesinde", "Etiennette", "Eudoxie", "Eusébie", "Fleur", "Floberte", "Flodoberte",
    "Flor", "Flore", "Foi", "Framehilde", "Franchilde", "Gabrielle", "Gausle", "Gebétrude", "Gerberge",
    "Gerberte", "Gerloc", "Gersinde", "Gillete", "Gillote", "Gisla", "Glossinde", "Gontrade", "Guen",
    "Guillemette", "Guiraude", "Hélits", "Hermine", "Hersent", "Hildegarde", "Huguette", "Hugonette",
    "Hylde", "Ide", "Inde", "Ingonde", "Jutta", "Lampagia", "Léceline", "Leudeberte", "Liutgarde", "Mahaud",
    "Mahaut", "Malorsie", "Marguerite", "Mathe", "Mathie", "Mathilde", "Mechtilde", "Mélie", "Métronie", "Mode",
    "Nantechilde", "Ode", "Odete", "Odile", "Odonette", "Opportune", "Ostrogotho", "Pétronille", "Phébalde",
    "Placidina", "Plectrude", "Poppa", "Praetoria", "Pulcelle", "Ragnachilde", "Régina", "Renaude", "Richilde",
    "Rictrude", "Rixende", "Robresse", "Rodheid", "Rosemonde", "Rothaïde", "Rotrude", "Sanche", "Sancie", "Sara",
    "Sédeleude", "Sénégonde", "Sichède", "Souveraine", "Thelchilde", "Théodechilde", "Théodora", "Théodrade",
    "Théophanie", "Waldrade", "Yolande", "Yselda", "Ysoir",
    "Aalais", "Aliénor", "Alix", "Anthéa", "Aremburge", "Artémise", "Astride", "Aude", "Barbe", "Barberine", "Béatrix",
    "Berthe", "Blanche", "Blancheflor", "Bradamante", "Brunehaut", "Cathau", "Diane", "Ermessende", "Gallendis",
    "Geneviève", "Grisélidis", "Gudule", "Guenièvre", "Hélix", "Héloïse", "Hermeline", "Hersende", "Hildegarde",
    "Iseult", "Léonor", "Letgarde", "Mahaut", "Mélissande", "Mélusine", "Milesende", "Morgane", "Ursule", "Viviane"]

    # condition : être chrétien
