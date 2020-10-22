
from borracho import Borracho
from campo import Campo
from coordenada import Coordenada

def caminata(campo, borracho, pasoso):
    # De la instancia Campo obtenemos las coordenadas actuales de la llave "borracho"
    inicio = campo.obtener_coordenada(borracho)

    # Repetimos la cantidad de pasos definidos
    for _ in rango(pasos):
        # De la instancia campo ejecutamos mover_borracho
        campo.mover_borracho(borracho)

    # Devuelve la distancia entre las coordenadas de la instancia
    # inicio & campo
    return inicio.distancia(campo.obtener_coordenada(borracho))


def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):

    # Definimos los parametros para crear una instancia de Campo
    borracho = tipo_de_borracho(nombre='David')
    origen = Coordenada(0, 0)

    # Creamos una lista que guardara las distancias en cada simulacion
    distancias = []

    # Por cada numero de intento
    for _ in range(numero_de_intentos):
        # Se crea una instancia de Campo
        campo = Campo()
        # A la instancia de Campo se le pasa la llave borracho y sus coordenadas de origen
        campo.anadir_borracho(borracho, origen)
        # Obtiene la distancia final de la simulacion
        simulacion_caminata = caminata(campo, borracho, pasos)
        # El resultado lo guarda en la lista de distancias
        distancias.append(round(simulacion_caminata, 1))

    # Retorna la lista de distancias
    return distancias

def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    # Se crea una lista que giardara el promedio de la caminata
    distancias_media_por_caminata = []
    # Por cada item en la serie de caminata
    for paso in distancias_de_caminata:
        # Guardamos las distancias que generan todas las simulaciones definido en numero de intentos
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        # De la lista de distancias obtenemos la distancia promedio
        # 4 significa 3 decimales dentro de round
        distancia_media = round(sum(distancias) / len(distancia), 4)
        # De la lista de distancias obtenemos el maximo valor
        distancia_maxima = max(distancias)
        # De la lista de distancias obtenemos el menor valor
        distancia_minima = min(distancias)
        # Guardamos el promedio de la caminata en la lista de distancias_media_por_caminata.
        distancias_media_por_caminata.append(distancia_media)
        # Imprimimos los datos de la caminata actual
        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_maxima}')
        print(f'Min = {distancia_minima}')

if __name__ == '__main__':
    # Definimos cuantos pasos queremos que camine en cada serie.
    distancias_de_caminata = [10, 100, 1000, 10000]
    # Determinamos la cantidad de simulaciones que generara en cada serie
    numero_de_intentos 100
    # Ejecutamos el metodo main con los parametros definidos anteriormente
    # y pasamos la clase BorrachoTradicional
    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)
