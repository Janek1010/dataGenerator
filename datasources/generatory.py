import csv
import faker  # Biblioteka do generowania fałszywych danych
from datetime import datetime, timedelta
import random
import calendar
import pandas as pd
import numpy as np
import shutil

ilosc_pracownikow = 50;
ilosc_szefow = 5;
ilosc_kas = 10
ilosc_obslug = 100
ilosc_wnioskow = ilosc_obslug

ile_lat = 3  # Ile lat wstecz generować daty
ile_nowych_lat = 1
fake = faker.Faker()
current_year = 2023

# nowy wniosek ma przyjmowac tlyko nowe daty
# generowanie daty2.csv od teraz do jakiegos okresu w przyszlosci
# zmiana stanu wniosku
def wygenerujPracownikowAll():
    wygenerujPracownikowExcel(1, 1, 'pracownicyExcel')
    wygenerujPracownikowExcel(ilosc_pracownikow + 1, 0.3, 'pracownicyExcel2')
    shutil.copy('pracownicyExcel.csv', 'pracownicyExcelTEMP.csv')
    wygenerujUpdatePracownikow('pracownicyExcelTEMP.csv')

    polacz_pliki_csv('pracownicyExcelTEMP.csv', 'pracownicyExcel2.csv', 'pracownicyExcel2.csv')


def wygenerujPracownikowExcel(start_index, procent_rekordow, csv_name):
    pracownicyExcel = ['id_pracownika_pk','imie_pracownika','Nazwisko_pracownika', 'data_zatrudnienia', 'data_urodzenia', 'Plec',
                       'pesel','szef','edukacja']
    csv_file = csv_name + '.csv'
    typy_edukacji = ['podstawowe', 'srednie', 'wyzsze']
    prawdopodobienstwa = [0.25, 0.4, 0.35]
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=pracownicyExcel)
        writer.writeheader()
        for i in range(start_index, int(start_index + (ilosc_pracownikow * procent_rekordow))):

            birth_date = fake.date_of_birth(minimum_age=18, maximum_age=65)
            age_difference = random.randint(20, 40)
            hire_date = birth_date + timedelta(days=365 * age_difference)

            if hire_date.year > current_year:
                hire_date = datetime(current_year, 12, 31)

            if ilosc_szefow >= i:
                szef = '-1'
            else:
                szef = random.randint(1, ilosc_szefow)

            fake_data = {
                pracownicyExcel[0]: i,
                pracownicyExcel[1]: fake.first_name(),
                pracownicyExcel[2]: fake.last_name(),
                pracownicyExcel[3]: hire_date.strftime('%Y-%m-%d'),
                pracownicyExcel[4]: birth_date.strftime('%Y-%m-%d'),
                pracownicyExcel[5]: fake.random_element(elements=['M', 'F']),
                pracownicyExcel[6]: fake.unique.random_int(min=10000000000, max=99999999999),
                pracownicyExcel[7]: szef,
                pracownicyExcel[8]: random.choices(typy_edukacji, prawdopodobienstwa)[0], # edukacja
            }
            writer.writerow(fake_data)

def wygenerujUpdatePracownikow(csv_name):
    nazwakolumny = "edukacja"
    df = pd.read_csv(csv_name)
    def generuj_zmiane(edukacja):
        if edukacja == 'podstawowe':
            return np.random.choice(['srednie', 'wyzsze','podstawowe'], p=[0.1, 0.1, 0.8])
        elif edukacja == 'srednie':
            return 'wyzsze' if np.random.rand() < 0.3 else 'srednie'
        else:
            return 'wyzsze'
    df[nazwakolumny] = df[nazwakolumny].apply(generuj_zmiane)

    df.to_csv(csv_name, index=False)





def wygenerujPracownikow(nazwa_wejsciowego_pliku, nazwa_wyjsciowego_pliku):
    with open(nazwa_wejsciowego_pliku, 'r', newline='') as plik_wejsciowy, open(nazwa_wyjsciowego_pliku, 'w', newline='') as plik_wyjsciowy:
        czytnik_csv = csv.DictReader(plik_wejsciowy)
        pola_wyjsciowe = ['id_pracownika_pk', 'data_urodzenia', 'data_zatrudnienia']

        pisarz_csv = csv.DictWriter(plik_wyjsciowy, fieldnames=pola_wyjsciowe)
        pisarz_csv.writeheader()

        for wiersz in czytnik_csv:
            nowy_wiersz = {
                'id_pracownika_pk': wiersz['id_pracownika_pk'],
                'data_urodzenia': wiersz['data_urodzenia'],
                'data_zatrudnienia': wiersz['data_zatrudnienia']
            }
            pisarz_csv.writerow(nowy_wiersz)


def wygenerujKasy(start_index, procent_rekordow, csv_name):
    stanowisko_kasowe = ['id_kasy_pk', 'numer_kasy']
    csv_file = csv_name + '.csv'

    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=stanowisko_kasowe)
        writer.writeheader()

        for i in range(start_index, int(start_index + (ilosc_kas * procent_rekordow))):
            fake_data = {
                stanowisko_kasowe[0]: i,
                stanowisko_kasowe[1]: i,
            }
            writer.writerow(fake_data)

def polacz_pliki_csv(plik1, plik2, plik_wyjsciowy):
    df1 = pd.read_csv(plik1)
    df2 = pd.read_csv(plik2)

    # Połącz obie ramki danych
    df_połaczony = pd.concat([df1, df2], ignore_index=True)

    # Zapisz połączony DataFrame do nowego pliku CSV
    df_połaczony.to_csv(plik_wyjsciowy, index=False)

def wygenerujObslugi(start_index, procent_rekordow, csv_name):
    obsluga = ['id_pk', 'id_wniosku_fk', 'id_pracownika_fk', 'id_stanowiska_fk']
    csv_file = csv_name + '.csv'

    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=obsluga)
        writer.writeheader()

        for i in range(start_index, int(start_index + (ilosc_obslug * procent_rekordow))):
            fake_data = {
                obsluga[0]: i,
                obsluga[1]: i,
                obsluga[2]: random.randint(1, ilosc_pracownikow),
                obsluga[3]: random.randint(1, ilosc_kas),
            }
            writer.writerow(fake_data)


def wygenerujDaty(start_index, czy_nowe):
    data = ['id_daty_pk', 'data_przyjecia_wniosku', 'czy_wakacje', 'czy_wolne', 'dzien_tygodnia', 'czy_weekend',
            'pora_roku']
    csv_file = 'data.csv'
    if czy_nowe:
        csv_file = 'data2.csv'

    ilosc_dat = 365 * ile_lat
    if czy_nowe:
        ilosc_dat = 365 * ile_nowych_lat
    # Otwarcie pliku CSV i zapisanie danych
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data)
        writer.writeheader()

        koniec_index = ilosc_dat + 1
        if czy_nowe:
            koniec_index = koniec_index + start_index

        for i in range(start_index, koniec_index):
            # Obliczenie daty na podstawie indeksu i liczby dni wstecz
            start_date = datetime.now() - timedelta(days=ilosc_dat - i)
            if czy_nowe:
                start_date = datetime.now() + timedelta(days=365 - (ilosc_dat - i))

            # Sprawdzenie, czy jest wakacje
            if start_date.month in [6, 7, 8]:
                czy_wakacje = 'tak_wakacje'
            else:
                czy_wakacje = 'nie_wakacje'

            # Sprawdzenie, czy jest dzień wolny
            if start_date.weekday() in [5, 6]:
                czy_wolne = 'tak_wolne'
            else:
                czy_wolne = 'nie_wolne'

            # Określenie dnia tygodnia
            dzien_tygodnia = calendar.day_name[start_date.weekday()]

            # Sprawdzenie, czy to weekend
            if start_date.weekday() in [4, 5]:
                czy_weekend = 'tak_weekend'
            else:
                czy_weekend = 'nie_weekend'

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


def wygenerujWnioski(start_index, procent_rekordow, csv_name, csv_daty):
    wniosek = ['id_wniosku_pk', 'id_obslugi_fk', 'id_daty_fk', 'typ_wnioskowanego_dokumentu', 'stan_wniosku',
               'godzina_pobrania_numerka', 'godzina_zeskanowania_wniosku_przy_okienku',
               'druga_godzina_zeskanowania']
    typy_dokumentow = ['paszport', 'dowod_osobisty', 'prawo_jazdy']
    stany_wnioskow = ['odrzucony', 'zaakceptowany', 'tworzony', 'Oczekuje_na_odbior', 'zakonczony']
    prawdopodobienstwa = [0.05, 0.35, 0.15, 0.1, 0.35]
    csv_file = csv_name + '.csv'

    dates = []
    with open(csv_daty, 'r') as datafile:
        datareader = csv.DictReader(datafile)
        for row in datareader:
            if row['czy_wolne'] == 'nie_wolne' or row['czy_weekend'] == 'nie_weekend':
                dates.append({
                    'id_daty_pk': row['id_daty_pk'],
                    'data_przyjecia_wniosku': row['data_przyjecia_wniosku']
                })

    # Otwarcie pliku CSV i zapisanie danych
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=wniosek)
        writer.writeheader()

        for i in range(start_index, int(start_index + (ilosc_wnioskow * procent_rekordow))):
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

            if random.randint(1, 10) <= 3:
                wniosek_7 = None
            else:
                wniosek_7 = czas_wniosek_5 + timedelta(minutes=losowy_czas_wniosek_6 + losowy_czas_wniosek_7)

            if wniosek_7 is not None:
                formatted_time = wniosek_7.strftime("%H:%M:%S")
            else:
                formatted_time = ''

            fake_data = {
                wniosek[0]: i,
                wniosek[1]: i,
                wniosek[2]: random_date_data['id_daty_pk'],
                wniosek[3]: random.choice(typy_dokumentow),
                wniosek[4]: random.choices(stany_wnioskow, prawdopodobienstwa)[0],
                wniosek[5]: czas_wniosek_5.strftime("%H:%M:%S"),
                wniosek[6]: czas_wniosek_6.strftime("%H:%M:%S"),
                wniosek[7]: formatted_time
            }

            # Zapisanie danych do pliku CSV
            writer.writerow(fake_data)

def wygenerujUpdateWnioskow():
    wnioski = ["id_wniosku_pk", "stan_wniosku"]
    stany_wnioskow = ['odrzucony', 'zaakceptowany', 'tworzony', 'Oczekuje_na_odbior', 'zakonczony']
    prawdopodobienstwa = [0.05, 0.35, 0.15, 0.1, 0.35]

    id = []
    stan = []

    with open('wniosek.csv', 'r') as datafile:
        datareader = csv.DictReader(datafile)
        for row in datareader:
            id.append(row['id_wniosku_pk'])
            stan.append(row['stan_wniosku'])


    with open('wniosek3.csv', 'w',newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=wnioski)
        writer.writeheader()

        for i in range (len(id)):
            if stan[i] != 'zakonczony': #Jak wniosek juz zakonczony to nie ma co zmieniac
                nowy_stan = ''
                while True:
                    nowy_stan = random.choices(stany_wnioskow, prawdopodobienstwa)[0]

                    if (stany_wnioskow.index(stan[i]) < stany_wnioskow.index(nowy_stan)):   #Zeby sie wniosek nie cofnal do poprzeniego etapu
                        break

                stan[i] = nowy_stan


            fake_data = {
                wnioski[0]: id[i],
                wnioski[1]: stan[i]
            }
            writer.writerow(fake_data)

