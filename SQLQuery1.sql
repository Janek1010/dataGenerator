drop table if exists data;
drop table if exists pracownik;
drop table if exists stanowisko_kasowe;
drop table if exists wniosek;
drop table if exists obsluga;

create table pracownik (
	id_pracownika_pk int,
	id_obslugi_fk int,
	data_urodzenia date,
	data_zatrudnienia date,

	primary key(id_pracownika_pk)
)

create table stanowisko_kasowe (
	id_stanowiska_pk int,
	id_obslugi_fk int,
	numer_kasy smallint,

	primary key(id_stanowiska_pk)
)

create table data (
	id_daty_pk int not null,
	id_wniosku_fk int,
	data_przyjecia_wniosku date,
	czy_wakacje bit,
	czy_wolne bit,
	dzien_tygodnia varchar(15) CHECK (dzien_tygodnia IN('poniedzialek', 'wtorek', 'sroda', 'czwartek', 'piatek', 'sobota', 'niedziela')),
	pora_roku varchar CHECK (pora_roku IN('wiosna', 'lato', 'jesien', 'zima'))


	primary key (id_daty_pk),
)

create table wniosek (
	id_wniosku_pk int not null,
	id_obslugi_fk int,
	id_daty_fk int,
	typ_wnioskowanego_dokumentu varchar(20) CHECK (typ_wnioskowanego_dokumentu IN('paszport', 'dowod_osobity', 'prawo_jazdy')),
	stan_wniosku varchar(20) CHECK (stan_wniosku IN('odrzucony', 'zaakceptowany', 'tworzony', 'oczekuje_na_odbior', 'zakonczony')),
	godzina_pobrania_numerka datetime,
	godzina_zeskanowania_wniosku_przy_okienku datetime,
	druga_godzina_zeskanowania datetime,
	

	primary key (id_wniosku_pk),
	FOREIGN KEY (id_daty_fk) REFERENCES data (id_daty_pk)
)



create table obsluga (
	id_obslugi_pk int,
	id_wniosku_fk int,
	id_pracownika_fk int,
	id_stanowiska_fk int,

	primary key (id_obslugi_pk),
	FOREIGN KEY (id_wniosku_fk) REFERENCES wniosek (id_wniosku_pk),
	FOREIGN KEY (id_pracownika_fk) REFERENCES pracownik (id_pracownika_pk),
	FOREIGN KEY (id_stanowiska_fk) REFERENCES stanowisko_kasowe (id_stanowiska_pk)
)

select * from wniosek;
select * from data;
select * from obsluga;
select * from pracownik;
select * from stanowisko_kasowe;