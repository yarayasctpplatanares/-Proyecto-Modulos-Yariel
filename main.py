# Proyecto: [Modulos y funciones]
# Estudiante: [Yariel Araya]
# Fecha de Inicio: [22/8/2025]
# Fecha de Entrega: [dd/mm/aaaa]
# Descripción: Este archivo contiene el punto de entrada principal del proyecto.
# Recuerda incluir tu nombre completo, la fecha en la que iniciaste el proyecto y la fecha estimada de entrega.
# Esto ayuda a mantener un registro claro del trabajo realizado.
from analisis_datos.carga_datos import generar_lista_compras
from analisis_datos.estadisticas import media

from analisis_datos
def saludar():
    print("¡Hola desde la funcion .")
    
if __name__ == "__main__":
    compras = generar_lista_compras()
    print(compras)
    media = media(list(compras.values()))
    print('promedio de costo por articulso: ', media)
    
    
