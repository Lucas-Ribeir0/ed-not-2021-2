"""
    1) Identifique o algoritmo abaixo.
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""

def m(n, o = 0, p = None): 
    # O Algoritmo "m" se refere ao QuickSort
    
    # A Variável "N" se refere a lista
    # A Variável "O" ao início da lista
    # A Variável "P" ao fim da lista

    # A variável "Q" se refere ao pivô da lista, possivelmente o último elemento
    # A variável "R" se refere ao divisor da lista, onde divide as listas em relação a posição do pivô

    if p is None:
        p = len(n) - 1

    if p <= o:
        return

    q = p
    r = o - 1

    for i in range(o, p):
        if n[i] < n[q]:
            r += 1
            if r != i: 
                n[r], n[i] = n[i], n[r]

    r += 1

    if n[q] < n[r] and q != r:
        n[q], n[r] = n[r], n[q]

    m(n, o, r - 1)
                    # Recursão do Algoritmo "m"
    m(n, r + 1, p)
