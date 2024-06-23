fruits = {
    "manzanas": 4,
    "peras": 2,
    "naranjas": 4,
    "plátano": 5
}
print(fruits)
bandera = 0
for key, value in fruits.items():
    if key == "peras":
        bandera = 1

if bandera == 1:
    print("true")
else:
    print("false")


