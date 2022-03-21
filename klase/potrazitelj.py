class Potrazitelj(object):
    def __init__(self, idKod, ime, prezime, broj_telefona,email):
        self.idKod = idKod
        self.ime = ime
        self.prezime= prezime
        self.broj_telefona = broj_telefona
        self.email=email
    def potrazitelj2str(self):
        return '|'.join(["\n"+self.idKod,self.ime,self.prezime,self.broj_telefona,self.email])

def str2potrazitelj(fajl):
    potrazitelji = []
    with open(fajl, "r") as f:
        for line in f.readlines():
            atributi = line.split("|")
            p = Potrazitelj(atributi[0], atributi[1],atributi[2],atributi[3], atributi[4])
            potrazitelji.append(p)
            return p
