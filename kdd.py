import time

def bubbleSort(arr):
    
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selectionSort(arr):
   
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def main():
    
    palavras = []
    with open('texto.txt', 'r') as arquivo:
        for linha in arquivo:
            palavras.extend(linha.split())

    
    palavras_bubble = palavras.copy()
    start_time = time.time()
    bubbleSort(palavras_bubble)
    end_time = time.time()
    print("Palavras ordenadas com Bubble Sort:")
    print(palavras_bubble)
    print(f"Tempo de execução do Bubble Sort: {end_time - start_time:.6f} segundos")

    
    palavras_selection = palavras.copy()
    start_time = time.time()
    selectionSort(palavras_selection)
    end_time = time.time()
    print("\nPalavras ordenadas com Selection Sort:")
    print(palavras_selection)
    print(f"Tempo de execução do Selection Sort: {end_time - start_time:.6f} segundos")

    
    palavras_sort = palavras.copy()
    start_time = time.time()
    palavras_sort.sort()
    end_time = time.time()
    print("\nPalavras ordenadas com o método sort():")
    print(palavras_sort)
    print(f"Tempo de execução do sort(): {end_time - start_time:.6f} segundos")

    
    with open('palavras_ordenadas.txt', 'w') as arquivo:
        for palavra in palavras_sort:
            arquivo.write(palavra + '\n')

    print("\nPalavras ordenadas salvas em 'palavras_ordenadas.txt'.")

if __name__ == "__main__":
    main()