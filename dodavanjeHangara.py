def dodavanje_hangara():
    from funkcije import citanje_iz_fajla
    from menu import meni_mh
    from klase import hangar
    from klase.hangar import Hangar
    hangar1=hangar.str2hangar("hangar.txt")
    oznaka = input("Unesite oznaku hangara:")
    naziv = input("Unesite naziv hangara:")
    try:
        duzina = int(input("Unesite duzinu hangara:"))
        sirina = int(input("Unesite sirinu hangara:"))
        visina = int(input("Unesite visinu hangara:"))
    except ValueError:
        print("Morate uneti broj")
        dodavanje_hangara()
    if oznaka != "" and naziv != "" and oznaka != hangar1.oznaka:
        hangar2=Hangar(oznaka,naziv,str(duzina),str(sirina),str(visina))
        string=Hangar.hangar2str(hangar2)
        otvori_fajl = open("hangar.txt", "a")
        otvori_fajl.write(string)
        print("Hangar uspesno dodat.")
        meni_mh()
    else:
        print("Hangar nije dodat,pokusajte ponovo.")
        meni_mh()