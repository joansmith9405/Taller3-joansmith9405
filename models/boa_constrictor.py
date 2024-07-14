from models.animal_exotico import Animal_Exotico
from models.ianimal import iAnimal

class Boa_Constrictor(Animal_Exotico,iAnimal):
    def __init__(self, nombre:str, peso:float, edad:int, pais_origen:str, impuestos:str) -> None:
        super().__init__(nombre, peso, edad,pais_origen,impuestos)
        self.ratonescomidos=10
             
    def hacer_sonido(self):
        return "TS TSSS"
              
    def agregar_ratones_comidos(self):
        if self.ratonescomidos < 20:
           self.ratonescomidos += 1
        else:  
            raise ValueError("La Boa esta llena")   
    
    def obtener_ratones_comidos(self):
        return self.ratonescomidos
        
