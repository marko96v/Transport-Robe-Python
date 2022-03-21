from funkcije import clear,citanje_iz_fajla
from klase import  avioni,aerodrom,hangar,prostorZaTeret,roba,zahtevZaSmestanjeAvionaUHangar,zahtevZaTransportRobe
from klase import korisnik,potrazitelj
def ucitatiOsobe(file_name):
    osoba = korisnik.str2korisnik(file_name)
    print("-----------------------------------------------------------------------------------")
    print("ID KOD:",osoba.idKod)
    print("IME:",osoba.ime)
    print("PREZIME:",osoba.prezime)
    print("KORISNICKO IME:",osoba.korisnickoIme)
    print("SIFRA ",osoba.sifra)
    print("ULOGA:",osoba.uloga)
    print("-----------------------------------------------------------------------------------")
    print("\n\n")


def ucitatiPotrazitelja(file_name):
    potrazitelj1=potrazitelj.str2potrazitelj(file_name)
    print("--------------------------------------------------------------------------------------------")
    print("ID KOD:",potrazitelj1.idKod)
    print("IME:",potrazitelj1.ime)
    print("PREZIME:",potrazitelj1.prezime)
    print("BROJ TELEFONA:",potrazitelj1.broj_telefona)
    print("E-MAIL",potrazitelj1.email)
    print("--------------------------------------------------------------------------------------------")
    print("\n\n")


def ucitatiOstalo(file_name):
            if file_name == "aerodrom.txt":
                ostalo=aerodrom.str2aerodrom(file_name)
                print("--------------------------------------------------------")
                print("NAZIV:",ostalo.naziv)
                print("ADRESA:",ostalo.adresa)
                print("MESTO:",ostalo.mesto)
                print("--------------------------------------------------------")
            elif file_name == "avioni.txt":
                avion=avioni.str2avion(file_name)
                print("-----------------------------------------------------------------------------------------------------")
                print("OZNAKA:",avion.oznaka)
                print("NAZIV:",avion.naziv)
                print("GODISTE:",avion.godiste)
                print("DUZINA:",avion.duzina)
                print("RASPON KRILA:",avion.rasponKrila)
                print("VISINA:",avion.visina)
                print("UKUPNA NOSIVOST:",avion.ukupnaNosivost)
                print("RELACIJA:",avion.relacija)
                print("-----------------------------------------------------------------------------------------------------")
            elif file_name == "hangar.txt":
                ostalo=hangar.str2hangar(file_name)
                print("-----------------------------------------------------------------------------------------------------")
                print("OZNAKA:", ostalo.oznaka)
                print("NAZIV:", ostalo.naziv)
                print("DUZINA:", ostalo.duzina)
                print("SIRINA:", ostalo.sirina)
                print("VISINA:", ostalo.visina)
                print("-----------------------------------------------------------------------------------------------------")
            elif file_name == "prostorZaTeret.txt":
                ostalo = prostorZaTeret.str2prostor(file_name)
                print("-----------------------------------------------------------------------------------------------------")
                print("OZNAKA:", ostalo.oznaka)
                print("NAZIV:", ostalo.naziv)
                print("DUZINA:", ostalo.duzina)
                print("SIRINA:", ostalo.sirina)
                print("VISINA:", ostalo.visina)
                print("-----------------------------------------------------------------------------------------------------")
            elif file_name == "roba.txt":
                ostalo=roba.str2roba(file_name)
                print("-----------------------------------------------------------------------------------------------------")
                print("OZNAKA:", ostalo.oznaka)
                print("NAZIV:", ostalo.naziv)
                print("OPIS:",ostalo.opis)
                print("DUZINA:", ostalo.duzina)
                print("SIRINA:", ostalo.sirina)
                print("VISINA:", ostalo.visina)
                print("TEZINA:",ostalo.tezina)
                print("STATUS:",ostalo.status)
                print("-----------------------------------------------------------------------------------------------------")
def ucitatiZahteve(file_name):
    if file_name == "zahtevZaSmestanjeAvionaUHangar.txt":
        zahtev = zahtevZaSmestanjeAvionaUHangar.str2zahtevHangar(file_name)
        print("-----------------------------------------------------------------------------------------------------")
        print("ID KOD:", zahtev.idKod)
        print("DATUM KREIRANJA:", zahtev.datumKreiranja)
        print("VREME SMESTANJA:", zahtev.vremeSmestanja)
        print("VREME NAPUSTANJA:", zahtev.vremeNapustanja)
        print("OZNAKA HANGARA:", zahtev.oznakaHangara)
        print("OZNAKA AVIONA:", zahtev.oznakaAviona)
        print("ID MENADZERA:", zahtev.idMenadzera)
        print("-----------------------------------------------------------------------------------------------------")
    elif file_name =="zahtevZaTransportRobe.txt":
        zahtev=zahtevZaTransportRobe.str2zahtevTransport(file_name)
        print("-----------------------------------------------------------------------------------------------------")
        print("ID KOD:", zahtev.idKod)
        print("DATUM KREIRANJA:", zahtev.datumKreiranja)
        print("DATUM TRANSPORTA:", zahtev.datumTransporta)
        print("ODREDISTE:", zahtev.odrediste)
        print("ID POTRAZITELJA:", zahtev.idPotrazitelja)
        print("OZNAKA AVIONA:", zahtev.oznakaAviona)
        print("STATUS:", zahtev.status)
        print("-----------------------------------------------------------------------------------------------------")
def citanjepodataka():
    print("1.Osobe\n2.Aerodrom\n3.Zahtevi\n0.Izlaz")
    komanda1 = input("Unesite komandu:")
    if komanda1 == "1":
        clear()
        print("1.Menadzer Hangara\n2.Menadzer Transporta\n3.Potrazitelj\n4.Radnici\n5.Nazad")
        k1 = input("Unesite komandu:")
        if k1 == "1":
            ucitatiOsobe("menadzerHangara.txt")
            citanjepodataka()
        elif k1 == "2":
            ucitatiOsobe("menadzerTransporta.txt")
            citanjepodataka()
        elif k1 == "3":
            ucitatiPotrazitelja("potrazitelji.txt")
            citanjepodataka()
        elif k1 == "4":
            ucitatiOsobe("radnici.txt")
            citanjepodataka()
        elif k1 == "5":
            citanjepodataka()

    elif komanda1 == "2":
        clear()
        print("1.Aerodrom\n2.Hangar\n3.Avioni\n4.Prostor za teret\n5.Roba\n6.Nazad")
        k1 = input("Unesiti komandu:")
        if k1 == "1":
            ucitatiOstalo("aerodrom.txt")
            citanjepodataka()
        elif k1 == "2":
            ucitatiOstalo("hangar.txt")
            citanjepodataka()
        elif k1 == "3":
            ucitatiOstalo("avioni.txt")
            citanjepodataka()
        elif k1 == "4":
            ucitatiOstalo("prostorZaTeret.txt")
            citanjepodataka()
        elif k1 == "5":
            ucitatiOstalo("roba.txt")
            citanjepodataka()
        elif k1 == "6":
            citanjepodataka()

    elif komanda1 == "3":
        clear()
        print("1.Zahtev za smestaj aviona\n2.Zahtev za transport robe\n3.Nazad")
        k1 = input("Unesite komandu:")
        if k1 == "1":
            ucitatiZahteve("zahtevZaSmestanjeAvionaUHangar.txt")
            citanjepodataka()
        elif k1 == "2":
            ucitatiZahteve("zahtevZaTransportRobe.txt")
            citanjepodataka()
        elif k1 == "3":
            citanjepodataka()
    elif komanda1 == "0":
        exit()
