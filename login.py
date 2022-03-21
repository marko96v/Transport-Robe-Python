from funkcije import citanje_iz_fajla,clear
from klase import korisnik
from menu import meni_mh,meni_r,meni_mt,potrazitelj
from provera import provera_svega
# funkcija za prijavu na sistem
def prijava_na_sistem():
    clear()
    print("\nUnesite ulogu u sistemu: ")
    print("1. Potrazitelj\n2. Zaposlen\n0. Izlaz")
    komanda = input("Unesite komandu:")
    if komanda == "1":
         clear()
         potrazitelj()
    elif komanda == "2":
        clear()
        prijava_zaposleni()
    elif komanda == "0":
        exit()
    else:
        print("Greska, molimo Vas izaberite jednu od ponudjenih odgovora.")
        prijava_na_sistem()

def prijava_zaposleni():
    clear()
    korisnickoime = input("Unesite korisnicko ime: ").strip()# korisnik unosi korisnicko ime
    sifra = input("Unesite sifru: ").strip() #korisnik unosi sifru
    menadzerHangara=korisnik.str2korisnik("menadzerHangara.txt")
    menadzerTransporta=korisnik.str2korisnik("menadzerTransporta.txt")
    radnik=korisnik.str2korisnik("radnici.txt")
    if korisnickoime == menadzerHangara.korisnickoIme and sifra == menadzerHangara.sifra:
        print("Uspesno ste se ulogovali kao menadzer hangara.")
        meni_mh()
    elif korisnickoime == menadzerTransporta.korisnickoIme and sifra == menadzerTransporta.sifra:
        print("Uspesno ste se ulogovali kao menadzer transporta.")
        meni_mt()
    elif korisnickoime == radnik.korisnickoIme and sifra == radnik.sifra:
        print("Uspesno ste se ulogovali kao radnik.")
        meni_r()
    else:
        print("Niste se ulogovali,pokusajte ponovo")
        prijava_na_sistem()