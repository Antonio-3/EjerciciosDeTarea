Dato_Recibido = int(input("Bienvenido, ingrese el limite de la suma sigma: "))
Limite = int(0)
Limite = Limite + Dato_Recibido
indice = int(0)
Cubo = int(0)
SumaTotal = int(0)

for indice in range(1,Limite+1):
    Cubo = (indice)*(indice)*(indice)
    SumaTotal = SumaTotal + Cubo
    print(Cubo, end=' + ')

print(f"La suma sigma total es : {SumaTotal}")