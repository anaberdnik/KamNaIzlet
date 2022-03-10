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

def izberi_lokacijo():
    niz = input("Vnesite del naziva lokacije > ")
    idji_lokacij = model.poisci_lokacije(niz)
    moznosti = [
        "{} ({})".format(naziv, regija) for _, naziv, regija in model.podatki_lokacij(idji_lokacij)
        ]
    izbira = izberi_moznost(moznosti)
    return None if izbira is None else idji_lokacij[izbira]
    
def poisci_lokacije_regije():
    regija =  izberi_regijo()
    print(f'Zanima vas lokacija v regiji {regija}.')

def prikazi_podatke_lokacije():
    id_lokacije = izberi_lokacijo()
    if id_lokacije is None:
        print("Nobena lokacija ne ustreza iskanemu nizu.")
    else:
        naziv, regija, url = model.podatki_lokacije(id_lokacije)
        print(f"{naziv}, {regija}: {url}")
        
    
    
def prikazi_moznosti():
    print(50 * '-')
    izbira = izberi_moznost([
        'prikaži podatke lokacije',
        'prikazi lokacije regije',
        'izhod',
        ])
    if izbira == 0:
        prikazi_podatke_lokacije()
    elif izbira == 1:
        poisci_lokacije_regije()
    elif izbira == 2:
        print('Nasvidenje')
        exit()

def main():
    print('Pozdravljeni v bazi lokacij!')
    while True:
        prikazi_moznosti()

main()

# def vnesi_izbiro(moznosti):
#     """
#     Uporabniku da na izbiro podane možnosti.
#     """
#     moznosti = list(moznosti)
#     for i, moznost in enumerate(moznosti, 1):
#         print(f'{i}) {moznost}')
#     izbira = None
#     while True:
#         try:
#             izbira = int(input('> ')) - 1
#             return moznosti[izbira]
#         except (ValueError, IndexError):
#             print("Napačna izbira!")




# def izpisi_lokacije_regije(regija):
#     """
#     Izpiše vse lokacije podane regije.
#     """
#     print(regija)
#     for naziv, url in regija.lokacije_v_regiji():
#         print(f'- {naziv}, {url}')

# def poisci_regijo():
#     """
#     Poišče regijo, ki jo vnese uporabnik.
#     """
#     while True:
#         regija_uporabnika = input("Katera regija te zanima? Na voljo so: Pomurska, Podravska, Koroška, Savinjska, Posavska, Zasavska, Osrednjeslovenska, Gorenjska, Goriška, Obalno-kraška, Primorsko-notranjska, Jugovzhodna-Slovenija.")
#         regije = ['Pomurska', 'Podravska', 'Koroška', 'Savinjska', 'Posavska', 'Zasavska', 'Osrednjeslovenska', 'Gorenjska', 'Goriška', 'Obalno-kraška', 'Primorsko-notranjska', 'Jugovzhodna-Slovenija']
#         if regija_uporabnika not in regije:
#             print("Regija ni ustrezna. Poskusi znova.")
#         else:
#             return regija_uporabnika

# #@prekinitev
# def iskanje_po_regiji():
#     """
#     Izpiše lokacij za regijo, ki jo vnese uporabnik.
#     """
#     regija = poisci_regijo()
#     izpisi_lokacije_regije(regija)



# def domov():
#     """
#     Pozdravi pred izhodom.
#     """
#     print('Adijo!')
# 
# 
# class GlavniMeni(Meni):
#     """
#     Izbire v glavnem meniju.
#     """
#     ISKAL_PO_REGIJI = ('Iskal po regiji', iskanje_po_regiji)
#     SEL_DOMOV = ('Šel domov', domov)


# #@prekinitev
# def glavni_meni():
#     """
#     Prikazuje glavni meni, dokler uporabnik ne izbere izhoda.
#     """
#     print('Pozdravljen v bazi filmov!')
#     while True:
#         print('Kaj bi rad delal?')
#         izbira = vnesi_izbiro(GlavniMeni)
#         izbira.funkcija()
#         if izbira == GlavniMeni.SEL_DOMOV:
#             return
# 
# 
# glavni_meni()


