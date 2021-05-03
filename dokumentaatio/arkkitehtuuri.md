# Arkkitehtuurikuvaus

## Rakenne
Sovellus koostuu käyttöliittymästä (pakkaus _ui_), tietokannasta (pakkaus _database_), jonne tiedot tallennetaan, ja näiden välillä tiedon välityksestä huolehtivasta sovelluslogiikan tasosta (pakkaus _logic_). Pakkaus _entities_ käsittää luokat, joita käytetään tiedon hallinnassa sovelluslogiikan tasolla.

## Käyttöliittymä
Käyttöliittymässä on kaksi näkymää: kirjautumisnäkymä ja kirjautumisen jälkeinen näkymä. Näkymistä vastaa luokka _UI_. Näkymistä voi olla kerrallaan vain yksi. Kirjautumisen jälkeinen näkymä koostuu kahdesta luokasta, _AfterLoginView_ ja _IngredientsView_, joista jälkimmäinen vastaa ainesosien listauksesta.

## Sovelluslogiikka
Toiminnallisuudesta vastaa pakkauksen _logic_ luokka _FoodService_. _FoodService_ tarjoaa käyttöliittymälle tarvittavat toiminnallisuudet, joita tarvitaan tietojen tallentamiseen ja noutamiseen tietokannasta, esim. käyttäjän lisäämien ainesosien listaus ```list_added_ingredients(username, expire=False)```. _FoodService_ käyttää myös luokkia ```Ingredient``` ja ```User``` tiedon mallintamisessa.

### Luokkien suhde toisiinsa
Luokkien suhdetta toisiinsa kuvaava pakkauskaavio sovelluslogiikan näkökulmasta:

![Pakkauskaavio](https://github.com/jupouta/ohjelmistotekniikka/blob/master/dokumentaatio/pakkauskaavio.jpg)

## Tietojen tallennus
Tietojen tallentaminen tapahtuu pakkauksen _database_ luokan _Database_ avulla, joka käyttää SQLitea tallentamiseen.

Käytössä on kaksi taulua: ```food``` ja ```users```. ```food``` tallentaa ainesosat ja ```users``` niihin yhdistetyt käyttäjät. Taulut alustetaan ohjelman alussa tiedoston ```initialize_database```n kautta.

## Päätoiminnallisuudet


### Kirjautuminen

Käyttäjä antaa kirjautuessaan käyttäjätunnuksen ja salasanan, jotka ovat esimerkissä 'testi' ja 'salis'.

![Sekvenssikaavio_kirjautumisesta](https://github.com/jupouta/ohjelmistotekniikka/blob/master/dokumentaatio/sekvenssikaavio_kirjautuminen.png)

Prosessi lähtee liikkeelle, kun käyttäjä painaa painiketta _Enter login_. Käyttöliittymä kutsuu ```FoodService```n metodia check_username, jolle annetaan parametreiksi saadut käyttäjätunnus ja salasana. ```FoodService``` taas kutsuu ```Database```n metodia get_user, joka tarkistaa, vastaavatko käyttäjätunnus ja salasana tietokannassa oleviin tietoihin. Jos ne vastaavat toisiaan, sekä ```Database``` että ```FoodService``` palauttavat ```True```, mikä aiheuttaa käyttöliittymän uudelleenrenderöinnin metodin show_after_login avulla.

### Ainesosan lisääminen

### Ainesosan päivittäminen

### Käyttäjän luominen

