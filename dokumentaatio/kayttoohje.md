# Käyttöohje

Viimeisimmän releasen saa ladattua projektin juuresta _Releases_-kohdasta.

## Asennus
Ennen ohjelman ajamista poetryn riippuvuudet täytyy asentaa. Aja komento `poetry install` _havikkisovellus_-kansiossa.

Nyt ohjelma pitäisi pystyä ajamaan _havikkisovellus_-kansiossa komennolla `poetry run invoke start`.

## Kirjautuminen
Sovellus avautuu automaattisesti kirjautumisnäkymään. Kirjautuminen onnistuu kirjoittamalla käyttäjätunnus ja salasana niille varattuihin kenttiin ja painamalla _Enter login_.

## Ainesosan lisääminen ja merkitseminen
Kun sovellukseen kirjautuu, käyttäjälle avautuu kirjautumisen jälkeinen näkymä. Ylhäällä on _Logout_-nappi, jota painamalla pääsee takaisin kirjautumisnäkymään.

Tämän alapuolella on listattuna kaikki ainesosat, jotka ovat vanhenemassa viiden päivän sisään. Ainesosat voi merkitä käytetyiksi valitsemalla ainesosan vasemmalla puolella olevan ruudun ja painamalla _Mark as eaten_. Merkityt ainesosat katoavat tällöin listalta.

Uuden ainesosan lisääminen tapahtuu näiden alapuolelta kirjoittamalla _Ingredient_-kenttään ainesosan nimen ja _Expire date_-kenttään päivämäärän, jolloin ainesosa. Tähän on kaksi tapaa:
- joko päivämäärä muodossa dd/mm/yyyy (esim. 31/12/2021)
- tai jättämällä kentän tyhjäksi, jolloin päivämäärä asetetaan automaattisesti 10 päivän päähän.
