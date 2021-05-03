# Ohjelmistotekniikka-kurssin laskarit ja harjoitustyö

## Harjoitustyö: Hävikkisovellus
Sovelluksen avulla käyttäjä voi vähentää ruoasta syntyvää hävikkiä. Sovellus muistuttaa käyttäjää vanhenevista ruoista.

## Dokumentaatio
- [Määrittelydokumentti](https://github.com/jupouta/ohjelmistotekniikka/blob/master/dokumentaatio/maarittelydokumentti.md)
- [Tuntikirjanpito](https://github.com/jupouta/ohjelmistotekniikka/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Arkkitehtuuri](https://github.com/jupouta/ohjelmistotekniikka/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Release 1](https://github.com/jupouta/ohjelmistotekniikka/releases/tag/viikko5)

## Ohjeet

### Asennus
Ennen ohjelman ajamista poetryn riippuvuudet täytyy asentaa. Aja komento `poetry install` _havikkisovellus_-kansiossa.

### Ohjelman suorittaminen
Ohjelma toimii ajamalla `poetry run invoke start` _havikkisovellus_-kansiossa. Ohjelman ajamiseen voi käyttää myös poetryn virtuaaliympäristöä komennolla `poetry shell`.

Ohjelma toimii ilman poetrya (Python-versio 3.6+) komennolla `python src/index.py` tai vaihtoehtoisesti `python3 src/index.py`.

Ohjelman testaamiseen voi käyttää kirjautumisessa käyttäjää `testi` ja tälle salasanaa `salis`.

HUOM! Kun ohjelma käynnistetään, tietokantaan lisätään kaksi ruoka-ainesta käyttäjälle `testi`, jotta ohjelmaa voi testata. Ruoka-ainekset poistetaan luonnollisesti lopullisesta versiosta.

### Testaus
Yksikkötestit saa ajettua komennolla `poetry run invoke test`.

Testikattavuusraportin saa luotua komennolla `poetry run invoke coverage-report`. Raportin tulokset löytyvät kansiosta _htmlcov_, ja niitä voi tarkastella tiedostosta index.html.

### Pylint
Pylint-tarkistuksen voi ajaa komennolla `poetry run invoke lint`.