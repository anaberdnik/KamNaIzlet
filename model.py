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



# ISKANJE LOKACIJE PO IMENU
def poisci_lokacije(niz):
    '''
    Funkcija vrne id-je vseh lokacij, katerih naziv vsebuje dani niz.
    '''
    
    poizvedba = """
        SELECT id
        FROM lokacija
        WHERE naziv LIKE ?
        ORDER BY id
    """
    idji_lokacij = []
    for(id_lokacije,) in conn.execute(poizvedba, ['%' + niz + '%']):
        idji_lokacij.append(id_lokacije)
    return idji_lokacij

# ISKANJE PO REGIJAH
def poisci_lokacije_regije(regija):
    '''
    Funkcija vrne IDje vseh lokacij, katere so v dani regiji.
    '''
    poizvedba = """
        SELECT id
        FROM lokacija
        WHERE regija = ?
        ORDER BY id
        """
    idji_lokacij =[]
    for (id_lokacije,) in conn.execute(poizvedba, [regija]):
        idji_lokacij.append(id_lokacije)
    return idji_lokacij

# ISKANJE PO VRSTI LOKACIJE
def seznam_vrst_lokacij():
    '''
    Funkcija poišče vse vrste lokacij in vrne seznam vseh vrst.
    To funkcijo potrebujemo zaradi možnega dodajanja novih vrst.
    '''
    poizvedba = """
        SELECT naziv
        FROM vrsta
    """
    vrste = []
    for (naziv_vrste,) in conn.execute(poizvedba):
        vrste.append(naziv_vrste)
    return vrste

def lokacije_glede_na_vrsto(vrsta):
    """
    Funkcija vrne seznam IDjev vseh lokacij, ki spadajo pod dano vrsto.
    """
    poizvedba = """
        SELECT lokacija.id
        FROM lokacija
        JOIN pripadaVrsta ON lokacija.id = pripadaVrsta.lokacija
        JOIN vrsta ON pripadaVrsta.vrsta = vrsta.id
        WHERE vrsta.naziv = ?
        ORDER BY lokacija.id
    """
    idji_lokacij = []
    for (id_lokacije,) in conn.execute(poizvedba, [vrsta]):
        idji_lokacij.append(id_lokacije)
    return idji_lokacij

# ISKANJE PO NAMENU LOKACIJE
def seznam_namenov_lokacij():
    '''
    Funkcija poišče vse namene lokacij in vrne seznam vseh namenov.
    To funkcijo potrebujemo zaradi možnega dodajanja novih namenov.
    '''
    poizvedba = """
        SELECT naziv
        FROM namen
    """
    nameni = []
    for (naziv_namena,) in conn.execute(poizvedba):
        nameni.append(naziv_namena)
    return nameni

def lokacije_glede_na_namen(namen):
    """
    Funkcija vrne seznam IDjev vseh lokacij, ki spadajo pod dan namen.
    """
    poizvedba = """
        SELECT lokacija.id
        FROM lokacija
        JOIN pripadaNamen ON lokacija.id = pripadaNamen.lokacija
        JOIN namen ON pripadaNamen.namen = namen.id
        WHERE namen.naziv = ?
        ORDER BY lokacija.id
    """
    idji_lokacij = []
    for (id_lokacije,) in conn.execute(poizvedba, [namen]):
        idji_lokacij.append(id_lokacije)
    return idji_lokacij

# ISKANJE LOKACIJ S POGOSTITVIJO IN PRENOČIŠČEM
def lokacije_pogostitev_in_prenocisce():
    """
    Funkcija vrne seznam IDjev vseh lokacij, ki ponujajo pogostitev in prenočišče.
    """
    poizvedba = """
        SELECT id 
        FROM lokacija
        WHERE pogostitev = 'Da'
        AND prenocišce = 'Da'
        ORDER BY id
    """
    idji_lokacij = []
    for (id_lokacije,) in conn.execute(poizvedba):
        idji_lokacij.append(id_lokacije)
    return idji_lokacij

# ISKANJE LOKACIJ ZA OTROKE
def lokacije_otroci():
    """
    Funkcija vrne seznam IDjev vseh lokacij, ki ponujajo animacije za otroke.
    """
    poizvedba = """
        SELECT id 
        FROM lokacija
        WHERE zaOtroke = 'Da'
        ORDER BY id
    """
    idji_lokacij = []
    for (id_lokacije,) in conn.execute(poizvedba):
        idji_lokacij.append(id_lokacije)
    return idji_lokacij    

# IZPISOVANJE PODATKOV LOKACIJ        
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

        
