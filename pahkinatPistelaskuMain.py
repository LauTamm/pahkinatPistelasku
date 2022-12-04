from pahkinatPistelaskuLuokat import Reitti
from pahkinatPistelaskuLuokat import Kiipeilija
from pahkinatPistelaskuLuokat import Tulos

while True:
    print("Tervehdys! Toivottavasti 12 pähkinää -kisat ovat sujuneet mukavasti. :)")
    print("Aloita tuloskirjaus kirjoittamalla nimesi:")
    kiipeilijanNimi = input()
    print("Kerro seuraavaksi sarjasi (naiset, miehet, junnut):")
    kiipeilijanSarja = input()
    uusiKiipeilija = Kiipeilija(kiipeilijanNimi,kiipeilijanSarja)
    print("Hei",uusiKiipeilija.nimi,"! Valitse a syöttääksesi flashina kiivetyn reitin numeron ja valitse b syöttääksesi useammalla yrityksellä kiivetyn reitin. Kun olet kokonaan valmis, kirjoita e.")
    valinta="a"
    kiipeilijanTulokset = Tulos(uusiKiipeilija)

    while valinta != "e":
        valinta = input()
        if (valinta == "a"):
            flashReittiNumero=int(input("Anna flashatyn reitin numero:"))
            uusiFlash = Reitti(flashReittiNumero, True) 
            kiipeilijanTulokset.reitit.append(uusiFlash) 
            print("Flashina kiivetyt reitit:")
            kiipeilijanTulokset.tulostaFlashReitit() 
        elif (valinta == "b"):
            reittiNumero=int(input("Anna useammalla yrityksellä kiivetyn reitin numero:"))
            uusiNormi = Reitti(reittiNumero, False) 
            kiipeilijanTulokset.reitit.append(uusiNormi)
            print("Useammalla yrityksellä kiivetyt reitit:")
            kiipeilijanTulokset.tulostaNormiReitit() 

    print("Kaikki flashina kiivetyt reittisi:")
    kiipeilijanTulokset.tulostaFlashReitit() 
    print("kaikki useammalla yrityksellä kiivetyt reittisi:")
    kiipeilijanTulokset.tulostaNormiReitit() 

    print("------------------------------------------------------------------------------------------------------")

    print("Flash-reittien kokonaispistemäärä:", kiipeilijanTulokset.laskeFlashPisteet()) 
    print("Muiden reittien kokonaispistemäärä:",kiipeilijanTulokset.laskeNormiPisteet())
    print("Kokonaispisteet yhteensä:",kiipeilijanTulokset.laskeKokonaisPisteet())

       
    print("------------------------------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------------------------------------")
        
