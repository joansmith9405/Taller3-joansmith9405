from models.animal import Animal
#from abc  import ABC, abstractmethod

class Animal_Exotico(Animal):
    def __init__(self, nombre:str, peso:float, edad:int, pais_origen:str, impuestos:str) -> None:
        super().__init__(nombre, peso, edad)
        self._pais_origen= pais_origen
        self._impuestos=impuestos
        
    def calcular_flete(self):
        return self._impuestos * self._peso    
    
    #@abstractmethod
    def hacer_sonido(self):
         pass