import faker  # Biblioteka do generowania fałszywych danych
from datetime import datetime, timedelta
import calendar
import locale  # Moduł do obsługi lokalizacji

# Ustawienie lokalizacji na polską
locale.setlocale(locale.LC_TIME, 'pl_PL.UTF-8')

ile_lat_wstecz = 3  # Ile lat wstecz generować daty
ile_lat_do_przodu = 1
fake = faker.Faker()
current_year = datetime.now().year

def wygenerujDaty(start_index):
    data = ['data_przyjecia_wniosku', 'czy_wakacje', 'czy_wolne', 'dzien_tygodnia', 'dzien_tygodnia_numer', 'czy_weekend',
            'pora_roku', 'rok', 'miesiac', 'miesiac_numer']
    sql_script = 'INSERT INTO data ({}) VALUES\n'.format(', '.join(data))

    ilosc_dat = 365 * (ile_lat_wstecz + ile_lat_do_przodu)
    koniec_index = ilosc_dat + 1

    for i in range(start_index, koniec_index):
        start_date = datetime.now() - timedelta(days=(ile_lat_wstecz*365) - i)

        czy_wakacje = 'tak_wakacje' if start_date.month in [6, 7, 8] else 'nie_wakacje'
        czy_wolne = 'tak_wolne' if start_date.weekday() in [5, 6] else 'nie_wolne'
        dzien_tygodnia = calendar.day_name[start_date.weekday()]
        dzien_tygodnia_numer = start_date.weekday() + 1  # Dni tygodnia numerowane od 1 do 7
        czy_weekend = 'tak_weekend' if start_date.weekday() in [4, 5] else 'nie_weekend'

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

        rok = start_date.year
        miesiac = start_date.strftime('%B')  # Pełna nazwa miesiąca
        miesiac_numer = start_date.month

        # Generowanie skryptu SQL
        fake_data = {
            data[0]: start_date.strftime('%Y-%m-%d'),
            data[1]: czy_wakacje,
            data[2]: czy_wolne,
            data[3]: dzien_tygodnia,
            data[4]: dzien_tygodnia_numer,
            data[5]: czy_weekend,
            data[6]: pora_roku,
            data[7]: rok,
            data[8]: miesiac,
            data[9]: miesiac_numer
        }
        values = ', '.join(["'{}'".format(value) for value in fake_data.values()])
        sql_script += '({}),\n'.format(values)

    # Usuwanie ostatniej przecinki i dodanie średnika
    sql_script = sql_script.rstrip(',\n') + ';'

    # Zapisywanie skryptu SQL do pliku
    filename = 'daty.sql'
    with open(filename, 'w') as sql_file:
        sql_file.write(sql_script)


def okres_dnia(godzina):
    if 5 <= godzina < 9:
        return "rano"
    elif 9 <= godzina < 11:
        return "przedpoludnie"
    elif 11 <= godzina < 13:
        return "poludnie"
    elif 13 <= godzina < 17:
        return "popoludnie"
    elif 17 <= godzina < 21:
        return "wieczor"
    else:
        return None

# Funkcja generująca skrypt SQL z insertami
def generuj_sql():
    with open("godzina.sql", "w") as file:
        for godzina in range(5, 22):
            for minuta in range(0, 60):
                # Zmiana formatu godziny
                data = datetime.time(godzina, minuta).strftime("%H:%M")
                okres = okres_dnia(godzina)
                if okres:
                    insert_statement = f"INSERT INTO godzina (godzina, pora_dnia) VALUES ('{data}', '{okres}');\n"
                    file.write(insert_statement)


if __name__ == "__main__":
    wygenerujDaty(1)
