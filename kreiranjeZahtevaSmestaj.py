import time
import uuid
from funkcije import  provera_hangara
def kreiranje_zahteva_za_smestaj_aviona_u_hangar():
    from menu import meni_mh
    from funkcije import citanje_iz_fajla
    from klase import avioni,hangar,korisnik,zahtevZaSmestanjeAvionaUHangar
    from klase.zahtevZaSmestanjeAvionaUHangar import ZahtevSmestanjeAviona
    avion1=avioni.str2avion("avioni.txt")
    hangar1=hangar.str2hangar("hangar.txt")
    korisnik1=korisnik.str2korisnik("menadzerHangara.txt")
    id_kod = str(uuid.uuid1())
    id_kod_6 = id_kod[:6]
    datum = time.strftime("%d/%m/%y")
    sat_smestanja = input("Unesi sat kada je avion smesten u hangar: ")
    minut_smestanja = input("Unesi minut kada je avion smesten u hangar: ")
    vreme_smestanja = sat_smestanja + ":" + minut_smestanja
    sat_napustanja = input("Unesi sat kada je avion napustio hangar: ")
    minut_napustanja = input("Unesi minut kada je avion napustio hangar: ")
    vreme_napustanja = sat_napustanja + ":" + minut_napustanja
    oznaka_hangara = input("Unesi oznaku hangara u koji se smesta avion:")
    oznaka_aviona = input("Unesi oznaku aviona koji se smesta u hangar:")
    id_kod_menadzera = input("Unesite id kod menadzera:")
    if sat_smestanja != "" and minut_smestanja != "" and sat_napustanja != "" and minut_napustanja != "" and id_kod_menadzera == korisnik1.idKod and oznaka_hangara == hangar1.oznaka and oznaka_aviona == avion1.oznaka and oznaka_aviona not in citanje_iz_fajla("zahtevZaSmestanjeAvionaUHangar.txt"):
        print("Provera...")
        if provera_hangara(oznaka_hangara,oznaka_aviona) == True:
            zahtev=ZahtevSmestanjeAviona(id_kod_6,datum,vreme_smestanja,vreme_napustanja,oznaka_hangara,oznaka_aviona,id_kod_menadzera)
            string=ZahtevSmestanjeAviona.zahtevHangar2str(zahtev)
            otvori_fajl = open("zahtevZaSmestanjeAvionaUHangar.txt", "a")
            otvori_fajl.write(string)
            print("Zahtev uspesno napravljen.")
            meni_mh()
        else:
            print("Uneli ste nepostojece informacije ili avion ne moze da stane u hangar")
            meni_mh()

    else:
        print("Niste dobro uneli podatke.Pokusajte ponovo")
        meni_mh()
