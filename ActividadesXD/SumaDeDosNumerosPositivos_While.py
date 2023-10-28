num1 = int(input("Ingrese el primer número entero positivo: "))
num2 = int(input("Ingrese el segundo número entero positivo: "))

# Inicializar el producto en 0
producto = 0

# Utilizar un bucle while para sumar num1 a sí mismo num2 veces
contador = 0
while contador < num2:
    producto += num1
    contador += 1

# Imprimir el resultado
print(f"El producto de {num1} y {num2} es: {producto}")