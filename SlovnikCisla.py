
def je_v_rozsahu(cislo, rozsah):
    # Z�sk�n� hodnot minimum a maximum ze slovn�ku
    minimum = rozsah.get('minimum', float('-inf'))
    maximum = rozsah.get('maximum', float('inf'))

    # Kontrola, zda je ��slo v rozsahu
    return minimum <= cislo <= maximum

# P��klad pou�it�
cislo_kontroly = 15
rozsah_kontroly = {'minimum': 10, 'maximum': 20}

vysledek = je_v_rozsahu(cislo_kontroly, rozsah_kontroly)
print(vysledek)
