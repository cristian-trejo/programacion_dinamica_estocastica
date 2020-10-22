
# La clase guardara las coordenadas del borracho
class Coordenada:

    # Definimos las posiciones iniciales
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Metodo mover, el cual simplemente le sumara a las coordenadas iniciales
    # las coordenadas x & y que se ingresen como parametro
    def mover(self, delta_x, delta_y):
        return Coordenada(self.x + delta_x, self.y + delta_y)

    # Metodo para calcular la distancia de un borracho con respecto
    # a unas coordenas, utilizando el Teorema de Pitagoras.
    def distancia(self, otra_coordenada):
        delta_x = self.x - otra_coordenada.x
        delta_y = self.y - otra_coordenada.y

        return (delta_x**2 + delta_y**2)**0.5
