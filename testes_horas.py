from horas import horas_para_minutos, horas_para_segundos
import unittest


class TestHoras(unittest.TestCase):
   
    def test_1_hora_em_minutos(self):
        minutos = horas_para_minutos(1)
        esperado = 60
        self.assertEqual(esperado, minutos, "para 1 hora devia retornar 60 minutos")
    
    def test_0_hora_em_minutos(self):
        minutos = horas_para_minutos(0)
        esperado = 0
        self.assertEqual(esperado, minutos, "para 0 horas devia retornar 0 minutos")

    def test_10_horas_em_minutos(self):
        minutos = horas_para_minutos(10)
        esperado = 600
        self.assertEqual(esperado, minutos, "para 10 horas devia retornar 0 minutos")

    def test_1_horas_em_segundos(self):
        segs = horas_para_segundos(1)
        esperado = 3600
        self.assertEqual(esperado, segs, "para 1 hora devia retornar 3600 segundos")

    def test_10_horas_em_segundos(self):
        segs = horas_para_segundos(10)
        esperado = 36000
        self.assertEqual(esperado, segs, "para 10 horas devia retornar 36000 segundos")

unittest.main()