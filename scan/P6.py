def ingresar_lista_numeros():
    global numeros_lista
    numeros = input("Ingresa los números separados por espacios: ")
    numeros_lista = numeros.split()
    numeros_lista = [int(num) for num in numeros_lista]  # Convertir los elementos a enteros
    return numeros_lista

def suma_y_multiplicacion(numeros_lista):
    suma = sum(numeros_lista)
    multiplicacion = 1
    for num in numeros_lista:
        multiplicacion *= num
    return suma, multiplicacion

# Ejemplo de uso
lista_numeros = ingresar_lista_numeros()
print(lista_numeros)

# Ejemplo de uso
resultado_suma, resultado_multiplicacion = suma_y_multiplicacion(lista_numeros)
print("Suma:", resultado_suma)
print("Multiplicación:", resultado_multiplicacion)
