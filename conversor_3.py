def conversor (tipo_pesos, valor_dolar):
    pesos = input ("?Cuantos pesos " + tipo_pesos + " Tienes?:  ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $ " + dolares + " Dólares")

menu = """
Bienvenido al conversor de monedas

Opción 1 pesos Colombianos
Opción 2 pesos Argentino
Opción 3 pesos Mexicanos
Opción 4 Soles Peruanos

elije una opción
"""
opcion = input(menu)

if opcion == '1' :
    conversor("Colombianos", 3605) 

elif opcion == '2' :
    conversor("Argentinos", 80)
elif opcion == '3' :
    conversor("Mexicanos", 24)

elif opcion == '4' :
    conversor("Peruanos", 3.8) 

else:
    print ("Selecciona una opción valida 😡")