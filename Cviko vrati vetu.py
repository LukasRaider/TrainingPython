#Vytvor vetu nejaka veta kontrol retezce ze neni prazdny pocet znaku a mavic prvni slovo retezce bude velkymi pismeny , 
#nahdate vsechny vyskyty pismen x pismem R a vysledek interpolovanym stringem

def zpracuj_retezec(retezec):
    # Kontrola, zda je �et�zec pr�zdn�
    if not retezec:
        return "Zadany retezec je prazdny."

    # Z�sk�n� po�tu znak� v �et�zci
    pocet_znaku = len(retezec)

    # Nahrazen� p�smena 'x' p�smenem 'R'
    upraveny_retezec = retezec.replace('x', 'R')

    # Z�sk�n� prvn�ho slova s velk�m po��te�n�m p�smenem
    prvni_slovo = retezec.split()[0].capitalize()

    # Vytvo�en� interpolovan�ho �et�zce
    vysledek = f"Pocet znaku: {pocet_znaku}, Prvni slovo: {prvni_slovo}, Nahrazeny retezec: {upraveny_retezec}"

    return vysledek

# Testov�n� programu
zadany_retezec = input("Zadejte retezec: ")
vysledek_programu = zpracuj_retezec(zadany_retezec)
print(vysledek_programu)

    
