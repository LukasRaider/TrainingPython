
import random
cisla = []
for i in range(0,5):
    cisla.append(random.random())
print{cisla}
   
cisla1 = []
for i in range(0,5):
    cisla1.append(random.uniform(3.75,8.06))
print{cisla1}
   
zaci = ['Ivan', 'Karel' , 'Radek']
zaci.extend(["Michal" , "Jaroslav", "Hynek"])
print{random.choice(zaci)}


zaci = ['Ivan', 'Karel' , 'Radek', 'Michal' , 'Jaroslav', 'Hynek']
print{random.choice(zaci, weights=[2,1,10,2,3], k = 10)}
