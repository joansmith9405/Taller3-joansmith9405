import unittest
from models.huron import Huron
from models.animal_exotico import Animal_Exotico


class Test_Huron(unittest.TestCase):
    def test_hacer_sonido(self):
        huron = Huron("Petro",70,15,"Colombia",10.5)
        self.assertEqual(huron.hacer_sonido(), "Eek Eek")
        
        
    def test_calcular_flete(self):
        huron = Animal_Exotico("Petro",70,15,"Colombia",10)
        self.assertEqual(huron.calcular_flete(),700)   