from re import I
import bottle
import model
import json

@bottle.get('/')
def zacetna_stran():
    return bottle.template('zacetek.html')

@bottle.get('/iskanje_lokacije')
def iskanje_lokacije():
    '''Iskanje lokacije.'''
    return bottle.template('iskanje_lokacije.html')

@bottle.post('/iskanje_lokacije')
def iskanje_lokacije_post():
    '''Prebere vneseni niz kot argument lokacija in poišče lokacije,
    ki vsebujejo dani niz.'''
    lokacija = bottle.request.forms['lokacija']
    id_lokacije = model.poisci_lokacije(lokacija)
    lok = []
    for i in id_lokacije:
        podatki = model.podatki_lokacije(i)
        lok.append(podatki[0])
    return bottle.template('izpisi_lokacije.html', lokacije = lok, idji = id_lokacije)

@bottle.get('/izpisi_podatke_lokacije_vmesna/<id>')
def podatki_lokacije(id):
    '''Izpiše podatke ustrezne lokacije.'''
    podatki = model.podatki_lokacije(id)
    return bottle.template('izpisi_podatke_lokacije.html', pod = podatki)
      
@bottle.get('/iskanje_regije')
def iskanje_regije():
    '''Iskanje po regiji.'''
    return bottle.template('iskanje_regije.html')

@bottle.post('/iskanje_regije')
def iskanje_regije_post():
    '''Prebere izbiro regije kot argument izberi_regijo in poišče lokacije
    v dani regiji.'''
    regija = bottle.request.forms.getunicode('izberi_regijo')
    id_lokacije_po_regiji = model.poisci_lokacije_regije(regija)
    lok_po_regijah = []
    for i in id_lokacije_po_regiji:
        podatki_po_regiji = model.podatki_lokacije(i)
        lok_po_regijah.append(podatki_po_regiji[0])
    return bottle.template('izpisi_lokacije_po_regijah.html', lokacije_po_regijah = lok_po_regijah, idji_po_regijah = id_lokacije_po_regiji)

@bottle.get('/izpisi_podatke_lokacije_po_regijah_vmesna/<id>')
def podatki_lokacije_po_regijah(id):
    '''Izpiše podatke ustrezne lokacije poiskane glede na regijo.'''
    podatki = model.podatki_lokacije(id)
    return bottle.template('izpisi_podatke_lokacije.html', pod = podatki)

@bottle.get('/iskanje_namen')
def iskanje_namen():
    '''Iskanje glede na namen obiska.'''
    return bottle.template('iskanje_namen.html')

@bottle.post('/iskanje_namen')
def iskanje_namen_post():
    '''Prebere izbiro namena obiska kot argument izberi_namen in poišče
    lokacije z danim namenom obiska.'''
    namen = bottle.request.forms.getunicode('izberi_namen')
    id_lokacije_po_namenu = model.lokacije_glede_na_namen(namen)
    lok_po_namenu = []
    for i in id_lokacije_po_namenu:
        podatki_po_namenu = model.podatki_lokacije(i)
        lok_po_namenu.append(podatki_po_namenu[0])
    return bottle.template('izpisi_lokacije_po_namenu.html', lokacije_po_namenu = lok_po_namenu, idji_po_namenu = id_lokacije_po_namenu)

@bottle.get('/izpisi_podatke_lokacije_po_namenu_vmesna/<id>')
def podatki_lokacije_po_namenu(id):
    '''Izpiše podatke ustrezne lokacije poiskane glede na namen obiska.'''
    podatki = model.podatki_lokacije(id)
    return bottle.template('izpisi_podatke_lokacije.html', pod = podatki)


@bottle.get('/iskanje_vrsta')
def iskanje_vrsta():
    '''Iskanje glede na vrsto.'''
    return bottle.template('iskanje_vrsta.html')

@bottle.post('/iskanje_vrsta')
def iskanje_vrsta_post():
    '''Prebere izbiro vrste kot argument izberi_vrsto in poišče
    lokacije z dano vrsto.'''
    vrsta = bottle.request.forms.getunicode('izberi_vrsto')
    id_lokacije_po_vrsti = model.lokacije_glede_na_vrsto(vrsta)
    lok_po_vrsti = []
    for i in id_lokacije_po_vrsti:
        podatki_po_vrsti = model.podatki_lokacije(i)
        lok_po_vrsti.append(podatki_po_vrsti[0])
    return bottle.template('izpisi_lokacije_po_vrsti.html', lokacije_po_vrsti = lok_po_vrsti, idji_po_vrsti = id_lokacije_po_vrsti)

@bottle.get('/izpisi_podatke_lokacije_po_vrsti_vmesna/<id>')
def podatki_lokacije_po_vrsti(id):
    '''Izpiše podatke ustrezne lokacije poiskane glede na vrsto.'''
    podatki = model.podatki_lokacije(id)
    return bottle.template('izpisi_podatke_lokacije.html', pod = podatki)

@bottle.get('/iskanje_cas')
def iskanje_lokacije_po_času():
    '''Iskanje glede na čas obiska.'''
    return bottle.template('iskanje_cas.html')

@bottle.post('/iskanje_cas')
def iskanje_lokacije_po_času_post():
    '''Prebere izbiro časa obiska kot argument izberi_cas in poišče
    lokacije, ki pripadajo danemu času obiska.'''
    čas = bottle.request.forms.getunicode('izberi_cas')
    id_lokacije_po_času = model.lokacije_glede_na_čas_obiska(čas)
    lok_po_času = []
    for i in id_lokacije_po_času:
        podatki = model.podatki_lokacije(i)
        lok_po_času.append(podatki[0])
    return bottle.template('izpisi_lokacije_po_casu.html', lokacije_po_času = lok_po_času, idji_po_času = id_lokacije_po_času)

@bottle.get('/izpisi_podatke_lokacije_po_casu_vmesna/<id>')
def podatki_lokacije_po_času(id):
    '''Izpiše podatke ustrezne lokacije poiskane glede na čas obiska.'''
    podatki = model.podatki_lokacije(id)
    return bottle.template('izpisi_podatke_lokacije.html', pod = podatki)

@bottle.get('/izpisi_lokacije_pog_pren')
def iskanje_lokacije_pog_pren():
    '''Poišče lokacije, ki nudijo pogostitev in prenočišče.'''
    id_lokacije_pog_pren = model.lokacije_pogostitev_in_prenocisce()
    lok_pog_pren = []
    for i in id_lokacije_pog_pren:
        podatki = model.podatki_lokacije(i)
        lok_pog_pren.append(podatki[0])
    return bottle.template('izpisi_lokacije_pog_pren.html',lokacije_pog_pren = lok_pog_pren, idji_pog_pren = id_lokacije_pog_pren)

@bottle.get('/izpisi_podatke_lokacije_pog_pren_vmesna/<id>')
def podatki_lokacije_pog_pren(id):
    '''Izpiše podatke ustrezne lokacije poiskane med tistimi, ki
    nudijo pogostitev in prenočišče.'''
    podatki = model.podatki_lokacije(id)
    return bottle.template('izpisi_podatke_lokacije.html', pod = podatki)

@bottle.get('/izpisi_lokacije_otroci')
def iskanje_lokacije_otroci():
    '''Poišče lokacije, ki organizirajo animacije ali delavnice za otroke.'''
    id_lokacije_otroci = model.lokacije_otroci()
    lok_otroci = []
    for i in id_lokacije_otroci:
        podatki = model.podatki_lokacije(i)
        lok_otroci.append(podatki[0])
    return bottle.template('izpisi_lokacije_otroci.html',lokacije_otroci = lok_otroci, idji_otroci = id_lokacije_otroci)

@bottle.get('/izpisi_podatke_lokacije_otroci_vmesna/<id>')
def podatki_lokacije_otroci(id):
    '''Izpiše podatke ustrezne lokacije poiskane med tistimi, ki
    organizirajo animacije ali delavnice za otroke.'''
    podatki = model.podatki_lokacije(id)
    return bottle.template('izpisi_podatke_lokacije.html', pod = podatki)

@bottle.get('/izpisi_lokacije_vstopnina')
def iskanje_lokacije_vstopnina():
    '''Poišče lokacije brez vstopnine.'''
    id_lokacije_vstopnina = model.lokacije_brez_vstopnine()
    lok_vstopnina = []
    for i in id_lokacije_vstopnina:
        podatki = model.podatki_lokacije(i)
        lok_vstopnina.append(podatki[0])
    return bottle.template('izpisi_lokacije_vstopnina.html',lokacije_vstopnina = lok_vstopnina, idji_vstopnina = id_lokacije_vstopnina)

@bottle.get('/izpisi_podatke_lokacije_vstopnina_vmesna/<id>')
def podatki_lokacije_vstopnina(id):
    '''Izpiše podatke ustrezne lokacije izbrane med tistimi, ki
    so brez vstopnine.'''
    podatki = model.podatki_lokacije(id)
    return bottle.template('izpisi_podatke_lokacije.html', pod = podatki)
 
bottle.run(debug=True, reloader=True)
