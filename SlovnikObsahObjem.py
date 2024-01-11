
def vypis_parametry_krabice(parametry):
    # Z�sk�n� hodnot v��ky, ���ky a hloubky ze slovn�ku
    vyska = parametry.get('vyska', 0)
    sirka = parametry.get('sirka', 0)
    hloubka = parametry.get('hloubka', 0)

    # V�po�et objemu krabice
    objem = vyska * sirka * hloubka

    # V�pis v�ech parametr� a objemu
    print("Parametry krabice:")
    print(f"V��ka: {vyska} cm")
    print(f"���ka: {sirka} cm")
    print(f"Hloubka: {hloubka} cm")
    print(f"Objem krabice: {objem} cm^3")

# P��klad pou�it�
parametry_krabice = {'vyska': 10, 'sirka': 5, 'hloubka': 8}
vypis_parametry_krabice(parametry_krabice)
