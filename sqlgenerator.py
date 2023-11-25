import datetime

# Funkcja do określania pory dnia na podstawie godziny
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
    with open("inserts.sql", "w") as file:
        for godzina in range(5, 22):
            for minuta in range(0, 60):
                # Zmiana formatu godziny
                data = datetime.time(godzina, minuta).strftime("%H:%M")
                okres = okres_dnia(godzina)
                if okres:
                    insert_statement = f"INSERT INTO godzina (godzina, pora_dnia) VALUES ('{data}', '{okres}');\n"
                    file.write(insert_statement)

if __name__ == "__main__":
    generuj_sql()
