class ZahtevZaTransport(object):
    def __init__(self, idKod, datumKreiranja, datumTransporta, odrediste, idPotrazitelja,oznakaRobe, oznakaAviona, status):
        self.idKod=idKod
        self.datumKreiranja = datumKreiranja
        self.datumTransporta=datumTransporta
        self.odrediste = odrediste
        self.idPotrazitelja = idPotrazitelja
        self.ozakaRobe=oznakaRobe
        self.oznakaAviona = oznakaAviona
        self.status = status


    def zahtevTransport2str(self):
        return '|'.join(["\n"+self.idKod,self.datumKreiranja,self.datumTransporta,self.odrediste,self.idPotrazitelja,self.ozakaRobe,self.oznakaAviona,self.status])

def str2zahtevTransport(fajl):
    zahtevit = []
    with open(fajl, "r") as f:
        for line in f.readlines():
            atributi = line.split("|")
            z = ZahtevZaTransport(atributi[0], atributi[1],atributi[2],atributi[3], atributi[4],atributi[5],atributi[6],atributi[7])
            zahtevit.append(z)
            return z
