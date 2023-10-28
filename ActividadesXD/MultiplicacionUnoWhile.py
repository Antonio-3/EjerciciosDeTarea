Dato_Recibido = int(input("Bienvenido, ingrese el limite de la sucesión Multiplicativa: "))
Limite = 0
Limite = Limite + Dato_Recibido
indice = 1
Sucesion = 0
MultiplicacionTotal = 1

while indice < Limite:
    Sucesion = Sucesion + 1
    MultiplicacionTotal = MultiplicacionTotal * Sucesion
    print(Sucesion, end=' * ')
    indice += 1

print(f"La Multiplicación total es: {MultiplicacionTotal}")