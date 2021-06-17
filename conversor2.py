menu = """
Bienvenido al conversor de monedas

Opción 1 pesos Colombianos
Opción 2 pesos Colombianos
Opción 3 pesos Colombianos
Opción 4 Soles Peruanos

elije una opción

"""
opcion = input(menu)

if opcion == '1' :
    pesos = input ("?Cuantos pesos Colombianos Tienes?:  ")
    pesos = float(pesos)
    valor_dolar = 3607
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $ " + dolares + " Dólares")

elif opcion == '2' :
    pesos = input ("?Cuantos pesos Agentinos Tienes?:  ")
    pesos = float(pesos)
    valor_dolar = 94.89
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $ " + dolares + " Dólares")

elif opcion == '3' :
    pesos = input ("?Cuantos pesos Mexicanos Tienes?:  ")
    pesos = float(pesos)
    valor_dolar = 19.84
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $ " + dolares + " Dólares")

elif opcion == '4' :
    pesos = input ("?Cuantos Soles Peruanos Tienes?:  ")
    pesos = float(pesos)
    valor_dolar = 3.84
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $ " + dolares + " Dólares")

else:
    print ("Selecciona una opción valida")

