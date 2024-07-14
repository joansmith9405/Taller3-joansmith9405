from animal import Animal
from ianimal import iAnimal
from boa_constrictor import Boa_Constrictor
from huron import Huron

boa1=Boa_Constrictor("Tatan",35,5,"Colombia",2500)

print("La Boa con el nombre de:",boa1.obtener_nombre() , "Ha comido :" ,  boa1.obtener_ratones_comidos(), "ratones")
boa1.agregar_ratones_comidos()
print("la Boa comio de nuevo:", boa1.obtener_ratones_comidos(), "Ratones")
print("la Boa hace ", boa1.hacer_sonido())


huron1=Huron("Cafu",3.5,1,"Australia",1050)
print("El Huron con el nombre de: " , huron1.obtener_nombre() , "hace" , huron1.hacer_sonido())