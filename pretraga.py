from funkcije import clear,citanje_iz_fajla
from klase import  hangar,avioni,roba

def pretraga():
		clear()
		print("\n1.Pretrazi hangare\n2.Pretrazi avione\n3.Pretrazi robu\n0.Izlaz")
		komanda = input("Unesite komandu:")
		if komanda == "1":
			clear()
			pretraga_hangara()
		elif komanda == "2":
			clear()
			pretraga_aviona()
		elif komanda == "3":
			clear()
			pretraga_robe()
		elif komanda == "0":
			exit()
		else:
			print("Uneli ste nepostojecu komandu,pokusajte ponovo")
			pretraga()

def pretraga_hangara():
	hangar1=hangar.str2hangar("hangar.txt")
	print("Pretrazi hangare po:\n1.Oznaci\n2.Nazivu\n3.Sirini\n4.Duzini\n5.Visini\n0.Nazad")
	komanda1 = input("Unesite komandu:")
	if komanda1 == "1":
		clear()
		oznaka = input("Unesite oznaku hangara:")
		if oznaka != hangar1.oznaka:
			pretraga_hangara()

	elif komanda1 == "2":
		clear()
		naziv = input("Unesite naziv hangara:")
		if naziv != hangar1.naziv:
			pretraga_hangara()
	elif komanda1 == "3":
		clear()
		sirina = input("Unesite sirinu hangara:")
		if sirina != hangar1.sirina:
			pretraga_hangara()
	elif komanda1 == "4":
		clear()
		duzina = input("Unesite duzinu hangara:")
		if duzina != hangar1.duzina:
			pretraga_hangara()
	elif komanda1 == "5":
		clear()
		visina = input("Unesite visinu hangara:")
		if visina != hangar1.visina:
			pretraga_hangara()
	elif komanda1 == "0":
		pretraga()
	else:
		print("Uneli ste nepostojecu komandu.Pokusajte ponovo")
		pretraga_hangara()
	print("-----------------------------------------------------------------------------------------------------")
	print("OZNAKA:", hangar1.oznaka)
	print("NAZIV:", hangar1.naziv)
	print("DUZINA:", hangar1.duzina)
	print("SIRINA:", hangar1.sirina)
	print("VISINA:", hangar1.visina)
	print("-----------------------------------------------------------------------------------------------------")
	pretraga_hangara()




def pretraga_aviona():
	avion=avioni.str2avion("avioni.txt")
	print("Pretrazi avione po:\n1.Oznaci\n2.Duzini\n3.Visini\n4.Rasponu krila\n5.Nosivosti\n6.Relaciji\n0.Nazad")
	komanda = input("Unesite komandu:")
	if komanda == "1":
		clear()
		oznaka = input("Unesite oznaku aviona:")
		if oznaka != avion.oznaka:
			pretraga_aviona()
	elif komanda == "2":
		clear()
		duzina = input("Unesite duzinu aviona:")
		if duzina != avion.duzina:
			pretraga_aviona()
	elif komanda == "3":
		clear()
		visina = input("Unesite visinu aviona:")
		if visina!=avion.visina:
			pretraga_aviona()
	elif komanda == "4":
		clear()
		raspon_krila = input("Unesite raspon krila:")
		if raspon_krila!=avion.rasponKrila:
			pretraga_aviona()
	elif komanda == "5":
		clear()
		nosivost = input("Unesite nosivost aviona:")
		if nosivost!=avion.ukupnaNosivost:
			pretraga_aviona()
	elif komanda == "6":
		clear()
		relacija = input("Unesite relaciju:")
		if relacija !=avion.relacija:
			pretraga_aviona()
	elif komanda == "0":
		pretraga()
	else:
		print("Uneli ste pogresnu komandu,pokusajte ponovo.")
		pretraga_aviona()
	print("-----------------------------------------------------------------------------------------------------")
	print("OZNAKA:", avion.oznaka)
	print("NAZIV:", avion.naziv)
	print("GODISTE:", avion.godiste)
	print("DUZINA:", avion.duzina)
	print("RASPON KRILA:", avion.rasponKrila)
	print("VISINA:", avion.visina)
	print("UKUPNA NOSIVOST:", avion.ukupnaNosivost)
	print("RELACIJA:", avion.relacija)
	print("-----------------------------------------------------------------------------------------------------")
	pretraga_aviona()
def pretraga_robe():
	roba1=roba.str2roba("roba.txt")
	print("Pretrazi robu po:\n1.Oznaci\n2.Naziv\n3.Opisu\n4.Sirini\n5.Duzini\n6.Visini\n7.Tezini robe\n8.Identifikacionom kodu potrazitelja\n0.Nazad")
	komanda = input("Unesite komandu:")
	if komanda == "1":
		clear()
		oznaka = input("Unesite oznaku robe:")
		if oznaka != roba1.oznaka:
			pretraga_robe()

	elif komanda == "2":
		clear()
		naziv = input("Unesite naziv robe:")
		if naziv !=roba1.naziv:
			pretraga_robe()

	elif komanda == "3":
		clear()
		opis = input("Unesite opis robe:")
		if opis != roba1.opis:
			pretraga_robe()

	elif komanda == "4":
		clear()
		sirina = input("Unesite sirinu robe:")
		if sirina != roba1.sirina:
			pretraga_robe()
	elif komanda =="5":
		clear()
		duzina=input("Unesite duzinu:")
		if duzina !=roba1.duzina:
			pretraga_robe()
	elif komanda == "6":
		clear()
		visina=input("Unesite visinu:")
		if visina != roba1.visina:
			pretraga_robe()
	elif komanda == "7":
		clear()
		tezina = input("Unesite tezinu robe:")
		if tezina != roba1.tezina:
			pretraga_robe()

	elif komanda == "8":
		clear()
		idpotrazitelja=input("Unesite id potrazitelja: ")
		print("nije dovrseno")
	elif komanda == "0":
		pretraga()
	else:
		print("Uneli ste pogresnu komandu,pokusajte ponovo.")
		pretraga_robe()

	print("-----------------------------------------------------------------------------------------------------")
	print("OZNAKA:", roba1.oznaka)
	print("NAZIV:", roba1.naziv)
	print("OPIS:", roba1.opis)
	print("DUZINA:", roba1.duzina)
	print("SIRINA:", roba1.sirina)
	print("VISINA:", roba1.visina)
	print("TEZINA:", roba1.tezina)
	print("STATUS:",roba1.status)
	print("-----------------------------------------------------------------------------------------------------")
	pretraga_robe()