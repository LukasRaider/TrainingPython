

def spocitej_pismena_a_cisla(retezec):
    pocet_pismen = 0
    pocet_cislic = 0

    # Projdi ka�d� znak ve zadan�m �et�zci
    for znak in retezec:
        if znak.isalpha():  # Kontrola, zda je znak p�smeno
            pocet_pismen += 1
        elif znak.isdigit():  # Kontrola, zda je znak ��slice
            pocet_cislic += 1

    return pocet_pismen, pocet_cislic

# P��klad pou�it�
vstupni_retezec = input("Zadejte �et�zec: ")
pismena, cisla = spocitej_pismena_a_cisla(vstupni_retezec)

print(f"Pocet pismen: {pismena}")
print(f"Pocet cislic: {cisla}")
