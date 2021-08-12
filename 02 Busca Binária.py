# Algoritmo de busca binária
# 
# Dada uma lista, que deve estar previamente ordenada, e um valor de busca, divide a lista em duas metades e procure pelo valor de busca apenas na metade onde o valor poderia estar. Novas subdivisões são feitas até que se encontre o valor de busca ou que reste apenas uma sublista vazia, quando se conclui que o valor de busca não existe na lista.

from data.lista_nomes import nomes
from time import time

def busca_binaria(lista, valorBusca):
    """
        Função que implementa o algoritmo de busca binária - Função de busca mais eficiente que busca sequencial caso a lista ja esteja ordenada.

        Retorna a posição onde valorBusca foi encontrado ou o valor convencional -1 se valorBusca
        não existir na lista
    """
    ini = 0                 # Primeira Pos.
    fim = len(lista) - 1    # Última Pos.

    while ini <= fim:
        meio = (ini + fim) // 2     # Operador // é divisão inteiro, descarta decimal
        contagem = contagem + 1
        #1º Caso: lista[meio] é igual a valor_busca
        if lista[meio] == valorBusca:   # Encontrou o valor de busca
            return meio   # Meio é a posição onde valorBusca está na lista

        #2º Caso: valorBusca é menor que lista[meio]
        elif valorBusca < lista[meio]:          
            fim = meio - 1 # Descarta a 2º metade da lista
        
        #3º Caso: valorBusca é maior que lista[meio]
        else: 
            ini = meio + 1 # Descarta a 1º metade da lista
    #4º Caso: valorBusca não é encontrado na lista
    return -1

hora_ini = time()
print(f"Posição de FAUSTO: {busca_binaria(nomes, 'FAUSTO')}")
hora_fim = time()
print(f"Tempo gasto procurando FAUSTO: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de ZULEICA: {busca_binaria(nomes, 'ZULEICA')}")
hora_fim = time()
print(f"Tempo gasto procurando ZULEICA: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de LUNISVALDO: {busca_binaria(nomes, 'LUNISVALDO')}")
hora_fim = time()
print(f"Tempo gasto procurando LUNISVALDO: {(hora_fim - hora_ini) * 1000}ms")
