
def zakaznik_s_nejvetsi_utratou(zakaznici):
    # Kontrola, zda slovník není prázdný
    if not zakaznici:
        return None

    # Nalezení zákazníka s nejvìtší utratou
    nejvetsi_utrata_zakaznika = max(zakaznici.values())
    zakaznik_s_nejvetsi_utratou = next((k for k, v in zakaznici.items() if v == nejvetsi_utrata_zakaznika), None)

    return zakaznik_s_nejvetsi_utratou

# Pøíklad použití
zakaznici = {
    'Zakaznik1': 150,
    'Zakaznik2': 200,
    'Zakaznik3': 120,
    'Zakaznik4': 250
}

nejvetsi_utrata_zakaznika = zakaznik_s_nejvetsi_utratou(zakaznici)

if nejvetsi_utrata_zakaznika is not None:
    print(f"Zákazník s nejvìtší utratou je {nejvetsi_utrata_zakaznika} s utratou {zakaznici[nejvetsi_utrata_zakaznika]} Kè.")
else:
    print("Slovník zákazníkù je prázdný.")
