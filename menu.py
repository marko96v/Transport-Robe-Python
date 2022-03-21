from citanjePodataka import citanjepodataka
from dodavanjeAviona import dodavanje_aviona
from dodavanjeHangara import dodavanje_hangara
from funkcije import  clear
from kreiranjeZahtevaSmestaj import kreiranje_zahteva_za_smestaj_aviona_u_hangar
from pretraga import  pretraga
from funkcije import utovari_robu
from citanje_podataka_mh import citanje_podataka_mhf
from citanjePodataka import citanjepodataka
from provera import provera_svega


def meni_mh():
	print("1.Citaj zahteve za smestanje aviona u hangar\n2.Citaj zahteve za transport robe\n3.Citaj ostalo\n4.Dodajte novi hangar\n5.Dodajte novi avion\n6.Kreiraj zahtev za smestanje aviona u hangar\n7.Pretraga\n8.Azuriraj sve\n0.Izlaz")
	komanda = input("Unesite komandu:")
	if komanda == "1":
		clear()
		citanje_podataka_mhf("zahtevZaSmestanjeAvionaUHangar.txt")
	elif komanda == "2":
		clear()
		citanje_podataka_mhf("zahtevZaTransportRobe.txt")
	elif komanda == "3":
		clear()
		citanjepodataka()
	elif komanda == "4":
		clear()
		dodavanje_hangara()
	elif komanda == "5":
		clear()
		dodavanje_aviona()
	elif komanda == "6":
		clear()
		kreiranje_zahteva_za_smestaj_aviona_u_hangar()
	elif komanda == "7":
		clear()
		pretraga()
	elif komanda=="8":
		provera_svega()
	elif komanda == "0":
		exit()
	else:
		print("Uneli ste pogresnu komandu,pokusajte ponovo.")
		meni_mh()
def meni_mt():
		print("\n1. Citanje podataka\n2. Pretraga\n3. Pregled zahteva za transport robe\n4. Zahtev za smestanje aviona u hangar\n5. Odobravanje zahteva za transport robe\n0. Izlaz")
		komanda = input("Unesite komandu:")
		if komanda == "1":
			clear()
			citanjepodataka()
		elif komanda == "2":
			clear()
			pretraga()
			komanda = input("Izaberite jednu od ponudjenih opcija")

		elif komanda == "3":
			clear()
			pregled_svih_zahteva_menadzer()

		elif komanda == "4":
			clear()
			pregled_svih_zahteva_za_smestaj_aviona_u_hangar_menadzer()
		elif komanda == "5":
			clear()
			idZateva, lokacijaZahteva, listaIdentifikatoraRobe = iniciraj_transport()
			odobrenje_zahteva_za_transport(idZateva, lokacijaZahteva, listaIdentifikatoraRobe)
		elif komanda=="0":
			clear()
			exit()
		else:
			print("Greska, niste uneli jednu od ponudjenih opcija")
			meni_mt()


def meni_r():
	print("\n1.Citanje podataka\n2.Pretraga\n3.Utovari robu\n0.Izlaz")
	komanda = input("Unesite komandu:")

	if komanda == "1":
		clear()
		citanjepodataka()
	elif komanda == "2":
		clear()
		pretraga()
	elif komanda == "3":
		utovari_robu()
	elif komanda == "0":
		clear()
		exit()

        
def potrazitelj():
		clear()
		print("Odaberite jednu od ponudjenih opcija:")
		print("\n1. Potrazivanje transporta za robu")
		print("2. Kreiranje zahteva za transport robe")
		print("3. Pregled svih odobrenih zahteva")
		print("0. Izlaz")

		komanda = input("Izaberite jednu od ponudnjenih opcija:")

		if komanda == "1":
			ime = potrazivanje_identifikacija_korisnika()
			potrazivanje_transporta(ime)
		elif komanda == "2":
			kreiranje_zahteva_za_transport()
		elif komanda == "3":
			pregled_svih_zahteva()
		elif komanda == "0":
			exit()
		else:
			print("Greska, niste uneli jednu od ponudjenih opcija.")
			potrazitelj()
