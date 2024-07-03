names = ("Luis", "Diego", "Andrés", "Carlos")
ages = [15, 30, 26, 12, 40]
text = "Geekipedia"

print(names)
print(ages)
print(text)

print("\nFunción zip() como iterable: \n")
conbination = zip(names, ages, text)
print(conbination)

print("\nFunción zip() con la función list(): \n")
conbination = list(zip(names, ages, text))
print(conbination)

print("\nFunción zip() con la función tuple(): \n")
conbination = tuple(zip(names, ages, text))
print(conbination)

print("\nFunción zip() con for: \n")
for name, age, text_1 in zip(names, ages, text):
    print(name, age, text_1)
