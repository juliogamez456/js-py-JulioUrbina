import random

def generar_numeros_aleatorios(cantidad, minimo, maximo):
    """Genera una lista de números aleatorios dentro de un rango dado."""
    return [random.randint(minimo, maximo) for _ in range(cantidad)]

def calcular_suma(numeros):
    """Calcula la suma de una lista de números."""
    return sum(numeros)

def main():
    """Función principal que genera números aleatorios, calcula su suma y muestra los resultados."""
    while True:
        try:
            cantidad = int(input("¿Cuántos números aleatorios quieres generar? "))
            minimo = int(input("Ingresa el valor mínimo: "))
            maximo = int(input("Ingresa el valor máximo: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor que cero.")
                continue
            if minimo > maximo:
                print("El valor mínimo no puede ser mayor que el máximo.")
                continue
            break
        except ValueError:
            print("Por favor, ingresa números enteros válidos.")

    numeros = generar_numeros_aleatorios(cantidad, minimo, maximo)
    suma = calcular_suma(numeros)

    print("\n Números generados:", numeros)
    print(f"➕ Suma total: {suma}")

if __name__ == "__main__":
    main()