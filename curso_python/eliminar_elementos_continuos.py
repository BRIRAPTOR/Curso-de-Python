Lista = ["A", "B", "b", "c", "E", "E", "f"]
print(f"Lista original: {Lista}")
del_elemento = input("Introduce el elemento que deséas eliminar: ")
for i in Lista.copy():
    if i.lower() == del_elemento.lower():
        Lista.remove(i)
print(f"Elemento eliminado: {Lista}")

