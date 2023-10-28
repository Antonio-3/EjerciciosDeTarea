Dato_Recibido = int(input("Bienvenido, ingrese el limite de la suma sigma: "))
Limite = 0
Limite = (Limite + Dato_Recibido) * 2
indice = 0
Suma = 0
SumaTotal = 0

while indice < Limite:
    Suma = Suma + 2
    SumaTotal = SumaTotal + Suma
    print(Suma, end=' + ')
    indice += 1

print(f"La suma sigma total es: {SumaTotal}")