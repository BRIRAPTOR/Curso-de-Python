frutas = ["manzana", "plátano", "uva", "sandía"]
print(frutas)

print("\nRecorrido con for: ")
for posicion, fruta in enumerate(frutas, start=101):
    print(f"Posición: {posicion} fruta: {fruta}")
print("\nConvertido a lista: ")
enumerado = list(enumerate(frutas))
print(enumerado)
