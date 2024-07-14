from models.boa_constrictor import Boa_Constrictor

class Guarderia(Boa_Constrictor):
    def __init__(self, nombre:str, peso:float, edad:int, pais_origen:str, impuestos:str) -> None:
        pass
    boas = [None]

    def alimentar_boa(self, boa:Boa_Constrictor):
        try:
            if boa is None:
                raise ValueError("Esta Boa no existe!")
            else:
                Boa_Constrictor.agregar_ratones_comidos()
                return "Éxito"
        except AttributeError:
            return "La boa está llena"
        except ValueError as e:
            return str(e)
