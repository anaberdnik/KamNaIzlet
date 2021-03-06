import csv


PARAM_FMT = ":{}" # za SQLite
# PARAM_FMT = "%s({})" # za PostgreSQL/MySQL


class Tabela:
    """
    Razred, ki predstavlja tabelo v bazi.
    Polja razreda:
    - ime: ime tabele
    - podatki: ime datoteke s podatki ali None
    """
    ime = None
    podatki = None

    def __init__(self, conn):
        """
        Konstruktor razreda.
        """
        self.conn = conn

    def ustvari(self):
        """
        Metoda za ustvarjanje tabele.
        Podrazredi morajo povoziti to metodo.
        """
        raise NotImplementedError

    def izbrisi(self):
        """
        Metoda za brisanje tabele.
        """
        self.conn.execute(f"DROP TABLE IF EXISTS {self.ime};")

    def uvozi(self):
        """
        Metoda za uvoz podatkov.
        Argumenti:
        - encoding: kodiranje znakov
        """
        if self.podatki is None:
            return
        with open(self.podatki, encoding = 'utf-8') as datoteka:
            podatki = csv.reader(datoteka, delimiter=";")
            stolpci = next(podatki)
            for vrstica in podatki:
                vrstica = {k: None if v == "" else v for k, v in zip(stolpci, vrstica)}
                self.dodaj_vrstico(**vrstica)

    def izprazni(self):
        """
        Metoda za praznjenje tabele.
        """
        self.conn.execute(f"DELETE FROM {self.ime};")

    def dodajanje(self, stolpci=None):
        """
        Metoda za gradnjo poizvedbe.
        Argumenti:
        - stolpci: seznam stolpcev
        """
        return f"""
            INSERT INTO {self.ime} ({", ".join(stolpci)})
            VALUES ({", ".join(PARAM_FMT.format(s) for s in stolpci)});
        """

    def dodaj_vrstico(self, **podatki):
        """
        Metoda za dodajanje vrstice.
        Argumenti:
        - poimenovani parametri: vrednosti v ustreznih stolpcih
        """
        podatki = {kljuc: vrednost for kljuc, vrednost in podatki.items()
                   if vrednost is not None}
        poizvedba = self.dodajanje(podatki.keys())
        cur = self.conn.execute(poizvedba, podatki)
        return cur.lastrowid

    
class Lokacija(Tabela):
    """
    Tabela vseh lokacij.
    """
    ime = "lokacija"
    podatki = "podatki/lokacija.csv"

    def ustvari(self):
        """
        Ustvari tabelo lokacija.
        """
        self.conn.execute("""
            CREATE TABLE lokacija (
                id           INTEGER PRIMARY KEY AUTOINCREMENT,
                naziv        TEXT UNIQUE NOT NULL,
                regija       TEXT CHECK (regija IN ('Pomurska', 'Podravska',
                       'Koro??ka', 'Savinjska', 'Posavska', 'Zasavska',
                       'Osrednjeslovenska', 'Gorenjska', 'Gori??ka',
                       'Obalno-kra??ka', 'Primorsko-notranjska', 
                       'Jugovzhodna-Slovenija')),
                opis         TEXT NOT NULL,
                url          TEXT,
                pogostitev   TEXT CHECK (pogostitev IN ('Da', 'Ne')),
                preno??i????e   TEXT CHECK (preno??i????e IN ('Da', 'Ne')),
                vstopnina    TEXT CHECK (vstopnina IN ('Da', 'Ne')),
                zaOtroke    TEXT CHECK (zaOtroke IN ('Da', 'Ne')),
                urlSlike   TEXT    DEFAULT ('https://www.ekoskladovnica.si/Content/images/ni_slike.jpg') 
            );
        """)


class ??as(Tabela):
    """
    Tabela za ??as obiska.
    """
    ime = "??as"
    podatki = "podatki/??as.csv"

    def ustvari(self):
        """
        Ustvari tabelo ??as.
        """
        self.conn.execute("""
            CREATE TABLE ??as(
                lokacija  INTEGER REFERENCES lokacija (id),
                tip       TEXT CHECK (tip IN ('Poletni ??as', 'Zimski ??as', 'Slabo vreme')),
            
            PRIMARY KEY (
                lokacija,
                tip
            ),
            
            UNIQUE (
                lokacija,
                tip
            )
            );
        """)


class Vrsta(Tabela):
    """
    Tabela vseh vrst lokacij.
    """
    ime = "vrsta"

    def ustvari(self):
        """
        Ustvari tabelo vseh vrst.
        """
        self.conn.execute("""
            CREATE TABLE vrsta (
                id    INTEGER PRIMARY KEY AUTOINCREMENT,
                naziv TEXT UNIQUE
            );
        """)

    def dodaj_vrstico(self, **podatki):
        """
        Dodaj vrsto.
        ce vrsta ??e obstaja, vrne obstojeci ID.
        Argumenti:
        - poimenovani parametri: vrednosti v ustreznih stolpcih
        """
        assert "naziv" in podatki
        cur = self.conn.execute("""
            SELECT id FROM vrsta
            WHERE naziv = :naziv;
        """, podatki)
        r = cur.fetchone()
        if r is None:
            return super().dodaj_vrstico(**podatki)
        else:
            id, = r
            return id

class Namen(Tabela):
    """
    Tabela vseh namenov obiska lokacije.
    """
    ime = "namen"

    def ustvari(self):
        """
        Ustvari tabelo vseh namenov.
        """
        self.conn.execute("""
            CREATE TABLE namen (
                id    INTEGER PRIMARY KEY AUTOINCREMENT,
                naziv TEXT UNIQUE
            );
        """)

    def dodaj_vrstico(self, **podatki):
        """
        Dodaj namen.
        ce namen ??e obstaja, vrne obstojeci ID.
        Argumenti:
        - poimenovani parametri: vrednosti v ustreznih stolpcih
        """
        assert "naziv" in podatki
        cur = self.conn.execute("""
            SELECT id FROM namen
            WHERE naziv = :naziv;
        """, podatki)
        r = cur.fetchone()
        if r is None:
            return super().dodaj_vrstico(**podatki)
        else:
            id, = r
            return id

class PripadaVrsta(Tabela):
    """
    Tabela za relacijo med lokacijo in vrsto lokacije.
    """
    ime = "pripadaVrsta"
    podatki = "podatki/vrsta.csv"

    def __init__(self, conn, Vrsta):
        """
        Konstruktor tabele pripadnosti ??anrom.
        Argumenti:
        - conn: povezava na bazo
        - vrsta: tabela vseh vrst
        """
        super().__init__(conn)
        self.vrsta = Vrsta

    def ustvari(self):
        """
        Ustvari tabelo pripadaVrsta.
        """
        self.conn.execute("""
            CREATE TABLE pripadaVrsta (
                lokacija INTEGER REFERENCES lokacija (id),
                vrsta INTEGER REFERENCES vrsta (id),
                PRIMARY KEY (lokacija, vrsta)
            );
        """)

    def dodaj_vrstico(self, **podatki):
        """
        Dodaj pripadnost lokacije in pripadajoce vrste.
        Argumenti:
        - podatki: slovar s podatki o pripadnosti
        """
        if podatki.get("naziv", None) is not None:
            podatki["vrsta"] = self.vrsta.dodaj_vrstico(naziv=podatki["naziv"])
            del podatki["naziv"]
        return super().dodaj_vrstico(**podatki)

class PripadaNamen(Tabela):
    """
    Tabela za relacijo med lokacijo in namenom.
    """
    ime = "pripadaNamen"
    podatki = "podatki/namen.csv"

    def __init__(self, conn, Namen):
        """
        Konstruktor tabele pripadnosti namenu.
        Argumenti:
        - conn: povezava na bazo
        - namen: tabela vseh namenom
        """
        super().__init__(conn)
        self.namen = Namen

    def ustvari(self):
        """
        Ustvari tabelo vseh namen.
        """
        self.conn.execute("""
            CREATE TABLE pripadaNamen (
                lokacija INTEGER REFERENCES lokacija (id),
                namen INTEGER REFERENCES namen (id),
                PRIMARY KEY (lokacija, namen)
            );
        """)

    def dodaj_vrstico(self, **podatki):
        """
        Dodaj pripadnost lokacije in pripadajoci namen.
        Argumenti:
        - podatki: slovar s podatki o pripadnosti
        """
        if podatki.get("naziv", None) is not None:
            podatki["namen"] = self.namen.dodaj_vrstico(naziv=podatki["naziv"])
            del podatki["naziv"]
        return super().dodaj_vrstico(**podatki)



def ustvari_tabele(tabele):
    """
    Ustvari podane tabele.
    """
    for t in tabele:
        t.ustvari()


def izbrisi_tabele(tabele):
    """
    Izbri??i podane tabele.
    """
    for t in tabele:
        t.izbrisi()


def uvozi_podatke(tabele):
    """
    Uvozi podatke v podane tabele.
    """
    for t in tabele:
        t.uvozi()


def izprazni_tabele(tabele):
    """
    Izprazni podane tabele.
    """
    for t in tabele:
        t.izprazni()


def ustvari_bazo(conn):
    """
    Izvede ustvarjanje baze.
    """
    tabele = pripravi_tabele(conn)
    izbrisi_tabele(tabele)
    ustvari_tabele(tabele)
    uvozi_podatke(tabele)


def pripravi_tabele(conn):
    """
    Pripravi objekte za tabele.
    """
    lokacija = Lokacija(conn)
    ??as = ??as(conn)
    vrsta = Vrsta(conn)
    namen = Namen(conn)
    pripadaVrsta = PripadaVrsta(conn, vrsta)
    pripadaNamen = PripadaNamen(conn, namen)

    return [lokacija, ??as, vrsta, namen, pripadaVrsta, pripadaNamen]

def ustvari_bazo_ce_ne_obstaja(conn):
    """
    Ustvari bazo, ce ta ??e ne obstaja.
    """
    with conn:
        cur = conn.execute("SELECT COUNT(*) FROM sqlite_master")
        if cur.fetchone() == (0, ):
            ustvari_bazo(conn)

