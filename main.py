import csv
import faker  # Biblioteka do generowania fałszywych danych
from datetime import datetime, timedelta
import random

ilosc_kas = 10
ilosc_pracownikow = 100
ilosc_obslug = 1000
ilosc_wnioskow = ilosc_obslug

fake = faker.Faker()
current_year = 2023

pracownicy = ['id_pracownika_pk', 'data_urodzenia', 'data_zatrudnienia']
stanowisko_kasowe = ['id_kasy_pk', 'numer_kasy']
obsluga = ['id_pk', 'id_wniosku_fk', 'id_pracownika_fk', 'id_stanowiska_fk']
wniosek = ['id_wniosku_pk', 'id_obslugi_fk', 'typ_wnioskowanego_dokumentu', 'id_daty_fk', 'stan_wniosku','godzina_pobrania_numerka','godzina_zeskanowania_wniosku_przy_okienku',
           'druga_godzina_zeskanowania']
data = ['id_daty_pk', 'data_przyjecia_wniosku', 'czy_wakacje', 'czy_wolne', 'dzien_tygodnia','czy_weekend','dzien_tygodnia_numer', 'pora_roku']


csv_file = 'pracownicy.csv'
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=pracownicy)
    writer.writeheader()

    for i in range(1, ilosc_pracownikow + 1):
        birth_date = fake.date_of_birth(minimum_age=18, maximum_age=65)
        # Generowanie losowej różnicy wieku między 20 a 40 lat
        age_difference = random.randint(20, 40)
        hire_date = birth_date + timedelta(days=365 * age_difference)

        # Sprawdzenie, czy data zatrudnienia przekracza bieżący rok
        if hire_date.year > current_year:
            hire_date = datetime(current_year, 12, 31)

        fake_data = {
            pracownicy[0]: i,
            pracownicy[1]: birth_date.strftime('%Y-%m-%d'),
            pracownicy[2]: hire_date.strftime('%Y-%m-%d'),
        }
        writer.writerow(fake_data)


csv_file = 'stanowisko_kasowe.csv'

with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=stanowisko_kasowe)
    writer.writeheader()

    for i in range(1, ilosc_kas + 1):
        fake_data = {
            stanowisko_kasowe[0]: i,
            stanowisko_kasowe[1]: i,
        }
        writer.writerow(fake_data)

csv_file = 'obsluga.csv'

with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=obsluga)
    writer.writeheader()

    for i in range(1, ilosc_obslug + 1):
        fake_data = {
            obsluga[0]: i,
            obsluga[1]: i,
            obsluga[2]: random.randint(1, ilosc_pracownikow),
            obsluga[3]: random.randint(1, ilosc_kas),
        }
        writer.writerow(fake_data)

csv_file = 'wniosek.csv'

with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=wniosek)
    writer.writeheader()

    for i in range(1, ilosc_wnioskow + 1):
        fake_data = {
            wniosek[0]: i, # 'id_wniosku_pk'
            wniosek[1]: i, # 'id_obslugi_fk'
            wniosek[2]: i, # 'typ_wnioskowanego_dokumentu'
            wniosek[3]: i, #  'id_daty_fk'
            wniosek[4]: i,  # 'id_wniosku'
            wniosek[5]: i,  # 'id_obslugi_fk'
            wniosek[6]: i,  # 'typ_wnioskowanego_dokumentu'
            wniosek[7]: i,  # 'id_daty_fk'
        }
        writer.writerow(fake_data)

wniosek =  'stan_wniosku','godzina_pobrania_numerka','godzina_zeskanowania_wniosku_przy_okienku',
           'druga_godzina_zeskanowania']