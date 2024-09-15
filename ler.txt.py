
arquivo = open('loremipsum.txt', 'r')


conteudo = arquivo.read()


print("Todo o conteúdo do arquivo:")
print(conteudo)


arquivo.seek(0)  
primeira_linha = arquivo.readline()
print("\nPrimeira linha do arquivo:")
print(primeira_linha.strip())


arquivo.seek(0)  
tres_primeiros_caracteres = arquivo.read(3)
print("\nPrimeiros 3 caracteres do arquivo:")
print(tres_primeiros_caracteres)


arquivo.close()


with open('loremipsum.txt', 'r') as arquivo:
    conteudo_with = arquivo.read()


print("\nConteúdo do arquivo lido com 'with':")
print(conteudo_with)