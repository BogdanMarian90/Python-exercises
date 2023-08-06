
#Partea 2 - Operatori, condiționale
print("-"*40)
# 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
# Este o structura care controleaza si permite o executare diferita a codului


# 2. Verifică și afișează dacă x este număr natural sau nu.
'''
x = int(input("Introdu un numar: "))
if x >= 1:
    print(f"numarul {x} este un numar natural")
else:
    print(f"numarul {x} nu este un numar natural")
'''



# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
'''
x = float(input("Introdu un numar: "))
if x > 0:
    print(f"Numarul {x} este pozitiv")
elif x == 0:
    print(f"Numarul {x} este neutru")
else:
    print(f"Numarul {x} este negativ")
'''



# 4. Verifică și afișează dacă x este între -2 și 13.
'''
x = float(input("Introdu un numar: "))
#if x > -2 and x < 13:
if x -2 < x < 13:
    print(f"Numarul {x} se afla in intervalul -2, 13")
else:
    print(f"Numarul {x} nu se afla in intervalul -2, 13")
'''


'''
#5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5
x = int(input("Introdu un numar: "))
y = int(input("Introdu un numar: "))
diferenta = abs(x - y) #calcularea valorii absolute a diferentei
if diferenta < 5:
    print(True)
else:
    print(False)
'''


#6. Verifică dacă x NU este între 5 și 27  - a se folosi ‘not’.
'''
x = int(input("Introdu un numar: "))
if x <= 5 and x >= 27:
    print(f"numarul {x} nu se afla intre 5 si 27")
else:
    print(f"numarul {x}  se afla intre 5 si 27")
'''


# 7.
# x și y (int)
# Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
'''
x = int(input("Introdu un numar: "))
y = int(input("Introdu un numar: "))
if x == y:
    print(f"{x} este egal cu {y}")
elif x > y:
    print(f"{x} mai maare ca {y}")
else:
    print(f"{x} mai mic ca {y}")
'''


# 8. X, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
'''
x = int(input("Introdu un numar: "))
y = int(input("Introdu un numar: "))
z = int(input("Introdu un numar: "))
if x == y == z:
    print(f"echilateral")
elif x == y or x == z or y == z:
    print("isoscel")
else:
    print("oarecare")
'''



# 9. Citește o literă de la tastatură.
#    Verifică și afișează dacă este vocală sau nu.
'''
letter = input("Enter your letter: ")
#if letter.lower() == "a" or letter.lower() == "e" or letter.lower() == "i" or letter.lower() == "o" or letter.lower() == "u":
if letter.lower() in ["a", "e", "i", "o", "u"]: # Chatgpt
    print(f"Your letter {letter} is vowel")
else:
    print(f"Your letter {letter} is not vowel")
'''


# 10.Transformă și printează notele din sistem românesc în  >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F
'''
grade = int(input("Enter your grade: "))
if grade > 9 and grade <= 10:
    print(f"Your {grade} is A")
    print("You pass the exam")
elif grade > 10:
    print(f"Your grade doesn't exit, enter form (o to 10)")
elif grade >= 8:
    print(f"Your {grade} is B")
    print("You pass the exam")
elif grade >= 7:
    print(f"Your {grade} is C")
    print("You pass the exam")
elif grade >= 6:
    print(f"Your {grade} is D")
    print("You pass the exam")
elif grade >= 4:
    print(f"Your {grade} is E")
    print("You pass the exam")
else:
    print(f"Your {grade} is F")
    print("You didn't pass the exam")
'''



# 11.Verifică dacă x are minim 4 cifre (x e int).
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
'''
x = int(input("Enter x value: "))
if abs(x) >= 1000:
    print("Your x have at least 4 digits")
else:
    print("Your x have didn't have 4 digits")
'''


# 12.Verifică dacă x are exact 6 cifre.
'''
x = int(input("Enter x value: "))
if 100000 <= abs(x) < 1000000:
    print(f"Your {x} have have 6 digits")
else:
    print(f"Your {x} not have 6 digits")
'''


# 13.Verifică dacă x este număr par sau impar (x e int).
'''
x = int(input("Enter x value: "))
if x %2 != 0:
    print(f"Your {x} is odd number")
else:
    print(f"Your {x} is even number")
'''

# 14.      x, y, z (int)
# Afișează care este cel mai mare dintre ele?
'''
x = int(input("Enter x value: "))
y = int(input("Enter y value: "))
z = int(input("Enter z value: "))
if x > y and x > z:
    print("x is higher number")
elif y > x and y > z:
    print("y is higher number")
elif z > x and z > y:
    print("z is higher number")
else:
    print("Your numbers are equals")
'''


# 15. X, y, z - reprezintă unghiurile unui triunghi
# Verifică și afișează dacă triunghiul este valid sau nu.
'''
x = int(input("Enter first triangle angle: "))
y = int(input("Enter second triangle angle: "))
z = int(input("Enter third triangle angle: "))
if x + y + z == 180:
    print("Your triangle is valid")
else:
    print("Your triangle is not valid")
'''



# 16. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# Citește de la tastatură un int x
# Afișează stringul fără ultimele x caractere
# Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'
'''
string = "Coral is either the stupidest animal or the smartest rock"
x = int(input("Enter your number: "))
if x >= len(string):
    print("x is higher then your string")
else:
    new_string = string[:-x]
    print(new_string)
'''
# Varianta 2
'''
text = 'Coral is either the stupidest animal or the smartest rock'  # Stringul inițial
x = int(input("Introdu un număr întreg: "))  # Citirea numărului de la tastatură

text_taiat = text[:-x]  # Obtinerea textului taiat fara ultimele x caractere

print(text_taiat)  # Afisarea textului taiat
'''


#17. Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5.
'''
string = "Coral is either the stupidest animal or the smartest rock"
if len(string) >= 10:
    new_string = string[:5] + string[-5:]
else:
    new_string = string

print(new_string)
'''



# 18. Același string.
# Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
# Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
# output: 'Coral is either the stupidest animal or the smartest'
'''
string = "Coral is either the stupidest animal or the smartest rock"
if "rock" in string:
    start_index = string.index("rock")
    print(f"rock index is {start_index}")
    new_string = string[:start_index]
    print(new_string)
else:
    print("rock is not in string")
'''



# 19. Joc ghicit zarul
# Caută pe net și vezi cum se generează un număr random
# Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
# Ia numărul ghicit de la utilizator
# Verifică și afișează dacă utilizatorul a ghicit
# Vei avea 3 opțiuni
# Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
# Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
# Ai ghicit. Felicitări! Ai ales x si zarul a fost y.
'''
import random
dice_roll = random.randint(1, 6)
guess_roll = int(input("Enter your number (1, 6): "))
if dice_roll > guess_roll:
    print("Ai pierdut")
elif dice_roll < guess_roll:
    print("Ai castigat")
else:
    print("Egalitate")
'''



# 20. Având stringul '0123456789'
# Afișează doar numerele pare
# Afișează doar numerele impare
# (hint: folosește slicing, controlează din pas)
'''
text = '0123456789'
numere_pare = text[::2]
print(numere_pare)
numere_impare = text[1::2]
print(numere_impare)
'''