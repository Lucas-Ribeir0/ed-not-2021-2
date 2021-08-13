# Algoritmo de busca binária
# 
# Dada uma lista, que deve estar previamente ordenada, e um valor de busca, divide a lista em duas metades e procure pelo valor de busca apenas na metade onde o valor poderia estar. Novas subdivisões são feitas até que se encontre o valor de busca ou que reste apenas uma sublista vazia, quando se conclui que o valor de busca não existe na lista.

from time import time
from data.lista_nomes import nomes

comps = 0 # Declarando a variável global

def busca_binaria(lista, valorBusca):
    """
        Função que implementa o algoritmo de busca binária - Função de busca mais eficiente que busca sequencial caso a lista ja esteja ordenada.

        Retorna a posição onde valorBusca foi encontrado ou o valor convencional -1 se valorBusca
        não existir na lista
    """
    global comps # Indica que estamos usando a variável declarada na linha 8
    comps = 0

    ini = 0                 # Primeira Pos.
    fim = len(lista) - 1    # Última Pos.

    while ini <= fim:
        meio = (ini + fim) // 2     # Operador // é divisão inteiro, descarta decimal
        #1º Caso: lista[meio] é igual a valor_busca
        if lista[meio] == valorBusca:   # Encontrou o valor de busca
            comps += 1
            return meio   # Meio é a posição onde valorBusca está na lista

        #2º Caso: valorBusca é menor que lista[meio]
        elif valorBusca < lista[meio]:
            comps += 2       
            fim = meio - 1 # Descarta a 2º metade da lista
        
        #3º Caso: valorBusca é maior que lista[meio]
        else: 
            comps += 2
            ini = meio + 1 # Descarta a 1º metade da lista
    #4º Caso: valorBusca não é encontrado na lista
    return -1


hora_ini = time()
print(f"Posição de FAUSTO: {busca_binaria(nomes, 'FAUSTO')}, {comps} Comparações")
hora_fim = time()
print(f"Tempo gasto procurando FAUSTO: {(hora_fim - hora_ini) * 1000}ms")


hora_ini = time()
print(f"Posição de ZULEICA: {busca_binaria(nomes, 'ZULEICA')}, {comps} Comparações")
hora_fim = time()
print(f"Tempo gasto procurando ZULEICA: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de LUNISVALDO: {busca_binaria(nomes, 'LUNISVALDO')}, {comps} Comparações")
hora_fim = time()
print(f"Tempo gasto procurando LUNISVALDO: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de NOEMIA: {busca_binaria(nomes, 'NOEMIA')}, {comps} Comparações")
hora_fim = time()
print(f"Tempo gasto procurando NOEMIA: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de JERDERSON: {busca_binaria(nomes, 'JERDERSON')}, {comps} Comparações")
hora_fim = time()
print(f"Tempo gasto procurando JERDERSON: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de AARAO: {busca_binaria(nomes, 'AARAO')}, {comps} Comparações")
hora_fim = time()
print(f"Tempo gasto procurando AARAO: {(hora_fim - hora_ini) * 1000}ms")