#from graphviz import Digraph


class Nodo:
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre  #campo/atributo guarda el nombre - lo que recibimos
        self.apellido = apellido #campo/atributo guarda el apellido
        self.carnet = carnet #campo/atributo guarda el carnet 
        self.siguiente = None  #PUNTERO AL SIGUIENTE NODO
        self.anterior = None   #PUNTERO AL NODO ANTERIOR

    def mostrar(self):
        return f"[{self.nombre} {self.apellido}, Carnet: {self.carnet}]"

class ListadoblementeEnlazada:
    def __init__(self): #instancia de clase self, constructor
        self.inicio = None #primer nodo de la lista/cabeza
        self.ultimo = None #ultimo nodo de la lista/cola

#metodo Insertar al princio: se encarga de agregar un nuevo nodo al inicio de la lista doblemente enlazada

    def insertar_al_principio(self, nombre, apellido, carnet):
        nuevo_nodo = Nodo(nombre, apellido, carnet) #nuevo nodo con datos proporcionados  #se enlaza el nuevo nodo que actualmente es el primer nodo, donde si la lista esta vacia, self.inici es None, por lo que nuevo_nodo.siguiente, tambien será none.
        if self.inicio is None:
            self.inicio = nuevo_nodo
            self.ultimo = nuevo_nodo   #todo es si la lista esta vacia, self.inicio es none, el nuevo nodo ahora sera el primer y ultimo nodo de la lista.
        else:
            nuevo_nodo.siguiente = self.inicio #enlaza el nuevo nodo con la cabeza actual
            self.inicio.anterior = nuevo_nodo  #el nodo actual apunta hacia atras al nuevo nodo
            self.inicio = nuevo_nodo    # El nuevo nodo se convierte en el primer nodo de la lista

    def insertar_al_final(self, nombre, apellido, carnet):
        nuevo_nodo = Nodo(nombre, apellido,carnet) #nuevo nodo de datos 
        if self.inicio is None: #si la lista esta vacia, self.inicio is none, el nuevo nodo sera el primer y ultimo nodo de la lista
            self.inicio = nuevo_nodo
            self.ultimo = nuevo_nodo  #ambos apuntan al mismo nodo.
        else:
            nuevo_nodo.anterior = self.ultimo  #como en el anterior, si la lista No ESTA VACIA se conecta el ultimo nodo actual con el nuevo nodo.
            self.ultimo.siguiente = nuevo_nodo   #el nuevo nodo señala atras al que era el ultimo nodo.
            self.ultimo = nuevo_nodo #el nuevo nodo ahora es el ultimo nodo.
        
    # Metodo Eliminar por valor
    def eliminar_por_valor(self, carnet):
        actual = self.inicio
        if actual is None:
            print("No hay elementos para eliminar")
        else:
            while actual:
                if actual.carnet == carnet:
                    if actual.anterior is not None:
                        actual.anterior.siguiente = actual.siguiente
                    else:
                        self.inicio = actual.siguiente
                    if actual.siguiente is not None:
                        actual.siguiente.anterior = actual.anterior
                    else:
                        self.ultimo = actual.anterior
                    del actual
                    print(f"Carnet {carnet} eliminado de la lista")
                    if self.inicio is None:
                        self.ultimo = None
                    self.visualizar("lista_doble") 
                    return
                actual = actual.siguiente
            print(f"Carnet {carnet} no encontrado.")

    # Metodo Mostrar lista
    def mostrar_lista(self):
        actual = self.inicio
        resultado = "None <- "
        while actual:
            resultado += actual.mostrar() + " <-> "  #correcto
            actual = actual.siguiente
        resultado += "None"
        print(resultado)

    # Metodo Visualizar lista con Graphviz
    def visualizar(self, filename="lista_doble"):
        dot = Digraph(format="png")
        dot.attr(rankdir="LR")  # Dirección de izquierda a derecha
        actual = self.inicio

        while actual:
            dot.node(str(id(actual)), actual.mostrar())  # Crear nodo con información
            if actual.siguiente:
                dot.edge(str(id(actual)), str(id(actual.siguiente)), dir="both")  # Conexión doble
            actual = actual.siguiente

        dot.render(filename, view=True)  # Guarda la imagen y la abre automáticamente

# Función del menú
def menu():
    lista = ListadoblementeEnlazada()
    while True:
        print("\nMenú:")
        print("1. Insertar al principio")
        print("2. Insertar al final")
        print("3. Eliminar por valor")
        print("4. Mostrar lista")
        print("5. Visualizar lista (Graphviz)")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            carnet = input("Carnet: ")
            lista.insertar_al_principio(nombre, apellido, carnet)
        elif opcion == "2":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            carnet = input("Carnet: ")
            lista.insertar_al_final(nombre, apellido, carnet)
        elif opcion == "3":
            carnet = input("Carnet a eliminar: ")
            lista.eliminar_por_valor(carnet)
        elif opcion == "4":
            lista.mostrar_lista()
        elif opcion == "5":
            lista.visualizar("lista_doble")
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()