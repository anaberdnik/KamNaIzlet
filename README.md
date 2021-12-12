# KamNaIzlet
Projektna naloga pri predmetu Podatkovne baze 1
Osnovna ideja je nabor lokacij kam lahko gremo na izlet po sloveniji. Uporabnik lahko potem filtrira glede na regije po Sloveniji, namen izleta, primeren (letni) čas izleta itd. 

ER diagram:
![ERD](https://user-images.githubusercontent.com/28532399/145731108-251c36ba-59cf-4bb7-9807-c24197bc2dd1.png)

Glavna entiteta **Lokacija** predstavlja osnovne lastnosti vsake lokacije: id, naziv, regija, kratek opis, URL povezava ter informacije ali lokacija omogoča pogostitev (hrana in pijača), prenočišče ter ali je primerno tudi za (manjše) otroke.

Omenjena entiteta **Lokacija** je s pomočjo povezovalne tabele **Kdaj obiskati** povezana z entiteto **Čas**, ki da informacijo, v katerem (letnem) času je to lokacijo primerno obiskati, npr.: _poletni čas, zimski čas_ ter _tudi v slabem vremenu_.

Podobno je s pomočjo povezovalne tabele **Kaj nas zanima** povezana z entiteto **Vrsta**, kjer so shranjene lastnosti vsake lokacije oz. za kakšno vrsto se gre, npr.: _grad, muzej, smučišče, znamenitost, kopališče ali terme_ ali _atraktivni kotiček_.

Na koncu imamo še eno povezovalno tabelo **Kaj si želimo** s katero je ponovno entiteta **Lokacija** povezana z entiteto **Namen**, na podlagi katere bi lahko uporabnik kasneje filtriral rezultate žlede na svoje želje, kaj želi z obiskom določene lokacije doseči, to je na primer _sprostitev, rekreacija, izobraževanje, ogled znamenitosti, oddih v naravi..._



