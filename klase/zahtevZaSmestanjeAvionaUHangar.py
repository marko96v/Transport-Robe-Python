class ZahtevSmestanjeAviona(object):
    def __init__(self, idKod, datumKreiranja, vremeSmestanja, vremeNapustanja, oznakaHangara, oznakaAviona, idMenadzera):
        self.idKod=idKod
        self.datumKreiranja = datumKreiranja
        self.vremeSmestanja = vremeSmestanja
        self.vremeNapustanja = vremeNapustanja
        self.oznakaHangara = oznakaHangara
        self.oznakaAviona = oznakaAviona
        self.idMenadzera = idMenadzera


    def zahtevHangar2str(self):
        return '|'.join(["\n"+self.idKod,self.datumKreiranja,self.vremeSmestanja,self.vremeNapustanja,self.oznakaHangara,self.oznakaAviona,self.idMenadzera])

def str2zahtevHangar(fajl):
    zahtevih = []
    with open(fajl, "r") as f:
        for line in f.readlines():
            atributi = line.split("|")
            z = ZahtevSmestanjeAviona(atributi[0], atributi[1],atributi[2],atributi[3], atributi[4],atributi[5],atributi[6])
            zahtevih.append(z)
            return z
