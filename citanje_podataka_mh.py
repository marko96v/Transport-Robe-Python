def citanje_podataka_mhf(file_name):
    from klase import zahtevZaSmestanjeAvionaUHangar, zahtevZaTransportRobe
    from menu import meni_mh
    if file_name == "zahtevZaSmestanjeAvionaUHangar.txt":
        zahtev = zahtevZaSmestanjeAvionaUHangar.str2zahtevHangar(file_name)
        print("-----------------------------------------------------------------------------------------------------")
        print("ID KOD:", zahtev.idKod)
        print("DATUM KREIRANJA:", zahtev.datumKreiranja)
        print("VREME SMESTANJA:", zahtev.vremeSmestanja)
        print("VREME NAPUSTANJA:", zahtev.vremeNapustanja)
        print("OZNAKA HANGARA:", zahtev.oznakaHangara)
        print("OZNAKA AVIONA:", zahtev.oznakaAviona)
        print("ID MENADZERA:", zahtev.idMenadzera)
        print("-----------------------------------------------------------------------------------------------------")
        meni_mh()
    elif file_name =="zahtevZaTransportRobe.txt":
        zahtev=zahtevZaTransportRobe.str2zahtevTransport(file_name)
        if zahtev.status == "roba utovarena":
            print("-----------------------------------------------------------------------------------------------------")
            print("ID KOD:", zahtev.idKod)
            print("DATUM KREIRANJA:", zahtev.datumKreiranja)
            print("DATUM TRANSPORTA:", zahtev.datumTransporta)
            print("ODREDISTE:", zahtev.odrediste)
            print("ID POTRAZITELJA:", zahtev.idPotrazitelja)
            print("OZNAKA AVIONA:", zahtev.oznakaAviona)
            print("STATUS:", zahtev.status)
            print("-----------------------------------------------------------------------------------------------------")
            meni_mh()
        else:
            meni_mh()




