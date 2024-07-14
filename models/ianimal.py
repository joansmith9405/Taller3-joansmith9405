from abc import ABC,  abstractmethod

#La interfaces (iAnimal) :son clases que no tienen atributos y ninguno de sus métodos tiene implementación
#Adicionalmente, todos los métodos son abstractos
class iAnimal(ABC):
    @abstractmethod
    def comer(self, kilos):
        pass
    
    @abstractmethod
    def obtener_kilos_comidos(self):
        pass