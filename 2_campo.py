
class Campo:

    # Inicializamos la clase Campo la cual tendra como atributo un diccionario
    def __init__(self):
        self.coordenadas_de_borrachos = {}

    # Metodo para agregar un borracho al diccionario
    def anadir_borracho(self, borracho, coordenada):
        # Cada borracho nuevo tendra sus coordenadas
        # Key = borracho value = coordenas
        self.coordenadas_de_borrachos[borracho] = coordenadas_de_borrachos

    def mover_borracho(self, borracho):
        # Cuando el borracho camina regresa las coordenadas de hacia donde se movera
        # y los deltas seran las nuevas coordenadas
        delta_x, delta_y = borracho.camina()
        # Obtenemos las coordenas actuales del borracho
        coordenada_actual = self.coordenadas_de_borrachos[borracho]
        # Atualizamos la posicion del borracho en el campo
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)

        # Guardamos la nueva posicion en el diccionario
        self.coordenadas_de_borrachos[borracho] = nueva_coordenada

    # Metodo para consultar la posicion actual de un borracho
    def obtener_coordenada(self, borracho):
        # Util para calcular la distancia al objetivo
        return self.coordenadas_de_borrachos[borracho]
