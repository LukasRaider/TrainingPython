

def spocitej_pismena_a_cisla(retezec):
    pocet_pismen = 0
    pocet_cislic = 0

    # Projdi každý znak ve zadaném øetìzci
    for znak in retezec:
        if znak.isalpha():  # Kontrola, zda je znak písmeno
            pocet_pismen += 1
        elif znak.isdigit():  # Kontrola, zda je znak èíslice
            pocet_cislic += 1

    return pocet_pismen, pocet_cislic

# Pøíklad použití
vstupni_retezec = input("Zadejte øetìzec: ")
pismena, cisla = spocitej_pismena_a_cisla(vstupni_retezec)

print(f"Pocet pismen: {pismena}")
print(f"Pocet cislic: {cisla}")
