
def je_v_rozsahu(cislo, rozsah):
    # Získání hodnot minimum a maximum ze slovníku
    minimum = rozsah.get('minimum', float('-inf'))
    maximum = rozsah.get('maximum', float('inf'))

    # Kontrola, zda je èíslo v rozsahu
    return minimum <= cislo <= maximum

# Pøíklad použití
cislo_kontroly = 15
rozsah_kontroly = {'minimum': 10, 'maximum': 20}

vysledek = je_v_rozsahu(cislo_kontroly, rozsah_kontroly)
print(vysledek)
