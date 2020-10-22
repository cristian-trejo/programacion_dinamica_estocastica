import random

class Borracho:

    # Inicializamos la clase borracho, recibiendo su nombre
    def __init__(self, nombre):
        self.nombre = nombre


class BorrachoTradicional(Borracho):
    # Inicializamos la clase borracho_tradicional que extiende de Borracho (super)
    def __init__(self, nombre):
        super().__init__(nombre)

    # Metodo que devolvera la direccion a la que ira
    def camina():
        # Con random.choce elige la direccion a donde movera el borracho
        # escogiendo un elemento aleatoriamente de la lista.

        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
