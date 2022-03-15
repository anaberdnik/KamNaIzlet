from re import I
import bottle
import model
import json

@bottle.get('/')
def zacetna_stran():
    return bottle.template('zacetek.html')

@bottle.get('/iskanje_lokacije')
def iskanje_lokacije():
    return bottle.template('iskanje_lokacije.html')

@bottle.post('/iskanje_lokacije')
def iskanje_lokacije_post():
    lokacija = bottle.request.forms['lokacija']
    id_lokacije = model.poisci_lokacije(lokacija)
    lok = []
    for i in id_lokacije:
        podatki = model.podatki_lokacije(i)
        lok.append(podatki[0])
    return bottle.template('izpisi_lokacije.html', lokacije = lok, idji = id_lokacije)

@bottle.get('/izpisi_podatke_lokacije_vmesna/<id>')
def podatki_lokacije(id):
    podatki = model.podatki_lokacije(id)
    return bottle.template('izpisi_podatke_lokacije.html', pod = podatki)
      
@bottle.get('/iskanje_regije')
def iskanje_regije():
    return bottle.template('iskanje_regije.html')

@bottle.post('/iskanje_regije')
def iskanje_regije_post():
    regija = bottle.request.forms.getunicode('izberi_regijo')
    id_lokacije_po_regiji = model.poisci_lokacije_regije(regija)
    lok_po_regijah = []
    for i in id_lokacije_po_regiji:
        podatki_po_regiji = model.podatki_lokacije(i)
        lok_po_regijah.append(podatki_po_regiji[0])
    return bottle.template('izpisi_lokacije_po_regijah.html', lokacije_po_regijah = lok_po_regijah, idji_po_regijah = id_lokacije_po_regiji)

@bottle.get('/izpisi_podatke_lokacije_po_regijah_vmesna/<id>')
def podatki_lokacije_po_regijah(id):
    podatki = model.podatki_lokacije(id)
    return bottle.template('izpisi_podatke_lokacije.html', pod = podatki)

@bottle.get('/iskanje_namen')
def iskanje_namen():
    return bottle.template('iskanje_namen.html')

@bottle.post('/iskanje_namen')
def iskanje_namen_post():
    namen = bottle.request.forms.getunicode('izberi_namen')
    id_lokacije_po_namenu = model.lokacije_glede_na_namen(namen)
    lok_po_namenu = []
    for i in id_lokacije_po_namenu:
        podatki_po_namenu = model.podatki_lokacije(i)
        lok_po_namenu.append(podatki_po_namenu[0])
    return bottle.template('izpisi_lokacije_po_namenu.html', lokacije_po_namenu = lok_po_namenu, idji_po_namenu = id_lokacije_po_namenu)

@bottle.get('/izpisi_podatke_lokacije_po_namenu_vmesna/<id>')
def podatki_lokacije_po_namenu(id):
    podatki = model.podatki_lokacije(id)
    return bottle.template('izpisi_podatke_lokacije.html', pod = podatki)


@bottle.get('/iskanje_vrsta')
def iskanje_vrsta():
    return bottle.template('iskanje_vrsta.html')

@bottle.post('/iskanje_vrsta')
def iskanje_vrsta_post():
    vrsta = bottle.request.forms.getunicode('izberi_vrsto')
    id_lokacije_po_vrsti = model.lokacije_glede_na_vrsto(vrsta)
    lok_po_vrsti = []
    for i in id_lokacije_po_vrsti:
        podatki_po_vrsti = model.podatki_lokacije(i)
        lok_po_vrsti.append(podatki_po_vrsti[0])
    return bottle.template('izpisi_lokacije_po_vrsti.html', lokacije_po_vrsti = lok_po_vrsti, idji_po_vrsti = id_lokacije_po_vrsti)

@bottle.get('/izpisi_podatke_lokacije_po_vrsti_vmesna/<id>')
def podatki_lokacije_po_vrsti(id):
    podatki = model.podatki_lokacije(id)
    return bottle.template('izpisi_podatke_lokacije.html', pod = podatki)

@bottle.get('/iskanje_cas')
def iskanje_lokacije_po_času():
    return bottle.template('iskanje_cas.html')

@bottle.post('/iskanje_cas')
def iskanje_lokacije_po_času_post():
    čas = bottle.request.forms.getunicode('izberi_cas')
    id_lokacije_po_času = model.lokacije_glede_na_čas_obiska(čas)
    lok_po_času = []
    for i in id_lokacije_po_času:
        podatki = model.podatki_lokacije(i)
        lok_po_času.append(podatki[0])
    return bottle.template('izpisi_lokacije_po_casu.html', lokacije_po_času = lok_po_času, idji_po_času = id_lokacije_po_času)

@bottle.get('/izpisi_podatke_lokacije_po_casu_vmesna/<id>')
def podatki_lokacije_po_času(id):
    podatki = model.podatki_lokacije(id)
    return bottle.template('izpisi_podatke_lokacije.html', pod = podatki)


bottle.run(debug=True, reloader=True)
