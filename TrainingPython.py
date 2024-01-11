#zakladni prace a syntaxe v jazyce pythonu
cislo = 3
print(cislo)

zaci = ['Ivan' , 'Karel' , 'Radek']

print(zaci)

print('raz' , 'dva' , 'tri')

#dale budu psat s promenymi zde vidim jak ukazuje typ promene

a = 3 
print(type(a))

b = 3.0
print(type(b))

c = '3'
print(type(c))

#dale prace s operatory a porovnavani

list1 = []
list2 = []
list3=list1

if(list1 == list2):
    print('True')
else:
    print('False')
    
if(list1 is list2):
    print('True')
else:
    print('False')
    
if(list1 is list3):
    print('True')
else:
    print('False')
    



#vstupni promena a prace s nimi

cislo = int(input("Zadej cislo : "))
if(cislo %3 ==0 and cislo % 4 ==0):
    print("cislo je delitelne 3 i 4")
else:
    print("cislo neni delitelne 3 i 4")

guestList = ['Adam' , 'Bara' , 'Dan']
for guest in guestList:
    print(guest)
    
guestList = ['Adam' , 'Bara' , 'Dan']
print(guestList)
print(guestList[0])
print(guestList[1])
print(guestList[2])

cisla = [10, 15, 30, 45]
for num in cisla:
    print(num+3)
    
#druha moznost

for num in [20, 25 , 35, 45]:
    print(num+3)

stop= int(input("Zadejte konec: "))
for i in range(stop):
    print(i)
    
#Cyklus for se zacatkem 

start= int(input("Zadejte start: "))
stop= int(input("Zadejte konec: "))
for i in range(start, stop):
    print(i)
    
i = 3
while i<6:
    print(i)
    i+=1

#retezec
    
print('Odnekud je konec, ten prijde')
print('a' + 'b' + 'c')

print('a'*3)

den = "pondeli"
pocasi = "jasno"
print(f'Dnes je {den} a venku je {pocasi}')

den = "patek"
teplota = -15
print(f'Dnes je {den.upper()} a teplota je {teplota+2} C')

# ciselne datove typy

b = 3
b+= True
print(b)

a = True
b = False
print(a or b)

a = True
b = False
print(a and b)

