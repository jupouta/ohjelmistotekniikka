# Testausdokumentti
Ohjelmaa on testattu yksikkö- ja integraatiotestein sekä manuaalisesti järjestelmää testaamalla. Käyttöliittymää ei ole testattu automaattisesti.

## Yksikkö- ja integraatiotestaus
Yksikkötestaus on suoritettu luokille `Database`, `FoodService` ja `Ingredient`. `FoodService` vastaa sovelluksen logiikasta, ja `TestFoodService`-testiluokan testauksessa on käytetty luokkaa `FakeDatabase` simuloimaan tietokantaa. Tietokanta annetaan parametrina `FoodService`-oliolle.

`Database` vastaa tietokantakyselyistä ja sitä varten on käytetty testitietokantaa, jonka tiedosto on konfiguroitu _env.test_-tiedostoon. Testitietokanta alustetaan joka testikerta tyhjäksi. Testiluokkana toimii `TestDatabase`.

Luokan `Ingredient` testeissä on testattu luokan metodeja `TestIngredient`-testiluokassa.


### Testauskattavuus
Testauksen haarautumakattavuus on 97%.

_initialize\_database.py_- ja _config.py_-tiedostot olisi voinut jättää testauksen ulkopuolelle, sillä niitä ei varsinaisesti testata.

## Järjestelmätestaus