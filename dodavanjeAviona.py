def dodavanje_aviona():
    from funkcije import citanje_iz_fajla
    from klase import avioni
    from klase.avioni import Avion
    from menu import meni_mh
    from klase import prostorZaTeret
    from klase.prostorZaTeret import ProstorZaTeret
    prostor1=prostorZaTeret.str2prostor("prostorZaTeret.txt")
    avion1=avioni.str2avion("avioni.txt")
    oznaka = input("Unesite oznaku aviona:")
    naziv = input("Unesite naziv aviona:")
    try:
        godiste = int(input("Unesite godiste aviona:"))
        duzina = int(input("Unesite duzinu aviona:"))
        raspon_krila = int(input("Unesite raspon krila:"))
        visina = int(input("Unesite visinu aviona:"))
        ukupna_nosivost = int(input("Unesi ukupnu nosivost(kg)"))
    except ValueError:
        print("Morate uneti broj")
        dodavanje_aviona()
    relacija=input("Unesi relaciju na kojoj avion leti(separator ""-""):")
    if "-" not in relacija:
        print("Niste dobro uneli relaciju.Pokusajte ponovo")
        dodavanje_aviona()
    elif oznaka != "" and naziv != "" and oznaka!= avion1.oznaka:
        avion2=Avion(oznaka,naziv,str(godiste),str(duzina),str(raspon_krila),str(visina),str(ukupna_nosivost),relacija)
        string=Avion.avion2str(avion2)
        otvori_fajl = open("avioni.txt", "a")
        otvori_fajl.write(string)
        print("Avion uspesno dodat.")
        naziv_prostora=input("Unesi naziv prostora za teret: ")
        duzinap=input("Unesite duzinu prostora za teret: ")
        sirina=input("Unesite sirinu prostora za teret: ")
        visinap=input("Unesite visinu prostora za teret: ")
        if naziv_prostora !="" and duzinap!="" and sirina !="" and visinap!="":
            prostor2=ProstorZaTeret(oznaka,naziv_prostora,duzinap,sirina,visinap)
            stringp=ProstorZaTeret.prostor2str(prostor2)
            otvori_fajlp=open("prostorZaTeret.txt", "a")
            otvori_fajlp.write(stringp)
            print("Prostor za teret uspesno dodat")
            meni_mh()
        else:
            print("Prostor za teret nije uspesno dodat.")
            meni_mh()

    else:
        print("Avion nije dodat,pokusajte ponovo.")
        meni_mh()

