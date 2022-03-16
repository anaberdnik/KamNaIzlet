import baza
import sqlite3
from sqlite3 import IntegrityError
from pomozne_funkcije import Seznam

conn = sqlite3.connect('KamNaIzlet.db')
baza.ustvari_bazo_ce_ne_obstaja(conn)
conn.execute('PRAGMA foreign_keys = ON')

lokacija, čas, vrsta, namen, pripadaVrsta, pripadaNamen = baza.pripravi_tabele(conn)


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

def vrste_lokacije(id_lokacije):
    '''
    Funkcija vrne vse vrste lokacije, ki ima podan ID.
    '''
    poizvedba = """
        SELECT vrsta.naziv
        FROM vrsta
        JOIN pripadaVrsta ON vrsta.id = pripadaVrsta.vrsta
        JOIN lokacija ON pripadaVrsta.lokacija = lokacija.id
        WHERE lokacija.id = ?
    """
    vrste_lokacije = []
    for (vrsta_lokacije,) in conn.execute(poizvedba, [id_lokacije]):
        vrste_lokacije.append(vrsta_lokacije)
    return vrste_lokacije
    

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

def nameni_lokacije(id_lokacije):
    '''
    Funkcija vrne vse namene lokacije, ki ima podan ID.
    '''
    poizvedba = """
        SELECT namen.naziv
        FROM namen
        JOIN pripadaNamen ON namen.id = pripadaNamen.namen
        JOIN lokacija ON pripadaNamen.lokacija = lokacija.id
        WHERE lokacija.id = ?
    """
    nameni_lokacije = []
    for (namen_lokacije,) in conn.execute(poizvedba, [id_lokacije]):
        nameni_lokacije.append(namen_lokacije)
    return nameni_lokacije

# ISKANJE LOKACIJ GLEDE NA ČAS OBISKA

def lokacije_glede_na_čas_obiska(čas_obiska):
    """
    Funkcija vrne seznam IDjev vseh lokacij, za katere primeren čas obiska ustreza podanemu.
    """
    poizvedba = """
        SELECT lokacija.id FROM lokacija
        JOIN čas ON lokacija.id = čas.lokacija
        WHERE čas.tip = ?
        ORDER BY lokacija.id
    """
    idji_lokacij = []
    for (id_lokacije,) in conn.execute(poizvedba, [čas_obiska]):
        idji_lokacij.append(id_lokacije)
    return idji_lokacij

def čas_obiska_lokacije(id_lokacije):
    '''
    Funkcija vrne vse primerne čase obiska lokacije, ki ima podan ID.
    '''
    poizvedba = """
        SELECT čas.tip
        FROM čas
        JOIN lokacija ON čas.lokacija = lokacija.id
        WHERE lokacija.id = ?
    """
    časi_obiska_lokacije = []
    for (čas_obiska_lokacije,) in conn.execute(poizvedba, [id_lokacije]):
        časi_obiska_lokacije.append(čas_obiska_lokacije)
    return časi_obiska_lokacije
    

# ISKANJE LOKACIJ S POGOSTITVIJO IN PRENOČIŠČEM
def lokacije_pogostitev_in_prenocisce():
    """
    Funkcija vrne seznam IDjev vseh lokacij, ki ponujajo pogostitev in prenočišče.
    """
    poizvedba = """
        SELECT id 
        FROM lokacija
        WHERE pogostitev = 'Da'
        AND prenočišče = 'Da'
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

# ISKANJE LOKACIJ BREZ VSTOPNINE
def lokacije_brez_vstopnine():
    """
    Funkcija vrne seznam IDjev vseh lokacij, ki so brez vstopnine.
    """
    poizvedba = """
        SELECT id 
        FROM lokacija
        WHERE vstopnina = 'Ne'
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
    SELECT naziv, regija, opis, url, pogostitev, prenočišče, vstopnina, zaOtroke, urlSlike
    FROM lokacija
    WHERE id = ?
    """
    
    osnovni_podatki = conn.execute(poizvedba, [id_lokacije]).fetchone()
    if osnovni_podatki is None:
        return None
    else:
        naziv, regija, opis, url, pogostitev, prenočišče, vstopnina, zaOtroke, urlSlike = osnovni_podatki
    return naziv, regija, opis, url, pogostitev, prenočišče, vstopnina, zaOtroke, urlSlike

# DODAJANJE LOKACIJE
def dodajanje_lokacije(osnovne_informacije, vrste, nameni, časi):
    poizvedba = """
        INSERT INTO lokacija (naziv, regija, opis, url, pogostitev, prenočišče, vstopnina, zaOtroke, urlSlike)
        VALUES (?,?,?,?,?,?,?,?,?);
    """
    conn.execute(poizvedba, osnovne_informacije)


        

