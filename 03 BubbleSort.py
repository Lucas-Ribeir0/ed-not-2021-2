# Algoritmo de ordenação Bubble Sort
#
# Percorre a lista a ser ordenada em sucessivas passadas,
# trocando elementos adjacentes entre si quando o segundo for
# menor que o primeiro. Efetua tantas passadas quanto necessárias 
# até que, na última passada, nenhuma troca seja efetuada.


# Variáveis globais
comps = 0       # Número de comparações
passadas = 0    # Número de passadas
trocas = 0      # Número de trocas 

def bubbleSort(lista):
    """
        Função que implementa o algoritmo de ordenação  Bubble Sort
    """
    global comps, passadas, trocas
    comps = 0          # Número de comparações  
    passadas = 0       # Número de passadas
    trocas = 0         # Número de trocas 

    while True: #Loop Eterno
        passadas += 1
        trocou = False
        #Loop na lista até o PENÚLTIMO elemento: len(lista) - 2 -> range(len(lista) - 1)
        # Ex. em uma lista de 10 elemenos, len(lista) == 10
        # A última posição estará em len(lista) - 1, ou seja, 9 -> range(len(lista))
        # A penúltima posição estará em len(lista) -2, ou seja, 8 -> range(len(lista))

        for i in range(len(lista) -1):      # Nova passada se iniciou
            comps += 1
            if lista[i + 1] < lista[i]:     # É necessário trocar
                lista[i + 1], lista[i] = lista[i], lista[i + 1] # Faz a troca
                trocas += 1
                trocou = True

        # Se houve troca, a lista está ordenada e podemos interromper
        # o loop while
        if not trocou: #Trocou == False
            break #Interrompe o while

# nums = [88, 44, 33, 0, 99, 55, 77, 22, 11, 66] 

# Pior caso: lista em ordem inversa
#nums = [99, 88, 77, 66, 55, 44, 33, 22, 11, 0]

# Melhor caso: Já ordenada
nums = [0, 11, 22, 33, 44, 55, 66, 77, 88, 99]

bubbleSort(nums)

print("\n", nums)

print("\nNúmero de passadas: ", passadas, "\nNúmero de comparações: ", comps, "\nNúmero de trocas:", trocas)

from data.nomes_desord import nomes
from time import time

nomes_parcial = nomes[:30000] # Usa apenas as primeiras 20 mil linhas

ini = time()
bubbleSort(nomes_parcial)
fim =  time()

print(nomes_parcial)
print(f"Tempo: {fim - ini} ")

print("\nNúmero de passadas: ", passadas, "\nNúmero de comparações: ", comps, "\nNúmero de trocas:", trocas)