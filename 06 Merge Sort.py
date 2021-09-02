# Algoritmo de ordenação MERGE SORT
#
# No processo de ordenação, esse algoritmo "desmonta" o vetor original
# contendo N elementos até obter N vetores de apenas um elemento cada  um.
# Em seguida, usando a técnica de mesclagem (merge), "remota" o vetor, dessa vez com os elementos já em ordem.

comps = 0
divisoes = 0
juncoes = 0

def mergeSort(lista):
    """
    Função que implementa o algoritmo merge sort usando o metódo Recursivo.
    """

    # Não podemos zerar as variáveis globais de estatísticas dentro da
    # função porque ela é recursiva e resetaria a contagem a cada chamada

    global comps, divisoes, juncoes


    # print(f"Lista recebida: {lista}")
    
    # Só continua se a lista tiver mais de um elemento
    if len(lista) <= 1:
        return lista
    
    meio = len(lista) // 2
    # Gera cópia da primeira metade da lista
    lista_esq = lista[:meio] # Do inicio ao meio -1

    # Gera cópia da segunda metade da lista
    lista_dir = lista[meio:] # Do meio ao fim

    divisoes += 1

    # Chamamos recursivamente a função para continuar
    # repartindo a lista em metades
    lista_esq = mergeSort(lista_esq)
    lista_dir = mergeSort(lista_dir)

    # print(f">>> lista_esq: {lista_esq}")
    # print(f">>> lista_dir: {lista_dir}")

    # Junta as duas metades em uma única lista, ordenada
    pos_esq = 0
    pos_dir = 0
    ordenada = [] # Lista vazia

    # Compara os elementos de cada lista entre si e insere na 
    # lista ordenada o que for menor
    while pos_esq < len(lista_esq) and pos_dir < len(lista_dir):
        # O elemento que se encontra na lista da esquerda
        # é menor que o que se encontra na lista da direita
        if lista_esq[pos_esq] < lista_dir[pos_dir]:
            ordenada.append(lista_esq[pos_esq])
            pos_esq += 1
        # O contrário
        else:
            ordenada.append(lista_dir[pos_dir])
            pos_dir += 1
        comps += 1
    sobra = None # A sobra da lista que ficou para trás

    if(pos_esq < pos_dir): # Houve sobra da lista esquerda
        sobra = lista_esq[pos_esq:] # Sobra do pos_esq até o final
    else: # Houve sobra a direita
        sobra = lista_dir[pos_dir:] # Sobra do pos_dir até o final

    # print(f">>>> Final ordenada: {ordenada + sobra}")

    # Retornamos a lista final ordenada, composta da ordenada + sobra
    juncoes += 1
    return ordenada + sobra         # "Soma" de duas listas

comps = 0
divisoes = 0
juncoes = 0

from data.nomes_desord import nomes
from time import time
import tracemalloc

lista = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]

ini = time()
tracemalloc.start() # Inicia a medição de memória

nomes_ord = mergeSort(nomes)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim = time()

print(nomes_ord)
print(f"A quantidade de Junções foram de: {juncoes} \nA quantidade de divisões foi: {divisoes} \nA quantidade de comparações foi de: {comps}\nO tempo necessário para a função foi de: {(fim - ini)}s\n")

print(f"Pico de memória: {mem_pico / 1024 / 1024} MB")

tracemalloc.stop() # Finaliza a medição de memória