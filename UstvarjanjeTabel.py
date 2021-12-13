import sqlite3

conn = sqlite3.connect('KamNaIzet.db')

cur = conn.cursor()
with conn:
    cur.execute("""
        CREATE TABLE lokacija (
            id	         INTEGER PRIMARY KEY AUTOINCREMENT,
            naziv        TEXT UNIQUE NOT NULL,
            regija       TEXT CHECK (regija IN ('Pomurska', 'Podravska',
                   'Koroška', 'Savinjska', 'Posavska', 'Zasavska',
                   'Osrednjeslovenska', 'Gorenjska', 'Goriška',
                   'Obalno-kraška', 'Pomursko-notranjska', 
                   'Jugovzhodna-Slovenija')),
            opis         TEXT NOT NULL,
            url          TEXT,
            pogostitev   TEXT CHECK (pogostitev IN ('Da', 'Ne')),
            prenočišče   TEXT CHECK (prenočišče IN ('Da', 'Ne')),
            vstopnina    TEXT CHECK (vstopnina IN ('Da', 'Ne')),
            za_otroke    TEXT CHECK (za_otroke IN ('Da', 'Ne'))
        );
        """)

    cur.execute("""
        CREATE TABLE namen(
            id 	     INTEGER PRIMARY KEY AUTOINCREMENT,
            naziv    TEXT UNIQUE NOT NULL
        );
    """)
    cur.execute(""" 
        CREATE TABLE čas(
            id 	     INTEGER PRIMARY KEY AUTOINCREMENT,
            naziv    TEXT UNIQUE NOT NULL
        );
    """)
    cur.execute("""
        CREATE TABLE vrsta(
            id 	     INTEGER PRIMARY KEY AUTOINCREMENT,
            naziv    TEXT UNIQUE NOT NULL
        );
    """)

    cur.execute("""
        CREATE TABLE kdajObiskati(
            lokacija    INTEGER REFERENCES lokacija(id),
            čas         INTEGER REFERENCES čas(id),
            PRIMARY KEY (lokacija, čas)
        );
    """)

    cur.execute("""
        CREATE TABLE kajSiŽelimo(
            lokacija    INTEGER REFERENCES lokacija(id),
            namen       INTEGER REFERENCES namen(id),
            PRIMARY KEY (lokacija, namen)
        );
    """)
    
    cur.execute("""
        CREATE TABLE kajNasZanima(
            lokacija    INTEGER REFERENCES lokacija(id),
            vrsta       INTEGER REFERENCES vrsta(id),
            PRIMARY KEY (lokacija, vrsta)
        );
    """)


    cur.execute("""
     INSERT INTO čas (naziv) VALUES ('Poletni čas');
     """)

    cur.execute("""
     INSERT INTO čas (naziv) VALUES ('Zimski čas');
     """)
    
    cur.execute("""
    INSERT INTO čas (naziv) VALUES ('Slabo vreme')
    """)

    cur.execute("""
     INSERT INTO vrsta (naziv) VALUES ('Gorovja in hribovja');
     """)

    cur.execute("""
     INSERT INTO vrsta (naziv) VALUES ('Kopališča in terme');
     """)
    
    cur.execute("""
    INSERT INTO vrsta (naziv) VALUES ('Muzeji')
    """)

    cur.execute("""
    INSERT INTO vrsta (naziv) VALUES ('Znamenitosti')
    """)
    
    cur.execute("""
    INSERT INTO vrsta (naziv) VALUES ('Gradovi')
    """)

    cur.execute("""
    INSERT INTO vrsta (naziv) VALUES ('Jezera')
    """)

    cur.execute("""
    INSERT INTO vrsta (naziv) VALUES ('Smučišča')
    """)

    cur.execute("""
    INSERT INTO vrsta (naziv) VALUES ('Atraktivni kotički')
    """)

    cur.execute("""
     INSERT INTO namen (naziv) VALUES ('Pohodništvo');
     """)

    cur.execute("""
     INSERT INTO namen (naziv) VALUES ('Rekreacija');
     """)
    
    cur.execute("""
     INSERT INTO namen (naziv) VALUES ('Ogled znameni');
     """)

    cur.execute("""
     INSERT INTO namen (naziv) VALUES ('Zabava');
     """)

    cur.execute("""
     INSERT INTO namen (naziv) VALUES ('Sprostitev');
     """)
    
    cur.execute("""
     INSERT INTO namen (naziv) VALUES ('Oddih v naravi');
     """)

    cur.execute("""
     INSERT INTO namen (naziv) VALUES ('Izobraževanje');
     """)




    
