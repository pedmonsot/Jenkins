import unittest
from detection import es_maliciosa

class TestDetector(unittest.TestCase):
    def test_maliciosa(self):
        self.assertTrue(es_maliciosa("192.168.1.10"))

    def test_segura(self):
        self.assertFalse(es_maliciosa("8.8.8.8"))

    def test_falla_controlada(self):
    self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()

