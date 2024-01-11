
def zakaznik_s_nejvetsi_utratou(zakaznici):
    # Kontrola, zda slovn�k nen� pr�zdn�
    if not zakaznici:
        return None

    # Nalezen� z�kazn�ka s nejv�t�� utratou
    nejvetsi_utrata_zakaznika = max(zakaznici.values())
    zakaznik_s_nejvetsi_utratou = next((k for k, v in zakaznici.items() if v == nejvetsi_utrata_zakaznika), None)

    return zakaznik_s_nejvetsi_utratou

# P��klad pou�it�
zakaznici = {
    'Zakaznik1': 150,
    'Zakaznik2': 200,
    'Zakaznik3': 120,
    'Zakaznik4': 250
}

nejvetsi_utrata_zakaznika = zakaznik_s_nejvetsi_utratou(zakaznici)

if nejvetsi_utrata_zakaznika is not None:
    print(f"Z�kazn�k s nejv�t�� utratou je {nejvetsi_utrata_zakaznika} s utratou {zakaznici[nejvetsi_utrata_zakaznika]} K�.")
else:
    print("Slovn�k z�kazn�k� je pr�zdn�.")
