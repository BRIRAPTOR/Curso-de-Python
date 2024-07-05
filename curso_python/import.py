# Importar un modulo completo
import math
# Importar un modulo con un alias
import math as m
# Importar solo lo necesario de un modulo
from math import sqrt, sin
# Importar todo de un modulo
from math import *
print("Importar un modulo completo")
print(math.sqrt(25))
print(math.sin(30))

print("Importar un modulo con alias")
print(m.sqrt(25))
print(m.tan(30))

print("Importar solo lo necesario de un modulo")
print(sqrt(25))
print(sin(30))

# Importar todo de un modulo
print("Importar todo de un modulo")
print(sqrt(25))
print(sin(30))
print(tan(30))
