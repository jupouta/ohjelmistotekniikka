### Pakkauskaavio

![Pakkauskaavio](https://github.com/jupouta/ohjelmistotekniikka/blob/master/dokumentaatio/pakkauskaavio.jpg)


### Sekvenssikaavio

#### Kirjautuminen

Käyttäjä antaa kirjautuessaan käyttäjätunnuksen ja salasanan, jotka ovat esimerkissä 'testi' ja 'salis'.

![Sekvenssikaavio_kirjautumisesta](https://github.com/jupouta/ohjelmistotekniikka/blob/master/dokumentaatio/sekvenssikaavio_kirjautuminen.png)

Prosessi lähtee liikkeelle, kun käyttäjä painaa painiketta _Enter login_. Käyttöliittymä kutsuu ```FoodService```n metodia check_username, jolle annetaan parametreiksi saadut käyttäjätunnus ja salasana. ```FoodService``` taas kutsuu ```Database```n metodia get_user, joka tarkistaa, vastaavatko käyttäjätunnus ja salasana tietokannassa oleviin tietoihin. Jos ne vastaavat toisiaan, sekä ```Database``` että ```FoodService``` palauttavat ```True``, mikä aiheuttaa käyttöliittymän uudelleenrenderöinnin metodin show_after_login avulla.