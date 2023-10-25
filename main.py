import csv
import random
import faker  # Biblioteka do generowania fałszywych danych

# Inicjalizacja generatora fałszywych danych
fake = faker.Faker()

# Struktura tabeli users
# Możesz dostosować ją do swoich potrzeb
fields = ['id', 'username', 'email', 'age']

# Ilość wierszy do wygenerowania
num_rows = 100

# Nazwa pliku CSV
csv_file = 'fake_data.csv'

# Otwieramy plik CSV do zapisu
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    # Tworzenie nagłówków kolumn
    writer.writeheader()

    # Generowanie nieprawdziwych danych i zapis do pliku
    for i in range(1, num_rows + 1):
        fake_data = {
            'id': i,
            'username': fake.user_name(),
            'email': fake.email(),
            'age': random.randint(18, 65)
        }
        writer.writerow(fake_data)

print(f'Wygenerowano {num_rows} wierszy danych i zapisano je w pliku {csv_file}')
