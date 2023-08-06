# 1.Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
#
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ‘Mașina mea preferată este x’.
# Fă același lucru cu un for each.
# Fă același lucru cu un while.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedses', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

# FOR loop
for masina in masini:
    print(f"Masina mea preferata este {masina}")

print("-"*30)

i = 0
while i < len(masini):
    masina = masini[i]
    print(f"Masina mea preferata este {masina}")
    i += 1

print("-"*30)

# 2. Aceeași listă:
# Folosește un for else În for
# Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul.
# În else:
# Printează lista.
masini = ['Audi', 'Volvo', 'BMW', 'Mercedses', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for index, masina in enumerate(masini): # functia enumerate este pentru a obtne indexul fiecarui element din lista
    if index == 0 or index == len(masini) - 1: # primul si ultimul element din lista va fi cu upper
        continue
    masini[index] = masina.upper() # modifica caracterele primului si ultimuli elem
else:
    print(masini)

print("-"*30)

# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Iterează prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
#    Printează ‘am găsit mașina dorită de dvs’
#    Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
#    Printează ‘Am găsit mașina X. Mai căutam‘
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == "Mercedes":
        print("am gasit masina")
        break
    else:
        print(f"Nu am gasit masina {masina}, mai cautam")
# Tema de casa cu WHILE

print("-"*30)

# 4. Aceeași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun.
#
# Dacă mașina e Trabant sau Lăstun:
#    Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
# Printează S-ar putea să vă placă mașina x.
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == "Trabamt" or masina == "Lastun":
        continue
    print(f"S-ar putea sa va placa masina {masina}")


print("-"*30)

# 5. Modernizează parcul de mașini:
#
# Crează o listă goală, masini_vechi.
# Iterează prin mașini.
# Când găsesti Lăstun sau Trabant:
# Salvează aceste mașini în masini_vechi.
# Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# Printează Modele vechi: x.
# Modele noi: x.
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []

for index, masina in enumerate(masini):
    if masina == "Lastun" or masina == "Trabant":
        masini_vechi.append(masina)
        masini[index] = "Tesla"    # Tesla va inlocui ambii indexi
        masini = list(set(masini)) # folosim set ca sa scoata duplicatul
print(f"Modele vechi: {masini_vechi}")
print(f"Modele noi: {masini}")

print("-"*30)

# 6. Având dict:
# pret_masini = {
#     'Dacia': 6800,
#     'Lăstun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
#
# Vine un client cu un buget de 15000 euro.
#
# Prezintă doar mașinile care se încadrează în acest buget.
# Iterează prin dict.items() și accesează mașina și prețul.
# Printează Pentru un buget de sub 15000 euro puteți alege mașină xLastun
# Iterează prin listă.

pret_masini = {
     'Dacia': 6800,
     'Lăstun': 500,
     'Opel': 1100,
     'Audi': 19000,
     'BMW': 23000
}
buget = 15000
for masina, pret in pret_masini.items(): # petru keye si valoare va merge prin fiecare item al dictionarului
    if pret <= buget:
        print(f"Pentru un buget sub 15000 euro iti poti permite {masina}")

print("-"*30)

# 7. Având lista:
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterează prin ea.
# Afișează de câte ori apare 3 (nu ai voie să folosești count).
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
aparitii = 0

for numar in numere:
    if numar == 3:
        aparitii += 1
print(f"Numarul 3 apare de {aparitii}")

print("-"*30)

# 8. Aceeași listă:
# Iterează prin ea
# Calculează și afișează suma numerelor (nu ai voie să folosești sum).

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for numar in numere:
    suma += numar
print(f"suma este {suma}")


print("-"*30)

# 9. Aceeași listă:
# Iterează prin ea.
# Afișază cel mai mare număr (nu ai voie să folosești max).
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
numar_max = 0
numar_min = 0

for numar in numere:
    if numar > numar_max:
        numar_max = numar
print(f"cel mai mare nr este {numar_max}")

for numar in numere:
    if numar < numar_min:
        numar_min = numar
print(f"Cel mai mic numar este {numar_min}")

print("-"*30)

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

for nr in numere:
    if nr == max(numere):
        print(nr)

for nr in numere:
    if nr == min(numere):
        print(nr)

print("-"*30)

# 10. Aceeași listă:
# Iterează prin ea.
# Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# Afișază noua listă.
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = -numere[i]
print(numere)

print("-"*30)


# 11.
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Itereaza prin listă alte_numere
# Populează corect celelalte liste
# Afișează cele 4 liste la final
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for numar in alte_numere:
    if numar %2 == 0:
        numere_pare.append(numar)
    else:
        numere_impare.append(numar)
    if numar > 0:
        numere_pozitive.append(numar)
    else:
        numere_negative.append(numar)
print(numere_pare)
print(numere_impare)
print(numere_pozitive)
print(numere_negative)

print("-"*30)



# 12. Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
#    User alege un număr
#    Programul îi spune:
# Nr secret e mai mare
# Nr secret e mai mic
# Felicitări! Ai ghicit!
'''
import random

numar_sercret = random.randint(1, 30)
numar_ghicit = None
numar_incercari = None

while True:
    numar_ghicit = int(input("Alege un numar de la 1 la 30 "))
    if numar_sercret > numar_ghicit:
        print("numarul ghicit este mai mare")
    elif numar_sercret < numar_ghicit:
        print("numarul ghicit este mai mic")
    else:
        print(f"Felicitari!, Ai castigat!, {numar_incercari}")
        break
'''
# 13. Alege un număr de la tastatură
# Ex: 7
# Scrie un program care să genereze în consolă următoarea piramidă
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
'''
numar = int(input("Alege numarul "))

for i in range(1, numar + 1):
    for j in range(i):
        print(i, end="")
    print()
'''

# 14.
# tastatura_telefon = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
# Iterează prin listă 2d
# Printează ‘Cifra curentă este x’

tastatura_telefon = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9],
   [0]
]
for i in tastatura_telefon:

    for j in i:
        print(f"cifra curenta este {j}")

print("-"*30)
lista_2d = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9],
   [0]
]
print(lista_2d[0])
print(lista_2d[2][2]) # Extragere date din lista 2d