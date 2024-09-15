def bubbleSort(array):
    
    n = len(array)
    for i in range(n):
        
        for j in range(0, n - i - 1):
            
            if array[j] > array[j + 1]:
                
                array[j], array[j + 1] = array[j + 1], array[j]


import random

array_numeros = [random.randint(1, 100) for _ in range(15)]
print("Array original:", array_numeros)


bubbleSort(array_numeros)

print("Array ordenado:", array_numeros)