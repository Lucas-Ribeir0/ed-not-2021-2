#    ALGORITMO DE ORDENAÇÃO QUICK SORT

#    Escolhe um dos elementos da lista para ser o pivô (na nossa implementação,
#    o último elemento) e, na primeira passada, divide a lista, a partir da posição
#    final da lista, em um sublsita à esquerda contendo apenas valores menores que
#    o pivô e outra sublista à direita, que contém apenas valores maiores que o pivô.
#    
#    Em seguida, recursivamente, repete o processo em cada um das sublistas até que
#    todo a lista esteja ordenado.

passadas = 0 
comps = 0
trocas = 0

def QuickSort(lista, ini = 0, fim = None):
    """
        Função que implementa  o algoritmo de ordenação Quick Sort
        de forma recursiva 
    """
    # Se fim for none, então consideramos a última posição da lista
    if fim is None:
        fim = len(lista) - 1

    # Para continuarmos, precisamos que a lista tenha pelo menos
    # DOIS elementos para ordenar
    if fim <= ini:
        return      # Sai da função sem fazer nada

    global passadas, comps, trocas

    passadas += 1

    pivot = fim     # O Pivô é o último elemento
    div = ini - 1   # O divisor inicia antes do primeiro elemento   

    # Percorre a lista da posição ini até a posição fim - 1
    for i in range(ini, fim):
        comps += 1
        if lista[i] < lista[pivot]:
            div += 1    # Incrementa o divisor
            # lista[div] e lista[i] trocam de lugar entre si,
            # caso não sejam o mesmo elemento
            if div != i:
                lista[div], lista[i] = lista[i], lista[div]
                trocas +=1

    # Depois que o percurso de i acaba, div é incrementado
    # mais uma vez
    div += 1

    # Colocamos o pivot em seu lugar definitivo. A troca acontece 
    # se o valor do pivot for menor que o valor da posição div
    comps += 1
    if lista[pivot] < lista[div] and pivot != div:
        lista[pivot], lista[div] = lista[div], lista[pivot]
        trocas += 1

    # Chamamos recursivamente a função para as sublistas à esquerda
    # da posição div    

    QuickSort(lista, ini, div - 1)

    # Chamamos recursivamente a função para as sublistas à direita 
    # da posição div
    
    QuickSort(lista, div + 1, fim)

# ------------------
passadas = 0
comps = 0
trocas = 0

import psutil


nums = [88, 44, 33, 0, 99, 55, 77, 22, 11, 66]

from time import time
import tracemalloc
from data.nomes_desord import nomes

ini = time()
tracemalloc.start()

QuickSort(nomes)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim = time()

print(nomes)
print(f"O tempo usado foi de {fim - ini}s \nA qtd de passadas, trocas e comparações foram de {passadas, trocas, comps}")
print(f"O uso de memória foi de {mem_pico / 1024 /1024 }MB")

tracemalloc.stop
print('The CPU usage is: ', psutil.cpu_percent(4))  