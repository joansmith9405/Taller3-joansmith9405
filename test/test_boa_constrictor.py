import unittest
from models.boa_constrictor import Boa_Constrictor
from models.animal_exotico import Animal_Exotico


class Test_Boa_Constrictor(unittest.TestCase):
    def test_hacer_sonido(self):
        boa = Boa_Constrictor("Petro",70,15,"Colombia",10.5)
        self.assertEqual(boa.hacer_sonido(), "TS TSSS")
        
        
    def test_calcular_flete(self):
        boa = Animal_Exotico("Petro",70,15,"Colombia",10)
        self.assertEqual(boa.calcular_flete(),700)   
        
    

    def test_agregar_ratones(self):
        boa = Boa_Constrictor("Petro",70,15,"Colombia",10.5)
        self.assertEqual(boa.agregar_ratones_comidos(),"Ratones OK")  