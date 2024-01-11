
def abecedni_seznam_studentu(studenti):
    # Se�azen� student� podle p��jmen� a k�estn�ho jm�na
    serazeni_studenti = sorted(studenti, key=lambda x: (studenti[x]['prijmeni'], studenti[x]['krestni_jmeno']))

    # Vytvo�en� seznamu ve form� listu
    seznam_ve_forme_listu = [(k, studenti[k]) for k in serazeni_studenti]

    return seznam_ve_forme_listu

# P��klad pou�it�
studenti = {
    'student1': {'krestni_jmeno': 'Jan', 'prijmeni': 'Novak', 'prumer': 3.5},
    'student2': {'krestni_jmeno': 'Eva', 'prijmeni': 'Svobodova', 'prumer': 4.0},
    'student3': {'krestni_jmeno': 'Pavel', 'prijmeni': 'Novotny', 'prumer': 3.8}
}

seznam_studentu = abecedni_seznam_studentu(studenti)
print(seznam_studentu)
