from abc  import ABC, abstractmethod
from models.ianimal import iAnimal

class Animal(iAnimal):
    
    def __init__(self, nomnbre:str, peso:float, edad:int) -> None:
        self._nombre= nomnbre
        self._peso = peso
        self._edad = edad
        self._kilos_comidos= 0
    
    def comer(self, kilos):
        self._kilos_comidos+=kilos
        
    def obtener_kilos_comidos(self):
        return self._kilos_comidos 
      
    @abstractmethod
    def hacer_sonido(self):
         pass
     #Pass -le indica al programa que ignore esa condición y continúe ejecutando el programa como de costumbre.
            
    
    def obtener_nombre(self) :
        return self._nombre
    
    def obtener_peso(self) :
        return self._peso
    
    def obtener_edad(self):
        return self._edad
        
   