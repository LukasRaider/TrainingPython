#Seznamy zakazniku a seradit je za sebe
# Dva seznamy zákazníkù
seznam_zakazniku1 = ["Anna", "David", "Michael", "Sophie"]
seznam_zakazniku2 = ["John", "Emma", "Robert", "Olivia"]

# Spojení seznamù
celkovy_seznam_zakazniku = seznam_zakazniku1 + seznam_zakazniku2

# Seøazení seznamu podle abecedy
serazeny_seznam = sorted(celkovy_seznam_zakazniku)

# Výpis výsledkù
print("Seznam zákazníkù (seøazený podle abecedy):")
for zakaznik in serazeny_seznam:
    print(zakaznik)

