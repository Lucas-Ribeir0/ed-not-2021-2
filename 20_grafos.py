# Usando a estrutura dict nativa do python
# para representar um grafo não direcionado
# refletindo sua matriz de adjacência

# Dentro de cada propriedade da dict usamos
# uma lista para representar as arestas entre
# os vértices
grafo_naodir = {
    'A': ['A', 'B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['C']
}

