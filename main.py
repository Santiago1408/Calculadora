print("Seleccione la operación que desea realizar: \n 1. Suma \n 2. Resta \n 3. Multiplicación \n 4. División")

operacion = input("Opereación: ")
import math
#Josue Garcia
def mult(num1, num2):
    return num1 * num2

def error():
    print("Hubo un error")

# Función para dividir dos números
def dividir_numeros(dividendo, divisor):
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero."
# María Laura Fernández Campos
# Milena Maya Torrico Santiestevez
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
resultado = num1 + num2
print(f"El resultado de la suma es: {resultado}")
#Juaquin Daniel Pickman Arce
def logaritmo(numero, base = 10):
    if numero > 0 and base > 0 and base != 1:
        return math.log(numero, base)
    else:
        return "Error: El número debe ser positivo y la base mayor que 0 y diferente de 1."
# Valeria Adriana Cabrera Chavarria 
def calcular_exponencial(base, exponente):
    resultado = base ** exponente
    print(f"{base}^{exponente} = {resultado}")
    return resultado


#funcion para sacar raiz de un numero 
#Maria Elena Bernabe
def calcular_raiz(numero):
    if numero < 0:
        return "No se puede calcular la raíz cuadrada de un número negativo"
    else:
        return math.sqrt(numero)

#Florencia Ramos Gamarra
#Resta
def resta(a, b):
    return a - b

try:
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))

    resultado = resta(numero1, numero2)
    print(f"La resta de {numero1} y {numero2} es: {resultado}")
    
except ValueError:
    print("Por favor, introduce un número válido.")

#Juan Adiel Butron
#El factorial de un numero
def Factorial(num):
    aux=1
    for i in range(1,num+1):
        aux=aux*i
    return aux

# GEOVANA RUTH QUISPE MAMANI 
# FUNCION PARA CALCULAR EL PORCENTAJE
def calcular_porcentaje(total, porcentaje):
    resultado = (porcentaje / 100) * total
    return resultado

#Alejandro Contreras
def llamar_funciones():
    print("Seleccione la operación que desea realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Factorial")
    print("6. Logaritmo")
    print("7. Exponencial")
    print("8. Raíz cuadrada")

    operacion = input("Operación: ")

    if operacion in ['1', '2', '3', '4']:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))

        if operacion == '1':
            resultado = num1 + num2  # Suma
            print(f"El resultado de la suma es: {resultado}")
        elif operacion == '2':
            resultado = resta(num1, num2)  # Resta
            print(f"La resta de {num1} y {num2} es: {resultado}")
        elif operacion == '3':
            resultado = mult(num1, num2)  # Multiplicación
            print(f"La multiplicación de {num1} y {num2} es: {resultado}")
        elif operacion == '4':
            resultado = dividir_numeros(num1, num2)  # División
            print(f"La división de {num1} entre {num2} es: {resultado}")
    elif operacion == '5':
        num = int(input("Introduce un número para calcular su factorial: "))
        resultado = factorial(num)
        print(f"El factorial de {num} es: {resultado}")
    elif operacion == '6':
        num = float(input("Introduce el número para el logaritmo: "))
        base = float(input("Introduce la base: "))
        resultado = logaritmo(num, base)
        print(f"El logaritmo de {num} en base {base} es: {resultado}")
    elif operacion == '7':
        base = float(input("Introduce la base: "))
        exponente = float(input("Introduce el exponente: "))
        calcular_exponencial(base, exponente)
    elif operacion == '8':
        num = float(input("Introduce el número para calcular su raíz cuadrada: "))
        resultado = calcular_raiz(num)
        print(f"La raíz cuadrada de {num} es: {resultado}")
    else:
        error()

if __name__ == "__main__":
    llamar_funciones()
