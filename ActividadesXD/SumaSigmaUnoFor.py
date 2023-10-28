Dato_Recibido = int(input("Bienvenido, ingrese el limite de la suma sigma: "))
Limite = int(0)
Limite = (Limite + Dato_Recibido)*2
indice = int(0)
Suma = int(0)
SumaTotal = int(0)

for indice in range(Limite):
    Suma= Suma+2
    SumaTotal = SumaTotal + Suma
    print(Suma, end=' + ')

print(f"La suma sigma total es : {SumaTotal}")