
def vypis_parametry_krabice(parametry):
    # Získání hodnot výšky, šíøky a hloubky ze slovníku
    vyska = parametry.get('vyska', 0)
    sirka = parametry.get('sirka', 0)
    hloubka = parametry.get('hloubka', 0)

    # Výpoèet objemu krabice
    objem = vyska * sirka * hloubka

    # Výpis všech parametrù a objemu
    print("Parametry krabice:")
    print(f"Výška: {vyska} cm")
    print(f"Šíøka: {sirka} cm")
    print(f"Hloubka: {hloubka} cm")
    print(f"Objem krabice: {objem} cm^3")

# Pøíklad použití
parametry_krabice = {'vyska': 10, 'sirka': 5, 'hloubka': 8}
vypis_parametry_krabice(parametry_krabice)
