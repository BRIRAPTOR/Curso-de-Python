print("Sistema para calcular el promedio de un alumno")
nombre = input("Para comenzar, ¿Cuál es tu nombre?: ")
cal_mate = int(input(nombre + " ¿Cuál es tu calificación en matematicas?: "))
cal_quimi = int(input(nombre + " ¿Cuál es tu calificación en química?: "))
cal_bio = int(input(nombre + " ¿Cuál es tu calificación en biologia?: "))
promedio = (cal_mate + cal_bio + cal_quimi)/3
if promedio >= 6 :
   print('Felicidades ' + nombre + ' "aprobaste" con un promedio de: ', promedio)
print("Fin")   
