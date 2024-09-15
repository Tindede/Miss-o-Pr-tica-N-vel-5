
arquivo = open('texto.txt', 'w')


texto = list()


texto.append("Esta é a primeira frase do arquivo.")
texto.append("Aqui temos a segunda frase.")
texto.append("Esta é a terceira frase que será escrita no arquivo.")
texto.append("E finalmente, a quarta e última frase.")


for frase in texto:
    arquivo.write(frase + '\n')  


arquivo.close()

print("Frases escritas com sucesso no arquivo 'texto.txt'.")