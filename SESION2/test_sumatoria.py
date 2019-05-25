from unittest import TestCase
from sumatoria import *
from datetime import datetime

class TestSumatoria(TestCase):

    def test_sumatoria(self):
        ahora=datetime.now()
        print(f'El algoritmo empezo {ahora}')
        dado=1000000000
        espero=500000000500000000
        realmente=sumatoria(dado)
        despues=datetime.now()
        print(f'el algoritmo terminó {despues}')
        self.assertEqual(espero,realmente)

    # def test_sumatoria(self):
    #     ahora=datetime.now()
    #     print(f'El algoritmo empezo {ahora}')
    #     dado=1000000000
    #     espero=500000000500000000
    #     realmente=sumatoria_v2(dado)
    #     despues=datetime.now()
    #     print(f'el algoritmo terminó {despues}')
    #     self.assertEqual(espero,realmente)