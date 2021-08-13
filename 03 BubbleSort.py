# Algoritmo de ordenação Bubble Sort
#
# Percorre a lista a ser ordenada em sucessivas passadas,
# trocando elementos adjacentes entre si quando o segundo for
# menor que o primeiro. Efetua tantas passadas quanto necessárias 
# até que, na última passada, nenhuma troca seja efetuada.

def bubbleSort(lista):
    """
        Função que implementa o algoritmo de ordenação  Bubble Sort
    """
    while True: #Loop Eterno
        trocou = False
        #Loop na lista até o penúltimo elemento: len(lista) - 2

        for i in range(len(lista) -2):      # Nova passada se iniciou
            if lista[i + 1] < lista[i]:     # É necessário trocar
                lista[i + 1], lista[i] = lista[i], lista[i + 1] # Faz a troca
                trocou = True

        # Se houve troca, a lista está ordenada e podemos interromper
        # o loop while
        if not trocou: #Trocou == False
            break #Interrompe o while
        