"""
nums_tuple = (1, 2, 3, 4, 5)
nums_tuple[1] = 10

info_tuple = ([1, 2, 3], {"uno": 1, "dos": 2}, (3, 2))
info_tuple[1] = 1
"""
info_tuple = ([1, 2, 3], {"uno": 1, "dos": 2}, (3, 2))
print(info_tuple)
info_tuple[0][1] = 99
print(info_tuple)
print()
info_tuple[1]['dos'] = 88
print(info_tuple)
