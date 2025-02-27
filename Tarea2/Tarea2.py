#CONVERTIR A BINARIO
def convetir_a_binario(numero):
 if numero == 0: #verifica si numero es 0 y no se hace nada mas y se devuelve 0 como resultado (caso base)
  return "0" #el que detiene la recursion/devuelve o como cadena
 if numero ==1: #verifica si es numero 1 y si es lo devuelve 
  return "1" #devuelve 1 como cadena
 return convetir_a_binario(numero//2)+str(numero%2) #recursion - division y residuo, ejemplo: 5 // 2 = 2, 5 % 2 = 1 → El residuo es 1.


#CONTADOR DIGITOS
def contador_digitos(numero):
 if numero < 10: #caso base donde la recursion termina y evalua si es menor que el 10 para sacar el numero
  return 1  #devuelve  1 que es 1 digito cada que cuenta
 return 1+ contador_digitos(numero//10) #recursividad elimina el ultimo digito del numero que se logra con la division entre 10 y entonces en este caso se hacen 5 divisiones por lo que se logra obtener la cantidad original de numeros.

#RAIZ CUADRADA ENTERA:
def calcular_raiz_cuadrada(numero, min_val, max_val):
    if min_val > max_val:
        return max_val  # Se mantiene igual porque max_val es la mejor aproximación entera

    mid = (min_val + max_val) // 2
    mid_squared = mid * mid  

    if mid_squared == numero:
        return mid
    elif mid_squared < numero:
        return calcular_raiz_cuadrada(numero, mid + 1, max_val)
    else:
        return calcular_raiz_cuadrada(numero, min_val, mid - 1)

def raiz_cuadrada_entera(numero):
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return calcular_raiz_cuadrada(numero, 0, numero)

#Numero a Romano 
def valores_romanos():
    return {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def convertir_a_decimal(romano, index=0):
    valores = valores_romanos()  # Obtiene los valores romanos
    if index >= len(romano):  # Caso base: si se recorrió toda la cadena
        return 0
    
    actual = valores[romano[index]]  # Valor del símbolo actual
    if index < len(romano) - 1:  # Si hay un siguiente símbolo
        siguiente = valores[romano[index + 1]]  # Valor del siguiente símbolo
        if actual < siguiente:  # Regla de sustracción (ej. IX = 9)
            return -actual + convertir_a_decimal(romano, index + 1)

    return actual + convertir_a_decimal(romano, index + 1)  # Suma normal


#SUMA DE ENTEROS
def suma_de_enteros(n):
 if n == 0: #numero es 0, la suma es 0 (caso base)
  return 0  #detiene la recursion y retorna 0
 return n+ suma_de_enteros(n-1) #se va restando 1 al número N hasta llegar a 0

def menu():
    while True:
        print("\n******* MENU PRINCIPAL ***********")
        print("1. Convertir a Binario")
        print("2. Contador de Dígitos")
        print("3. Raíz Cuadrada Entera")
        print("4. Convertir a Decimal desde Romano")
        print("5. Suma de Enteros")
        print("6. SALIR")
        
        opcion = input("SELECCIONE UNA OPCIÓN: ")

        if opcion == "1":
            num = int(input("Ingrese un número entero: "))
            print(f"Binario: {convetir_a_binario(num)}")
        
        elif opcion == "2":
            num = int(input("Ingrese un número entero: "))
            print(f"Cantidad de dígitos: {contador_digitos(num)}")

        elif opcion == "3":
           num = int(input("Ingrese un número entero positivo: "))
           print(f"Raíz cuadrada entera: {raiz_cuadrada_entera(num)}")

        elif opcion == "4":
            romano = input("Ingrese un número romano en mayúsculas: ")
            print(f"Decimal: {convertir_a_decimal(romano)}")

        elif opcion == "5":
            num = int(input("Ingrese un número entero positivo: "))
            print(f"Suma de números enteros: {suma_de_enteros(num)}")

        elif opcion == "6":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, intente de nuevo.")

menu()