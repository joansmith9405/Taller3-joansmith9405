from models.animal_exotico import Animal_Exotico
from models.ianimal import iAnimal

class Huron(Animal_Exotico,iAnimal):
   
    #Metodo que se hereda de la clase hija animal_exotico y  a su vez de la superclase Animal     
    def hacer_sonido(self):
        return "Eek Eek"