# Testausdokumentti
Ohjelmaa on testattu yksikkö- ja integraatiotestein sekä manuaalisesti järjestelmää testaamalla. Käyttöliittymää ei ole testattu automaattisesti.

## Yksikkö- ja integraatiotestaus
Yksikkötestaus on suoritettu luokille `Database`, `FoodService` ja `Ingredient`. `FoodService` vastaa sovelluksen logiikasta, ja `TestFoodService`-testiluokan testauksessa on käytetty luokkaa `FakeDatabase` simuloimaan tietokantaa. Tietokanta annetaan parametrina `FoodService`-oliolle.

`Database` vastaa tietokantakyselyistä ja sitä varten on käytetty testitietokantaa, jonka tiedosto on konfiguroitu _env.test_-tiedostoon. Testitietokanta alustetaan joka testikerta tyhjäksi. Testiluokkana toimii `TestDatabase`.

Luokan `Ingredient` testeissä on testattu luokan metodeja `TestIngredient`-testiluokassa.


### Testauskattavuus
Testauksen haarautumakattavuus on 96%.

![Haarautumakattavuus](https://github.com/jupouta/ohjelmistotekniikka/blob/master/dokumentaatio/kuvat/haarautumakattavuus.png)

Tiedostojen _database.py_ ja _initialize\_database.py_ puuttuvat testiosuudet johtuvat testauksen vaatimuksista (käyttäjän 'testi' lisääminen sekä testiympäristönä on 'TEST').

_initialize\_database.py_- ja _config.py_-tiedostot olisi voinut jättää testauksen ulkopuolelle, sillä niitä ei varsinaisesti voi testata, mutta niitä on testattu järjestelmätasolla.

## Järjestelmätestaus
Järjestelmätestausta on suoritettu manuaalisesti. Kaikkia toiminnallisuuksia on testattu, ja kaikista on yritetty löytää mahdolliset ongelmat, kuten tyhjän käyttäjänimen lisääminen.

Tietokantatiedostoa on testattu sekä niin, että tiedosto on poistettu, että sen ollessa paikallaan.