import csv 

class Pracownik:
    def __init__(self, imie, nazwisko, w_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.w_brutto = w_brutto

    @property
    def wynagrodzenie_netto(self) -> float:
        sk_chorobowa = round(self.w_brutto * 0.0245, 2)
        sk_emerytalna = round(self.w_brutto * 0.0976, 2)
        sk_rentowa = round(self.w_brutto * 0.015, 2)
        podstawa_skladki_zdrowotnej = self.w_brutto - \
            sk_emerytalna - sk_rentowa - sk_chorobowa
        sk_zdrowotna = round(podstawa_skladki_zdrowotnej * 0.09, 2)
        kwota_zmiejszajaca_podatek = 300
        podstawa_opodatkowania = self.w_brutto - \
            sk_emerytalna - sk_rentowa - sk_chorobowa
        zaliczka_na_podatek = round(
            (podstawa_opodatkowania * 0.12) - kwota_zmiejszajaca_podatek, 2)

        return self.w_brutto - sk_emerytalna - sk_rentowa - sk_chorobowa - sk_zdrowotna - zaliczka_na_podatek

    @property
    def calkowity_koszt(self) -> float:
        sk_emerytalna = round(self.w_brutto * 0.0976)
        sk_rentowa = round(self.w_brutto * 0.065)
        skladka_wypadkowa = round(self.w_brutto * 0.0167)
        fundusz_pracy = round(self.w_brutto * 0.0245)
        fgsp = round(self.w_brutto * 0.001)

        return self.w_brutto + sk_emerytalna + sk_rentowa + skladka_wypadkowa + fundusz_pracy + fgsp


pracownicy = []

with open('\C:\Users\HP\Desktop\inz\example-project01\pracownicy.csv', 'r', encoding='utf-8') as csv_data_file:
# with open('pracownicy.csv', 'r', encoding='utf-8') as csv_data_file:
    next(csv_data_file)  # Pomija nagłówek pliku CSV
    for line in csv_data_file:
        imie, nazwisko, w_brutto = line.strip().split(',')
        pracownicy.append(Pracownik(imie, nazwisko, float(w_brutto)))

koszt_pracodawcy = sum(pracownik.calkowity_koszt for pracownik in pracownicy)

print(f'Całkowity koszt pracodawcy: {koszt_pracodawcy}')

for pracownik in pracownicy:
    print(f'Koszt pracownika {pracownik.imie} {pracownik.nazwisko} dla pracodawcy: {pracownik.calkowity_koszt}')