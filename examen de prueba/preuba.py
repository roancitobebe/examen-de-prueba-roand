puntos = int(input("cuantos puntos tienes papa : "))
objeto = input("¿cual es el objeto ssshhh? : ")
if puntos == 5000 and objeto.lower() == "bicho" :
    print("te abrimos las puertas del ano")
elif puntos == 5000 and objeto.lower() != "bicho" :
    print("papa tiene los puntos pero te falta un objeto")
elif puntos != 5000 and objeto.lower() == "bicho" :
    print("mira mano tienes el objeto pero papa te faltan los puntos")
else :
    print("papa sigue echandole te falta")