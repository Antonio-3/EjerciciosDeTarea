Dato_Recibido = int(input("Bienvenido, ingrese el limite de la suma sigma: "))
Limite = 0
Limite = Limite + Dato_Recibido
indice = 1
Cubo = 0
SumaTotal = 0

while indice <= Limite:
    Cubo = (indice) * (indice) * (indice)
    SumaTotal = SumaTotal + Cubo
    print(Cubo, end=' + ')
    indice += 1

print(f"La suma sigma total es : {SumaTotal}")