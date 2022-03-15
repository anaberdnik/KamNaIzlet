# KamNaIzlet
Projektna naloga pri predmetu Podatkovne baze 1.

Ideja je uporabniku predstaviti nabor lokacij oz. idej, kam se lahko odpravi na izlet po sloveniji. Pri tem lahko iskanje zoža glede na svoje preference: npr. zanimajo ga lokacije, kjer si lahko po potrebi uredi tudi prenočišče, ali pa lokacije, ki so namenjene rekreaciji / sprostivi / zabavi in podobno.

ER diagram:
![ERD](https://user-images.githubusercontent.com/28532399/145731108-251c36ba-59cf-4bb7-9807-c24197bc2dd1.png)

Glavna entiteta **Lokacija** predstavlja osnovne lastnosti vsake lokacije: id, naziv, regija, kratek opis, URL povezava do strani lokacije in URL povezava do slike lokacije ter informacije ali lokacija omogoča pogostitev (hrana in pijača), prenočišče, vstopnino ter ali organizira delavnice za otroke.

Omenjena entiteta **Lokacija** je s pomočjo povezovalne tabele **pripadaVrsta** povezana z entiteto **Vrsta**, v kateri so shranjene lastnosti o vrsti lokacije. Npr.: _grad_, _muzej_, _kmetija_, _atraktiven kotiček_ ipd. Podobno je s pomočjo povezovalne tabele **pripadaNamen** povezana z entiteto **Namen**, ki pa hrani podatke o namenu obiska. Preko te, se lahko uporabnik odloča, ali ga zanima _pohodništvo_, _rekreacija_, _ogled znamenitosti_, _sprostitev_ ipd.
Dodana pa je še ena entiteta **Čas**, ki uporabniku pove, kdaj je primeren čas za obisk poljubne lokacije. Naj bo to zimski ali poletni čas in katere izmed njih lahko obiščeš tudi v slabem vremenu.





