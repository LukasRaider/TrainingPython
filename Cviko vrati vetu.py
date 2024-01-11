#Vytvor vetu nejaka veta kontrol retezce ze neni prazdny pocet znaku a mavic prvni slovo retezce bude velkymi pismeny , 
#nahdate vsechny vyskyty pismen x pismem R a vysledek interpolovanym stringem

def zpracuj_retezec(retezec):
    # Kontrola, zda je øetìzec prázdný
    if not retezec:
        return "Zadany retezec je prazdny."

    # Získání poètu znakù v øetìzci
    pocet_znaku = len(retezec)

    # Nahrazení písmena 'x' písmenem 'R'
    upraveny_retezec = retezec.replace('x', 'R')

    # Získání prvního slova s velkým poèáteèním písmenem
    prvni_slovo = retezec.split()[0].capitalize()

    # Vytvoøení interpolovaného øetìzce
    vysledek = f"Pocet znaku: {pocet_znaku}, Prvni slovo: {prvni_slovo}, Nahrazeny retezec: {upraveny_retezec}"

    return vysledek

# Testování programu
zadany_retezec = input("Zadejte retezec: ")
vysledek_programu = zpracuj_retezec(zadany_retezec)
print(vysledek_programu)

    
