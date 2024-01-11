#Vuygeneruj 20 cisle do pole max min prumer a vratit posledni prvek
import random

# Generování pole 20 náhodných èísel
pole_cisel = [random.randint(1, 100) for _ in range(20)]

# Vyhledání maximum a minimum
maximum = max(pole_cisel)
minimum = min(pole_cisel)

# Výpoèet prùmìru
prumer = sum(pole_cisel) / len(pole_cisel)

# Získání posledního prvku
posledni_prvek = pole_cisel[-1]

# Výpis výsledkù
print(f"Pole èísel: {pole_cisel}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
print(f"Prùmìr: {prumer}")
print(f"Poslední prvek: {posledni_prvek}")
