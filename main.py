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
