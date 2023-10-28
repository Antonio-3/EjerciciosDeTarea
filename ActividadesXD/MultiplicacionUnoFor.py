Dato_Recibido = int(input("Bienvenido, ingrese el limite de la sucesion Multiplicativa: "))
Limite = int(0)
Limite = Limite + Dato_Recibido
indice = int(0)
Sucesion = int(0)
MultiplicacionTotal = int(1)

for indice in range(1,Limite):
    Sucesion = Sucesion + 1
    MultiplicacionTotal = MultiplicacionTotal * Sucesion
    print(Sucesion, end=' * ')

print(f"La Multiplicacion total es : {MultiplicacionTotal}")