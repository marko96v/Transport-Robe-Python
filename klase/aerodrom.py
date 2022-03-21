class Aerodrom(object):
    def __init__(self, naziv, adresa, mesto):
        self.naziv = naziv
        self.adresa = adresa
        self.mesto = mesto

    def aerodrom2str(self):
        return '|'.join(["\n"+self.naziv, self.adresa, self.mesto])


def str2aerodrom(fajl):
    aerodromi = []
    with open(fajl, "r") as f:
        for line in f.readlines():
            atributi = line.split("|")
            aer = Aerodrom(atributi[0], atributi[1],atributi[2])
            aerodromi.append(aer)
            return aer
