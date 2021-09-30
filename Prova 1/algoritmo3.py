"""
    1) Identifique o algoritmo abaixo.
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""

def m(n):
    # O algoritmo "m" se refere ao BubbleSort

    # A variável "n" se refere a lista
    # A variável "o" informa se o número no valor de "p" foi trocado - False ou True
    # "p" é variável utilizada para percorrer a lista

    while 1 > 0: # Formato de Loop infinito
        o = False
        for p in range(len(n) - 1):
            if n[p + 1] < n[p]:
                n[p + 1], n[p] = n[p], n[p + 1]
                o = True
        if not o:
            break

