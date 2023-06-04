class Trojkat:
    def __init__ (self, a, b, c, h_a):
        self.bok_a = a
        self.b = b
        self.c = c
        self.h_a = h_a
        # self.obwod = a + b + c

    def obwod(self):
        return self.bok_a + self.b + self.c  
    
    def pole(self):
        return self.bok_a * self.h_a * 1/2

trojkat_rownoboczny = Trojkat(10, 10, 10, 8)
print(trojkat_rownoboczny.obwod())
    
trojkat_Darii = Trojkat(12, 10, 8, 6)    
print(trojkat_Darii.obwod())
print(trojkat_Darii.pole())

#trapez 
class Trapez:
    def __init__ (self, a, b, c, d, h):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.h = h

    def obwod(self):
        return self.a + self.b + self.c + self.d
    def pole(self):
        return ((self.a + self.b) * self.h)/2
    
trapez_darii = Trapez(6, 9, 5, 5, 2)
print(trapez_darii.obwod())
print(trapez_darii.pole())


print("---------------------------------")


#Student 
class Student:
    def __init__ (self, imie, nazwisko, numer_indeksu):
        self.imie = imie
        self.nazwisko = nazwisko 
        self.numer_indeksu = numer_indeksu 
        self.oceny = []

    def __str__ (self):
        # return self.imie + " " + self.nazwisko 
        return f"{self.imie} {self.nazwisko} {self.numer_indeksu}"
    
    def __int__ (self):
        return 6
    
    def dodaj_ocene (self, ocena):
        self.oceny.append(ocena)

    def zwroc_srednia(self):
        return(sum(self.oceny) / len(self.oceny))
    
student_daria = Student("Daria", "Chorenza", 120011)
student_daria.dodaj_ocene(4.5)
student_daria.dodaj_ocene(5)

print(int(student_daria))
print(student_daria.oceny)

print("--------------------------")

#Nowa klasa klub_pilkarski
class Klub_pilkarski:
    def __init__ (self, nazwa_klubu, kapitan, trener, miasto_pochodzenia, rok_zalozenia, kolor_klubu, data_najblizszego_meczu, ilosc_wygranych, ilosc_przegranych, ilosc_zawodnikow):
        self.nazwa_klubu = nazwa_klubu
        self.kapitan = kapitan 
        self.trener = trener 
        self.miasto_pochodzenia = miasto_pochodzenia
        self.rok_zalozenia = rok_zalozenia
        self.kolor_klubu = kolor_klubu
        self.data_najblizszego_meczu = data_najblizszego_meczu 
        self.ilosc_wygranych = int(ilosc_wygranych)
        self.ilosc_przegranych = int(ilosc_przegranych)
        self.ilosc_zawodnikow = int(ilosc_zawodnikow)
        self.zawodnicy = []
        self.mecze = []

        for i in range(self.ilosc_zawodnikow):
            self.zawodnicy.append(f"Zawodnik {i+1}")
    
    def __str__ (self):
        return f"{self.nazwa_klubu} {self.kapitan} {self.data_najblizszego_meczu} {self.miasto_pochodzenia}"
    
    def dodaj_zawodnika(self, zawodnik):
        self.zawodnicy.append(zawodnik)

    def aktualna_liczba_zawodnikow(self):
        return len(self.zawodnicy)

    def dodaj_mecz(self, mecz):
        self.mecze.append(mecz)

    def oblicz_procent_wygranych(self):
        if self.ilosc_wygranych == 0 and self.ilosc_przegranych == 0:
            return 0.0
        else:
            procent_wygranych = (self.ilosc_wygranych / (self.ilosc_wygranych + self.ilosc_przegranych)) * 100
            return round(procent_wygranych, 2)

klub_darii = Klub_pilkarski("Lech", "Nowak", "Kowalski", "Poznan", "1990", "Niebiesko-bialy", "06.06.2023", 20, 10, 25)
print("Dane o klubie darii:")
print(klub_darii)

klub_darii.dodaj_zawodnika("Jan Kowalski")
klub_darii.dodaj_zawodnika("Adam Nowak")
klub_darii.dodaj_zawodnika("Piotr Malinowski")

print("Aktualna liczba zawodników:", klub_darii.aktualna_liczba_zawodnikow())

klub_darii.dodaj_mecz("Lech vs. Legia - 1:0")
klub_darii.dodaj_mecz("Lech vs. Wisła - 2:2")

print("Dodane mecze:")
print(klub_darii.mecze)

print("Procentowa ilośc wygranych meczy:")
print(klub_darii.oblicz_procent_wygranych())