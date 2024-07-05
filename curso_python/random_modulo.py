import random
num = random.randint(1, 100)
print("num = random.randint(1, 100): ", num)

# random(), devuelve un número de punto flotante en el rango [0.0, 1.0]
num = random.random()
print("num = random.random(): ", num)

num = random.randrange(0, 100, 2)
print("num = random.randrange(0, 100, 2): ", num)
