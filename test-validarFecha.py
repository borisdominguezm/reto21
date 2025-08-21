import unittest
from validarFecha import validar_fecha  

class TestValidarFecha(unittest.TestCase):
    def test_fecha_valida(self):
        self.assertTrue(validar_fecha("2025-08-20"))

    def test_fecha_invalida_dia(self):
        self.assertFalse(validar_fecha("2025-02-30"))

    def test_fecha_invalida_mes(self):
        self.assertFalse(validar_fecha("2025-13-01"))

    def test_fecha_invalida_formato(self):
        self.assertFalse(validar_fecha("20-08-2025"))

if __name__ == "__main__":
    unittest.main()
