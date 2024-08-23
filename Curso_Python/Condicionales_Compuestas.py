print("Sistema para calcular el promedio de un alumno")
nombre = input("Para comenzar, ¿Cuál es tu nombre?: ")
cal_mate = float(input(nombre + " ¿Cuál es tu calificación en matematicas?: "))
cal_quimi = float(input(nombre + " ¿Cuál es tu calificación en química?: "))
cal_bio = float(input(nombre + " ¿Cuál es tu calificación en biologia?: "))
promedio = (cal_mate + cal_bio + cal_quimi)/3
if promedio >= 6:
   print('Felicidades ' + nombre + ' "aprobaste" con un promedio de: ', promedio)
   print('Felicidades ' + nombre + ' "aprobaste" con un promedio de: ', round(promedio, 2))

else:
    print("Lo sentimos " + nombre + " has 'reprobado' con un promedio de: " , promedio)
    print("Lo sentimos " + nombre + " has 'reprobado' con un promedio de: " , round(promedio, 1))
print("Fin.")   
