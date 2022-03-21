import os
import platform
from klase import aerodrom,avioni,hangar,korisnik,prostorZaTeret,roba,zahtevZaTransportRobe,zahtevZaSmestanjeAvionaUHangar
from klase.roba import Roba
# funkcija koja cita fajlove
from klase.zahtevZaTransportRobe import ZahtevZaTransport


def citanje_iz_fajla(file_name):
	otvori_fajl = open(file_name, "r")  # otvori fajl u rezimu za citanje
	linije = otvori_fajl.readlines()  # citaj linije fajla)
	otvori_fajl.close()  # zatvori fajl]
	return "|".join(linije)

#print(citanje_iz_fajla("hangar.txt"))

def clear():
		windows = "Windows"
		linux = "Linux"

		#U zavisnosti od OS-a na kome se pokrece, komanda za ciscenje moze biti 'clear' ili 'cls'
		if platform.system() == linux:
			os.system("clear")
		elif platform.system() == windows:
			os.system("cls")

def provera_hangara(oznaka_hangara,oznaka_aviona):
	avion1=avioni.str2avion("avioni.txt")
	hangar1=hangar.str2hangar("hangar.txt")
	if int(hangar1.duzina)>int(avion1.duzina)and int(hangar1.sirina)>int(avion1.rasponKrila) and int(hangar1.visina) >int(avion1.visina):
		return True
	else:
		return False

def utovari_robu():
	from menu import meni_r

	robaa=roba.str2roba("roba.txt")
	prostor=prostorZaTeret.str2prostor("prostorZaTeret.txt")
	zahtev=zahtevZaTransportRobe.str2zahtevTransport("zahtevZaTransportRobe.txt")
	roba_oznaka_unos=input("Unesi oznaku robe: ")
	prostor_oznaka_unos=zahtev.oznakaAviona
	if roba_oznaka_unos == zahtev.ozakaRobe and prostor_oznaka_unos==prostor.oznaka and robaa.status != "roba utovarena":
		print("Provera...")
		if prostor.duzina >robaa.duzina and prostor.sirina>robaa.sirina and prostor.duzina >robaa.duzina:
			status="roba utovarena"
			oznaka=robaa.oznaka
			naziv=robaa.naziv
			opis=robaa.opis
			duzina=robaa.duzina
			sirina=robaa.sirina
			visina=robaa.visina
			tezina=robaa.tezina
			roba1=Roba(oznaka,naziv,opis,duzina,sirina,visina,tezina,status)
			string=oznaka+"|"+naziv+"|"+opis+"|"+duzina+"|"+sirina+"|"+visina+"|"+tezina+"|"+status
			otvori_fajl = open("roba.txt", "w")
			otvori_fajl.write(string)
			idKod=zahtev.idKod
			datumKreiranja=zahtev.datumKreiranja
			datumTransporta=zahtev.datumTransporta
			oznakaRobe=zahtev.ozakaRobe
			oznakaAviona =zahtev.oznakaAviona
			odrediste=zahtev.odrediste
			idPotrazitelja=zahtev.idPotrazitelja
			zatev1=ZahtevZaTransport(idKod,datumKreiranja,datumTransporta,odrediste,idPotrazitelja,oznakaRobe,oznakaAviona,status)
			stringz=idKod+"|"+datumKreiranja+"|"+datumTransporta+"|"+odrediste+"|"+idPotrazitelja+"|"+oznakaRobe+"|"+oznakaAviona+"|"+status
			otvori_fajl1=open("zahtevZaTransportRobe.txt", "w")
			otvori_fajl1.write(stringz)
			print("Roba je uspesno utovarena")
			meni_r()
		else:
			print("Roba ne moze da stane u izabrani prostor za teret")
			meni_r()


	else:
		print("Oznaka aviona,robe ne postoii ili je roba vec utovarena.")
		meni_r()
