Dato_Recibido = int(input("Bienvenido, ingrese el límite de la sucesión Multiplicativa: "))
Limite = 0
Limite = (Limite + Dato_Recibido) * 2
indice = 2
Sucesion = 0
MultiplicacionTotal = 1

while indice < Limite:
    Sucesion = Sucesion + 2
    MultiplicacionTotal = MultiplicacionTotal * Sucesion
    print(Sucesion, end=' * ')
    indice += 2

print(f"La Multiplicación total es: {MultiplicacionTotal}")