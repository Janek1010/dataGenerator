import csv
import faker  # Biblioteka do generowania fałszywych danych
from datetime import datetime, timedelta
import random

# Inicjalizacja generatora fałszywych danych
fake = faker.Faker()

# Bieżący rok
current_year = 2023

# Struktura tabeli users
# Możesz dostosować ją do swoich potrzeb
fields = ['id_pracownika_pk', 'data_urodzenia', 'data_zatrudnienia']

# Ilość wierszy do wygenerowania
num_rows = 100

# Nazwa pliku CSV
csv_file = 'pracownicy.csv'

# Otwieramy plik CSV do zapisu
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    # Tworzenie nagłówków kolumn
    writer.writeheader()

    # Generowanie nieprawdziwych danych i zapis do pliku
    for i in range(1, num_rows + 1):
        birth_date = fake.date_of_birth(minimum_age=18, maximum_age=65)
        # Generowanie losowej różnicy wieku między 20 a 40 lat
        age_difference = random.randint(20, 40)
        hire_date = birth_date + timedelta(days=365 * age_difference)

        # Sprawdzenie, czy data zatrudnienia przekracza bieżący rok
        if hire_date.year > current_year:
            hire_date = datetime(current_year, 12, 31)

        fake_data = {
            'id_pracownika_pk': i,
            'data_urodzenia': birth_date.strftime('%Y-%m-%d'),
            'data_zatrudnienia': hire_date.strftime('%Y-%m-%d'),
        }
        writer.writerow(fake_data)

print(f'Wygenerowano {num_rows} wierszy danych i zapisano je w pliku {csv_file}')
