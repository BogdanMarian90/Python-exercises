# Partea 1 - Setup, Variabile, Tipuri de date

# 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
# Variabila reprezinta un spatiu de stocare



print("-"*40)
# 2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă:
# string
# int
# float
# bool
# Observație: Valorile vor fi alese de tine după preferințe.
name = "Bogdan"
age = 33
height = 1.75
male = True



print("-"*40)
# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
print(type(name))
print(type(age))
print(type(height))
print(type(male))



print("-"*40)
# 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
# Verifică tipul acesteia.
# Luam din nou variabila height
height = 1.75
print("Tipul varabile este", type(height))
# rotunjim variabila
height = round(height)
print("Tipul variabile este", type(height))
print(height)



print("-"*40)
# 5. Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile.
# Rezolvă nepotrivirile de tip prin ce modalitate dorești.
print(f"Hi your name is {name}")
print(f"You are {age} years old")
print(f"Your high is: {height}, you are tall :))")
print(f"You are male? {male}")



print("-"*40)
# 6. Citește de la tastatură:
# numele;
# prenumele.
# Afișează: 'Numele complet are x caractere'.
'''
first_name = input("Enter your first_name: ")
last_name = input("Enter your last_name: ")
full_name = first_name + last_name
print(len(full_name))
'''



print("-"*40)
# 7. Citește de la tastatură:
# lungimea;
# lățimea.
# Afișează: 'Aria dreptunghiului este x
# L = int(input("Enter length: "))
# l = int(input("Enter width: "))
# triangle_area = L * l
# print(f"Triangle are is: {triangle_area} m^2")



print("-"*40)
# 8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
# afișează de câte ori apare cuvântul 'the';
proposition = "Coral is either the stupidest animal or the smartest rock"
print(proposition.count("the"))



print("-"*40)
# 9. Același string:
# Afișează de câte ori apare cuvântul 'the';
# Printează rezultatul.



print("-"*40)
# 10. Același string:
# Folosește un assert ca să verifici dacă acest string conține doar numere.
proposition = "Coral is either the stupidest animal or the smartest rock"
assert proposition.isdigit() == False



print("-"*40)
# 11. Exercițiu:
# citește de la tastatură un string de dimensiune impară;
# afișează caracterul din mijloc.

# trebuie sa citim un string de la tastatura
#input_string = input("Introdu un string de dim impara: ")
# verificam daca lungimea stringului e impara
'''
if len(input_string) %2 != 0:
    # afisam caracterul din mijloc
    mijloc = len(input_string)//2
    caracter_mijloc = input_string[mijloc]
    print(f"Caracter mijloc este {caracter_mijloc}")
else:
    print("Lungimea stringului nu este impara")
# Liste [0,1,2,3,4] - se pot modifica
# Tuple (1,2,3,4)
# Dictionar {key:valoare}
'''


print("-"*40)
# 12. Folosind o singură linie de cod :
# citește un string de la tastatură (ex: 'alabala portocala');
# salvează fiecare cuvânt într-o variabilă;
# printează ambele variabile pentru verificare.
'''
cuvant1, cuvant2 = input("Introdu un string din doua cuvinte.... ").split()
print(cuvant1)
print(cuvant2)
'''


print("-"*40)
# 13. Exercițiu:
# citește un string de la tastatură (ex: alabala portocala);
# salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
# capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => aLABALA PORTOCALa.
#Tema de casa
'''
input_string = input("enter string: ")
primul_caracter = input_string[0]
ultimul_caracter = input_string[-1]
capitalized_string = primul_caracter + input_string[1:-1].upper() + ultimul_caracter
print(capitalized_string)
'''




print("-"*40)
# 14.Exercițiu:
# citește un user de la tastatură;
# citește o parolă;
# afișează: 'Parola pt user x este ***** și are x caractere';
# ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.
#
# eg: parola abc => ***
# parola abcd => ****
'''
#introducem user si parola
user = input("enter user: ")
password = input("enter password: ")

# Calculam nr din parola
lungime_parola = len(password)

#construim stringul cu caracterele * in functie de lungimea parolei
caractere_asterix = "*" * lungime_parola

#afisam rezultatul
print(f"parola pentru userul {user} este {caractere_asterix} si are lungimea {lungime_parola} caractere")
'''