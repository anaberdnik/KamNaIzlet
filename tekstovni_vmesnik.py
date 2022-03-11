from pomozne_funkcije import Meni, JaNe, prekinitev
import model

def izberi_moznost(moznosti):
    '''
    Funkcija izpiše seznam možnosti in vrne indeks izbrane možnosti.
    
    Če na voljo ni nobene možnosti, uporabnika o tem opozori ter izpiše None.
    Če je na voljo samo ena možnost, vrne '.
    '''
    
    if len(moznosti) == 0:
        return
    elif len(moznosti) == 1:
        return 0
    else:
        for i, moznost in enumerate(moznosti, 1):
            print(f'{i}) {moznost}')
        
        stevilo_moznosti = len(moznosti)
        while True:
            izbira = input('Vnesite izbiro > ')
            if not izbira.isdigit():
                print('NAPAKA: vnesti morate število.')
            else:
                n = int(izbira)
                if 1 <= n <= stevilo_moznosti:
                    return n - 1
                else:
                    print(f'NAPAKA: vnesti morate število med 1 in {stevilo_moznosti}!')

# IZBIRA 1
def izberi_lokacijo():
    niz = input("Vnesite del naziva lokacije > ")
    idji_lokacij = model.poisci_lokacije(niz)
    moznosti = [
        "{} ({})".format(naziv, regija) for _, naziv, regija in model.podatki_lokacij(idji_lokacij)
        ]
    izbira = izberi_moznost(moznosti)
    return None if izbira is None else idji_lokacij[izbira]

def prikazi_podatke_lokacije():
    id_lokacije = izberi_lokacijo()
    if id_lokacije is None:
        print("Nobena lokacija ne ustreza iskanemu nizu.")
    else:
        naziv, regija, url = model.podatki_lokacije(id_lokacije)
        print(f"{naziv}, {regija}: {url}")

# IZBIRA 2
def izberi_regijo():
    regije = ['Pomurska', 'Podravska', 'Koroška', 'Savinjska', 'Posavska', 'Zasavska', 'Osrednjeslovenska', 'Gorenjska', 'Goriška', 'Obalno-kraška', 'Primorsko-notranjska', 'Jugovzhodna-Slovenija']
    izbira = izberi_moznost([ 
        'Pomurska',
        'Podravska',
        'Koroška',
        'Savinjska',
        'Posavska',
        'Zasavska',
        'Osrednjeslovenska',
        'Gorenjska',
        'Goriška',
        'Obalno-kraška',
        'Primorsko-notranjska',
        'Jugovzhodna-Slovenija'
        ])
    return regije[izbira]
    
def poisci_lokacije_regije():
    regija = izberi_regijo()
    idji_lokacij = model.poisci_lokacije_regije(regija)
    print()
    print(f'Lokacije v regiji {regija}:')
    moznosti = [
        "{} ({})".format(naziv, regija) for _, naziv, regija in model.podatki_lokacij(idji_lokacij)
        ]
    izbira = izberi_moznost(moznosti)
    naziv, regija, url = model.podatki_lokacije(idji_lokacij[izbira])
    print(f"{naziv}, {regija}: {url}")

# IZBIRA 3
def izberi_vrsto():
    vse_vrste = model.seznam_vrst_lokacij()
    izbira = izberi_moznost(vse_vrste)
    return vse_vrste[izbira]

def poisci_lokacije_vrsta():
    vrsta = izberi_vrsto()
    idji_lokacij = model.lokacije_glede_na_vrsto(vrsta)
    print()
    print(f"Lokacije vrste {vrsta}")
    moznosti = [
        "{} ({})".format(naziv, regija) for _, naziv, regija in model.podatki_lokacij(idji_lokacij)
        ]
    izbira = izberi_moznost(moznosti)
    naziv, regija, url = model.podatki_lokacije(idji_lokacij[izbira])
    print(f"{naziv}, {regija}: {url}")

# IZBIRA 4
def izberi_namen():
    vsi_nameni = model.seznam_namenov_lokacij()
    izbira = izberi_moznost(vsi_nameni)
    return vsi_nameni[izbira]

def poisci_lokacije_namen():
    namen = izberi_namen()
    idji_lokacij = model.lokacije_glede_na_namen(namen)
    print()
    print(f"Lokacije namena {namen}")
    moznosti = [
        "{} ({})".format(naziv, regija) for _, naziv, regija in model.podatki_lokacij(idji_lokacij)
        ]
    izbira = izberi_moznost(moznosti)
    naziv, regija, url = model.podatki_lokacije(idji_lokacij[izbira])
    print(f"{naziv}, {regija}: {url}")

# IZBIRA 4 
def poisci_lokacije_pogostitev_in_prenocisce():
    idji_lokacij = model.lokacije_pogostitev_in_prenocisce()
    print()
    print("Lokacije s pogostitvijo in prenočiščem: ")
    moznosti = [
        "{} ({})".format(naziv, regija) for _, naziv, regija in model.podatki_lokacij(idji_lokacij)
        ]
    izbira = izberi_moznost(moznosti)
    naziv, regija, url = model.podatki_lokacije(idji_lokacij[izbira])
    print(f"{naziv}, {regija}: {url}")

# IZBIRA 5
def poisci_lokacije_otroci():
    idji_lokacij = model.lokacije_otroci()
    print()
    print("Lokacije z animacijami za otroke: ")
    moznosti = [
        "{} ({})".format(naziv, regija) for _, naziv, regija in model.podatki_lokacij(idji_lokacij)
        ]
    izbira = izberi_moznost(moznosti)
    naziv, regija, url = model.podatki_lokacije(idji_lokacij[izbira])
    print(f"{naziv}, {regija}: {url}")   
    
#MENI (izbire):
def prikazi_moznosti():
    print(50 * '-')
    izbira = izberi_moznost([
        'prikaži podatke lokacije',
        'prikaži lokacije regije',
        'prikaži lokacije glede vrsto',
        'prikaži lokacije glede namen obiska',
        'prikaži lokacije z možnostjo pogostitve in prenočišča',
        'prikaži lokacije z animacijami za otroke',
        'izhod',
        ])
    if izbira == 0:
        prikazi_podatke_lokacije()
    elif izbira == 1:
        poisci_lokacije_regije()
    elif izbira == 2:
        poisci_lokacije_vrsta()
    elif izbira == 3:
        poisci_lokacije_namen()
    elif izbira == 4:
        poisci_lokacije_pogostitev_in_prenocisce()
    elif izbira == 5:
        poisci_lokacije_otroci()
    elif izbira == 6:
        print('Nasvidenje')
        exit()

def main():
    print('Pozdravljeni v bazi lokacij!')
    while True:
        prikazi_moznosti()

main()
