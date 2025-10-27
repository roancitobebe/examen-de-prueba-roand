edad = int(input("cual es tu edad papa: "))
estudiante =(input(" ¿eres estudiante? si/no : "))
if edad >= 13 and edad <= 64 and estudiante.lower() == "no" :
    print("pagas 12$ papa")
elif edad <= 12 and estudiante.lower() == "no"  :
    print("pagas 7$ lukitas peque")
elif edad >= 65 and estudiante.lower() == "no" :
    print("papa ya tercera edad pagas 8$")
elif  edad >= 13 and edad <= 64 and estudiante.lower() == "si" :
    print("papa págas 9$ lukitas")
else :
    print("pon la vaina bien mano")