from lib.deque import Deque

deque = Deque()
print(deque.to_str())

#Inserções "normais"
deque.insert_back("Tertuliano")
deque.insert_back("Castorina")
deque.insert_back("Wesclerson")
deque.insert_back("Astolfo")
deque.insert_back("Junin")

print(deque.to_str())

deque.insert_front("Hermógenes") 
deque.insert_front("Querência")

print(deque.to_str())

# Remoções Normais
atendido = deque.remove_front()
print(f"Atendido: {atendido}")
print(deque.to_str())

atendido = deque.remove_front()
print(f"Atendido: {atendido}")
print(deque.to_str())

# Desistências (remoção no finalc)
desistencia = deque.remove_back()
print(f"Desistente: {desistencia}")
print(deque.to_str())

desistencia = deque.remove_back()
print(f"Desistente: {desistencia}")
print(deque.to_str())

# Consultando as extremidades do deque
primeiro = deque.peek_front()
ultimo = deque.peek_back()
print(f"Primeiro: {primeiro}, último: {ultimo}")
print(deque.to_str())