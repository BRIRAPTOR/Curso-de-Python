texto = input('Ingrese un texto: ')
dic_text = {}
for letra in texto:
    dic_text.update({letra: texto.count(letra)})
print(dic_text)
