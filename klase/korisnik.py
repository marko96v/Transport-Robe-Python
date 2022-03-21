class Korisnik(object):
    def __init__(self, idKod, ime, prezime, korisnickoIme,sifra,uloga):
        self.idKod = idKod
        self.ime = ime
        self.prezime= prezime
        self.korisnickoIme = korisnickoIme
        self.sifra=sifra
        self.uloga=uloga

    def korisnik2str(self):
        return '|'.join(["\n"+self.idKod,self.ime,self.prezime,self.korisnickoIme,self.sifra,self.uloga])

def str2korisnik(fajl):
    korisnici = []
    with open(fajl, "r") as f:
        for line in f.readlines():
            atributi = line.split("|")
            k = Korisnik(atributi[0], atributi[1],atributi[2],atributi[3], atributi[4],atributi[5])
            korisnici.append(k)
            return k
