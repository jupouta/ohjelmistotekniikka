import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_saldo_on_oikein(self):
        self.assertEqual(str(self.maksukortti), 'saldo: 0.1')
    
    def test_saldon_kasvatus_kasvattaa_oikein(self):
        self.maksukortti.lataa_rahaa(300)
        self.assertEqual(str(self.maksukortti), 'saldo: 3.1')
    
    def test_saldo_vahenee_jos_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), 'saldo: 0.05')
    
    def test_saldo_ei_vahene_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(50)
        self.assertEqual(str(self.maksukortti), 'saldo: 0.1')
    
    def test_ota_rahaa_tosi_jos_rahat_riittivat(self):
        tulos = self.maksukortti.ota_rahaa(5)
        self.assertTrue(tulos)
    
    def test_ota_rahaa_epatosi_jos_rahaa_ei_tarpeeksi(self):
        tulos = self.maksukortti.ota_rahaa(50)
        self.assertFalse(tulos)