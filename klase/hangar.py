class Hangar(object):
    def __init__(self, oznaka,naziv,duzina,sirina,visina):
        self.oznaka = oznaka
        self.naziv = naziv
        self.duzina = duzina
        self.sirina = sirina
        self.visina = visina


    def hangar2str(self):
        return '|'.join(["\n"+self.oznaka, self.naziv,self.duzina,self.sirina,self.visina])

def str2hangar(fajl):
    hangari = []
    with open(fajl, "r") as f:
        for line in f.readlines():
            atributi = line.split("|")
            h = Hangar(atributi[0], atributi[1],atributi[2],atributi[3], atributi[4])
            hangari.append(h)
            return h
