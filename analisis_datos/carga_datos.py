
import random
def generar_lista_compras():
    compras = {}
    canasta_basica = {
        'Arroz': 2000,
        'Frijoles': 1500,
        'Huevos':1300,
        'Aceite':2500,
        'Cerveza':1200,
        'Leche':1100,
        'Café':2100,
        'Chocolate':1400,
        'Atún': 500,
        'Sal':480,
        'Azucar':1250,
        'Numar': 198,
        'Pescado':6375,
        'Posta Cerdo': 3800,
        'Cereal':1200,
        'Galletas':995,
        'Pollo':2000,
        'Harina': 1050,
        'Masa':1480,
        'Coca Cola': 1400  
    }
    lista_seleccionada = random.sample(list(canasta_basica.keys()), k=5)
    #print(lista_seleccionada)
    
    for item in lista_seleccionada:
        compras[item] = canasta_basica[item]
    
    return compras


if __name__ == "__main__":
    lista_seleccionada = generar_lista_compras()
    # Example: iterate over the selected items
    for key in lista_seleccionada:
        print(f"Producto seleccionado: {key}")