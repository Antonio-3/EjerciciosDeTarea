num1 = int(input("Ingrese el primer número entero positivo: "))
num2 = int(input("Ingrese el segundo número entero positivo: "))
producto = 0

for i in range(num2):
    producto += num1
    
print(f"El producto de {num1} y {num2} es: {producto}")