#Seznamy zakazniku a seradit je za sebe
# Dva seznamy z�kazn�k�
seznam_zakazniku1 = ["Anna", "David", "Michael", "Sophie"]
seznam_zakazniku2 = ["John", "Emma", "Robert", "Olivia"]

# Spojen� seznam�
celkovy_seznam_zakazniku = seznam_zakazniku1 + seznam_zakazniku2

# Se�azen� seznamu podle abecedy
serazeny_seznam = sorted(celkovy_seznam_zakazniku)

# V�pis v�sledk�
print("Seznam z�kazn�k� (se�azen� podle abecedy):")
for zakaznik in serazeny_seznam:
    print(zakaznik)

