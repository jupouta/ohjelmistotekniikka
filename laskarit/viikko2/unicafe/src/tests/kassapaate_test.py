import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(500)
    
    def test_kassan_saldo_on_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_lounaita_ei_viela_myyty(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_syo_edullisesti_kateisella_kasvattaa_saldoa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_syo_edullisesti_kateisella_palauttaa_vaihdon(self):
        maksu = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(maksu, 60)
    
    def test_syo_edullisesti_kateisella_kasvattaa_lounaita(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 2)
    
    def test_syo_edullisesti_kateinen_ei_riita_ja_saldo_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_syo_edullisesti_kateinen_ei_riita_ja_rahat_palautetaan(self):
        maksu = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(maksu, 200)
    
    def test_syo_edullisesti_kateinen_ei_riita_ja_lounaat_eivat_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_syo_maukkaasti_kateisella_kasvattaa_saldoa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_syo_maukkaasti_kateisella_palauttaa_vaihdon(self):
        maksu = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(maksu, 100)
    
    def test_syo_maukkaasti_kateisella_kasvattaa_lounaita(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 2)
    
    def test_syo_maukkaasti_kateinen_ei_riita_ja_saldo_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_syo_maukkaasti_kateinen_ei_riita_ja_rahat_palautetaan(self):
        maksu = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(maksu, 300)
    
    def test_syo_maukkaasti_kateinen_ei_riita_ja_lounaat_eivat_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_syo_edullisesti_kortilla_kortin_saldo_oikein(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 260)
    
    def test_syo_edullisesti_kortilla_palauttaa_true(self):
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertTrue(tulos)
    
    def test_syo_edullisesti_kortilla_kasvattaa_lounaita(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_syo_edullisesti_ei_rahaa_ei_muuta_kortin_saldoa(self):
        self.maksukortti.saldo = 200
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 200)
    
    def test_syo_edullisesti_ei_rahaa_ei_kasvata_lounaita(self):
        self.maksukortti.saldo = 200
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_syo_edullisesti_ei_rahaa_palauttaa_false(self):
        self.maksukortti.saldo = 200
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertFalse(tulos)
    
    def test_syo_edullisesti_kortilla_ei_muuta_kassan_saldoa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_syo_maukkaasti_kortilla_kortin_saldo_oikein(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 100)
    
    def test_syo_maukkaasti_kortilla_palauttaa_true(self):
        tulos = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertTrue(tulos)
    
    def test_syo_maukkaasti_kortilla_kasvattaa_lounaita(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_syo_maukkaasti_ei_rahaa_ei_muuta_kortin_saldoa(self):
        self.maksukortti.saldo = 350
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 350)
    
    def test_syo_maukkaasti_ei_rahaa_ei_kasvata_lounaita(self):
        self.maksukortti.saldo = 350
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_syo_maukkaasti_ei_rahaa_palauttaa_false(self):
        self.maksukortti.saldo = 350
        tulos = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertFalse(tulos)
    
    def test_syo_maukkaasti_kortilla_ei_muuta_kassan_saldoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_rahan_lataus_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(str(self.maksukortti), 'saldo: 10.0')
    
    def test_rahan_lataus_kassan_saldo_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)
    
    def test_negatiivinen_summa_ei_kasvata_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)