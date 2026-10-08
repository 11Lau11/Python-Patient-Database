
gen_valid = {"Masculin", "Feminin", "M", "F", "masculin", "feminin", "m", "f"} # Un set creat pentru validarea genului pacientului

baza_pacienti = [] # Lista pacientilor inregistrati

inregistrare = True

while inregistrare: # Cat timp inregistrarea este activa se afiseaza meniul principal
    print("\n--- MENIU PACIENȚI ---")
    print("1. Introduceti datele (Înregistrare)")
    print("2. Autentificare (Verificare date)")
    print("3. Lista pacienți înregistrați")
    print("4. Iesire \n")
    
    optiune = input("Selecteaza o optiune (1-4): ")# permite selectarea unei optiuni din meniu
    
    if optiune == "1":# daca s-a ales optiunea 1 se face inregistrarea
        print("\n--- ÎNREGISTRARE PACIENT NOU ---")
        nume = input("Introduceti numele pacientului: ")
        
        
        if nume.strip() == "":# daca nu s-a introdus nimic sau daca se incearac a se pune spatiu gol se va afisa un mesaj de eroare
            print("Eroare: Numele nu poate fi gol!")
            continue

        
        anul_nasterii = int(input("Introduceti anul nasterii pacientului: "))# aici se introduce anul nasterii
        Varsta = 2026 - anul_nasterii# aici se face calculul pentru a determina varsta
        if anul_nasterii < 1900 or anul_nasterii > 2026:# se face o verificate pentru a se introduce un an valid
            print(f"Eroare: Anul nasterii {anul_nasterii} este invalid! Trebuie sa fie intre 1900 si 2026.")
            continue  

        gen_pacient = input("Introduceti genul pacientului (Masculin/Feminin): ")# aici se introduce genul pacientului
        
        
        if gen_pacient in gen_valid:# daca genul introdus este valid se va face inregistrarea pacientului
            
            pacient_nou = { # se creeaza un dictionar pentru a stoca informatiile pacientului
                "Nume": nume,
                "Anul nasterii": anul_nasterii,
                "Varsta": Varsta,
                "Gen": gen_pacient
            }
            
            
            baza_pacienti.append(pacient_nou) # dupa ce pacientul a fost inregistrat, se adauga in lista de pacienti
            print(f"Informatiile pacientului {nume} au fost inregistrate cu succes!")
        else:
            print(f"Eroare: Genul '{gen_pacient}' nu este valid.")

    elif optiune == "2":# daca s-a selectat optiunea 2 se poate face autentificarea
        print("\n--- AUTENTIFICARE / VERIFICARE ---")
        if not baza_pacienti:# daca nu exista nimic in baza de date atunci se va afisa un mesaj de eroare
            print("Nu exista niciun pacient inregistrat in baza de date!")
        else:
            nume = input("Introduceti numele pacientului: ")
            anul_nasterii = int(input("Introduceti anul nasterii: "))
            gen_pacient = input("Introduceti genul: ")
            
            gasit = False
            
            for p in baza_pacienti:# se parcurge lista de pacienti pentru a verifica daca informatiile introduse corespund cu un pacient inregistrat
                if p["Nume"] == nume and p["Anul nasterii"] == anul_nasterii and p["Gen"] == gen_pacient:
                    gasit = True
                    break
            
            if gasit:
                print(f"Succes: Informatiile pacientului {nume} sunt corecte si exista in sistem!")
            else:
                print("Informatiile introduse nu corespund cu niciun pacient inregistrat.")
        
    elif optiune == "3":# aici se poate afisa lista pacientilor inregistrati
        print("\n--- LISTA PACIENȚI ÎNREGISTRATI ---")
        if not baza_pacienti:
            print("Nu exista niciun pacient inregistrat in baza de date!")
        else:
            for i, p in enumerate(baza_pacienti, start=1):
                print(f"{i}. Nume: {p['Nume']}, Anul nasterii: {p['Anul nasterii']}, Varsta: {p['Varsta']}, Gen: {p['Gen']}")
    elif optiune == "4":# aici se face iesirea din program
        inregistrare = False
        print("Iesire din program. O zi buna!")
    else:
        print("Optiune invalida! Alege 1, 2, 3 sau 4.")