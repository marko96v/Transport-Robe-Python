class Avion(object):
    def __init__(self, oznaka,naziv,godiste,duzina,rasponKrila,visina,ukupnaNosivost,relacija):
        self.oznaka = oznaka
        self.naziv = naziv
        self.godiste = godiste
        self.duzina = duzina
        self.rasponKrila = rasponKrila
        self.visina = visina
        self.ukupnaNosivost = ukupnaNosivost
        self.relacija = relacija
    def avion2str(self):
        return '|'.join(["\n"+self.oznaka, self.naziv,self.godiste,self.duzina,self.rasponKrila,self.visina,self.ukupnaNosivost,self.relacija])

def str2avion(fajl):
    avioni = []
    with open(fajl, "r") as f:
        for line in f.readlines():
            atributi = line.split("|")
            a = Avion(atributi[0], atributi[1],atributi[2],atributi[3], atributi[4],atributi[5],atributi[6],atributi[7])
            avioni.append(a)
            return a
