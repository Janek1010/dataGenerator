use lab_4
go

drop table if exists przyjecie_wniosku;
drop table if exists wniosek;
drop table if exists data;
drop table if exists pracownik;
drop table if exists stanowisko_kasowe;
drop table if exists godzina;


create table data (
	id_daty_pk numeric primary key,
	data_przyjecia_wniosku date,
	czy_wakacje varchar(10) CHECK (czy_wakacje IN('tak', 'nie')),
	czy_wolne varchar(10) CHECK (czy_wolne IN('tak', 'nie')),
	dzien_tygodnia varchar(15) CHECK (dzien_tygodnia IN('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')),
	czy_weekend varchar(5) CHECK (czy_weekend IN('tak', 'nie')),
	pora_roku varchar(10) CHECK (pora_roku IN('wiosna', 'lato', 'jesien', 'zima'))
)

create table stanowisko_kasowe (
	id_stanowiska_pk numeric primary key,
	numer_kasy varchar(25),

)

create table wniosek (
	id_wniosku_pk numeric primary key,
	typ_wnioskowanego_dokumentu varchar(20) CHECK (typ_wnioskowanego_dokumentu IN('paszport', 'dowod_osobity', 'prawo_jazdy')),
	stan_wniosku varchar(20) CHECK (stan_wniosku IN('odrzucony', 'zaakceptowany', 'tworzony', 'oczekuje_na_odbior', 'zakonczony')),
	czy_z_domu varchar(15)
)

create table pracownik (
	id_pracownika_pk numeric primary key,
	wiek varchar(10),
	staz_pracy varchar(10),
	imie_nazwisko varchar (60),
	plec varchar(10),
	szef numeric,
	edukacja varchar(20),
	aktualnosc bit,

	FOREIGN KEY (szef) REFERENCES pracownik (id_pracownika_pk)
)

create table godzina (
	id_godziny_pk numeric primary key,
	godzina varchar(10),
	pora_dnia varchar(20)
)

create table przyjecie_wniosku (
	numer_przyjecia_wniosku numeric primary key IDENTITY(1,1),
	id_daty_fk numeric,
	godzina_pobrania_numerka_fk numeric,
	godzina_zeskanowania_wniosku_przy_okienku numeric,
	druga_godzina_zeskanowania numeric,
	id_wniosku_fk numeric,
	id_stanowiska_fk numeric,
	id_pracownika_fk numeric,
	wiek_pracownika numeric,
	staz_pracy_pracownika numeric,
	czas_obslugi numeric

	FOREIGN KEY (id_wniosku_fk) REFERENCES wniosek (id_wniosku_pk),
	FOREIGN KEY (id_daty_fk) REFERENCES data (id_daty_pk),
	FOREIGN KEY (godzina_pobrania_numerka_fk) REFERENCES godzina (id_godziny_pk),
	FOREIGN KEY (godzina_zeskanowania_wniosku_przy_okienku) REFERENCES godzina (id_godziny_pk),
	FOREIGN KEY (druga_godzina_zeskanowania) REFERENCES godzina (id_godziny_pk),
	FOREIGN KEY (id_stanowiska_fk) REFERENCES stanowisko_kasowe (id_stanowiska_pk),
	FOREIGN KEY (id_pracownika_fk) REFERENCES pracownik (id_pracownika_pk)
)



select * from wniosek;
select * from data;
select * from pracownik;
select * from stanowisko_kasowe;
select * from godzina;
select * from przyjecie_wniosku;