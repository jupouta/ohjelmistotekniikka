# Ohjelmistotekniikka-kurssin laskarit ja harjoitustyö

## Harjoitustyö: Hävikkisovellus
Sovelluksen avulla käyttäjä voi vähentää ruoasta syntyvää hävikkiä. Sovellus muistuttaa käyttäjää vanhenevista ruoista.

## Dokumentaatio
- [Määrittelydokumentti](https://github.com/jupouta/ohjelmistotekniikka/blob/master/dokumentaatio/maarittelydokumentti.md)
- [Tuntikirjanpito](https://github.com/jupouta/ohjelmistotekniikka/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Arkkitehtuuri](https://github.com/jupouta/ohjelmistotekniikka/blob/master/dokumentaatio/arkkitehtuuri.md)

## Ohjeet

### Ohjelman ajaminen
Ohjelma toimii käynnistämällä virtuaaliympäristön `poetry shell` ja ajamalla sen jälkeen `poetry run invoke start`.

Ohjelma toimii ilman virtuaaliympäristöä (Python-versio 3.6+) komennolla `python src/index.py`.

Ohjelman testaamiseen voi käyttää kirjautumisessa käyttäjää `testi` ja tälle salasanaa `salis`.

### Testaus
Yksikkötestit saa ajettua komennolla `poetry run invoke test`.
