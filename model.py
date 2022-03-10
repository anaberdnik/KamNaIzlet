import baza
import sqlite3
from sqlite3 import IntegrityError
from pomozne_funkcije import Seznam
from geslo import sifriraj_geslo, preveri_geslo

conn = sqlite3.connect('KamNaIzlet.db')
baza.ustvari_bazo_ce_ne_obstaja(conn)
conn.execute('PRAGMA foreign_keys = ON')

uporabnik, lokacija, cas, vrsta, namen, pripadaVrsta, pripadaNamen = baza.pripravi_tabele(conn)

class LoginError(Exception):
    """
    Napaka ob napacnem uporabniškem imenu ali geslu.
    """
    pass

class Uporabnik:
    """
    Razred za uporabnika.
    """

    def __init__(self, ime, *, id=None):
        """
        Konstruktor uporabnika.
        """
        self.id = id
        self.ime = ime

    def __str__(self):
        """
        Znakovna predstavitev uporabnika.
        Vrne uporabniško ime.
        """
        return self.ime

    @staticmethod
    def prijava(ime, geslo):
        """
        Preveri, ali sta uporabniško ime geslo pravilna.
        """
        sql = """
            SELECT id, zgostitev, sol FROM uporabnik
            WHERE ime = ?
        """
        try:
            id, zgostitev, sol = conn.execute(sql, [ime]).fetchone()
            if preveri_geslo(geslo, zgostitev, sol):
                return Uporabnik(ime, id=id)
        except TypeError:
            pass
        raise LoginError(ime)

    def dodaj_v_bazo(self, geslo):
        """
        V bazo doda uporabnika s podanim geslom.
        """
        assert self.id is None
        zgostitev, sol = sifriraj_geslo(geslo)
        try:
            with conn:
                self.id = uporabnik.dodaj_vrstico(ime=self.ime, zgostitev=zgostitev, sol=sol)
        except IntegrityError:
            raise LoginError(self.ime)

class Lokacija:
    """
    Razred za lokacijo.
    """

    def __init__(self, naziv, regija, opis, url, pogostitev, prenocišce, vstopnina, zaOtroke, id=None):
        """
        Konstruktor filma.
        """
        self.id = id
        self.naziv = naziv
        self.regija = regija
        self.opis = opis
        self.url = url
        self.pogostitev = pogostitev
        self.prenocišce = prenocišce
        self.vstopnina = vstopnina
        self.zaOtroke = zaOtroke

    def __str__(self):
        """
        Znakovna predstavitev filma.
        Vrne naslov filma.
        """
        return self.naziv
    
    @staticmethod
    def lokacije_v_regiji(regija):
        """
        Vrne vse lokacije dane regije.
        """
        sql = """
            SELECT naziv, url
            FROM lokacija
            WHERE regija = ? 
        """
        for naslov, url in conn.execute(sql, [regija]):
            yield Lokacija(naslov, url)


def poisci_lokacije(niz):
    '''
    Funkcija vrne id-je vseh filmov, katerih naziv vsebuje dani niz.
    '''
    
    poizvedba = """
        SELECT id
        FROM lokacija
        WHERE naziv like ?
    """
    idji_lokacij = []
    for(id_lokacije,) in conn.execute(poizvedba, ['%' + niz + '%']):
        idji_lokacij.append(id_lokacije)
    return idji_lokacij
        
def podatki_lokacij(idji_lokacij):
    """
    Funkcija vrne osnovne podatke vseh lokacij z danimi IDji.
    """
    poizvedba = """
        SELECT id, naziv, regija
        FROM lokacija
        WHERE id IN ({})
    """.format(', '.join('?' for _ in range(len(idji_lokacij))))
    return conn.execute(poizvedba, idji_lokacij).fetchall()

def podatki_lokacije(id_lokacije):
    """
    Funkcija vrne podatke o lokaciji z danim IDjem.
    """
    poizvedba = """
    SELECT naziv, regija, url
    FROM lokacija
    WHERE id = ?
    """
    
    osnovni_podatki = conn.execute(poizvedba, [id_lokacije]).fetchone()
    if osnovni_podatki is None:
        return None
    else:
        naziv, regija, url = osnovni_podatki
    return naziv, regija, url
        