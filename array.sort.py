import random

array_numeros = [random.randint(1, 100) for _ in range(15)]
print("Array original (números inteiros):", array_numeros)

array_numeros.sort()
print("Array ordenado (crescente):", array_numeros)

array_numeros.sort(reverse=True)
print("Array ordenado (decrescente):", array_numeros)

array_strings = ['nome', 'dataNascimento', 'cpf', 'rg']
print("Array original (strings):", array_strings)

array_strings.sort()
print("Array ordenado (crescente):", array_strings)

array_strings.sort(reverse=True)
print("Array ordenado (decrescente):", array_strings)
