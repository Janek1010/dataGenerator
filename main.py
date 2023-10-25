import csv
import faker  # Biblioteka do generowania fałszywych danych
from datetime import datetime, timedelta
import random
import calendar

ilosc_kas = 10
ilosc_pracownikow = 100
ilosc_obslug = 1000
ilosc_wnioskow = ilosc_obslug
ilosc_dat = 200
ile_lat = 3  # Ile lat wstecz generować daty
fake = faker.Faker()
current_year = 2023

pracownicy = ['id_pracownika_pk', 'data_urodzenia', 'data_zatrudnienia']
stanowisko_kasowe = ['id_kasy_pk', 'numer_kasy']
obsluga = ['id_pk', 'id_wniosku_fk', 'id_pracownika_fk', 'id_stanowiska_fk']
wniosek = ['id_wniosku_pk', 'id_obslugi_fk', 'typ_wnioskowanego_dokumentu', 'id_daty_fk', 'stan_wniosku',
           'godzina_pobrania_numerka', 'godzina_zeskanowania_wniosku_przy_okienku',
           'druga_godzina_zeskanowania']
data = ['id_daty_pk', 'data_przyjecia_wniosku', 'czy_wakacje', 'czy_wolne', 'dzien_tygodnia', 'czy_weekend',
        'pora_roku']
typy_dokumentow = ['paszport', 'dowod_osobisty', 'prawo_jazdy']
stany_wnioskow = ['odrzucony', 'zaakceptowany', 'tworzony', 'Oczekuje_na_odbior', 'zakonczony']
prawdopodobienstwa = [0.05, 0.35, 0.15, 0.1, 0.35]

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

csv_file = 'data.csv'

ilosc_dat = 365 * ile_lat
# Otwarcie pliku CSV i zapisanie danych
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=data)
    writer.writeheader()

    for i in range(1, ilosc_dat + 1):
        # Obliczenie daty na podstawie indeksu i liczby dni wstecz
        start_date = datetime.now() - timedelta(days=ilosc_dat - i)

        # Sprawdzenie, czy jest wakacje
        if start_date.month in [6, 7, 8]:
            czy_wakacje = 'tak'
        else:
            czy_wakacje = 'nie'

        # Sprawdzenie, czy jest dzień wolny
        if start_date.weekday() in [5, 6]:
            czy_wolne = 'tak'
        else:
            czy_wolne = 'nie'

        # Określenie dnia tygodnia
        dzien_tygodnia = calendar.day_name[start_date.weekday()]

        # Sprawdzenie, czy to weekend
        if start_date.weekday() in [4, 5]:
            czy_weekend = 'tak'
        else:
            czy_weekend = 'nie'

        # Określenie pory roku
        month = start_date.month
        if 3 <= month <= 5:
            pora_roku = 'wiosna'
        elif 6 <= month <= 8:
            pora_roku = 'lato'
        elif 9 <= month <= 11:
            pora_roku = 'jesien'
        else:
            pora_roku = 'zima'

        fake_data = {
            data[0]: i,
            data[1]: start_date.strftime('%Y-%m-%d'),
            data[2]: czy_wakacje,
            data[3]: czy_wolne,
            data[4]: dzien_tygodnia,
            data[5]: czy_weekend,
            data[6]: pora_roku
        }
        writer.writerow(fake_data)

csv_file = 'wniosek.csv'

dates = []
with open('data.csv', 'r') as datafile:
    datareader = csv.DictReader(datafile)
    for row in datareader:
        if row['czy_wolne'] == 'nie' or row['czy_weekend'] == 'nie':
            dates.append({
                'id_daty_pk': row['id_daty_pk'],
                'data_przyjecia_wniosku': row['data_przyjecia_wniosku']
            })

# Otwarcie pliku CSV i zapisanie danych
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=wniosek)
    writer.writeheader()

    for i in range(1, ilosc_wnioskow + 1):
        # Generowanie losowych danych
        random_date_data = random.choice(dates)
        czas_oczekiwania = random.randint(0, 600)

        pierwsza_godzina_zeskanowania = f"{random.randint(8, 15):02d}:{random.randint(0, 59):02d}"

        # Losowy czas dodawany do wniosek[6] i wniosek[7]
        losowy_czas_wniosek_6 = random.randint(2, 10)
        losowy_czas_wniosek_7 = random.randint(2, 10)

        # Obliczenie czasu w formacie "00:00:00" po dodaniu do wniosek[5]
        czas_wniosek_5 = datetime.strptime(pierwsza_godzina_zeskanowania, "%H:%M")
        czas_wniosek_6 = czas_wniosek_5 + timedelta(minutes=losowy_czas_wniosek_6)
        czas_wniosek_7 = czas_wniosek_5 + timedelta(minutes=losowy_czas_wniosek_6 + losowy_czas_wniosek_7)


        if random.randint(1, 10) <= 3:
            wniosek_7 = None
        else:
            wniosek_7 = czas_wniosek_5 + timedelta(minutes=losowy_czas_wniosek_6 + losowy_czas_wniosek_7)

        if wniosek_7 is not None:
            formatted_time = wniosek_7.strftime("%H:%M:%S")
        else:
            formatted_time = 'null'


        fake_data = {
            wniosek[0]: i,
            wniosek[1]: i,
            wniosek[2]: random.choice(typy_dokumentow),
            wniosek[3]: random_date_data['id_daty_pk'],
            wniosek[4]: random.choices(stany_wnioskow, prawdopodobienstwa)[0],
            wniosek[5]: czas_wniosek_5.strftime("%H:%M:%S"),
            wniosek[6]: czas_wniosek_6.strftime("%H:%M:%S"),
            wniosek[7]: formatted_time
        }

        # Zapisanie danych do pliku CSV
        writer.writerow(fake_data)
