from extremis.coteries import coterie
from extremis.socio_eco.metiers import metier
from extremis.humanite import trait
from extremis.geographie import quartier
import random

class Conquistadors(coterie.Coterie):

    NOM = u"Conquistadors"
    ID = u"conquistadors"

    def __init__(self):
        self.nom_ = Conquistadors.NOM
        self.id_ = Conquistadors.ID
        self.quartier_ = quartier.SaintMalo.NOM

    def getLabelUniversite(self):
        return "univConquistadors"

    def GetTraitsCompatibles(self):
        """
        si le perso a ces caracs il a plus de chances de vouloir rejoindre cette coterie
        """
        return [ \
            trait.Ambition.NOM, \
            trait.Opportunisme.NOM, \
            trait.Cupidite.NOM, \
            trait.Constitution.NOM, \
            trait.Pragmatisme.NOM, \
            trait.Violence.NOM
            ]

    def GetMetiersCompatibles(self):
        """
        si le perso a des compétences dans ces métiers il a plus de chances de vouloir rejoindre cette coterie où ils sont souvent pratiqués
        """
        return [ \
            metier.Cartographe.NOM, \
            metier.Marchand.NOM, \
            metier.Forgeron.NOM, \
            metier.TueurDeMonstres.NOM, \
            metier.Aventurier.NOM, \
            metier.Marin.NOM, \
            metier.Chasseur.NOM, \
            metier.Guerrier.NOM
            ]

    def GetTraitsIncompatibles(self):
        """
        si le perso a ces caracs il a moins de chances de ne pas vouloir rejoindre cette coterie
        """
        return [ \
            trait.Prudence.NOM, \
            trait.Altruisme.NOM, \
            trait.Industrie.NOM, \
            trait.Sexualite.NOM, \
            trait.Poids.NOM, \
            trait.Richesse.NOM # les riches laissent rarement leur possession pour les aventures dangereuses
            ]

    def GetGentile(self, masculin):
        return "Conquistador"

    def GetPoidsDemo(self):
        """
        à quel point cette coterie est nombreuse dans la population
        1.0 = normal
        0.1 = 10 fois moins que la moyenne
        """
        return 0.7

    def GenererPortraits(self, age, masculin, metObj, portraits, traits):
        """
        ajoute des portraits correspondants aux caracs en paramètre (et à la coterie courante)
        traits : liste de tous les traits du perso sous forme d'objets 'Trait'
        """
        if masculin:
            if age >= 15:
                if age >= 20:
                    if age >= 30:
                        if age >= 40:
                            portraits.append("images/coteries/conquistadors/portraits/portrait_40+.jpg")
                            if age >= 50:
                                portraits.append("images/coteries/conquistadors/portraits/portrait_50+.jpg")
                                portraits.append("images/coteries/conquistadors/portraits/portrait_50+_b.jpg")
                                if age >= 60:
                                    portraits.append("images/coteries/conquistadors/portraits/portrait_60+.jpg")
                        # age > 30 ans
                        if age <= 60:
                            portraits.append("images/coteries/conquistadors/portraits/portrait_30-60.jpg")

                    # age > 20 ans
                    if age <= 50:
                        portraits.append("images/coteries/conquistadors/portraits/portrait_20-50.jpg")
                        portraits.append("images/coteries/conquistadors/portraits/portrait_20-50_b.jpg")
                        portraits.append("images/coteries/conquistadors/portraits/portrait_20-50_c.jpg")
                        portraits.append("images/coteries/conquistadors/portraits/portrait_20-50_d.jpg")
                        portraits.append("images/coteries/conquistadors/portraits/portrait_20-50_e.jpg")
                        portraits.append("images/coteries/conquistadors/portraits/portrait_20-50_f.jpg")
                        if metObj is not None and metObj.nom_ == metier.Pretre.NOM:
                            portraits.append("images/coteries/conquistadors/portraits/pretre_20-50.jpg")
                        if age < 40:
                            portraits.append("images/coteries/conquistadors/portraits/portrait_20-40.jpg")
                            portraits.append("images/coteries/conquistadors/portraits/portrait_20-40_b.jpg")
            # age > 15 ans
            if age < 40:
                portraits.append("images/coteries/conquistadors/portraits/portrait_15-40.jpg")
                portraits.append("images/coteries/conquistadors/portraits/portrait_15-40_b.jpg")
                portraits.append("images/coteries/conquistadors/portraits/portrait_15-40_c.jpg")
        else:
            if age > 15:
                if age < 35:
                    portraits.append("images/coteries/conquistadors/portraits/femme15_35.jpg")
                    portraits.append("images/coteries/conquistadors/portraits/femme15_35_b.jpg")
                    portraits.append("images/coteries/conquistadors/portraits/femme15_35_c.jpg")
                    portraits.append("images/coteries/conquistadors/portraits/femme15_35_d.jpg")
                    portraits.append("images/coteries/conquistadors/portraits/femme15_35_e.jpg")
                    portraits.append("images/coteries/conquistadors/portraits/femme15_35_f.jpg")
                if age >= 20:
                    if age >= 30:
                        if age <= 50:
                            portraits.append("images/coteries/conquistadors/portraits/femme30_50.jpg")
                        if age >= 40:
                            portraits.append("images/coteries/conquistadors/portraits/femme40+.jpg")
                            if age >= 50:
                                portraits.append("images/coteries/conquistadors/portraits/femme50+.jpg")
                    # age > 20 ans
                    if age < 45:
                        portraits.append("images/coteries/conquistadors/portraits/femme20_45.jpg")
                        if age < 35:
                            portraits.append("images/coteries/conquistadors/portraits/femme20_35.jpg")


        return portraits

    def CreerNom(self, masculin):
        """
        génère un patronyme correspondant à la coterie en question
        """
        return random.choice(Conquistadors.NOMS)

    def CreerPrenom(self, masculin):
        """
        génère un patronyme correspondant à la coterie en question
        """
        if masculin:
            return random.choice(Conquistadors.PRENOMS_M)
        else:
            return random.choice(Conquistadors.PRENOMS_F)

    PRENOMS_M = [ u"Rodrigo", u"Adis", u"Albertino", u"Alcidès",
    u"Ãšrbez",u"AgostÃ­n",u"Aimadeio",u"Aimadeo",u"Aima",u"Aimor",u"Albaro",u"Aleixandro",
    u"Aleixo",u"Alexandro",u"Alexo",u"Alfons",u"Alfred",u"Alifonso",u"Alixandre",
    u"Alodio",u"Alois",u"AltabÃ¡s",u"Alvaro",u"Alziz",u"Amancio",u"Amanzio",u"Amat",
    u"Anchel",u"Andre",u"Anizeto",u"Antan",u"Antoni",u"Aparizio",u"Arbert",u"Archentino",
    u"Archimiro",u"Armenchol",u"Arna",u"Artal",u"Ato",u"Augusto",u"Ausiais",u"Balanda­n",
    u"BalantÃ­n",u"BaldobÃ­n",u"BaldovÃ­n",u"Baleriano",u"Balero",u"Bartome",u"Bascuas",
    u"Bastian",u"Bauzis",u"Belasco",u"Belian",u"Benanzio",u"BenchamÃ­n",u"Benet",u"Benino",
    u"Bentura",u"Beremundo",u"Berenguer",u"Berenice",u"Bernal",u"Bernat",
    u"Bertolomeo",u"Bertran",u"Beturian",u"Beturio",u"BibiÃ¡n",u"Bisorio",u"Bital",
    u"Bitelio",u"Bitor",u"BizÃ©n",u"Blasco",u"Boecio",u"Boezio",u"Borrell",
    u"Borxa",u"Bras",u"Bruis",u"Buil",u"Burna",u"Calisto",u"Calixto",u"Calvet",u"Cancio",
    u"Canzio",u"Carapas",u"Carles",u"CeferÃ­n",u"Celdoni",u"Celesta­n",u"Celidonio",
    u"Celipe",u"Cerilo",u"Cesar",u"Chabier",u"Chacinto",u"Chacobo",u"Chaime",u"Chavier",u"Chazinto",
    u"Chenaro",u"Chenta­l",u"Cherardo",u"Cherbasio",u"Cherem­as",u"Cherian",
    u"Cherman",u"Cheromo",u"Cheronimo",u"Chervasio",u"Chesaos",u"Chil",u"Chiman",u"Chinaos",
    u"Chodofrodo",u"Choel",u"Chonas",u"Chonatain",u"Chorche",u"Chuan",u"Chuaqua­n",
    u"Chubenal",u"Chudes",u"Chulian",u"Chulio",u"Chusao",u"Chusta­n",u"Chustino",u"Chusto",
    u"Chuvenal",u"Ciceron",u"Cilipo",u"Climaon",u"Climent",u"Colas",u"Cristian",
    u"Cristofo",u"Daba­",u"Dachoberto",u"Dacil",u"Dalmacio",u"Dalma",u"Dalmazio",u"Davi­",
    u"Dazil",u"Dimetrio",u"Diochenes",u"Diochens",u"Dolcet",u"Domanech",u"Domingo",
    u"Donisio",u"Ebardo",u"Ela­",u"Elicio",u"Eliodoro",u"Elizio",u"Emerenziano",u"Eran",
    u"Ercules",u"Eriberto",u"Ermelando",u"Ermeneixildo",u"Ermenexildo",u"Ermengol",
    u"Ermes",u"Esteve",u"Etelbino",u"Etelva­n",u"Euchenio",u"Euloxio",u"Eunizie",
    u"Euridize",u"Eustazio",u"Fabricio",u"Fabrizio",u"Feli",u"Felip",u"Ferrain",u"Ferran",
    u"Ferrando",u"FertÃºs",u"Filipo",u"Flabio",u"Flavio",u"Florencio",u"Florenzio",u"Floriain",
    u"Franco",u"Francesc",u"Francho",u"Frederic",u"Gaba­n",u"Gabriel",u"Galeon",
    u"Galceran",u"Galindo",u"Garapasio",u"Garcia",u"Gausfred",u"GenÃ­s",u"Gibert",
    u"Gil",u"Gilabert",u"Gombal",u"Gomba",u"Grabiel",u"Graciain",u"Gracilian",u"Grapas",
    u"Graziliano",u"Guera",u"Guergorio",u"GuifrÃ©",u"GuillÃ©n",u"Guillem",u"Guillen",u"Guislabert",
    u"Gustabo",u"Gusta",u"Honorato",u"Honorio",u"Hug",u"Iago",u"IbÃ¡n",
    u"IbÃ³n",u"Ilario",u"Inacio",u"Indalecio",u"Indalezio",u"Inico",u"Inocencio",u"Inozencio",
    u"Ipol",u"Iram",u"Istebe",u"IvÃ¡n",u"Ixinio",u"Iziar",u"Izurbe",u"Jaume",
    u"Jeroni",u"Joan",u"Jordi",u"Josep",u"Ladisla",u"Laude",u"Lauriano",u"Leobixildo",u"Leovixildo",
    u"LiÃ³n",u"Libio",u"Licer",u"Licinio",u"Lixandro",u"Lizer",u"Lizinio",
    u"LlorenÃ§",u"LluÃ­s",u"LoÃ­s",u"Locadio",u"Lodosis",u"Loncio",u"Loren",u"Lorent",u"Lorente",
    u"LoriÃ©n",u"Lorient",u"Lucer",u"Luciano",u"Lucio",u"Lupercio",u"Luperzio",
    u"Luterio",u"Luzer",u"Luziano",u"Luzio",u"MachÃ­n",u"MaiximiliÃ¡n",u"Maiximo",u"Manel",u"Marc",
    u"MarcelÃ­n",u"Marcelo",u"MarciÃ¡n",u"MartÃ­",u"Marzal",u"Marzelino",
    u"Marzelo",u"Marziano",u"Masimiliano",u"Masimo",u"MatalÃ³n",u"Mate",u"Mauricio",u"Maurizio",
    u"Medardo",u"Menancio",u"Mencio",u"Meneixildo",u"Menzio",u"Merenciano",
    u"Meterio",u"Miguel",u"Milbio",u"Milio",u"Milvio",u"Minerbo",u"Minervo",u"Miquel",
    u"Mir",u"MiranÃ³n",u"Miterio",u"Moisen",u"NarcÃ­s",u"Narciso",u"Narziso",u"NazarÃ©",
    u"Nazaret",u"Nazario",u"Niceto",u"Nicola",u"Nunildo",u"Octavio",u"Olechario",u"Oleguer",
    u"Oliba",u"Olivar",u"Omero",u"Onorato",u"Onorio",u"Oracio",u"Orazio",
    u"Osbaldo",u"Osvaldo",u"Ot",u"Otabio",u"Otger",u"PÃ­o",u"PÃ³liz",u"Pancracio",
    u"Pancrazio",u"Paricio",u"Patrizio",u"Patrozinio",u"Paulo",u"Pedro",u"Peirod",u"Pelayo",
    u"Penya",u"Pere",u"Pero",u"PetrÃºs",u"Pietro",u"Pifanio",u"Placido",u"Plazido",
    u"Polito",u"Polonio",u"PonÃ§",u"Poncio",u"Ponzio",u"Pricio",u"Primitibo",u"Primitivo",
    u"Prizio",u"Prudencio",u"Prudenzio",u"Pueyo",u"Pulinario",u"Puy",u"Puyal",u"Rafael",
    u"Rafel",u"Raimundo",u"Rais",u"Ramiro",u"Ramon",u"Reimundo",u"Remiro",u"Remund",
    u"Ricart",u"Rochelio",u"Roger",u"RolÃ¡n",u"RoldÃ¡n",u"RomÃ¡n",u"Romeral",u"Rome",
    u"Ruixero",u"Ruxer",u"Salas",u"Salbador",u"Salbiano",u"Salbino",u"SalvÃ­n",u"Salvador",
    u"SalviÃ¡n",u"Salvino",u"SanÃ§",u"Sancho",u"SatornÃ­l",u"Satornil",u"Saturiano",u"Seberino",u"Sechio",u"Seguinus",u"Serbando",u"Servando",u"Severino",u"Siervo",u"Silbestre",u"Silvestre",u"SimÃ³",u"SimÃ³n",u"Simon",u"Sisto",u"Sixto",u"Solpicio",u"Solpizio",u"Sunyer",u"Superio",u"Taciano",u"Tarsicio",u"Tarsizio",u"Taziano",u"Terencio",u"Terenzio",u"Tito",u"TomÃ¡s",u"TornÃ­l",u"Ualdo",u"Uc",u"Uchenio",u"Ufemio",u"Ufrasio",u"Ugo",u"Uloixio",u"Uloxio",u"Umberto",u"UrruÃ©s",u"Usebio",u"Ustacio",u"ValantÃ­n",u"ValeriÃ¡n",u"Valero",u"Venancio",u"Ventura",u"Veremundo",u"VeturiÃ¡n",u"Veturino",u"Veturio",u"VibiÃ¡n",u"VicenÃ§",u"Vicent",u"Vidal",u"Violant",u"Vital",u"Vitelio",u"Vitor",u"Wenceslao",u"Wencesla",u"XimÃ©n",u"Ximeno",u"Yacma",u"Yacme",u"Zeferino",u"Zelestino",u"Zequiel",u"Zerilo",u"Zesar",u"Zirilo",
    u"Alioth",	u"Alirio",	u"Alterio",	u"Anyelo",
    u"Arcadio",	u"Arcangel",	u"Arles",	u"Alfie",
    u"Agapito",  	u"Ari",	u"Aureliano",  	u"Amancio",
    u"Ambrosio",  	u"Américo",  	u"Adolfito",  	u"Alejo",
    u"Amado",  	u"Apolinar",  	u"Asdrubal",  	u"Alonso",
    u"Arsenio",  	u"Audie",	u"Anibal",	u"Arnold",
    u"Albano",	u"Agustin", 	u"Andréas",	u"Andrès",
    u"Alexis",	u"Alejandro",	u"Alex",	u"Adam",
    u"Adan",	u"Alvaro",	u"Adriel",	u"Aristides",
    u"Angel",	u"Absalon",	u"Axel",
    u"Adonis",	u"Abelardo", u"Bélisario",	u"Blumaro",	u"Borris",
    u"Baldomero",	u"Bolívar",  	u"Baudelio",
    u"Bautista",	u"Bartolomé",  	u"Blas",	u"Buenaventura",
    u"Bernardo",	u"Baltasar",	u"Baltazar",	u"Bernabe", u"Clotario",	u"Crissolorio",	u"Curro",  	u"Carlito",
    u"Carlitos",  	u"Chuy",  	u"Chimo",  	u"Chester",
    u"Che",  	u"Candelario",  	u"Custodio",
    u"Calixto",	u"Chucho",  	u"Cayetano",	u"Clímaco",
    u"Conrado",	u"Cebrián",  	u"Ceferino",	u"Ciríaco",
    u"Celestino",  	u"Cecilio",  	u"Casimiro",  	u"Cruz",
    u"Constantino",	u"Cornelio",	u"Carol",	u"Carlos",
    u"Camilo",	u"Cristian",	u"Cristobal",	u"Christoph",
    u"Cipriano",	u"Cirilo",	u"César", u"Dago",	u"Dagoberto",	u"Dalmacio",	u"Dalmiro",
    u"Donaldo",	u"Desi",	u"Didacus",
    u"Diogenes",	u"Dimas",	u"Delfin",
    u"Diogène",	u"Daniel",	u"Damian",	u"Dennis",
    u"Dérek",	u"Dan",	u"Donovan",	u"Domingo",
    u"Duncan", u"Edagar",	u"Edelberto",	u"Edin",	u"Eras",	u"Euclido",	u"Ever",
    u"Epifanio",  	u"Eleuterio",  	u"Eustaquio",  	u"Ezequiel",
    u"Edelmiro",  	u"Emigdio",  	u"Efrain",	u"Eutimio",
    u"Eutropio",  	u"Eberardo",	u"Espiridión", 	u"Estavan",
    u"Esteban",	u"Ezéchiel",	u"Emanuel",	u"Eduardo",	u"Eduard",
    u"Ewen",	u"Edgar",	u"Eléazar",	u"Elias",
    u"Eli",	u"Elian",	u"Enrique",	u"Enzo",
    u"Elviro",	u"Eric",	u"Elmer",	u"Eladio",
    u"Edmundo", u"Fernan",	u"Facundo",	u"Fantino",	u"Fito",
    u"Felipe",	u"Florentino",  	u"Fulgencio",  	u"Fabricio",
    u"Fermin",	u"Fabian",	u"Florencio",	u"Félix",
    u"Faustin",	u"Faustino",	u"Fidel",	u"Francisco",
    u"Faride", u"Galeno",	u"Genaro",	u"Gerson",	u"Giano",
    u"Gildardo",	u"Gilmer",	u"Goar",	u"Gaspare",	u"Gasparo",	u"Gervasio",
    u"Godofredo",	u"Graciano",	u"Goyo",  	u"Gabino",
    u"Galo",  	u"Gualterio",	u"Gaston",	u"German",
    u"Gabriel",	u"Gaspard",	u"Gaspar",	u"Georges",
    u"Gérard",	u"Gerhard",	u"Geraldo",	u"Gonzalo",
    u"Guillermo",	u"Gideon",	u"Gadiel", u"Honorato",	u"Harlin",	u"Haroldo",	u"Homero",	u"Honorio",	u"Horaz",
    u"Huberto",	u"Heber",	u"Horacio",	u"Hiram",
    u"Hernan",	u"Hermenegildo",	u"Herberto",  	u"Heraclio",
    u"Hazel",	u"Herminio",	u"Hector",	u"Hernando",
    u"Hermès",	u"Hipolito",	u"Héliodoro",	u"Hubert",
    u"Humberto",	u"Hugo",	u"Heriberto",	u"Horace", u"Iberico",	u"Idelfonso",	u"Iskandar",
    u"Inocencio",  	u"Ildefonso",  	u"Isidro",	u"Ismaël",	u"Imanol",	u"Isaï",	u"Isaias",
    u"Isidoro",	u"Ignace",	u"Ignacio",
    u"Iñigo",	u"Ilian",	u"Israël",	u"Isaac", u"Jairo",	u"Janoc",	u"Jorvic",	u"Justo",
    u"Juanito",  	u"Jair",	u"Jenaro",	u"Jafet",
    u"Joaquin",	u"Jimeno",  	u"Jojo",	u"Julio",	u"Joshua",	u"Josue",
    u"José",	u"José-Luis",	u"Jeremias",	u"Juan", u"Juan-Cruz",	u"Juan-José",	u"Juan-Manuel",	u"Juan-Carlos",
    u"Juan-Pablo",	u"Juan-Domingo",	u"Jésus",	u"Jasper",
    u"Jorge",	u"Javier",	u"Jéronimo",	u"Jacinto",
    u"Jason",	u"Justino",	u"Jacob",
    u"Jacques",	u"Jakob",	u"Jacobo", 	u"Kaspar", u"Lautaro",	u"Leal",	u"Lenin",	u"Leobardo",
    u"Liberato",	u"Lonhard",	u"Lucero",	u"Lorencio",
    u"Lalo",  	u"Lincoln",	u"Ladislao",	u"Leocadio",
    u"Leoncio",  	u"Lope",  	u"Lisandro",	u"Lennard",
    u"Loreto",	u"Lancelot",	u"Laurent", u"Lazaro",	u"Léonard", u"Luis",	 u"Lino",	u"Léo",	u"Léonel",	u"Léonidas",
    u"Léonidès",	u"Luc",	u"Lucas",	u"Lilian",
    u"Lillian",	u"Lévi", u"Macedonio",	u"Magno",	u"Malaquias",	u"Marconio",
    u"Marquesio",	u"Mesias",	u"Milciades",	u"Misael",
    u"Miguelito",  	u"Marcelino",  	u"Marcelo",	u"Maximiano",
    u"Maximino",  	u"Moïses",	u"Manolo",  	u"Melchor",
    u"Macario",  	u"Marian",	u"Marcel",	u"Martin",
    u"Marcos",	u"Marco-Antonio",	u"Marcial",	u"Manuel",
    u"Malcom",	u"Mateo",	u"Matias",	u"Maximiliano",
    u"Maximo",	u"Michel",	u"Miguel",	u"Milton",
    u"Melchior",	u"Mauricio", u"Neftali",	u"Neptali",	u"Néron",	u"Nacho",
    u"Nicanor",	u"Nahum",	u"Nahuel",	u"Nando",
    u"Nacio",  	u"Natanael",  	u"Nicolao",  	u"Nelson", u"Nataniel",	u"Noël",	u"Natalio",
    u"Néréo",	u"Napoléon",	u"Nazareno",	u"Nicolas",
    u"Nestor", u"Oderico",	u"Onan",	u"Orangel",	u"Origenes",
    u"Obed",	u"Olegario",	u"Ona",	u"Oswaldo",
    u"Octavio",	u"Ovidio",	u"Otto",	u"Oliverio", u"Pancracio",	u"Patrocinio",	u"Pompeyo",	u"Pantaleon",
    u"Pastor",  	u"Pancho",	u"Pepe",  	u"Pepito",
    u"Pánfilo",  	u"Pacifico",	u"Paris",	u"Paco",
    u"Paquito",	u"Patricio",	u"Pascual",	u"Pablo",
    u"Paulino",	u"Paulo",	u"Pedro", u"Quique",  	u"Quintin", u"Radames",	u"Rainiero",	u"Randolfo",	u"Recaredo", u"Rigoberto", u"Rico",
    u"Raimundo",	u"Raymundo",  	u"Régulo",  	u"Rodolfito",
    u"Rosendo",  	u"Rainerio",  	u"Roldán",  	u"Ruperto",
    u"Remedios",	u"Rocio",	u"Robin",	u"Renzo",
    u"Rafaël",	u"Ramiro",	u"Roger",	u"Rogelio", u"Ramsès",	u"Ricardo",	u"Richard",
    u"Reynaldo",	u"Ramon",	u"Raymond",	u"Remigio",
    u"René",	u"Roque", u"Sigfrido",	u"Solimar",	u"Saulo",	u"Saveiro",
    u"Segismundo",	u"Segundo",	u"Shaqueel",	u"Silvino", u"Santino",	u"Santos",	u"Sans",
    u"Seve",  	u"Sandalio",  	u"Sofronio",  	u"Sosimo",
    u"Saturnino",  	u"Sabas",  	u"Saul", u"Sandro",	u"Santiago",	u"Sévero",	u"Silvestre",
    u"Sanson",	u"Salomon",	u"Simon",	u"Sébastian",
    u"Sancho",	u"Socrates",	u"Salvador",	u"Sol",
    u"Samuel", u"Transito",	u"Tomeo",	u"Torcuato",	u"Troilo",
    u"Telemaco",	u"Tulio",	u"Tercero",  	u"Tiago",
    u"Tiburcio",  	u"Toño",  	u"Tancredo",  	u"Teódulo",
    u"Tadeo",	u"Téo",	u"Tobias",	u"Téodoro",
    u"Tyrone",	u"Toni",	u"Tomas",	u"Tirso",
    u"Téobaldo",	u"Telmo",	u"Téofilo",	u"Toribio", u"Ubaldino",	u"Urso",	u"Uzziel",	u"Ulises", u"Valdo",	u"Venancio",	u"Venceslao",	u"Velasco",
    u"Valdemar",	u"Victorino",  	u"Vidal", u"Venceslas",	u"Vilmar",	u"Vicente",	u"Valentin", u"Victor", u"Wenceslao",	u"Waldo", u"Wilfredo", u"Waldemar", u"Ximeno",  	u"Xaver",	u"Xavier",
    u"Ysmaël",	u"Yamil",	u"Yago",	u"Yaël",
    u"Yuli", u"Zafiro",	u"Zacarias", u"Zoilo" ]

    PRENOMS_F = [ u"Gabriella", u"Adalia", u"Abi", u"Abril", u"Adamaris",
    u"Abelina",u"Adela",u"AgnÃ¨s",u"Agostina",u"Aimor",u"Alba",u"Aledis",u"Aleixandra",u"Alexandra",u"Alicia",u"Alizia",u"Almodis",u"Alodia",u"AltabÃ¡s",u"Alvira",u"Alziz",u"Anchela",u"Ancheles",u"Anchels",u"Andreya",u"Anna",u"Antona",u"AnunciaciÃ³n",u"AnunziaziÃ³n",u"Araceli",u"Arazeli",u"Arraro",u"AscensiÃ³n",u"Asenoma",u"Asperanza",u"AsunciÃ³n",u"AsunziÃ³n",u"AszensiÃ³n",u"AusiÃ¡s",u"Avelina",u"Azucena",u"Azuzena",u"Balandina",u"Baldesca",u"Baleria",u"Baleriana",u"Balma",u"Banesa",u"BascuÃ©s",u"Baucis",u"Beatriu",u"Begonia",u"Benchamina",u"Bera",u"Berenguela",u"Berenice",u"Berenize",u"Beronica",u"Berta",u"Bilma",u"Biolante",u"Bioleta",u"Birchinia",u"Biridiana",u"Birila",u"Birilia",u"Birtudes",u"Bitoria",u"Bizena",u"Blanca",u"Blanga",u"Brichida",u"Brixida",u"Bruis",u"Buil",u"Carmeta",u"Casbas",u"Celena",u"Celia",u"Celidonia",u"Celipa",u"Chacinta",u"Chanira",u"Chazinta",u"ChazmÃ­n",u"Chenobeba",u"Chenoveba",u"ChentÃ­l",u"Chesusa",u"ChinÃ©s",u"Chinebra",u"Chorcha",u"Chuana",u"Chuaquina",u"Chulia",u"Chuliana",u"Chulieta",u"Chusefa",u"Chusta",u"Cilia",u"Cillas",u"Cintia",u"Cirenia",u"Clara",u"Colasa",u"ConcepciÃ³n",u"ConstanÃ§a",u"ConzeziÃ³n",u"Crestina",u"Cristeta",u"Delia",u"Dimetria",u"DolÃ§a",u"Dolors",u"Dominga",u"Donata",u"Donisia",u"DulcÃ­a",u"Dulza",u"Dulze",u"Dulzis",u"Ebanchelina",u"Ebelina",u"ElÃ­",u"Elbira",u"Elionor",u"Elisabet",u"Emma",u"EncarnaciÃ³n",u"EncarnaziÃ³n",u"Engracia",u"Engrazia",u"Enriqueta",u"Erenia",u"Ermessenda",u"Erminia",u"Ersilia",u"EsaltaziÃ³n",u"Esperia",u"Estela",u"EulÃ lia",u"Evanchelina",u"Evelina",u"ExaltaciÃ³n",u"FelÃ­cia",u"Feli",u"Felicidat",u"Felicitas",u"Felisa",u"FelizidÃ¡",u"Felizitas",u"Ferranda",u"Fonfrida",u"Francesca",u"Francha",u"Francina",u"Franzina",u"Gala",u"Gisela",u"Gorba",u"Grabiela",u"Graciela",u"Graziela",u"GuayÃ©n",u"Guergoria",u"Guillema",u"Guillena",u"Guisla",u"Iciar",u"IdalÃ­",u"Idoia",u"IguÃ¡cel",u"IguÃ¡zel",u"Ilda",u"Iliena",u"Illarz",u"Iracena",u"Iram",u"Irazena",u"Isabel",u"Isabela",u"Isperia",u"Ixeia",u"Ixeya",u"Ixinia",u"Izarbe",u"Izurbe",u"Jara",u"Joana",u"LÃºzia",u"Laude",u"Lauriana",u"Lena",u"Leticia",u"Letizia",u"LibertÃ¡",u"Libertat",u"Liena",u"LiliÃ¡n",u"LluÃ¯sa",u"Loisa",u"Loreto",u"LucÃ­a",u"Lucila",u"Lutecia",u"Lutezia",u"LuzÃ­a",u"Luzila",u"Madalena",u"Magdalena",u"Malba",u"Malbina",u"Malva",u"Malvina",u"MarÃ­a",u"Mara",u"Marcela",u"Margarida",u"Maria",u"Mariona",u"Marta",u"Martina",u"Marzela",u"Masima",u"Maxima",u"Mercet",u"Merenciana",u"Milia",u"Minerva",u"Miraglos",u"Monlora",u"NatibidÃ¡",u"Natividat",u"Nieus",u"Nunila",u"Nuria",u"NuvÃ­lia",u"Obarra",u"Odulia",u"Olaria",u"Olibia",u"Oliva",u"Olivia",u"OrdÃ¡s",u"Orosia",u"Ortensia",u"Patricia",u"Patrizia",u"Patrocinio",u"PeÃ±a",u"Penya",u"Peronella",u"PiedÃ¡",u"Piedat",u"Piera",u"Pifania",u"Pilar",u"Pilara",u"Pineta",u"Pirineye",u"Polita",u"Polonia",u"PonÃ§a",u"Porzia",u"Priscila",u"Priszila",u"Pueyo",u"Puy",u"Puyeta",u"Rafela",u"Raimunda",u"Raina",u"Rais",u"Reixina",u"ResurreciÃ³n",u"Rexina",u"Romeral",u"Rosabel",u"Rosenda",u"RoxÃ­o",u"RozÃ­o",u"Rut",u"SalÃº",u"Salas",u"Salut",u"Salz",u"SanÃ§a",u"SescÃºn",u"Silbia",u"Silvia",u"Sis",u"SoledÃ¡",u"Soledat",u"Telba",u"Telva",u"Teresa",u"Tremedal",u"Tresa",u"Tricia",u"TrinidÃ¡",u"Trinidat",u"Trizia",u"Ufemia",u"Unicie",u"Uridice",u"UrruÃ©s",u"Usebia",u"Valandina",u"Valantina",u"Valeria",u"Valeriana",u"Vanesa",u"Vera",u"Veronica",u"Vicena",u"Violant",u"Violeta",u"Virchinia",u"Viridiana",u"Virilia",u"Virtutz",u"Vitoria",u"Xara",u"Ysabel",u"Zelena",u"Zelia",u"Zilia",u"Zillas",u"Zintia",u"Zirenia",u"Zoya",
    u"Adelma",	u"Agostina",	u"Agueda",	u"Aidée",
    u"Ailen",	u"Alcira",	u"Aldana",	u"Alejandra",
    u"Alfonsina",	u"Almudena",	u"Alondra",	u"Ambar",
    u"America",	u"Amparo",	u"Anaeli",	u"Analia",
    u"Analis",	u"Angeles",	u"Antonieta",	u"Araceli",
    u"Arantza",	u"Aranza",	u"Arcelia",	u"Arellys",
    u"Ariadna",	u"Ariana",	u"Arianne",	u"Aroa",
    u"Ayelen",	u"Aylen",	u"Azucena",	u"Azul",
    u"Asunción",  	u"Asun",  	u"Ascensión",  	u"Amarilis",
    u"Amaranta",  	u"Adoración",  	u"Aracelis",  	u"Aracely",
    u"Anunciación",  	u"Angelita",  	u"Amada",  	u"Alita",
    u"Adora",  	u"Adelita",  	u"Azeneth",  	u"Amaya",
    u"Amy",	u"Amadéa",	u"Alanis",	u"Aïsha",
    u"Agnès",	u"Agustina",	u"Andréa",	u"Adelaïda",
    u"Alicia",	u"Alison",	u"Alexa",	u"Alexandra",
    u"Alexia",	u"Aglaé",	u"Aura",	u"Arantxa",
    u"Ana",	u"Anabel",	u"Anabella",
    u"Ana-Maria",	u"Ana-Laura",	u"Ana-Clara",	u"Ana-Luisa",
    u"Ambrosia",	u"Ariel",	u"Angalina",
    u"Adela",	u"Adelina",	u"Aline",	u"Amaranthe",
    u"Ainhoa",	u"Afra",	u"Avelina", u"Benilda",	u"Betiana",	u"Betina",	u"Betsabe",
    u"Briseyda",	u"Benigna",  	u"Bernardita",
    u"Bethania",  	u"Bienvenida",  	u"Brunilda",  	u"Brunella",	u"Benita",	u"Bertha",	u"Blanca",
    u"Blanca-Estèla",	u"Bella",	u"Beatriz",	u"Begoña",
    u"Brenda",	u"Belen", u"Candela",	u"Candelaria",	u"Caridad",	u"Carlina",
    u"Carlota",	u"Catalia",	u"Celene",	u"Charo",
    u"Chita",	u"Concepcion",	u"Conception",	u"Conchita",
    u"Cintia",	u"Circe",	u"Citlalli",	u"Claudina",
    u"Calixta",  	u"Cande",  	u"Candelas",  	u"Carmelita",
    u"Celestina",  	u"Chelo",  	u"Chus",  	u"Concha",
    u"Consuela",	u"Crescencia",  	u"Cruzita",  	u"Custodia",
    u"Célia",	u"Carmina",	u"Coral",	u"Constanza",
    u"Carolin",	u"Clarisa",	u"Chiara-Maria",
    u"Corina",	u"Cloé",	u"Célina",
    u"Carina",	u"Catalina",	u"Catherine",	u"Casandra", u"Dalma",	u"Damaris",	u"Darlyne",	u"Deidamia",
    u"Delicia",	u"Denisse",	u"Dilcia",
    u"Dilean",	u"Dinora",	u"Dominga",	u"Domitila",
    u"Dina",	u"Danaé",	u"Désirée",	u"Dana",
    u"Dania",	u"Dulce",	u"Delta",	u"Doïna",
    u"Dominica",	u"Dominico",	u"Daina", 	u"Edelmira",	u"Edilma",	u"Eduina",
    u"Elba",	u"Elcira",	u"Elenor",	u"Elida",
    u"Elinathan",	u"Eloisa",	u"Elva",
    u"Emilce",	u"Encarnacion",	u"Enriqueta",	u"Ercilia",
    u"Erlinda",	u"Esneda",	u"Etelvina",	u"Evangelina",
    u"Evelia",	u"Elodia",  	u"Emelina",  	u"Emigdia",
    u"Emperatriz",  	u"Encarna",  	u"Encarnita",  	u"Eléonor",
    u"Estefania",	u"Emanuella",	u"Elena-Ofelia",
    u"Esther",	u"Estèla",	u"Estrella",	u"Ethel",
    u"Elvia",	u"Erika",	u"Eda",	u"Enid",
    u"Ernestina",	u"Esperanza",	u"Ermanda",	u"Emilia",
    u"Edna",	u"Ema",    u"Eve",	u"Evita", u"Felicidad",	u"Farina",	u"Felicitas",	u"Felipa",
    u"Felisa",	u"Fiama",	u"Filis",	u"Fina",
    u"Florentina",	u"Francisca",	u"Feliciana",  	u"Fran",
    u"Fernanda",	u"Fiona",	u"Florencia",	u"Félicia",
    u"Fidelia",	u"Fidelina",	u"Fidela",	u"Fania", u"Genovea",	u"Geraldina",	u"Gimena",	u"Ginna",
    u"Gintare",	u"Glorymar",	u"Goretti",	u"Graciela",
    u"Grecia",	u"Grisel",	u"Griselda",	u"Guadalupe",
    u"Guillermina",	u"Garsea",  	u"Graciana",  	u"Gala",
    u"Gina",	u"Giulianna",	u"Galia",	u"Gilberta",
    u"Gil",	u"Giselle",	u"Gisel",	u"Gisela",
    u"Giselda",	u"Gisell",	u"Gabriela",	u"Grace",
    u"Gracia",	u"Georgina",	u"Gertrudis", u"Gretel",	u"Gladys",	u"Glenda", u"Hebe",	u"Herendiara",	u"Herminia",
    u"Higinia",	u"Hilda",	u"Helena",	u"Hannah",	u"Hortensia",	u"Helga",	u"Heidi",	u"Hedda", u"Idalia",	u"Iracema",	u"Irupe",	u"Iselda",
    u"Isolda",	u"Itati",	u"Izana",	u"Idoya",
    u"Inmaculada",  	u"Isabela",  	u"Ivette",  	u"Iliana",
    u"Isolde",	u"Iona",	u"Itzel",	u"Inma",
    u"Isabel",	u"Isadora",	u"Ignacia",	u"Isaura",
    u"Isis",	u"Ina",	u"Irina", u"Jacinta",	u"Javiera",	u"Janeth",	u"Jannette",
    u"Jazmin",	u"Jerie",	u"Jimena", u"Jocabed",	u"Jorgelina",	u"Julieta",
    u"Justiniana",	u"Jesenia",  	u"Jessenia",  	u"Jesusa",
    u"Joaquina",  	u"Jordana",  	u"Jovita",  u"Julia",	u"Julieta",	u"Juliana",
    u"Jade",	u"Josépha",	u"Joséfina",	u"Jane",
    u"Janet",	u"Jeanne",	u"Joanna",	u"Johanna",
    u"Juanita",	u"Jeanette",	u"Jenna",	u"Joana",
    u"Juana",	u"Jo-Ann",	u"Jocelin",	u"Jésabel", u"Katja",	u"Kristine",	u"Karyme",	u"Katsya",
    u"Keisi",	u"Kobra",	u"Kyra",	u"Kiara",u"Karla",	u"Karina", 	u"Laisha",	u"Larisa",
    u"Laurentina",	u"Léonela",	u"Libertad",	u"Libia",
    u"Ligia",	u"Lihuen",	u"Liliam",	u"Lilyane",
    u"Lisaida",	u"Lisseth",	u"Lissette",	u"Lizzeth",
    u"Llisaida",	u"Lorelis",	u"Loyda",	u"Lucrecia",
    u"Luisiana",	u"Luisina",	u"Lupina",	u"Lupita",
    u"Luz",	u"Laurita",  	u"Loida",  	u"Ludmila",
    u"Léticia",	u"Lynda",	u"Léonor",	u"Laurence", u"Loren",	u"Lorna",	u"Laureana",
    u"Lida",	u"Lis",	u"Lola",	u"Lolita",
    u"Lupe",	u"Leslie",	u"Lucila",	u"Lucina",
    u"Lucinda",	u"Lilia", u"Lila",	u"Lourdes",	u"Lidia-Cira", u"Maca",	u"Macarena",	u"Maida",	u"Malenca",
    u"Marcela",	u"Margoth",	u"Marianela",	u"Mariangela",
    u"Mariangeles",	u"Maricel",	u"Maricela",	u"Marilina",
    u"Marilu",	u"Marlena",	u"Marzela",	u"Marzul",
    u"Mayra",	u"Merlina",	u"Micaela", u"Miguelina",	u"Milénia",	u"Millie",
    u"Mireya",	u"Mora",	u"Morela",	u"Macaria",
    u"Manola",  	u"Manuelita",  	u"Marianita",  	u"Maricruz",
    u"Marisela",  	u"Maristela",  	u"Martirio",  	u"Martita",
    u"Máxima",  	u"Mayte",  	u"Merche",  	u"Miguela",
    u"Modesta",  	u"Mélina",	u"Mélinda",	u"Mélisa",
    u"Mabel",	u"Magnolia",	u"Marita",	u"Maïtena",
    u"Maria-Auxiliadora",	u"Maria-Emilce",	u"Maria-Socorro",	u"Mariel",
    u"Mariela",	u"Mariella",	u"Marietta",	u"Marisol",	u"Marissa",	u"Mia",
    u"Myrna",	u"Maria-Eugénia",	u"Maria-Del-Carmen",	u"Maria-Inès",
    u"Maria-Fernanda",	u"Maria-José",	u"Maria-Del-Jésus",	u"Maria-Hélèna",
    u"Maria-Eléna",	u"Maïté",	u"Maria-Clara",	u"Maria-Paz",
    u"Maria-Lourdes",	u"Maritza",	u"Maria-Emilia",	u"Mariana",
    u"Maribel",	u"Maribella",	u"Martha",	u"Marta-Lucia",
    u"Martha-Sonia",	u"Marcelina",	u"Marcia",	u"Manel",
    u"Manuela",	u"Manuella",	u"Madeleine",	u"Madeline",
    u"Maddelline",	u"Madelyn",	u"Magdalena",	u"Malena",
    u"Milagros",	u"Monserrath",	u"Montserrat",	u"Mélanie",
    u"Magali",	u"Margaret",	u"Margot",	u"Marjorie",
    u"Margarita",	u"Maya", u"Nicolasa",  	u"Nohemi",  	u"Nieve",  	u"Narcisa",
    u"Nayeli",	u"Nelda",	u"Nelida",	u"Nellida",
    u"Nereida",	u"Nicolasia",	u"Nidia",	u"Nilda",
    u"Niriel",	u"Nube",	u"Nubia", u"Naomi", u"Nadina", u"Nuria", u"Nina",	u"Natacha",
    u"Natasha",	u"Nathalie",	u"Natali",	u"Noélia",	u"Nieves",	u"Nerea",
    u"Natividad",	u"Nazarena",	u"Nicole", u"Olalla",  	u"Odalys",  	u"Obdulia",	u"Odalis",
    u"Odili",	u"Olenca",	u"Onelia",	u"Orfilia",
    u"Orieta",	u"Oliva",	u"Olivera", u"Perpetua",  	u"Paca",  	u"Pastora",  	u"Pepita",
    u"Pascuala",  	u"Pacífica",  	u"Pandora",	u"Priscila",
    u"Paloma",	u"Paquita",	u"Paz",	u"Patricia",
    u"Petra",	u"Paula",	u"Paulina",	u"Piedad",
    u"Pia", u"Rosenda",  	u"Reyes",  	u"Ricarda",  	u"Ruperta",
    u"Rosalva",  	u"Rafa",	u"Rosita",	u"Rebeca",
    u"Reyna",	u"Rudecinda",	u"Roxana",	u"Raquel", u"Rafaëla",	u"Reina",	u"Romane",
    u"Rosalba",	u"Roselia",	u"Rosella",	u"Rosinda", u"Sancha",  	u"Sanchia",  	u"Sens",  	u"Sence",
    u"Salud",  	u"Susanita", u"Socorro",
    u"Stela", u"Surama",	u"Sahara",
    u"Salena",	u"Silvina",	u"Siomara",	u"Sylma",
    u"Samanta",	u"Samara",	u"Sandra",	u"Sasha",
    u"Stella-Maris",	u"Savannah",	u"Sélina",	u"Susana",
    u"Salomé",	u"Shakira",	u"Saraï",
    u"Selenia",	u"Soledad", u"Teresita",  	u"Teófila",  	u"Tomasa",  	u"Tere",
    u"Taalia",	u"Taua",	u"Trinidad",	u"Talia",
    u"Trini",	u"Thaïs",	u"Thelma",	u"Telma", u"Uma",	u"Uriel", u"Valencia",  	u"Visitación",  	u"Varinia",	u"Vicenta",
    u"Vasti",	u"Venecia",	u"Ventura",	u"Verenice",
    u"Violeta",	u"Valeska",	u"Vanina",	u"Vanesa",
    u"Vilma",	u"Victoria",	u"Verena", u"Xochilt",  	u"Ximena",	u"Xiomara",	u"Xochitl",
    u"Xénia", u"Yesenia",  	u"Ysabel",  	u"Yanet",	u"Yannel",
    u"Yadira",	u"Yanina",	u"Yazmin",	u"Yaima",
    u"Yamila",	u"Yamile",	u"Yaneth",	u"Yanira",
    u"Yara",	u"Yareni",	u"Yasna",	u"Yennifer",
    u"Yesmine",	u"Yessena",	u"Yhoalibeth",	u"Yilda",
    u"Yuana",	u"Yolanda",	u"Yasmina",	u"Yasmin",
    u"Yvonne", u"Zarela",	u"Ziva",	u"Zenaïda",	u"Zaïda",
    u"Zulema",	u"Zulma",	u"Zunilda",	u"Zurine",
    u"Zoraïda",	u"Zoila" ]

    NOMS = [ u"Acosta", u"Acuña", u"Adalbéron",     u"Abril",
    u"AbadÃ­a",u"Abarca",u"AbellÃ¡n",u"Abiego",u"Acorella",u"AdriÃ¡n",u"Agea",u"Ager",u"Agramunt",u"AgustÃ­n",u"AlbarracÃ­n",
    u"AlberÃ³",u"AlcalÃ¡",u"Alcolea",u"Alfaro",u"Alicante",u"Almunia",u"Alos",u"Amalric",u"AragonÃ©s",u"Arcas",u"Aymerich",
    u"Aznar",u"Balaguer",u"Baldovinos",u"BandrÃ©s",u"Baptista",u"Barrachina",u"Batista",u"Bautista",u"Bermund",u"Boix",
    u"Bonfill",u"Borrell",u"Bruguer",u"Burguera",u"Burrell",u"Caballer­a",u"Caballero",u"Cabra",u"Cacho",u"Cajal",u"Calasanz",
    u"Calderaña",u"Canyelles",u"Castellblanc",u"Cebriaña",u"Centelles",u"Cerdaña",u"Ceret",u"Cirera",u"Claver",u"Clemente",
    u"Desclot",u"Donat",u"Egea",u"Ena",u"Entenza",u"Ermengol",u"Escolano",u"EstÃ©banez",u"Estanyol",u"Feliu",u"Ferrer",
    u"Font",u"Fortiaño ",u"Garcia",u"Gironella",u"Grau",u"Gualba",u"Guitarra",u"Jofre",u"Lagos",u"Latorre",u"March",u"Marquet",
    u"Martell",u"Martorell",u"Mas",u"Massa",u"Massot",u"Miran",u"Morer",u"Muntaner",u"Murillo",u"Navarro",u"Noguera",u"Notario",
    u"Oms",u"Penyafort",u"Planas",u"Ponts",u"Prat",u"Puig",u"Rami­rez",u"Ramon",u"Riba",u"Riera",u"Roca",u"Roig",u"Roldaño",u"Romero",u"Rosellao",u"Rovira",u"Sacristaño",u"Sagarra",u"Samper",u"Sanz",u"Segarra",u"Texidor",u"Torquelles",u"VallÃ¨s",u"Vilagrassa",u"Vilaregut",u"de Arcas",u"de la CaballerÃ­au"
    u"Aguilar",
    u"Aguilera",
    u"Aguirre",
    u"Alcaraz",
    u"Almodóvar",
    u"Alvar",
    u"Álvarez",
    u"Álvaro",
    u"Arocena",
    u"Arregui",
    u"Arteaga",
    u"Arteta",
    u"Aznar",
    u"Baeza",
    u"Bahamonte",
    u"Balaguer",
    u"Bañuelos",
    u"Barberá",
    u"Bárcenas",
    u"Bello",
    u"Berdugo",
    u"Berenguer",
    u"Biraben",
    u"Blasco",
    u"Bolívar",
    u"Cabestany",
    u"Cadalso",
    u"Campos",
    u"Campuzano",
    u"Canuto",
    u"Caperochipi",
    u"Carvallo",
    u"Casal",
    u"Castro",
    u"Catalán",
    u"Cebrián",
    u"Cedeño",
    u"Cervantes",
    u"Cervera",
    u"Cisneros",
    u"Colón",
    u"Cortés",
    u"Domínguez",
    u"Echeberría",
    u"Echepare",
    u"Encinas",
    u"Escobar",
    u"Feijoó",
    u"Fernández",
    u"Ferrando",
    u"Fraga",
    u"Francés",
    u"Franco",
    u"Gabaldón",
    u"Gacía",
    u"Gacías",
    u"Gació",
    u"Garcés",
    u"Garsés",
    u"Garzia",
    u"Garzón",
    u"Gaztea",
    u"Pérez",
    u"Gaciot",
    u"Garcea",
    u"Garceller",
    u"Gárcez",
    u"Garci",
    u"García",
    u"Garcías",
    u"Garibay",
    u"Garsea",
    u"Gartzea",
    u"Gartzes",
    u"Gartzia",
    u"Garzea",
    u"Gasía",
    u"Gassía",
    u"Gassías",
    u"Giménez",
    u"Gomez",
    u"Gómez",
    u"Góngora",
    u"González",
    u"Gorrochategui",
    u"Goya",
    u"Gutiérrez",
    u"Heredia",
    u"Hernández",
    u"Herrera",
    u"Herrero",
    u"Hortelano",
    u"Ibáñez",
    u"Irigoyen",
    u"Jiménez",
    u"Láñez",
    u"Llorente",
    u"López",
    u"Machado",
    u"Machain",
    u"Machinandiarena",
    u"maestre",
    u"Marichalar",
    u"Martínez",
    u"Matilla",
    u"Melo",
    u"Mendoza",
    u"Molina",
    u"Monardes",
    u"Montoya",
    u"Morales",
    u"Moreno",
    u"Morestin",
    u"Múgica",
    u"Muñoz",
    u"Murillo",
    u"Núñez",
    u"Ordoqui",
    u"Ortiz",
    u"Pacheco",
    u"Pastor",
    u"Pinilla",
    u"Puértolas",
    u"Quesada",
    u"Quílez",
    u"Ramírez",
    u"Ribera",
    u"Robledo",
    u"Rodas",
    u"Rodríguez",
    u"Rumi",
    u"Sanches",
    u"Sánchez",
    u"Sancho",
    u"Santana",
    u"Santín",
    u"Sedeño",
    u"Segura",
    u"Sepúlveda",
    u"Somoza",
    u"Soriano",
    u"Suárez",
    u"Tarín",
    u"Torres",
    u"Trujillo",
    u"Ubeda",
    u"Ubieto",
    u"Unamuno",
    u"Urcelay",
    u"Valenciano",
    u"Vargas",
    u"Velasco",
    u"Velasques",
    u"Velásquez",
    u"Velázquez",
    u"Vera",
    u"Verdugo",
    u"Vicente",
    u"Vidal",
    u"Villalobos",
    u"Villanueva", u"Villar", u"Ximenes", u"Ximénez", u"Zamora", u"Zapatero", u"Zaplana"
     ]

    # pour intégrer la coterie tests sur : beauté (dur) taille, habileté, poids
