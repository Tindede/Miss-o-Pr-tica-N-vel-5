import random

array = [random.randint(1, 100) for _ in range(15)]
print("Array original:", array)

def selectionSort(array):
   
    n = len(array)
    for i in range(n):
        
        min_index = i
        for j in range(i + 1, n):
            
            if array[j] < array[min_index]:
                
                min_index = j
        
       
        array[i], array[min_index] = array[min_index], array[i]


selectionSort(array)


print("Array ordenado:", array)