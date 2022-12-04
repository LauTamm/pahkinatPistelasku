class Reitti:
    numero:0
    onkoFlash = False
    flashKerroin = 1.1

    def __init__(self,n,f):
        self.numero = n
        self.onkoFlash = f
        self.flashKerroin = 1.1

    def tulostaReittiNumero(self):
        print("Reitti numero", self.numero)

    def laskePisteet(self):
        if(self.onkoFlash):
            return self.numero * self.flashKerroin
        else:
            return self.numero

class Kiipeilija:
    nimi = ""
    sarja = ""

    def __init__(self,n,s):
        self.nimi = n
        self.sarja = s

    def tulostaKiipeilija(self):
        print(self.nimi, self.sarja)

class Tulos:
    kiipeilija = Kiipeilija("","")
    reitit = []

    def __init__(self,kiipeilija):
        self.kiipeilija = kiipeilija
        self.reitit = []
    
    def tulostaFlashReitit(self):
        for reitti in self.reitit:
            if reitti.onkoFlash:
                print(reitti.numero)
    
    def tulostaNormiReitit(self):
        for reitti in self.reitit:
            if not reitti.onkoFlash:
                print(reitti.numero)

    def laskeFlashPisteet(self):
        pisteet = 0
        for reitti in self.reitit:
            if reitti.onkoFlash:
                pisteet += reitti.laskePisteet()
        return pisteet

    def laskeNormiPisteet(self):
        pisteet = 0
        for reitti in self.reitit:
            if not reitti.onkoFlash:
                pisteet += reitti.laskePisteet()
        return pisteet
    
    def laskeKokonaisPisteet(self):
        return self.laskeFlashPisteet() + self.laskeNormiPisteet()

    def tulostaKilpailija(self):
        print(self.kiipeilija.tulostaKiipeilija())
