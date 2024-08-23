print(" Sistema de control vacacional Rappi ")
nombre = input("¿Cuál es tu nombre?: ")
clave = int(input("¿Cuál es tu clave?: "))
años = float(input("¿Cuántos años tienes en Rappi?: "))

if clave == 1:
    
    if años == 1:
        print(nombre + " tienes derecho a 6 días de vacaciones.")
    elif años > 1 and años < 7:
         print(nombre + " tienes derecho a 14 días de vacaciones.")
    elif años >= 7:
         print(nombre + " tienes derecho a 20 días de vacaciones.")
    else:
         print(nombre + " sin derecho a vacaciones.")
         
elif clave == 2:
    
    if años == 1:
         print(nombre + " tienes derecho a 7 días de vacaciones.")
    elif años > 1 and años < 7:
         print(nombre + " tienes derecho a 15 días de vacaciones.")
    elif años >= 7:
         print(nombre + " tienes derecho a 22 días de vacaciones.")

    else:
         print(nombre + " sin derecho a vacaciones.")
         
elif clave == 3:
    
    if años == 1:
         print(nombre + " tienes derecho a 10 días de vacaciones.")
         
    elif años > 1 and años < 7:
         print(nombre + " tienes derecho a 20 días de vacaciones.")
         
    elif años >= 7:
         print(nombre + " tienes derecho a 30 días de vacaciones.")
         
    else:
         print(nombre + " sin derecho a vacaciones.")

else:
    print("La clave no existe.")

    
