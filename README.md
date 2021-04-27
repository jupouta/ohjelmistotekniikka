# Ohjelmistotekniikka-kurssin laskarit ja harjoitustyö

## Harjoitustyö: Hävikkisovellus
Sovelluksen avulla käyttäjä voi vähentää ruoasta syntyvää hävikkiä. Sovellus muistuttaa käyttäjää vanhenevista ruoista.

## Dokumentaatio
- [Määrittelydokumentti](https://github.com/jupouta/ohjelmistotekniikka/blob/master/dokumentaatio/maarittelydokumentti.md)
- [Tuntikirjanpito](https://github.com/jupouta/ohjelmistotekniikka/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Arkkitehtuuri](https://github.com/jupouta/ohjelmistotekniikka/blob/master/dokumentaatio/arkkitehtuuri.md)

## Ohjeet

### Ohjelman ajaminen
Ohjelma toimii ajamalla `poetry run invoke start` havikkisovellus-kansiossa. Ohjelman ajamiseen voi käyttää myös poetryn virtuaaliympäristöä komennolla `poetry shell`.

Ohjelma toimii ilman poetrya (Python-versio 3.6+) komennolla `python src/index.py`.

Ohjelman testaamiseen voi käyttää kirjautumisessa käyttäjää `testi` ja tälle salasanaa `salis`.

### Testaus
Yksikkötestit saa ajettua komennolla `poetry run invoke test`.

Testikattavuusraportin saa luotua komennolla `poetry run invoke coverage-report`. Raportin tulokset löytyvät kansiosta htmlcov, ja niitä voi tarkastella tiedostosta index.html.

### Pylint
Pylint-tarkistuksen voi ajaa komennolla `poetry run invoke lint`.