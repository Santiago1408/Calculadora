def resta(a, b):
    return a - b

#Florencia Ramos Gamarra
try:
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))

    resultado = resta(numero1, numero2)
    print(f"La resta de {numero1} y {numero2} es: {resultado}")
    
except ValueError:
    print("Por favor, introduce un número válido.")