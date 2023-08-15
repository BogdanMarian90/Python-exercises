# DEF EXERCITII FUNCTII
# 1.Funcție care să calculeze și să returneze suma a două numere
# Varianta 1
'''
def sum(x, y):
    return x + y


resultat = sum(14, 32)
print(resultat)
'''
'''
# Varianta 2
def sum2(a, b):
    suma = a + b
    return suma


rezultat2 = sum(12, 4)
print(rezultat2)
'''
print("-" * 30)

'''
# 2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar
# Varianta 1
def numar(x):
    if x % 2 == 0:
        return "True"
    else:
        return "False"


resultat = numar(2)
resultat2 = numar(1)
print(resultat)
print(resultat2)
'''
print("-" * 30)
'''
# Varianta 2
def numar_par(y):
    if y % 2 == 0:
        return True
    else:
        return False

rezultat3 = numar_par(3)
print(rezultat3) 
'''

# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)
# Varianta1
'''
def nr_caractere(nume, prenume, nume_mijlociu):
    return len(nume), len(prenume), len(nume_mijlociu)


print(nr_caractere("Bogdan", "Marian", "Ion"))

print("-" * 30)
'''
'''
# Varianta 2
def calcul_caractere(nume, prenume, nume_mijlociu):
    nume_complet = nume + prenume + nume_mijlociu
    numar_caractere = len(nume_complet)
    return numar_caractere

rezultat = calcul_caractere("Bogdan", "Marian", "Gyo")
print(rezultat)
'''

# 4. Funcție care returnează aria dreptunghiului
# Varianta 1
'''
def aria_derptunghi(l, L):
    return L * l


aria = aria_derptunghi(19, 34)
print(aria)
'''
print("-" * 30)

'''
# Varianta 2
def arai_drept(l, L):
    arie = l * L
    return arie


rezultat = arai_drept(20, 34)
print(rezultat)
'''

# 5. Funcție care returnează aria cercului

'''
# V2
import math
def arie_c(raza):
    aria = math.pi * raza ** 2
    return aria

rezultat = arie_c(10)
print(rezultat)
'''

# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.
'''
def caracter(str):
    if "a" in str:
        return True
    else:
        return False


print(caracter("dipari"))

print("-" * 30)
'''

'''
# V2
def gaseste_caracter(x, string):
    if x in string:
        return True
    else:
        return False


rezultat = gaseste_caracter("b", "abc")
print(rezultat)
'''

# 7. Funcție fără return, primește un string și printează pe ecran:
# Numărul de caractere lower case este x
# Numărul de caractere upper case exte y
'''
# v1
def numar_caractere_lowercase_uppercase(text):
    numar_lowercase = 0
    numar_uppercase = 0

    for caracter in text:
        if caracter.islower():
            numar_lowercase += 1
        elif caracter.isupper():
            numar_uppercase += 1

    print(f"Numărul de caractere lower case este {numar_lowercase}")
    print(f"Numărul de caractere upper case este {numar_uppercase}")


rezultat = numar_caractere_lowercase_uppercase("Hai Pa")
print(rezultat)
'''
print("-" * 30)

'''
# v2
def numar_caractere(str):
    lower = 0
    upper = 0
    for caracter in str:
        if caracter.islower():
            lower += 1
        elif caracter.isupper():
            upper += 1
    print("Numar caractere lower: ", lower)
    print("Numar caractere lower: ", upper)


numar_caractere("Ala Bala Portocala")
'''

# 8. Funcție care primește o LISTĂ de numere și returnează o LISTĂ doar cu numerele pozitive.
# V1
'''
def numere_pozitive(list):
    lista_pozitiva = []
    for numar in list:
        if numar > 0:
            lista_pozitiva.append(numar)
    return lista_pozitiva


lista_numere = [10, 23, -1, -23, -19]
resultat = numere_pozitive(lista_numere)
print(resultat)
'''
print("-" * 30)

'''
# V2
def filtreaza_nr_pozitive(lista):

    # Fucnctia preia o lista de numere pozitive si negative si
    # returneaza numa numere pozitive

    numere_pozitive = []
    for numar in lista:
        if numar >= 0:
            numere_pozitive.append(numar)
    return numere_pozitive


numere = [1, 3, 5, - 4, 56, -4, - 3, -445, - 6]
rezultat = filtreaza_nr_pozitive(numere)
print(rezultat)
'''

# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ
# Primul număr x este mai mare decat al doilea număr y
# Al doilea număr y este mai mare decat primul număr x
# Numerele sunt egale.
# V1
'''
def numere(x, y):
    if x > y:
        print(f"{x} este mai mare ca {y}")
    elif x < y:
        print(f"{x} este mai mic ca {y}")
    else:
        print(f"{x} este egal cu {y}")


numere(2, 2)
'''
print("-" * 30)

'''
# v2
def compar_numere(x, y):
    if x > y:
        print('Primul numar', x, 'este mai mare ca ', y)
    elif x < y:
        print('Al 2 - lea numar', y, 'este mai mare ca ', x)
    else:
        print('egale')


compar_numere(3, 5)
'''

# 10. Funcție care primește un număr și un set de numere.
# Printează ‘am adaugat numărul nou în set’ + returnează True
# Printează ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False
# V1
'''
def numar_si_set(numar, set_numere):
    if numar not in set_numere:
        set_numere.add(numar)
        print(f"am adaugat {numar} in set")
        return True
    else:
        print(f"{numar} se afla deja in set")
        return False


print(numar_si_set(12, {10, 22, 13, 15}))

print("-" * 30)

'''
'''
# V2
def adauga_nr_in_set(numar, setul):
    if numar in setul:
        print(f"nu am adaugat numarul {numar} in set, acesta exista in set, acesta exista deja")
        return False
    else:
        setul.add(numar)
        print(f"Am adaugat {numar}")
        return True


setul = {1, 2, 4}
rezultat = adauga_nr_in_set(4, setul) 
'''

'''
# 11. Funcție care primește o lună din an și returnează câte zile are acea lună.
def numar_zile_luna(luna):
    if luna == 2:
        return 28
    elif luna in [4, 6, 9, 11]:
        return 30
    else:
        return 31

numar_zile = numar_zile_luna(7)
print(numar_zile)
'''

print("-" * 30)

# 12. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.
#
# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)
# V1
'''
def calculator(x, y):
    suma = print(f"Suma este {x + y}")
    diferenta = print(f"Diferenta este {x - y}")
    inmultire = print(f"Inmultirea este {x * y}")
    impartirea = print(f"Impartirea este {x / y}")


print(calculator(10, 2))

print("-" * 30)
'''
'''

# V2
def calculator2(a, b):
    sum = a + b
    dif = a - b
    add = a * b
    division = a / b
    return sum, dif, add, substract


rezultat = calculator2(2, 10)
print(rezultat)
'''

'''
# 13. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele.
# V1
def maxim(x, y, z):
    return max(x, y, z)


rezultat = maxim(1, 2, 3)
print(rezultat)

print("-" * 30)

'''

'''
# 14. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr.
# Exemplu: dacă dăm numărul 3, suma va fi 6 (0+1+2+3)
# V1
def suma_numar(x):
    suma = 0
    for i in range(x + 1):
        suma += i
    return suma


print(suma_numar(8))
'''
print("-" * 30)
'''

# V2
def calculeaza_suma_pana_la(numar):
    suma = 0
    for i in range(numar + 1):  # + 1 este pentru al inculude in interval
        suma += i
    return suma

rezultat = calculeaza_suma_pana_la(3)
print(rezultat)
'''

# 15.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.
#
# Exemplu:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Răspuns: {2, 3}
# V1
'''
def liste_numere(lista1, lista2):
    set_lista1 = set(lista1)
    set_lista2 = set(lista2)
    liste_numere = set_lista1.intersection(lista2)
    return liste_numere


list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
print(liste_numere(list1, list2))
'''
'''
# V2
def gasete_numere_comune(lista1, lista2):
    set_lista1 = set(lista1)
    set_lista2 = set(lista2)
    numere_comune = set_lista1.intersection(set_lista2)
    return numere_comune


list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]

rezultat = gasete_numere_comune(list1, list2)
'''

# 16. Funcție care să aplice o reducere de preț.
# Dacă produsul costă 100 lei și aplicăm reducere de 10%. Pretul va fi 90 de lei.
# Tratează cazurile în care reducerea e invalidă. De exemplu o reducere de 110% e invalidă.
# V1
'''
def aplicare_reducere(pret_initial, discount):
    reducere = pret_initial * discount / 100
    pret_final = pret_initial - reducere
    if discount < 0 or discount > 100:
        print("Discount invalid")
        return pret_final


pret_initial = 100
discount = 123
print(aplicare_reducere(pret_initial, discount))
'''
'''
# V2
def aplieca_reducere(pret, reducere):
    if reducere < 0 or reducere > 100:
        print("reducere invalida")
        return None
    else:
        pret_redus = pret * (1 - reducere / 100)
        return pret_redus

pret_initial1 = 100
reducere = 10
pret_redus = aplieca_reducere(pret_initial1, reducere)
if pret_redus is not None:
    print("Pretul redus este:", pret_redus)
print(pret_redus)


'''
#  17.Funcție care să afișeze data și ora curentă din România.
# (bonus: afișazăi și data și ora curentă din China)
# V1
'''
import datetime
import pytz


def data_curenta():
    data = datetime.datetime.now()
    ora_si_minute = data.strftime('%H:%M:%S')
    return ora_si_minute


def data_china():
    data = datetime.datetime.now()
    ora_si_minute = data.strftime('%H:%M:%S')
    fus_orar_china = pytz.timezone('Asia/Shanghai')
    ora_china = data.astimezone(fus_orar_china)
    return ora_china


print(data_curenta())
print(data_china())

print("-" * 30)
'''
'''
# 18. Funcție care să afișeze câte zile mai sunt până la ziua ta /
# sau până la Crăciun dacă nu vrei să ne zici cand e ziua ta :)
from datetime import date


def zile_pana_la_ziua_mea(data_nasterii):
    data_curenta = date.today()
    ziua_mea = date(data_curenta.year, data_nasterii.month, data_nasterii.day)

    # Verificăm dacă ziua de naștere din acest an a trecut sau nu
    if ziua_mea < data_curenta:
        ziua_mea = date(data_curenta.year + 1, data_nasterii.month, data_nasterii.day)

    # Calculăm diferența dintre cele două date
    diferenta = ziua_mea - data_curenta
    return diferenta.days


# Introdu data ta de naștere în formatul (an, luna, ziua)
data_nasterii = date(2023, 12, 25)
zile_ramase = zile_pana_la_ziua_mea(data_nasterii)

print(f"Mai sunt {zile_ramase} zile până la Craciun.")

print("-" * 30)
'''

# 19. Funcție care primește o listă de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }
'''
# V1
def afiseaza_lista(lista_cifre):
    cifra_count = {}  # Facem un dictionar gol
    for cifra in lista_cifre:
        if cifra in cifra_count:
            cifra_count[cifra] += 1
        else:
            cifra_count[cifra] = 1
    return cifra_count


lista_mea = [1, 3, 1, 5, 9, 7, 7, 5, 5]
print(afiseaza_lista(lista_mea))

Nu e ok
'''
'''
# V2
def numar_aparitii_cifre(lista):
    aparitii_cifre = {}  # initializam un dictionar gol
    for cifra in lista:  # parcurgem fiecare cifra din lista de intrare
        if cifra not in aparitii_cifre:  # verificam daca cifra nu a fost intalinta in dict
            aparitii_cifre[cifra] = 1  # daca cifra e intalinita prima data adauga 1
        else:
            aparitii_cifre[cifra] += 1  # daca a fost gasita de mai multe ori adauga +1
    for cifra in range(10):  # parcurge cifrele de la 0 la 9 pentru a completa dictionarul
        if cifra not in aparitii_cifre:  # daca cifra lipseste o adauga in dictionar aduga 0 in dictionar
            aparitii_cifre[cifra] = 0
    return aparitii_cifre # afiseaza dictionarul

lista = [1, 3, 1, 5, 9, 7, 7, 5, 5]
rezultat = numar_aparitii_cifre(lista)
print(rezultat)
'''

'''
# my_list = [-2, 4, 5, 6, 77]
# new_lis1 = sorted(my_list)
# print(new_lis1)
# new_list2 = sorted(my_list, reverse=True)
# print(new_list2)
'''

# # 20.
# import datetime
# import pytz
# import time
#
#
# def afiseaza_data_ora():
#     fus_orar_ro = pytz.timezone('Europe/Bucharest')
#     data_ora_ro = datetime.datetime.now(fus_orar_ro) # ora calculatorului sau ora serverului
#     print("data si ora in RO este:", data_ora_ro)
#     # pt china copiem tot
#
# afiseaza_data_ora()
#
# for i in range(10):
#     afiseaza_data_ora()
#     time.sleep(1)
