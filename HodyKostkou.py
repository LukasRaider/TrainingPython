# Vygeneruj nahodne 20x2 a secti pocet z kostek
import random

# Generov�n� dvakr�t 20 ��sel od 1 do 6
hody1 = [random.randint(1, 6) for _ in range(20)]
hody2 = [random.randint(1, 6) for _ in range(20)]

# Se��t�n� o�� z ka�d�ho hodu
soucet_hodu1 = sum(hody1)
soucet_hodu2 = sum(hody2)

# V�pis v�sledk�
print("Prvn� sada hod�:", hody1)
print("Sou�et o�� z prvn� sady hod�:", soucet_hodu1)
print("\nDruh� sada hod�:", hody2)
print("Sou�et o�� z druh� sady hod�:", soucet_hodu2)

