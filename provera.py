from klase import zahtevZaSmestanjeAvionaUHangar,zahtevZaTransportRobe,roba
from funkcije import citanje_iz_fajla
import datetime
from funkcije import clear
def provera_svega():
    from menu import meni_mh
    zahtev_smestanje=zahtevZaSmestanjeAvionaUHangar.str2zahtevHangar("zahtevZaSmestanjeAvionaUHangar.txt")
    zahtev_transport=zahtevZaTransportRobe.str2zahtevTransport("zahtevZaTransportRobe.txt")
    roba1=roba.str2roba("roba.txt")
    vreme=str(datetime.datetime.now())
    sat_trenutni=vreme[11:13]
    minuti_trenutni=vreme[14:16]
    sat_zahtev=zahtev_smestanje.vremeNapustanja[:2]
    minuti_zahtev=zahtev_smestanje.vremeNapustanja[3:5]
    if sat_trenutni >= sat_zahtev:
        brisi("zahtevZaSmestanjeAvionaUHangar.txt")
        status="roba transportovana"
        id=zahtev_transport.idKod
        datum_kreiranja=zahtev_transport.datumKreiranja
        datum_transporta=zahtev_transport.datumTransporta
        odrediste=zahtev_transport.odrediste
        id_potrazitelja=zahtev_transport.idPotrazitelja
        oznaka_robe=zahtev_transport.ozakaRobe
        oznaka_aviona=zahtev_transport.oznakaAviona
        string=id+"|"+datum_kreiranja+"|"+datum_transporta+'|'+odrediste+"|"+id_potrazitelja+"|"+oznaka_robe+"|"+oznaka_aviona+"|"+status
        open_file=open("zahtevZaTransportRobe.txt","w")
        open_file.write(string)
        open_file.close()
        oznaka=roba1.oznaka
        naziv=roba1.naziv
        opis=roba1.opis
        duzina=roba1.duzina
        sirina=roba1.sirina
        visina=roba1.visina
        tezina=roba1.tezina
        string1=oznaka+"|"+naziv+"|"+opis+'|'+duzina+"|"+sirina+"|"+visina+"|"+tezina+"|"+status
        open_file1=open("roba.txt","w")
        open_file1.write(string1)
        open_file1.close()
    elif sat_trenutni == sat_zahtev and minuti_trenutni>minuti_zahtev:
        brisi("roba.txt")
        brisi("zahtevZaSmestanjeAvionaUHangar.txt")
        status = "roba transportovana"
        id = zahtev_transport.idKod
        datum_kreiranja = zahtev_transport.datumKreiranja
        datum_transporta = zahtev_transport.datumTransporta
        odrediste = zahtev_transport.odrediste
        id_potrazitelja = zahtev_transport.idPotrazitelja
        oznaka_robe = zahtev_transport.ozakaRobe
        oznaka_aviona = zahtev_transport.oznakaAviona
        string = id + "|" + datum_kreiranja + "|" + datum_transporta + '|' + odrediste + "|" + id_potrazitelja + "|" + oznaka_robe + "|" + oznaka_aviona + "|" + status
        open_file = open("zahtevZaTransportRobe.txt", "w")
        open_file.write(string)
        open_file.close()
        oznaka = roba1.oznaka
        naziv = roba1.naziv
        opis = roba1.opis
        duzina = roba1.duzina
        sirina = roba1.sirina
        visina = roba1.visina
        string1 = oznaka + "|" + naziv + "|" + opis + '|' + duzina + "|" + sirina + "|" + visina + "|" + status
        open_file1 = open("roba.txt", "w")
        open_file1.write(string1)
        open_file1.close()

    else:
        pass
    clear()
    print("\n\nSve je azurirano\n\n")
    meni_mh()

def brisi(file_name):
    otvori_fajl = open(file_name, "w")
    otvori_fajl.write("")
    otvori_fajl.close()