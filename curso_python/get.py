fruits_dict = {'apple': 1.55,
               'banana': 3.55,
               'orange': 1.25
               }
print(f"Dictionary: {fruits_dict}")

precio_manzana = fruits_dict.get("apple")
print(f"Precio Manzana: {precio_manzana}")

precio_mango = fruits_dict.get("mango")
print(f"Precio Mango: {precio_mango}")

precio_mango = fruits_dict.get("mango", 4.55)
print(f"Precio Mango: {precio_mango}")
