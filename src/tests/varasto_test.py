import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase
    def setUp(self):
        self.varasto = Varasto(10)

    def test_virh_setup(self):
        self.var = Varasto(-100, -100)

        self.assertAlmostEqual(self.var.tilavuus, 0.0)

        self.assertAlmostEqual(self.var.saldo, 0.0)

    def test_liikaa_setup(self):
        self.va = Varasto(10, 100)

        self.assertAlmostEqual(self.va.tilavuus, self.va.saldo)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_virheellinen_saldo(self):
        self.varasto.lisaa_varastoon(-100)

        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisaa_liikaa_saldoa(self):
        self.varasto.lisaa_varastoon(100)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_negatiivisen_ottaminen(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-100), 0.0)

    def test_maksimin_ottaminen(self):
        self.varasto.lisaa_varastoon(6)

        self.assertAlmostEqual(self.varasto.ota_varastosta(20), 6)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_str_palauttaa_oikean_merkkijonon(self):
        tulos = str(self.varasto)

        self.assertEqual(tulos, "saldo = 0, vielä tilaa 10")

