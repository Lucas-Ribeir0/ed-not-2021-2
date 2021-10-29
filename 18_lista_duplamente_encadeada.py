from lib.doubly_linked_list import DoublyLinkedList

lista = DoublyLinkedList()
print(lista.to_str())

# Inserção em lista vazia
lista.insert(0, 'Fusca')

# Inserção no inicio da lista
lista.insert(0, 'Chevette')

# Inserção no final da lista
lista.insert(3, 'Maverick')

# Inserção no final da lista
lista.insert(3, 'Passat')

# Inserção no final da lista
lista.insert(3, 'Voyage')

# Inserção no final da lista
lista.insert(4, 'Opala')

# Inserção no final da lista
lista.insert(5, 'Corcel')

# Inserção em posição intermediária
lista.insert(1, 'Gol')

print(lista.to_str())

# Remoção do primeiro nodo
removido = lista.remove(0)
print(f"Removido primeira posição: {removido}")
print(lista.to_str())

# Remoção do primeiro nodo
removido = lista.remove(lista.count() - 1)
print(f"Removido última posição: {removido}")
print(lista.to_str())

# Remoção da posição intermediária
removido = lista.remove(2)
print(f"Removido da posição 2: {removido}")
print(lista.to_str())

# Consulta o último nodo
ultimo = lista.peek_tail()
print(f"Último nodo consultado: {ultimo}")
print(lista.to_str())

# Inserções adicionais no final da lista
lista.insert_tail('Passat')
lista.insert_tail('Fiorino')
lista.insert_tail('Variant')
lista.insert_tail('Escort')
print(lista.to_str())

idxCorcel = lista.index('Corcel')
idxVariant = lista.index('Variant')
idxEscort = lista.index('Escort')
idxGol = lista.index('Gol')
idxChevette = lista.index('Chevette')
idxPassat = lista.index('Passat')

print(f"Posições: Corcel: {idxCorcel}, Variant: {idxVariant}, Escort: {idxEscort}, Gol: {idxGol}, Chevette: {idxChevette}, Passat: {idxPassat}")