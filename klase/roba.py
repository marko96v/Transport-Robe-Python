class Roba(object):
    def __init__(self, oznaka, naziv, opis, duzina, sirina, visina, tezina,status):
        self.oznaka = oznaka
        self.naziv = naziv
        self.opis = opis
        self.duzina = duzina
        self.sirina = sirina
        self.visina = visina
        self.tezina = tezina
        self.status=status
    def roba2str(self):
        return '|'.join(["\n"+self.oznaka,self.naziv,self.opis,self.duzina,self.sirina,self.visina,self.tezina,self.status])

def str2roba(fajl):
    robe = []
    with open(fajl, "r") as f:
        for line in f.readlines():
            atributi = line.split("|")
            r = Roba(atributi[0], atributi[1],atributi[2],atributi[3], atributi[4],atributi[5],atributi[6],atributi[7])
            robe.append(r)
            return r
