# Algoritmo de Ordenação SELECTION SORT

# Isola (seleciona) o primeiro elemento da lista e, em seguida, encontra o menor
# valor no restante da lista. Se o valor encontrado for menor que o valor selecionado, efetua a troca.
# Em seguida, isola o segundo número da lista, buscando pelo menor valor das posições subsequentes. Faz
# a troca entre os dois valores, se necessário. Continua o processo, até isolar o penúltimo elemento
# da lista

comps = 0
passadas = 0
trocas = 0

from time import time
import tracemalloc

def SelectionSort(lista):
    """
        Função que implementa o algoritmo de ordenação Selection Sort
    """
    
    global comps, passadas, trocas  
    comps = 0
    passadas = 0
    trocas = 0
    
    # Percurso da lista até a penúltima posição
    
    # Seleciona (isola) o elemento que será  comparado
    for posSel in range(len(lista) - 1):
        passadas += 1

        posMenor = posSel + 1

        # Rotina para encontrar o menor número no resto da lista
        # Percurso da lista da posição[i + 2] até o fim
        for j in range(posSel + 2, len(lista)):
            comps += 1
            # Se o elemento da posição atual (j) for menor que o elemento
            # na posição do menor (posMenor), atualizamos posMenor
            if lista[j] < lista[posMenor]:
                
                posMenor = j
        
        # Comparamos lista[sel] com a lista[posMenor] e, se segundo
        # for menor que o primeiro, efetuamos a troca entre eles
        comps += 1
        if lista[posMenor] < lista[posSel]:
            lista[posMenor], lista[posSel] = lista[posSel], lista[posMenor]
            trocas += 1

# Valores das variáveis no inicio do SelectionSort:
# posSel: 0 (onde está o 88)
# posMenor: 1 (onde está o 44)
# j: 2 (onde está o 33) 

# nums = [88, 44, 33, 0, 99, 55, 77, 22, 11, 66]

#Não é o pior caso: Lista Inversa
#nums = [99, 88, 77, 66, 55, 44, 33, 22, 11, 0]

#Melhor Caso
nums = [0, 11, 22, 33, 44, 55, 66, 77,  88, 99]



# ini = time()
# SelectionSort(nums)
# fim = time()


# print(f"A quantidade de trocas foi de: {trocas} \nA quantidade de passadas foi: {passadas} \nA quantidade de comparações foi de: {comps}\nO tempo necessário para a função foi de: {(fim - ini) * 1000}ms")

from data.nomes_desord import nomes

nomesParcial = nomes[:30000]


ini = time()
tracemalloc.start()

SelectionSort(nomes)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim = time()

print(nomes)
print(f"A quantidade de trocas foi de: {trocas} \nA quantidade de passadas foi: {passadas} \nA quantidade de comparações foi de: {comps}\nO tempo necessário para a função foi de: {(fim - ini)}s\n")
print(f"Pico de memóri: {mem_pico / 1024 / 1024}MB")

tracemalloc.stop()