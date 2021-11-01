from extremis.coteries import coterie
from extremis.socio_eco.metiers import metier
from abs.humanite import trait
from extremis.geographie import quartier
import random

class Orks(coterie.Coterie):

    NOM = u"Orks"
    ID = u"orks"

    def __init__(self):
        self.nom_ = Orks.NOM
        self.id_ = Orks.ID
        self.quartier_ = quartier.Poissy.NOM

    def getLabelUniversite(self):
        return "univOrks"

    def GetTraitsCompatibles(self):
        """
        si le perso a ces caracs il a plus de chances de vouloir rejoindre cette coterie
        """
        return [ \
            trait.Violence.NOM, \
            trait.Franchise.NOM, \
            trait.Assurance.NOM, \
            ]

    def GetTraitsIncompatibles(self):
        """
        si le perso a ces caracs il a plus de chances de ne pas vouloir rejoindre cette coterie
        """
        return [ \
            trait.Intellectualisme.NOM, \
            trait.Industrie.NOM, \
            trait.Ambition.NOM, \
            trait.Sensibilite.NOM, \
            trait.Altruisme.NOM, \
            trait.Charme.NOM, \
            trait.Spiritualite.NOM, \
            trait.Artiste.NOM, \
            trait.Ascetisme.NOM, \
            trait.Sexualite.NOM, \
            trait.Prudence.NOM, \
            ]


    def GetPoidsDemo(self):
        """
        à quel point cette coterie est nombreuse dans la population
        2.0 = très grosse coterie
        1.0 = normal
        0.1 = 10 fois moins que la moyenne
        """
        return 3.0

    def GetMetiersCompatibles(self):
        """
        si le perso a des compétences dans ces métiers il a plus de chances de vouloir rejoindre cette coterie où ils sont souvent pratiqués
        """
        return [ \
            metier.Pilote.NOM, \
            metier.Guerrier.NOM, \
            metier.Parasite.NOM, \
            ]

    def GenererPortraits(self, age, masculin, metObj, portraits, valeursTraits):
        """
        ajoute des portraits correspondants aux caracs en paramtre (et à la coterie courante)
        valeursTraits : dico contenant en clé le nom des traits possédés par le personnage et en valeur leur niveau
        """
        constitutionVal = 0
        tailleVal = 0

        if trait.Constitution.NOM in valeursTraits:
            constitutionVal = valeursTraits[trait.Constitution.NOM]

        if trait.Taille.NOM in valeursTraits:
            tailleVal = valeursTraits[trait.Taille.NOM]

        if masculin:
            if constitutionVal < 1 and tailleVal < 1:
                # gretchins mâles
                if age >= 15:
                    if metObj is not None and metObj.nom_ == metier.Musicien.NOM:
                        portraits.append("images/coteries/orks/portraits/portrait_gobelin_musicien_15+.jpg")
                    if age >= 25:
                        portraits.append("images/coteries/orks/portraits/portrait_gobelin_25+.jpg")
            else:
                # orks mâles
                if age >= 15:
                    portraits.append("images/coteries/orks/portraits/portrait_15+.jpg")
                    if age >= 20:
                        if age >= 30:
                            portraits.append("images/coteries/orks/portraits/portrait_30+.jpg")
                            if age >= 40:
                                portraits.append("images/coteries/orks/portraits/portrait_40+.jpg")
                            # >= 30
                            if age < 50:
                                portraits.append("images/coteries/orks/portraits/portrait30-50.jpg")
                        # >= 20
                        if age < 50:
                            portraits.append("images/coteries/orks/portraits/portrait20-50.jpg")
                            portraits.append("images/coteries/orks/portraits/portrait20-50_b.jpg")
                            portraits.append("images/coteries/orks/portraits/portrait20-50_c.jpg")
                    if age <= 40:
                        portraits.append("images/coteries/orks/portraits/portrait15-40.jpg")

        else:
            # femelles
            pass

        return portraits

    def GetGentile(self, masculin):
        return "Ork"

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
            return random.choice(Orks.PRENOMS_M)
        else:
            return random.choice(Orks.PRENOMS_F)

    PRENOMS_M = [
    u"Ghazat", u"Abghat", u"Adgulg", u"Aghed", u"Agugh", u"Aguk", u"Almthu", u"Alog", u"Ambilge", u"Apaugh", u"Argha", u"Argigoth", u"Argug",
    u"Arpigig", u"Auhgan", u"Azhug", u"Bagdud", u"Baghig", u"Bahgigoth", u"Bandagh", u"Barfu", u"Bargulg", u"Baugh", u"Bidgug", u"Bildud", u"Bilge", u"Bog", u"Boghat", u"Bogugh", u"Borgan",
    u"Borug", u"Braugh", u"Brougha", u"Brugagh", u"Bruigig", u"Buadagh", u"Buggug", u"Builge", u"Buimghig", u"Bulgan", u"Bumhug", u"Buomaugh",
    u"Buordud", u"Burghed", u"Buugug", u"Cabugbu", u"Cagan", u"Carguk", u"Carthurg", u"Clog", u"Corgak", u"Crothu", u"Cubub", u"Cukgilug",
    u"Curbag", u"Dabub", u"Dakgorim", u"Dakgu", u"Dalthu", u"Darfu", u"Deakgu", u"Dergu", u"Derthag", u"Digdug", u"Diggu", u"Dilug", u"Ditgurat",
    u"Dorgarag", u"Dregu", u"Dretkag", u"Drigka", u"Drikdarok", u"Drutha", u"Dudagog", u"Dugarod", u"Dugorim", u"Duiltag", u"Durbag", u"Eagungad", u"Eggha", u"Eggugat", u"Egharod", u"Eghuglat",
    u"Eichelberbog", u"Ekganit", u"Epkagut", u"Ergoth", u"Ertguth", u"Ewkbanok", u"Fagdud", u"Faghig", u"Fandagh", u"Farfu", u"Farghed", u"Fargigoth", u"Farod", u"Faugh", u"Feldgulg", u"Fidgug",
    u"Filge", u"Fodagog", u"Fogugh", u"Fozhug", u"Frikug", u"Frug", u"Frukag", u"Fubdagog", u"Fudhagh", u"Fupgugh", u"Furbog", u"Futgarek", u"Gaakt", u"Garekk", u"Gelub", u"Gholug", u"Gilaktug",
    u"Ginug", u"Gnabadug", u"Gnadug", u"Gnalurg", u"Gnarg", u"Gnarlug", u"Gnorl", u"Gnorth", u"Gnoth", u"Gnurl", u"Golag", u"Golub", u"Gomatug", u"Gomoku", u"Gorgu", u"Gorlag", u"Grikug", u"Grug",
    u"Grukag", u"Grukk", u"Grung", u"Gruul", u"Guag", u"Gubdagog", u"Gudhagh", u"Gug", u"Gujarek", u"Gujek", u"Gujjab", u"Gulm", u"Gulrn", u"Gunaakt", u"Gunag", u"Gunug", u"Gurukk", u"Guthakug", u"Guthug",
    u"Gutjja", u"Hagob", u"Hagu", u"Hagub", u"Haguk", u"Hebub", u"Hegug", u"Hibub", u"Hig", u"Hogug", u"Hoknath", u"Hoknuk", u"Hokulk", u"Holkurg", u"Horknuth", u"Hrolkug", u"Hugagug", u"Hugmug", u"Hugolm",
    u"Ig", u"Igmut", u"Ignatz", u"Ignorg", u"Igubat", u"Igug", u"Igurg", u"Ikgnath", u"Ikkath", u"Inkathu", u"Inkathurg", u"Isagubat", u"Jogug", u"Jokgagu", u"Jolagh", u"Jorgagu", u"Jregh", u"Jreghug",
    u"Jugag", u"Jughog", u"Jughragh", u"Jukha", u"Jukkhag", u"Julakgh", u"Kabugbu", u"Kagan", u"Kaghed", u"Kahigig", u"Karfu", u"Karguk", u"Karrghed", u"Karrhig", u"Karthurg", u"Kebub", u"Kegigoth",
    u"Kegth", u"Kerghug", u"Kertug", u"Kilug", u"Klapdud", u"Klog", u"Klughig", u"Knagh", u"Knaraugh", u"Knodagh", u"Knorgh", u"Knuguk", u"Knurigig", u"Kodagog", u"Kog", u"Kogan", u"Komarod",
    u"Korgak", u"Korgulg", u"Koughat", u"Kraugug", u"Krilge", u"Krothu", u"Krouthu", u"Krugbu", u"Krugorim", u"Kubub", u"Kugbu", u"Kukgilug", u"Kulgha", u"Kupgugh", u"Kurbag", u"Kurmbag", u"Laghed",
    u"Lamgugh", u"Mabub", u"Magdud", u"Malthu", u"Marfu", u"Margulg", u"Mazhug", u"Meakgu", u"Mergigoth", u"Milug", u"Mudagog", u"Mugarod", u"Mughragh", u"Mugorim", u"Murbag", u"Naghat", u"Naghig",
    u"Naguk", u"Nahgigoth", u"Nakgu", u"Narfu", u"Nargulg", u"Narhbub", u"Narod", u"Neghed", u"Nehrakgu", u"Nildud", u"Nodagog", u"Nofhug", u"Nogugh", u"Nomgulg", u"Noogugh", u"Nugbu", u"Nughilug",
    u"Nulgha", u"Numhug", u"Nurbag", u"Nurghed", u"Oagungad", u"Oakgu", u"Obghat", u"Oggha", u"Oggugat", u"Ogharod", u"Oghuglat", u"Oguk", u"Ohomdud", u"Ohulhug", u"Oilug", u"Okganit", u"Olaghig",
    u"Olaugh", u"Olmthu", u"Olodagh", u"Olog", u"Omaghed", u"Ombilge", u"Omegugh", u"Omogulg", u"Omugug", u"Onog", u"Onubub", u"Onugug", u"Oodagh", u"Oogorim", u"Oogugbu", u"Oomigig", u"Opathu",
    u"Opaugh", u"Opeghat", u"Opilge", u"Opkagut", u"Opoguk", u"Oquagan", u"Orgha", u"Orgoth", u"Orgug", u"Orpigig", u"Ortguth", u"Otugbu", u"Ougha", u"Ougigoth", u"Ouhgan", u"Owkbanok", u"Paghorim",
    u"Pahgigoth", u"Pahgorim", u"Pakgu", u"Parfu", u"Pargu", u"Parhbub", u"Parod", u"Peghed", u"Pehrakgu", u"Pergu", u"Perthag", u"Pigdug", u"Piggu", u"Pitgurat", u"Podagog", u"Pofhug", u"Pomgulg",
    u"Poogugh", u"Porgarag", u"Pregu", u"Pretkag", u"Prigka", u"Prikdarok", u"Prutha", u"Pughilug", u"Puiltag", u"Purbag", u"Qog", u"Quadagh", u"Quilge", u"Quimghig", u"Quomaugh", u"Quordud", u"Quugug",
    u"Raghat", u"Raguk", u"Rakgu", u"Rarfu", u"Rebub", u"Rilug", u"Rodagog", u"Rogan", u"Romarod", u"Routhu", u"Rugbu", u"Rugorim", u"Rurbag", u"Rurigig", u"Sabub", u"Saghig", u"Sahgigoth", u"Sahgorim",
    u"Sakgu", u"Salthu", u"Saraugug", u"Sarfu", u"Sargulg", u"Sarhbub", u"Sarod", u"Sbghat", u"Seakgu", u"Sguk", u"Shomdud", u"Shulhug", u"Sildud", u"Silge", u"Silug", u"Sinsbog", u"Slaghig", u"Slapdud",
    u"Slaugh", u"Slodagh", u"Slog", u"Slughig", u"Smaghed", u"Smegugh", u"Smogulg", u"Snog", u"Snubub", u"Snugug", u"Sodagh", u"Sog", u"Sogorim", u"Sogugbu", u"Sogugh", u"Sombilge", u"Somigig", u"Sonagh",
    u"Sorgulg", u"Sornaraugh", u"Soughat", u"Spathu", u"Speghat", u"Spilge", u"Spoguk", u"Squagan", u"Stugbu", u"Sudagog", u"Sugarod", u"Sugbu", u"Sugha", u"Sugigoth", u"Sugorim", u"Suhgan", u"Sulgha",
    u"Sulmthu", u"Sumhug", u"Sunodagh", u"Sunuguk", u"Supaugh", u"Supgugh", u"Surbag", u"Surgha", u"Surghed", u"Surgug", u"Surpigig", u"Tagdud", u"Taghig", u"Tandagh", u"Tarfu", u"Targhed", u"Targigoth",
    u"Tarod", u"Taugh", u"Teldgulg", u"Tidgug", u"Tilge", u"Todagog", u"Tog", u"Toghat", u"Togugh", u"Torgan", u"Torug", u"Tozhug", u"Traugh", u"Trilug", u"Trougha", u"Trugagh", u"Truigig", u"Tuggug",
    u"Tulgan", u"Turbag", u"Turge", u"Ug", u"Ugghra", u"Uggug", u"Ughat", u"Ulgan", u"Ulmragha", u"Ulmrougha", u"Umhra", u"Umragig", u"Umruigig", u"Ungagh", u"Unrugagh", u"Urag", u"Uraugh", u"Urg",
    u"Urgan", u"Urghat", u"Urgran", u"Urlgan", u"Urmug", u"Urug", u"Urulg", u"Vabugbu", u"Vagan", u"Vagrungad", u"Vagungad", u"Vakgar", u"Vakgu", u"Vakmu", u"Valthurg", u"Vambag", u"Vamugbu", u"Varbu",
    u"Varbuk", u"Varfu", u"Vargan", u"Varguk", u"Varkgorim", u"Varthurg", u"Vegum", u"Vergu", u"Verlgu", u"Verthag", u"Verthurg", u"Vetorkag", u"Vidarok", u"Vigdolg", u"Vigdug", u"Viggu", u"Viggulm",
    u"Viguka", u"Vitgurat", u"Vitgut", u"Vlog", u"Vlorg", u"Vorgak", u"Vorgarag", u"Vothug", u"Vregu", u"Vretkag", u"Vrigka", u"Vrikdarok", u"Vrogak", u"Vrograg", u"Vrothu", u"Vruhag", u"Vrutha",
    u"Vubub", u"Vugub", u"Vuiltag", u"Vukgilug", u"Vultog", u"Vulug", u"Vurbag", u"Wakgut", u"Wanug", u"Wapkagut", u"Waruk", u"Wauktug", u"Wegub", u"Welub", u"Wholug", u"Wilaktug", u"Wingloug",
    u"Winug", u"Woabadug", u"Woggha", u"Woggugat", u"Wogharod", u"Woghuglat", u"Woglug", u"Wokganit", u"Womkug", u"Womrikug", u"Wonabadug", u"Worthag", u"Wraog", u"Wrug", u"Wrukag", u"Wrukaog",
    u"Wubdagog", u"Wudgh", u"Wudhagh", u"Wudugog", u"Wuglat", u"Wumanok", u"Wumkbanok", u"Wurgoth", u"Wurmha", u"Wurtguth", u"Wurthu", u"Wutgarek", u"Xaakt", u"Xago", u"Xagok", u"Xagu", u"Xaguk",
    u"Xarlug", u"Xarpug", u"Xegug", u"Xepug", u"Xig", u"Xnath", u"Xnaurl", u"Xnurl", u"Xoknath", u"Xokuk", u"Xolag", u"Xolkug", u"Xomath", u"Xomkug", u"Xomoku", u"Xonoth", u"Xorag", u"Xorakk",
    u"Xoroku", u"Xoruk", u"Xothkug", u"Xruul", u"Xuag", u"Xug", u"Xugaa", u"Xugag", u"Xugagug", u"Xugar", u"Xugarf", u"Xugha", u"Xugor", u"Xugug", u"Xujarek", u"Xuk", u"Xulgag", u"Xunaakt", u"Xunag",
    u"Xunug", u"Xurek", u"Xurl", u"Xurug", u"Xurukk", u"Xutag", u"Xuthakug", u"Xutjja", u"Yaghed", u"Yagnar", u"Yagnatz", u"Yahg", u"Yahigig", u"Yakgnath", u"Yakha", u"Yalakgh", u"Yargug", u"Yegigoth",
    u"Yegoth", u"Yerghug", u"Yerug", u"Ymafubag", u"Yokgagu", u"Yokgu", u"Yolmar", u"Yonkathu", u"Yregh", u"Yroh", u"Ysagubar", u"Yughragh", u"Yugug", u"Yukgnath", u"Yukha", u"Yulakgh", u"Yunkathu",
    u"Zabghat", u"Zabub", u"Zaghig", u"Zahgigoth", u"Zahgorim", u"Zalthu", u"Zaraugug", u"Zarfu", u"Zargulg", u"Zarhbub", u"Zarod", u"Zeakgu", u"Zguk", u"Zildud", u"Zilge", u"Zilug", u"Zinsbog",
    u"Zlapdud", u"Zlog", u"Zlughig", u"Zodagh", u"Zog", u"Zogugbu", u"Zogugh", u"Zombilge", u"Zonagh", u"Zorfu", u"Zorgulg", u"Zorhgigoth", u"Zornaraugh", u"Zoughat", u"Zudagog", u"Zugarod",
    u"Zugbu", u"Zugorim", u"Zuhgan", u"Zulgha", u"Zulmthu", u"Zumhug", u"Zunodagh", u"Zunuguk", u"Zupaugh", u"Zupgugh", u"Zurbag", u"Zurgha", u"Zurghed", u"Zurgug", u"Zurpigig", u"Atulg",
    u"Azuk", u"Bagamul", u"Bakh", u"Baronk", u"Bashag", u"Bazgulub", u"Bogakh", u"Borug", u"Both", u"Bugdul", u"Bugharz", u"Bugrash", u"Bugrol", u"Bumbub", u"Burul", u"Dul", u"Dular", u"Duluk",
    u"Duma", u"Dumbuk", u"Dumburz", u"Dur", u"Durbul", u"Durgash", u"Durz", u"Durzol", u"Durzub", u"Durzum", u"Garothmuk", u"Garzonk", u"Gashna", u"Ghamborz", u"Ghamonk", u"Ghoragdush",
    u"Ghorlorz", u"Glush", u"Grat", u"Guarg", u"Gurak", u"Khadba", u"Khagra", u"Khargol", u"Koffutto", u"Largakh", u"Lorbumol", u"Lorzub", u"Lugdum", u"Lugrub", u"Lurog", u"Mash", u"Matuk",
    u"Mauhul", u"Mazorn", u"Mol", u"Morbash", u"Mug", u"Mugdul", u"Muk", u"Murag", u"Murkub", u"Murzol", u"Muzgonk", u"Nag", u"Nar", u"Nash", u"Ogrul", u"Ogrumbu", u"Olfin", u"Olumba", u"Orakh",
    u"Rogdul", u"Shakh", u"Shamar", u"Shamob", u"Shargam", u"Sharkub", u"Shat", u"Shulong", u"Shura", u"Shurkul", u"Shuzug", u"Snaglak", u"Snakha", u"Snat", u"Ugdumph", u"Ughash", u"Ulam",
    u"Umug", u"Uram", u"Urim", u"Urul", u"Urzog", u"Ushamph", u"Yadba", u"Yagak", u"Yak", u"Yam", u"Yambagorn", u"Yambul", u"Yargol", u"Yashnarz", u"Yatur", u"Agronak", u"Bat", u"Bazur",
    u"Brugo", u"Bogrum", u"Brag", u"Brokil", u"Bugak", u"Buramog", u"Burz", u"Dubok", u"Dul", u"Dulfish", u"Dumag", u"Dulphumph", u"Gaturn", u"Gogron", u"Gorgo", u"Graklak", u"Graman",
    u"Grommok", u"Gul", u"Hanz", u"Krognak", u"Kurdan", u"Kurz", u"Rugdumph", u"Lum", u"Lumdum", u"Luronk", u"Magra", u"Magub", u"Maknok", u"Mug", u"Orok", u"Shagol", u"Shagrol", u"Shobob",
    u"Shum", u"Ulmug", u"Urbul", u"Urul", u"Ushnar", u"Uzul", u"Arob", u"Balogog", u"Borkul", u"Burguk", u"Dushnamub", u"Gat", u"Ghamorz", u"Ghorbash", u"Gradba", u"Grogmar", u"Grushnag",
    u"Gularzob", u"Kharag", u"Larek", u"Lob", u"Lurbuk", u"Mahk", u"Makhel", u"Abbas", u"Mauhulakh", u"Moth", u"Mul", u"Mulush", u"Nagrub", u"Oglub", u"Ogol", u"Olur", u"Ulag", u"Umurn",
    u"Urag", u"Yamarz", u"Yar" ]

    PRENOMS_F = [
    u"Agrob", u"Badbog", u"Bashuk", u"Bogdub", u"Bugdurash", u"Bula", u"Bulak", u"Bulfim", u"Bum", u"Burzob", u"Burub", u"Dura", u"Durgat", u"Durz", u"Gashnakh", u"Ghob", u"Glasha",
    u"Glob", u"Gluronk", u"Gonk", u"Grat", u"Grazob", u"Gulfim", u"Kharzug", u"Lagakh", u"Lambug", u"Lazgar", u"Mogak", u"Morn", u"Murob", u"Murzush", u"Nargol", u"Rolfish", u"Orbul",
    u"Ragash", u"Rulfim", u"Shadbak", u"Shagar", u"Shagdub", u"Sharn", u"Sharog", u"Shazgob", u"Shelur", u"Uloth", u"Ulumpha", u"Urzoth", u"Urzul", u"Ushat", u"Ushug", u"Yazgash",
    u"Batul", u"Borba", u"Bumph", u"Homraz", u"Rogbut", u"Mazoga", u"Mog", u"Mor", u"Oghash", u"Rogmesh", u"Snak", u"Ugak", u"Umog", u"Arob", u"Atub", u"Bagrak", u"Bolar", u"Bor",
    u"Borgakh", u"Dulug", u"Garakh", u"Ghak", u"Gharol", u"Ghorza", u"Gul", u"Lash", u"Murbol", u"Sharamph", u"Shel", u"Shufharz", u"Ugor", u"Urog", u"Yotul"
    ]
