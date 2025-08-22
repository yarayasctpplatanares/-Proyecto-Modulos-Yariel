# estadisticas.py
def media(datos):
    media_aritmetica = sum(datos) / len(datos)
    return media_aritmetica

def mediana(datos):
    datos = sorted(datos)
    n = len(datos)
    mitad = n // 2
    if n % 2 == 0:
        mediana_valor = (datos[mitad - 1] + datos[mitad]) / 2
    else:
        mediana_valor = datos[mitad]
    return mediana_valor

if __name__ == "__main__":
    notas = [100,50,100,78,100]
    compras = {'articulo1': 100, 'articulo2': 50, 'articulo3': 100, 'articulo4': 78, 'articulo5': 100}
    print(mediana(list(compras.values())))
    mediana_valor = mediana(list(compras.values()))
    print('mediana de costo por articulos: ', mediana_valor)