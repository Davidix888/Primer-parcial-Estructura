 #Parcial Estructura de datos
class Nodo:
    def __init__(self, coeficiente, exponente):
        self.coeficiente = coeficiente
        self.exponente = exponente
        self.siguiente = None

class Polinomios:
    def __init__(self):
        self.nodo1 = None
        
    def ingresar_numeros(self, coeficiente):
        nodo_ingreso = Nodo(coeficiente, 0)
        nodo_ingreso.siguiente = self.nodo1
        self.nodo1 = nodo_ingreso
        self.ingresar_grados()

    def ingresar_grados(self):
        nodo_actual = self.nodo1
        grado = 0
        while nodo_actual:
            nodo_actual.exponente = grado
            grado += 1
            nodo_actual = nodo_actual.siguiente

    def mostrar_datos(self):
        nodo_actual = self.nodo1
        polinomio = ""
        while nodo_actual:
            if nodo_actual.coeficiente != 0:
                if nodo_actual.coeficiente > 0 and polinomio:
                    polinomio += "+" 
                elif nodo_actual.coeficiente < 0 and polinomio:
                    polinomio += "-"
                if abs(nodo_actual.coeficiente) != 1 or nodo_actual.exponente == 0:
                    polinomio += str(abs(nodo_actual.coeficiente))
                if nodo_actual.exponente > 0:
                    polinomio += "x"
                    if nodo_actual.exponente > 1:
                        polinomio += "^" + str(nodo_actual.exponente)
            nodo_actual = nodo_actual.siguiente
        print(polinomio)

def ingresar_datos(polinomio):
    coeficientes = float(input("Ingrese por orden los coeficientes del polinomio: "))
    polinomio.ingresar_numeros(coeficientes)

def sumar_polinomios(a, b):
    resultado = Polinomios()
    nodo_a = a.nodo1
    nodo_b = b.nodo1

    while nodo_a is not None or nodo_b is not None:
        coeficiente_a = 0 if nodo_a is None else nodo_a.coeficiente
        coeficiente_b = 0 if nodo_b is None else nodo_b.coeficiente
        coeficiente_suma = coeficiente_a + coeficiente_b

        resultado.ingresar_numeros(coeficiente_suma)

        if nodo_a:
            nodo_a = nodo_a.siguiente
        if nodo_b:
            nodo_b = nodo_b.siguiente

    return resultado

def menu():
    a = Polinomios()
    b = Polinomios()

    while True:
        print("Menu")
        print("1. Ingresar polinomio 1")
        print("2. Ingresar polinomio 2")
        print("3. Mostrar polinomios")
        print("4. Sumar polinomios")
        print("5. Salir")
        opcion = input("Ingrese la opcion que necesitas: ")
        match opcion:
            case '1':
                print("Ingresa los datos del polinomio a")
                ingresar_datos(a)
            case '2':
                print("Ingresa los datos del polinomio b")
                ingresar_datos(b)
            case '3':
                print("Primer polinomio:")
                a.mostrar_datos()
                print("Segundo polinomio:")
                b.mostrar_datos()
            case '4':
                print("La suma de los polinomios es:")
                resultado = sumar_polinomios(a, b)
                resultado.mostrar_datos()
            case '5':
                break
            case _:
                print("Opcion no valida")

menu()
