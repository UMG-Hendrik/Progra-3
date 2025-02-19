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

        #elif opcion == "3":
           # num = int(input("Ingrese un número entero positivo: "))
           # print(f"Raíz cuadrada entera: {raiz_cuadrada_entera(num)}")

        #elif opcion == "4":
           # romano = input("Ingrese un número romano en mayúsculas: ")
            #print(f"Decimal: {convertir_a_decimal(romano)}")

        elif opcion == "5":
            num = int(input("Ingrese un número entero positivo: "))
            print(f"Suma de números enteros: {suma_de_enteros(num)}")

        elif opcion == "6":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, intente de nuevo.")

menu()