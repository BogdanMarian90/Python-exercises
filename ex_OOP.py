# 1.Clasa Cerc
#     Atribute: rază, culoare
#     Constructor pentru ambele atribute
#     Metode:
# descrie_cerc() - va PRINTA culoarea și raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()
'''
class Cerc:
    raza = None
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descriere_cerc(self):
        return f"Raza cercului este {self.raza}, cularea este {self.culoare}"

    def aria_cerc(self):
        return 3.14 * (self.raza ** 2)

    def diametru(self):
        return 2 * self.raza

    def circumferinta(self):
        return 3.14 * 2 * self.diametru()

cerc = Cerc(20, "Negru")
print(cerc.descriere_cerc())
print(f"Aria este {cerc.aria_cerc()}")
print(f"Diametrul este {cerc.diametru()}")
print(f"Circumferinta este {cerc.circumferinta()}")
'''

# 2. Clasa Dreptunghi
#      Atribute: lungime, lățime, culoare
#      Constructor pentru toate atributele
#      Metode:
# descrie()
# aria()
# perimetrul()
# schimbă_culoarea(noua_culoare) -
# această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare.
# Poți verifica schimbarea culorii prin apelarea metodei descrie().
'''
class Dreptunghi:
    lungime = None
    latime = None
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere(self):
        return f"Dreptunghiul are lungimea: {self.lungime}mm, latimea: {self.latime}mm si cularea: {self.culoare}"

    def aria(self):
        return self.lungime * self.latime

    def perimetru(self):
        return (self.lungime + self.latime) * 2

    def schimba_culoare(self, noua_culoare):
        self.culoare = noua_culoare
        print(f"Noua culoare este: {noua_culoare}")


d1 = Dreptunghi(20, 10, "Red")
print(d1.descriere())
print(f"Aria este {d1.aria()}")
print(f"Perimetrul este {d1.perimetru()}")
d1.schimba_culoare("Black")
print(d1.descriere())
'''

# 3. Clasa Angajat
#      Atribute: nume, prenume, salariu
#      Constructor pentru toate atributele
#      Metode:
# descrie()
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)
'''
class Angajat:
    nume = None
    prenume = None
    salariu = None

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.salariu = salariu
        self.prenume = prenume

    def descriere(self):
        return f"Angajatul: {self.nume}, {self.prenume} are salariul de {self.salariu} lei"

    def nume_complet(self):
        return f"{self.nume} {self.prenume}"

    def salariu_lunar(self):
        return f"Salar lunar = {self.salariu}"

    def salariu_anual(self):
        return f"Salariu anual = {self.salariu * 12}"

    def marire_salariu(self, procent):
        self.procent = procent
        return self.salariu * (1 + procent / 100)


angajat1 = Angajat("Bogdan", "Marian", 3000)
print(angajat1.descriere())
print(angajat1.nume_complet())
print(angajat1.salariu_lunar())
print(angajat1.salariu_anual())
print(f"Marire salar {angajat1.marire_salariu(25)}")
'''

# 4. Clasa Cont
#    Atribute: iban, titular_cont, sold
#    Constructor pentru toate atributele
#    Metode:
# afisare_sold() - Titularul x are în contul y suma de n lei
# debitare_cont(suma)
# creditare_cont(suma)
'''
class Cont:
    iban = None
    titular_cont = None
    sold = None

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        return f"Titularul {self.titular_cont}, are in contul {self.iban} suma de {self.sold} lei"

    def debitare_cont(self, suma):
        if suma > self.sold:
            print("Fonduri insuficente")
        elif suma == 0:
            print("Nu se poate debita 0 lei in cont")
        else:
            self.sold -= suma
            print(f"S-a debitat suma de {suma} lei din contul {self.iban}")

    def creditare_cont(self, suma):
        self.sold += suma
        print(f"S-a adugat in cont suma de {suma} lei din contul {self.iban}")


cont1 = Cont("RORNCB1289383993490", "Marian Bogdan", 2000)
print(cont1.afisare_sold())
cont1.debitare_cont(4000)
cont1.debitare_cont(400)
cont1.debitare_cont(0)
cont1.creditare_cont(9999)
print(cont1.afisare_sold())
'''

#  5. Clasa Factură
#      Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor avea aceeași serie), număr, nume_produs, cantitate, pret_buc
#      Constructor: toate atributele, fără serie
#      Metode:
# schimbă_cantitatea(cantitate)
# schimbă_prețul(pret)
# schimbă_nume_produs(nume)
# generează_factura() - va printa tabelar dacă reușiți

# Factura seria x număr y
# Data: generează automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon |      7       |       700       | 4900
'''
from datetime import date
from tabulate import tabulate


class Factura:
    seria = "ROIDX#"

    def __init__(self, numar, nume_produs, cantitate, pret_bucata):
        self.numar = numar
        self.nume_produs = nume_produs
        self.pret_bucata = pret_bucata
        self.cantitate = cantitate

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate

    def schimba_pret(self, pret):
        self.pret_bucata = pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume

    def schimba_numar(self, numar):
        self.numar = numar

    def genereaza_factura(self):
        data = date.today().strftime("%d.%m.%Y")  # strftime (ziua, luna, an)
        total = self.cantitate * self.pret_bucata
        # print("Factura seria", Factura.seria, "numarul", self.numar)
        # print("Data:", data)
        # print("Produs\t|\tCantitate\t|\tPret bucata\t|\tTotal")
        # print(self.nume_produs, "\t|\t", self.cantitate, "\t\t|\t", self.pret_bucata, "\t\t|\t", total)
        header = ["Produs", "Cantitate", "Pret bucata", "Total"]  # Mai intai facem headerul
        col_names = [[self.nume_produs, self.cantitate, self.pret_bucata, total]]
        print("Factura seria", Factura.seria, "numarul", self.numar)
        print("Data:", data)
        print(tabulate(col_names, headers=header, tablefmt="grid"))


factura1 = Factura("1", "Bicarbonat de sodiu", 10, 8000)
factura1.genereaza_factura()
factura1.schimba_cantitatea(450)
factura1.schimba_pret(1000)
factura1.schimba_numar("2")
factura1.schimba_nume_produs("Oled")
factura1.genereaza_factura()
'''



# ABSTRACTION
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’

from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    @classmethod
    def descriere(cls):
        print('Cel mai probabil am colturi')


'''
    INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură

    ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)
'''


class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    def aria(self):
        return self.__latura * self.__latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Getter : latura este {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura):
        print(f'Setter : noua latura este {latura}')
        self.__latura = latura

    @latura.deleter
    def latura(self):
        print(f'Deletter : am sters latura ')
        self.__latura = None


patrat1 = Patrat(20)
patrat1.descriere()
# patrat1.latura()
patrat1.aria()
print(f'Latura este : {patrat1.latura}')
print(f'Aria este : {patrat1.aria()}')
# print(f'Latura este {patrat1.latura} si aria este {patrat1.aria()}')
patrat1.latura = 30
del patrat1.latura

'''
Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda abstractă aria)
'''


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Raza cercului este {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza):
        print(f'Noua valoare a razei este: {raza}')
        self.__raza = raza

    @raza.deleter
    def raza(self):
        print("Am sters valoarea razei")
        self.__raza = None

    def aria(self):
        aria_cercului = self.PI * self.__raza ** 2
        return aria_cercului

    def descriere(self):
        print('Eu nu am colturi!')


cerc1 = Cerc(10)
cerc1.descriere()
print(f'Aria cercului este : {cerc1.aria()}')
cerc1.raza
cerc1.raza = 20
print(f'Aria cercului este : {cerc1.aria()}')
del cerc1.raza


class Car:
    color = "Grey"
    actual_speed = 0
    chosen_colors = ["Red", "Black", "Blue"]
    brand = "Dacia"
    registered = False

    def __init__(self, model, max_speed):
        self.model = model
        self.max_speed = max_speed
        self._paint = self.color

    def description(self):
        print(f"Car {self.brand}, "
              f"{self.model}, "
              f"{self._paint}, "  # Folosim _paint aici
              f"{self.actual_speed},"
              f"{self.max_speed},"
              f"{self.registered}")

    def register(self):
        self.registered = True

    @property
    def paint(self):
        return self._paint

    @paint.setter
    def paint(self, chosen_color):
        print(f"New color is {chosen_color}")
        if chosen_color not in self.chosen_colors:
            raise Exception("Color is not in the optional list")
        self._paint = chosen_color

    def accelerate(self):
        if self.actual_speed < 0:
            raise Exception("Speed is negative")
        if self.actual_speed == 0:
            print("The car is not moving")
        else:
            print(f"Accelerate up to {self.max_speed}")

    def stop(self):
        print(f"The car is Stopped, {self.actual_speed}")


my_car = Car("Logan", 180)
my_car.description()
my_car.accelerate()
my_car.stop()
my_car.paint = "Red"
my_car.register()
my_car.description()

