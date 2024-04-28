lista = [1, 2, 3, 4, 5]
print(f"Lista números: {lista}")
list_del = []
list_del.append(lista.pop(0))
list_del.append(lista.pop())
print(f"Lista números: {lista}")
print(f"Lista números eliminados: {list_del}")