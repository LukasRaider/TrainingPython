#Vuygeneruj 20 cisle do pole max min prumer a vratit posledni prvek
import random

# Generov�n� pole 20 n�hodn�ch ��sel
pole_cisel = [random.randint(1, 100) for _ in range(20)]

# Vyhled�n� maximum a minimum
maximum = max(pole_cisel)
minimum = min(pole_cisel)

# V�po�et pr�m�ru
prumer = sum(pole_cisel) / len(pole_cisel)

# Z�sk�n� posledn�ho prvku
posledni_prvek = pole_cisel[-1]

# V�pis v�sledk�
print(f"Pole ��sel: {pole_cisel}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
print(f"Pr�m�r: {prumer}")
print(f"Posledn� prvek: {posledni_prvek}")
