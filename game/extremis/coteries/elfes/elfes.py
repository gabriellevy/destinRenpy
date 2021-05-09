from extremis.coteries import coterie
from extremis.socio_eco.metiers import metier
from extremis.humanite import trait
from extremis.geographie import quartier
import random

class Elfes(coterie.Coterie):

    NOM = u"Elfes"
    ID = u"elfes"

    def __init__(self):
        self.nom_ = Elfes.NOM
        self.id_ = Elfes.ID
        self.quartier_ = quartier.SaintGermainEnLaye.NOM

    def getLabelUniversite(self):
        return "univElfes"

    def GetTraitsCompatibles(self):
        """
        si le perso a ces caracs il a plus de chances de vouloir rejoindre cette coterie
        """
        return [ \
            trait.Nature.NOM, \
            trait.Artiste.NOM, \
            trait.Serenite.NOM, \
            trait.Sensibilite.NOM, \
            ]

    def GetMetiersCompatibles(self):
        """
        si le perso a des compétences dans ces métiers il a plus de chances de vouloir rejoindre cette coterie où ils sont souvent pratiqués
        """
        return [ \
            metier.Acteur.NOM, \
            metier.Danseur.NOM, \
            metier.Dessinateur.NOM, \
            metier.Musicien.NOM, \
            metier.Poete.NOM, \
            metier.Alchimiste.NOM \
            ]

    def GetTraitsIncompatibles(self):
        """
        si le perso a ces caracs il a plus de chances de ne pas vouloir rejoindre cette coterie
        """
        return [ \
            trait.Violence.NOM, \
            trait.Franchise.NOM, \
            trait.Ambition.NOM \
            # les blessures en particuliers être défiguré
            ]

    def GenererPortraits(self, age, masculin, metier, portraits, valeursTraits):
        """
        ajoute des portraits correspondants aux caracs en paramtre (et à la coterie courante)
        valeursTraits : dico contenant en clé le nom des traits possédés par le personnage et en valeur leur niveau
        """
        global situation_
        if masculin:
            if age >= 15:
                if age >= 20:
                    if age >= 30:
                        portraits.append("images/coteries/elfes/portraits/portrait_30+.jpg")
                        if age >= 50:
                            portraits.append("images/coteries/elfes/portraits/portrait_50+.jpg")
                            portraits.append("images/coteries/elfes/portraits/portrait50+.png")

                    if age <= 50:
                        if trait.Franchise.NOM in valeursTraits and valeursTraits[trait.Franchise.NOM] <= trait.Trait.SEUIL_A_PAS: # A FAIRE : pas testé
                            portraits.append("images/coteries/elfes/portraits/sournois20_50.jpg")
                        if age <= 40:
                            portraits.append("images/coteries/elfes/portraits/portrait20-40.png")
                if age <= 40:
                    portraits.append("images/coteries/elfes/portraits/portrait_15-40_c.jpg")
                    portraits.append("images/coteries/elfes/portraits/portrait_15-40_d.jpg")
                    if age <= 30:
                        portraits.append("images/coteries/elfes/portraits/portrait_15-30.jpg")
        else:
            if age >= 15:
                if age >= 20:
                    if age >= 30:
                        portraits.append("images/coteries/elfes/portraits/femme30+.jpg")
                        # > 30 ans
                        if age <= 60:
                            portraits.append("images/coteries/elfes/portraits/portrait_30_60.jpg")
                    # >= 20 ans
                    if age <= 40:
                        portraits.append("images/coteries/elfes/portraits/Fportrait20-40.png")
                        portraits.append("images/coteries/elfes/portraits/Fportrait20-40_2.png")

                # age >= 15
                if age <= 40:
                    portraits.append("images/coteries/elfes/portraits/femme15_40.jpg")
                    if age <= 30:
                        portraits.append("images/coteries/elfes/portraits/portrait_15-30_b.jpg")
                        portraits.append("images/coteries/elfes/portraits/portrait_15-30_c.jpg")
                        portraits.append("images/coteries/elfes/portraits/portrait_15-30_d.jpg")

        return portraits

    # pour intégrer la coterie tests sur : beauté (dur) taille, habileté, poids

    def CreerNom(self, masculin):
        """
        génère un patronyme correspondant à la coterie en question
        """
        return ""

    def CreerPrenom(self, masculin):
        """
        génère un patronyme correspondant à la coterie en question
        """
        if masculin:
            return u"{}{}{}".format(random.choice(Elfes.NOMS_M1), random.choice(Elfes.NOMS_M2), random.choice(Elfes.NOMS_M3))
        else:
            return u"{}{}".format(random.choice(Elfes.NOMS_F1), random.choice(Elfes.NOMS_F2))

    NOMS_M1 = [
    u"Aba",u"Ada",u"Adan",u"Ado",u"Adr",u"Aeg",u"Ael",u"Aer",u"Aes",u"Afa",u"Aga",u"Agi",u"Aia",u"Aid",u"Aie",u"Ail",u"Aim",u"Air",u"Ait",u"Aiw",u"Akk",u"Ala",u"Alb",
    u"Ald",u"Ale",u"Ali",u"All",u"Alm",u"Alo",u"Alr",u"Alt",u"Alw",u"Am",u"Amr",u"And",u"Anf",u"Anl",u"Aol",u"Aqu",u"Ara",u"Aran",u"Arb",u"Ard",u"Arl",u"Aru",u"Asc",
    u"Ath",u"Aub",u"Aum",u"Avo",u"Aya",u"Ayd",u"Aye",u"Ayl",u"Aym",u"Ayr",u"Ayw",u"Bara",u"Bel",u"Beleg",u"Bia",u"Bra",u"Cai",u"Cam",u"Cas",u"Celeb",u"Cha",u"Che",
    u"Clu",u"Coh",u"Con",u"Cor",u"Curu",u"Dag",u"Dai",u"Dak",u"Dal",u"Dar",u"Del",u"Dev",u"Dra",u"Dru",u"Dur",u"Dyf",u"Edw",u"Edy",u"Ehl",u"Ehr",u"Eil",u"Ele",u"El",
    u"Ela",u"Elb",u"Eld",u"Ele",u"Eli",u"Elk",u"Ell",u"Elm",u"Elo",u"Elp",u"Elr",u"Elt",u"Elw",u"Ely",u"Emm",u"Ent",u"Ere",u"Erg",u"Eri",u"Erl",u"Ero",u"Esc",u"Est",
    u"Eth",u"Ett",u"Evi",u"Eyr",u"Fae",u"Fal",u"Fel",u"Fela",u"Fen",u"Fha",u"Fil",u"Fin",u"Fla",u"Fli",u"Fol",u"Fox",u"Fyl",u"Gae",u"Gal",u"Gan",u"Gar",u"Gil",u"Giu",
    u"Gla",u"Glo",u"Gol",u"Gor",u"Gra",u"Hae",u"Hag",u"Hal",u"Ham",u"Har",u"Has",u"Hat",u"Hoc",u"Hor",u"Hub",u"Ief",u"Iev",u"Ilb",u"Ili",u"Ill",u"Ilp",u"Ilr",u"Ilt",
    u"Inc",u"Ing",u"Ini",u"Inj",u"Int",u"Iol",u"Ith",u"Ivo",u"Ivl",u"Ivr",u"Iym",u"Iyr",u"Jan",u"Jao",u"Jas",u"Jha",u"Jon",u"Jor",u"Jos",u"Jup",u"Kai",u"Kat",u"Kel",
    u"Ken",u"Ker",u"Kes",u"Kha",u"Khi",u"Khu",u"Khy",u"Kie",u"Kii",u"Kin",u"Kiv",u"Kiy",u"Kla",u"Kol",u"Kuo",u"Kus",u"Kym",u"Kyr",u"Lae",u"Laf",u"Lam",u"Lao",u"Lar",
    u"Las",u"Lat",u"Leo",u"Lho",u"Lia",u"Lin",u"Lla",u"Lle",u"Llo",u"Lor",u"Lui",u"Lut",u"Luv",u"Lya",u"Lyk",u"Lys",u"Mae",u"Mai",u"Mal",u"Mar",u"Mel",u"Mer",u"Met",
    u"Mha",u"Mi'",u"Mih",u"Mii",u"Mir",u"Mla",u"Mol",u"Mon",u"Mor",u"Myr",u"Myt",u"Nae",u"Nar",u"Nas",u"Nav",u"Nel",u"Nes",u"Nev",u"Nha",u"Nie",u"Nin",u"Nlo",u"Nop",
    u"Nre",u"Nuv",u"Nyl",u"Nym",u"Nyv",u"Oac",u"Oen",u"Ohm",u"Ola",u"Ona",u"Onc",u"Onv",u"Ori",u"Orl",u"Orn",u"Orr",u"Ory",u"Osl",u"Ota",u"Oth",u"Pae",u"Pel",u"Pen",
    u"Pha",u"Phr",u"Pir",u"Ple",u"Pur",u"Pyr",u"Pyw",u"Qil",u"Quy",u"Rae",u"Rai",u"Ral",u"Rat",u"Rau",u"Rel",u"Ren",u"Rep",u"Res",u"Rha",u"Rhi",u"Rho",u"Rhy",u"Ril",
    u"Rol",u"Rot",u"Rua",u"Rue",u"Rui",u"Ruv",u"Ryc",u"Ryf",u"Ryo",u"Ryu",u"Sae",u"Sal",u"Sam",u"San",u"Sei",u"Sel",u"Sha",u"Shi",u"Shy",u"Sii",u"Sil",u"Sim",u"Sin",
    u"Ska",u"Son",u"Sor",u"Sud",u"Sun",u"Syl",u"Sym",u"Syt",u"Taa",u"Tae",u"Tal",u"Tam",u"Tan",u"Tar",u"Tas",u"Tat",u"Teh",u"Tei",u"Tha",u"The",u"Thu",u"Thurin",u"Tia",
    u"Tla",u"Tol",u"Tor",u"Tra",u"Tri",u"Ual",u"Uev",u"Ul",u"Uld",u"Urd",u"Usu",u"Uth",u"Vaa",u"Vae",u"Vam",u"Van",u"Var",u"Vel",u"Ven",u"Ves",u"Vir",u"Vol",u"Vor",u"Vud",
    u"Vul",u"Wis",u"Wyl",u"Wyn",u"Wyr",u"Xal",u"Xan",u"Xha",u"Yal",u"Yes",u"Yhe",u"Yly",u"Zab",u"Zal",u"Zan",u"Zao",u"Zel",u"Zen",u"Zho",u"Ab",u"Ad",u"Ae",u"Af",u"Ag",u"Ai",
    u"Ak",u"Al",u"Am",u"An",u"Ao",u"Aq",u"Ar",u"As",u"At",u"Au",u"Av",u"Ay",u"Be",u"Bi",u"Br",u"Ca",u"Ch",u"Cl",u"Co",u"Da",u"De",u"Dr",u"Du",u"Dy",u"Ed",u"Eh",u"Ei",u"El",u"Em",
    u"En",u"Er",u"Es",u"Et",u"Ev",u"Ey",u"Fa",u"Fe",u"Fh",u"Fi",u"Fl",u"Fo",u"Fy",u"Ga",u"Gi",u"Gl",u"Go",u"Gr",u"Ha",u"Ho",u"Hu",u"Ie",u"Il",u"In",u"Io",u"It",u"Iv",u"Iy",u"Ja",
    u"Jh",u"Jo",u"Ju",u"Ka",u"Ke",u"Kh",u"Ki",u"Kl",u"Ko",u"Ku",u"Ky",u"La",u"Le",u"Lh",u"Li",u"Ll",u"Lo",u"Lu",u"Ly",u"Ma",u"Me",u"Mh",u"Mi",u"Ml",u"Mo",u"My",u"Na",u"Ne",u"Nh",
    u"Ni",u"Nl",u"No",u"Nr",u"Nu",u"Ny",u"Oa",u"Oe",u"Oh",u"Ol",u"On",u"Or",u"Os",u"Ot",u"Pa",u"Pe",u"Ph",u"Pi",u"Pl",u"Pu",u"Py",u"Qi",u"Qu",u"Ra",u"Re",u"Rh",u"Ri",u"Ro",u"Ru",
    u"Ry",u"Sa",u"Se",u"Sh",u"Si",u"Sk",u"So",u"Su",u"Sy",u"Ta",u"Te",u"Th",u"Ti",u"Tl",u"To",u"Tr",u"Ua",u"Ue",u"Ul",u"Ur",u"Us",u"Ut",u"Va",u"Ve",u"Vi",u"Vo",u"Vu",u"Wi",u"Wy",
    u"Xa",u"Xh",u"Ya",u"Ye",u"Yh",u"Yl",u"Za",u"Ze",u"Zh" ]

    NOMS_M2 = [ u"a",u"e",u"o",u"i",u"",u"" ]

    NOMS_M3 = [
    u"aan",u"acvar",u"adan",u"adavar",u"ael",u"aen",u"aerae",u"aern",u"aernth",u"aeron",u"aeryn",u"afarin",u"aht",u"air",u"al",u"alen",u"ali",u"all",u"aln",u"alos",u"am",
    u"amar",u"amede",u"an",u"anas",u"anath",u"andal",u"andrach",u"andrar",u"ane",u"angyl",u"anlar",u"anor",u"anthir",u"aor",u"ar",u"arallin",u"aran",u"arelar",u"areth",
    u"arion",u"ark",u"arre",u"artael",u"arth",u"as",u"ath",u"athan",u"athanil",u"ather",u"athiel",u"authin",u"auver",u"bas",u"beth",u"blar",u"bor",u"born",u"bryl",u"bryn",
    u"byr",u"byran",u"car",u"cassan",u"chant",u"chyr",u"dacil",u"damar",u"dan",u"dar",u"ddin",u"deiym",u"del",u"dell",u"der",u"devv",u"dir",u"dor",u"drach",u"dreithen",
    u"dro",u"drol",u"droth",u"dual",u"duin",u"dusk",u"dynnar",u"dyr",u"e",u"ed",u"edd",u"efehon",u"eh",u"ehryn",u"eisin",u"el",u"elar",u"ele",u"eliorn",u"elladon",u"ellien",
    u"en",u"enal",u"endar",u"endil",u"endyl",u"enic",u"enth",u"er",u"ern",u"eron",u"eros",u"esin",u"essin",u"etheryl",u"ethuil",u"evar",u"fildor",u"fin",u"fire",u"flar",
    u"fros",u"fyndar",u"gan",u"gath",u"gauth",u"gen",u"had",u"haeryn",u"hai",u"hais",u"hal",u"hallus",u"haln",u"hanthar",u"har",u"haral",u"has",u"hazel",u"hel",u"hell",
    u"hidon",u"hild",u"hilion",u"hlaeril",u"hlin",u"hon",u"hul",u"hurach",u"huryn",u"ian",u"ianaro",u"idiah",u"iil",u"ik",u"ikanthae",u"ikoth",u"il",u"ilan",u"ilarro",
    u"ildyn",u"im",u"imar",u"in",u"indar",u"ion",u"ir",u"iral",u"is",u"isar",u"itar",u"ith",u"ithil",u"ithor",u"itran",u"jym",u"k",u"kalr",u"kyn",u"l",u"ladar",u"laer",
    u"lam",u"lan",u"lando",u"lanil",u"lanis",u"lar",u"lareo",u"las",u"leas",u"leath",u"lethil",u"levaur",u"lh",u"lin",u"lith",u"llan",u"llio",u"lmar",u"lor",u"lseith",
    u"lth",u"lu",u"luin",u"lyf",u"lyn",u"lyun",u"m",u"mar",u"mashal",u"mbaerth",u"mer",u"mir",u"mitar",u"mon",u"moth",u"mrail",u"muth",u"myn",u"n",u"naar",u"naeril",u"naeuth",
    u"naith",u"nak",u"nal",u"nalor",u"nar",u"naran",u"naril",u"ndal",u"ndar",u"ndaur",u"ndorn",u"ndorr",u"ndriel",u"nduil",u"ngyl",u"nivh",u"nn",u"nnatar",u"nnor",u"nor",
    u"nos",u"nthorn",u"nyll",u"nyn",u"nyth",u"o",u"odar",u"odas",u"odemar",u"oden",u"odluin",u"odmer",u"odmon",u"odre",u"odred",u"oduin",u"odwin",u"on",u"ondiel",u"ongar",
    u"onym",u"or",u"orim",u"orion",u"orlas",u"ornik",u"os",u"oss",u"ostroi",u"othil",u"otter",u"par",u"pen",u"perr",u"ph",u"phal",u"phant",u"phar",u"phon",u"phor",u"r",
    u"raddyth",u"rak",u"ral",u"rald",u"ran",u"randal",u"randir",u"randuil",u"ranthur",u"ras",u"rat",u"rath",u"rathath",u"rauth",u"ravym",u"rdan",u"rdh",u"rdryn",u"re",
    u"red",u"reiyn",u"rel",u"rellan",u"reth",u"ri",u"rian",u"rik",u"ril",u"rin",u"rindel",u"rion",u"ris",u"rist",u"rlan",u"rlion",u"rm",u"rmn",u"rnos",u"rntym",u"rod",u"rom",
    u"ron",u"rond",u"ros",u"roth",u"rphys",u"rrik",u"rshin",u"rshus",u"rtho",u"rtlar",u"ruil",u"rydal",u"ryl",u"ryll",u"rym",u"ryn",u"ryndam",u"s",u"saar",u"sala",u"san",
    u"saran",u"sarion",u"shor",u"sin",u"son",u"srin",u"ssae",u"st",u"stan",u"stel",u"sx",u"taar",u"tagor",u"tan",u"tar",u"tari",u"tarish",u"terin",u"th",u"thal",u"thalas",
    u"thalion",u"thalor",u"tham",u"thanglas",u"the",u"thgor",u"thil",u"thir",u"thomir",u"thoridan",u"thorn",u"tien",u"tos",u"uaneth",u"uar",u"ueth",u"ueve",u"ufan",u"uigh",
    u"uil",u"uin",u"umal",u"undyl",u"une",u"unia",u"urae",u"uraun",u"urel",u"us",u"uvethel",u"var",u"varan",u"vel",u"velore",u"ven",u"vendor",u"verel",u"veril",u"vhan",u"vyr",
    u"we",u"wellenar",u"win",u"yk",u"yl",u"ym",u"yn",u"ynn",u"ynnhv",u"ynnon",u"yor",u"yr",u"yrd",u"yrth",u"yth" ]

    NOMS_F2 = [
    u"a",u"adh",u"adyl",u"ae",u"ael",u"aela",u"aera",u"aerae",u"aestra",u"aethra",u"aevar",u"afain",u"ah",u"ahala",u"ahava",u"ain",u"ainn",u"ais",u"al",u"ala",u"alar",u"aleth",
    u"alla",u"alue",u"alurie",u"alya",u"alyn",u"ana",u"anae",u"anda",u"andi",u"andra",u"ani",u"ania",u"anna",u"anor",u"anthae",u"anthe",u"ar",u"ara",u"arda",u"aril",u"arla",
    u"arrel",u"aru",u"arzah",u"as",u"asha",u"ashta",u"asta",u"at",u"ath",u"atha",u"athla",u"athria",u"auntha",u"aya",u"biyra",u"ca",u"cca",u"cia",u"dal",u"dalar",u"dha",u"dia",
    u"dis",u"dra",u"drelle",u"due",u"dya",u"dyl",u"e",u"eae",u"edha",u"ee",u"eene",u"ei",u"eia",u"eira",u"el",u"ela",u"ele",u"elyth",u"ema",u"en",u"ena",u"endra",u"ene",u"enee",
    u"enoel",u"er",u"era",u"erae",u"erele",u"erina",u"erla",u"ern",u"eru",u"esca",u"esra",u"essa",u"esse",u"estri",u"eth",u"ethae",u"fain",u"farrel",u"gan",u"gara",u"ggan",
    u"gil",u"h",u"ha",u"hala",u"handra",u"hara",u"hee",u"heira",u"hen",u"hia",u"hie",u"hion",u"hleene",u"hn",u"hnee",u"honel",u"hra",u"hrel",u"hswana",u"hyl",u"hynna",u"hyrra",
    u"i",u"ia",u"iah",u"ian",u"ianna",u"iar",u"ica",u"ie",u"iel",u"ihn",u"ii",u"iisa",u"il",u"ilue",u"imnda",u"in",u"indra",u"inn",u"inne",u"io",u"ion",u"ira",u"is",u"isa",u"issa",
    u"italia",u"itia",u"ka",u"l",u"la",u"laevar",u"lahava",u"lanae",u"lara",u"laya",u"lda",u"le",u"lee",u"leene",u"lei",u"leia",u"lesca",u"leth",u"lia",u"limnda",u"litia",u"ll",
    u"lla",u"llee",u"llyss",u"lo",u"los",u"lossa",u"lsraa",u"lue",u"lurie",u"lya",u"lyn",u"lyntra",u"lyss",u"lyth",u"ma",u"mara",u"mbiyra",u"mna",u"mrithe",u"n",u"na",u"naestra",
    u"nas",u"nashta",u"nath",u"nda",u"ndi",u"ndra",u"ndue",u"ne",u"nee",u"nesra",u"nestri",u"ngara",u"ni",u"nia",u"nii",u"nilue",u"nna",u"nne",u"nnia",u"noel",u"nor",u"ntha",
    u"nthae",u"nthe",u"nthi",u"nyn",u"o",u"oel",u"ola",u"on",u"ona",u"onel",u"onyn",u"or",u"ora",u"orna",u"oru",u"ossa",u"owmoon",u"r",u"ra",u"radh",u"rae",u"raen",u"raethra",
    u"ralla",u"re",u"reae",u"rel",u"rele",u"relle",u"ren",u"reth",u"ria",u"rian",u"riel",u"rien",u"ril",u"rin",u"rina",u"rindra",u"rine",u"rio",u"ris",u"rissa",u"rithe",u"rl",
    u"rla",u"rlda",u"rn",u"rna",u"roel",u"ronel",u"rra",u"rria",u"rtala",u"rtha",u"ru",u"rue",u"ruil",u"ryl",u"ryllia",u"s",u"sa",u"sarda",u"sha",u"shnee",u"sia",u"sola",u"sra",
    u"sraa",u"ss",u"ssa",u"sse",u"ssra",u"sta",u"star",u"strae",u"stria",u"swana",u"synora",u"tala",u"talia",u"tarzah",u"ter",u"th",u"tha",u"thae",u"thara",u"thi",u"thiia",u"thla",
    u"thra",u"thria",u"thyl",u"thynna",u"ti",u"tora",u"trae",u"tria",u"trine",u"ua",u"ue",u"uil",u"uilas",u"uilos",u"untha",u"urel",u"uria",u"ustar",u"uthiia",u"vel",u"vren",u"wais",
    u"wen",u"wing",u"wmoon",u"ya",u"yat",u"ye",u"yl",u"ylla",u"yllia",u"ymna",u"yn",u"yna",u"ynor",u"ynora",u"yntra",u"yrl",u"yrra",u"yrria",u"ys",u"zee" ]

    NOMS_F1 = [
    u"Adan",u"Ae",u"Ael",u"Aer",u"Ah",u"Ahr",u"Ahs",u"Ai",u"Ail",u"Al",u"Ala",u"Ale",u"All",u"Alm",u"Alv",u"Aly",u"Am",u"Ama",u"Ame",u"Amk",u"Aml",u"Amn",u"Amr",u"An",u"Ana",u"And",
    u"Ane",u"Anh",u"Ann",u"Ar",u"Ara",u"Arc",u"Ari",u"Arl",u"Arn",u"Arr",u"Art",u"As",u"Ash",u"Au",u"Aul",u"Aur",u"Av",u"Ava",u"Ax",u"Axi",u"Ay",u"Ayd",u"Az",u"Aza",u"Be",u"Bel",u"Bem",
    u"Bl",u"Bly",u"Bo",u"Bon",u"Br",u"Bra",u"Breg",u"Bu",u"Bur",u"Ca",u"Cae",u"Cal",u"Ce",u"Cel",u"Celeb",u"Ch",u"Cha",u"Cho",u"Ci",u"Cil",u"Ciy",u"Cl",u"Cla",u"Cr",u"Cre",u"Cy",u"Cyi",
    u"Da",u"Dar",u"Das",u"Dat",u"De",u"Del",u"Deu",u"Dol",u"Du",u"Dui",u"Dur",u"Ea",u"Eal",u"Ec",u"Eca",u"Ed",u"Ede",u"Edhel",u"Edr",u"Ei",u"Eir",u"El",u"Ela",u"Ele",u"Eli",u"Ell",u"Elm",
    u"Elo",u"Ely",u"En",u"Ena",u"Es",u"Esh",u"Ess",u"Est",u"Esy",u"Fa",u"Fal",u"Fan",u"Far",u"Fau",u"Fay",u"Fh",u"Fha",u"Fi",u"Fie",u"Fil",u"Find",u"Ga",u"Gae",u"Galadh",u"Gay",u"Ge",
    u"Gem",u"Gh",u"Ghi",u"Gil",u"Gl",u"Gly",u"Gw",u"Gwe",u"Gwy",u"Gy",u"Gyl",u"Ha",u"Hac",u"Hal",u"Ham",u"Har",u"He",u"Hel",u"Hir",u"Ho",u"Hol",u"Hu",u"Huq",u"Hy",u"Hyc",u"Ia",u"Ial",
    u"Ik",u"Ike",u"Il",u"Ild",u"Ilm",u"Ils",u"Ily",u"Im",u"Imi",u"Imm",u"Imr",u"Io",u"Ioe",u"Ior",u"Ir",u"Irh",u"Is",u"Isi",u"It",u"Iti",u"Ity",u"Iy",u"Iyt",u"Ja",u"Jas",u"Je",u"Jea",
    u"Jh",u"Jha",u"Jhi",u"Ka",u"Kas",u"Kav",u"Kay",u"Ke",u"Kee",u"Kei",u"Ket",u"Key",u"Ky",u"Kyt",u"La",u"Laa",u"Lae",u"Lal",u"Laz",u"Le",u"Lei",u"Len",u"Let",u"Li",u"Lie",u"Lil",u"Lix",
    u"Ll",u"Lla",u"Lo",u"Lor",u"Lu",u"Lur",u"Lus",u"Ly",u"Lye",u"Lyi",u"Lym",u"Lyn",u"Ma",u"Mae",u"Mak",u"Mal",u"Mar",u"May",u"Me",u"Mei",u"Mel",u"Mer",u"Mi",u"Mic",u"Ml",u"Mla",u"Mn",
    u"Mnu",u"Mo",u"Mor",u"Mu",u"Mue",u"My",u"Myl",u"Myr",u"Na",u"Nab",u"Nae",u"Nak",u"Nam",u"Nan",u"Nau",u"Ne",u"Nei",u"Nep",u"Nex",u"Ni",u"Nim",u"Nit",u"Nl",u"Nla",u"Nu",u"Nua",u"Nue",
    u"Nuo",u"Nus",u"Ny",u"Nyl",u"Nyn",u"Oc",u"Och",u"Om",u"Omy",u"Os",u"Oso",u"Pe",u"Pen",u"Ph",u"Pha",u"Phe",u"Phu",u"Phy",u"Pyr",u"Qu",u"Qua",u"Ra",u"Rad",u"Rae",u"Ran",u"Rat",u"Re",
    u"Ren",u"Ri",u"Rin",u"Ro",u"Rod",u"Ros",u"Ru",u"Rub",u"Ry",u"Ryl",u"SaÃ©",u"Sa",u"Sae",u"Sael",u"Sai",u"Sak",u"San",u"Sar",u"Se",u"Sei",u"Sel",u"Sh",u"Sha",u"She",u"Shi",u"Shy",u"Si",
    u"Sin",u"So",u"Sol",u"Soo",u"Sor",u"Sp",u"Sph",u"Su",u"Sum",u"Sus",u"Sy",u"Syl",u"Sym",u"Syn",u"Syv",u"Ta",u"Tae",u"Tai",u"Tal",u"Tan",u"Tar",u"Te",u"Teh",u"Ter",u"Tet",u"Th",u"Tha",
    u"Ti",u"Tia",u"Tin",u"Tinu",u"Tir",u"Tis",u"Ts",u"Tsa",u"Ui",u"Uia",u"Ul",u"Ule",u"Um",u"Umr",u"Ur",u"Urm",u"Us",u"Usc",u"Va",u"Val",u"Vas",u"Ve",u"Vel",u"Ver",u"Ves",u"Vi",u"Via",
    u"Wy",u"Wyn",u"Ya",u"Yae",u"Yal",u"Yat",u"Yg",u"Ygr",u"Yn",u"Yns",u"Yr",u"Yrl",u"Yrn",u"Yrt",u"Ys",u"Ysm",u"Yu",u"Yul",u"Yun",u"Zo",u"Zoa" ]
