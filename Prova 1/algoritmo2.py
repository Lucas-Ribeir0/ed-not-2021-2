"""
    1) Identifique o algoritmo abaixo.
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""

def m(n, o):    
    # O Algoritmo "m" se refere a Busca Binária

    # A variável "n" se refere a lista
    # A variável "o" se refere ao valor da busca, o valor que estamos a buscar

    # A variável "p" se refere ao inicio da lista
    # A variável "q" se refere ao final da lista

    # A variável "r" se refere ao meio da lista, usada para guardar e/ou descartar uma metade da lista
    p = 0                 
    q = len(n) - 1  

    while p <= q:
        r = (p + q) // 2     
        if n[r] == o: 
            return r     

        elif o < n[r]:
             q = r - 1  

        else: 
            p = r + 1  
    return -1
