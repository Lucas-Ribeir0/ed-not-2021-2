#    ALGORITMO DE ORDENAÇÃO QUICK SORT

#    Escolhe um dos elementos da lista para ser o pivô (na nossa implementação,
#    o último elemento) e, na primeira passada, divide a lista, a partir da posição
#    final da lista, em um sublsita à esquerda contendo apenas valores menores que
#    o pivô e outra sublista à direita, que contém apenas valores maiores que o pivô.
#    
#    Em seguida, recursivamente, repete o processo em cada um das sublistas até que
#    todo a lista esteja ordenado.

def QuickSort(lista, ini = 0, fim = None):
    """
        Função que implementa  o algoritmo de ordenação Quick Sort
        de forma recursiva 
    """

    