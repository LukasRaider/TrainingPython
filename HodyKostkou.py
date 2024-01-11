# Vygeneruj nahodne 20x2 a secti pocet z kostek
import random

# Generování dvakrát 20 èísel od 1 do 6
hody1 = [random.randint(1, 6) for _ in range(20)]
hody2 = [random.randint(1, 6) for _ in range(20)]

# Seèítání oèí z každého hodu
soucet_hodu1 = sum(hody1)
soucet_hodu2 = sum(hody2)

# Výpis výsledkù
print("První sada hodù:", hody1)
print("Souèet oèí z první sady hodù:", soucet_hodu1)
print("\nDruhá sada hodù:", hody2)
print("Souèet oèí z druhé sady hodù:", soucet_hodu2)

