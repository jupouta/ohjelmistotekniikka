# Arkkitehtuurikuvaus

## Rakenne
Sovellus koostuu käyttöliittymästä (pakkaus _ui_), tietokannasta (pakkaus _database_), jonne tiedot tallennetaan, ja näiden välillä tiedon välityksestä huolehtivasta sovelluslogiikan tasosta (pakkaus _logic_). Pakkaus _entities_ käsittää luokat, joita käytetään tiedon hallinnassa sovelluslogiikan tasolla.

## Käyttöliittymä
Käyttöliittymässä on kolme näkymää: kirjautumisnäkymä, kirjautumisen jälkeinen näkymä ja käyttäjän luomiseen tarkoitettu näkymä. Näkymistä vastaa luokka _UI_. Näkymistä voi olla kerrallaan käynnissä vain yksi. Kirjautumisen jälkeinen näkymä koostuu kahdesta luokasta, _AfterLoginView_ ja _IngredientsView_, joista jälkimmäinen vastaa ainesosien listauksesta.

## Sovelluslogiikka
Toiminnallisuudesta vastaa pakkauksen _logic_ luokka _FoodService_. _FoodService_ tarjoaa käyttöliittymälle tarvittavat toiminnallisuudet, joita tarvitaan tietojen tallentamiseen ja noutamiseen tietokannasta, esim. käyttäjän lisäämien ainesosien listaus ```list_added_ingredients(username, expire=False)```. _FoodService_ käyttää myös luokkia ```Ingredient``` ja ```User``` tiedon mallintamisessa.

### Luokkien suhde toisiinsa
Luokkien suhdetta toisiinsa kuvaava pakkauskaavio sovelluslogiikan näkökulmasta:

![Pakkauskaavio](https://github.com/jupouta/ohjelmistotekniikka/blob/master/dokumentaatio/kuvat/pakkauskaavio.jpg)

## Tietojen tallennus
Tietojen tallentaminen tapahtuu pakkauksen _database_ luokan _Database_ avulla, joka käyttää SQLitea tallentamiseen.

Käytössä on kaksi taulua: ```food``` ja ```users```. ```food``` tallentaa ainesosat ja ```users``` niihin yhdistetyt käyttäjät. Taulut alustetaan ohjelman alussa tiedoston ```initialize_database```n kautta.

Konfiguraatiotiedostoon .env on määritelty tietokannassa käytettävän tiedoston nimi.

## Päätoiminnallisuudet


### Kirjautuminen

Käyttäjä antaa kirjautuessaan käyttäjätunnuksen ja salasanan, jotka ovat esimerkissä 'testi' ja 'salis'.

![Sekvenssikaavio_kirjautumisesta](https://github.com/jupouta/ohjelmistotekniikka/blob/master/dokumentaatio/kuvat/sekvenssikaavio_kirjautuminen.png)

Prosessi lähtee liikkeelle, kun käyttäjä painaa painiketta _Enter login_. Käyttöliittymä kutsuu ```FoodService```n metodia check_username, jolle annetaan parametreiksi saadut käyttäjätunnus ja salasana. ```FoodService``` taas kutsuu ```Database```n metodia get_user, joka tarkistaa, vastaavatko käyttäjätunnus ja salasana tietokannassa oleviin tietoihin. Jos ne vastaavat toisiaan, sekä ```Database``` että ```FoodService``` palauttavat ```True```, mikä aiheuttaa käyttöliittymän uudelleenrenderöinnin metodin show_after_login avulla.

### Ainesosan lisääminen
Käyttäjä lisää ainesosan. Esimerkissä käyttäjä 'testi' lisää ainesosan 'porkkana', jolle annetaan viimeiseksi käyttöpäiväksi '21/05/2021'. Käyttäjä kirjoittaa ainesosan nimen ja viimeisen käyttöpäivän ja painaa sen jälkeen nappia _Add new ingredient_.

![Sekvenssikaavio lisäämisestä](https://github.com/jupouta/ohjelmistotekniikka/blob/master/dokumentaatio/kuvat/sekvenssikaavio_ainesosan_lisaaminen.png)

Ensin käyttöliittymä kysyy `FoodService`ltä käyttäjää metodin get_user avulla, joka taas kutsuu luokan `User` metodia get_username. Molemmat metodit palauttavat käyttäjän käyttäjänimen ('testi').

Seuraavaksi käyttäjän antama päivämäärä ('21/05/2021') muunnetaan `FoodService`n metodin convert_expire_date avulla, joka palauttaa päivämäärää vastaavan kokonaisluvun (1621591391).

Nyt voidaan kutsua `FoodService`n add_ingredient-metodia, jolle annetaan parametreiksi nykyinen päivä kokonaislukumuodossa, ainesosan nimi('porkkana'), vanhenemispäivämäärä kokonaislukuna ja käyttäjän käyttäjänimi. Tämä saa aikaan `Database`-luokan metodin insert_a_new_ingredient kutsumisen, ja sille annetaan samat parametrit kuin sovelluslogiikan metodille. Tietokanta tallentaa uuden ainesosan, ja ohjelma palautuu takaisin lähtötilanteeseen. Tämä aiheuttaa ainesosien uudelleen päivittämisen käyttöliittymän metodin show_ingredient_list kautta.

### Ainesosan päivittäminen
Käyttäjä merkitsee ainesosan käytetyksi. Esimerkissä on käytetty käyttäjää 'testi' ja ainesosaa 'tomaatti'.

![Sekvenssikaavio päivittämisestä](https://github.com/jupouta/ohjelmistotekniikka/blob/master/dokumentaatio/kuvat/sekvenssikaavio_ainesosan_merkitseminen.png)

Käyttäjä valitsee ensin merkittävät ainesosat ja painaa sitten _Mark as eaten_. Käyttöliittymä kutsuu ```FoodService```n metodia mark_ingredient_as_eaten, jolle annetaan parametreiksi käyttäjätunnus ja kyseisen ainesosan nimi. Tällöin kutsutaan ```Database```n samannimistä metodia, joka merkitsee käyttäjätunnuksen ainesosan käytetyksi, ja lopuksi palauttaa muokatun ainesosan. ```FoodService``` taas palauttaa ainesosan Ingredient-luokan oliona. Lopuksi käyttöiittymä renderöidään uudelleen metodin _show_ingredient_list kautta.

### Käyttäjän luominen
Käyttäjä lisää uuden käyttäjän kirjoittamalla haluamansa käyttäjänimen ja salasanan niille tarkoitettuihin kenttiin. Esimerkissä on käytetty käyttäjänimeä 'testi' ja salasanaa 'salis'.

![Sekvenssikaavio käyttäjän lisäämisestä](https://github.com/jupouta/ohjelmistotekniikka/blob/master/dokumentaatio/kuvat/sekvenssikaavio_kayttajan_lisaaminen.png)

Kun käyttäjä klikkaa nappia _Create user_, käyttöliittymä kutsuu ```FoodService```n metodia add_user, jolle annetaan parametreiksi halutut käyttäjätunnus ja salasana. ```FoodService``` kysyy tietokannalta metodin get_user avulla, löytyykö tietokannasta jo tällaista käyttäjätunnusta. Jos ei, `Database` palauttaa arvon `True`. Nyt ohjelma palautuu takaisin käyttöliittymään, ja näkymä päivittyy uudelleen metodin show_login_view kautta.

## Ohjelman puutteet

Joissakin luokissa on liikaa instanssimuuttuja (instance variables)