## Vaatimusmäärittely

### Sovelluksen tarkoitus
Käyttäjä voi kirjata hävikkisovellukseen ruoka-aineksia, joiden vanhenemisesta sovellus ilmoittaa käyttäjän kirjautuessa sisään. Hävikkisovelluksen avulla käyttäjän on mahdollista vähentää tulevaa ruokahävikkiä.

### Käyttäjät
Sovelluksella on tällä hetkellä vain yksi käyttäjärooli, normaali käyttäjä.

### Sovelluksen toiminnallisuuksia

- [x] Käyttäjä voi kirjautua järjestelmään tunnuksillaan
- [x] Käyttäjä voi luoda käyttäjätunnuksen
- [x] Käyttäjä näkee kirjauduttuaan seuraavaksi vanhenevat ruoka-ainekset (viiden päivän sisään vanhenevat) aikajärjestyksessä
- [x] Käyttäjä voi lisätä uuden ruoka-aineksen
    - [x] Ruoka-aineesta annetaan lisättäessä kaksi tietoa: nimi ja päivämäärä, jolloin aines vanhenee
- [x] Käyttäjä voi merkitä ruoka-aineksen syödyksi (ja samalla se katoaa listalta)
- [x] Käyttäjä voi kirjautua ulos


### Jatkokehitysideoita
- Ruoka-ainesten, joiden päivämäärä on jo mennyt, esittäminen korostetummin
- Kaikkien (ei vielä vanhenevien ja vanhenevien) ainesten listaaminen
- Listalle lisättyjen ruoka-ainesten tietojen muokkaus (esim. vanhenemispäivän muuttaminen)
- Reseptien liittäminen tiettyihin ruoka-aineksiin
- Ruoka-ainesta lisättäessä voisi olla kenttä, johon annetaan lisätietoa aineksesta

### Toimintaympäristön rajoitteet

Sovelluksen tulee toimia Linux- ja OS X -käyttöjärjestelmissä. Käyttäjien ja ruoka-ainesten tiedot talletetaan paikallisesti.
