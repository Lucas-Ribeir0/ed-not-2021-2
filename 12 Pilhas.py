# Palíndromo: é um texto que, quando lido de trás pra frente
# mantém o mesmo conteudo (desprezando acentos e espaçamentos)

# texto = "SOCORRAM-ME, SUBI NO ÔNIBUS EM MARROCOS"


texto = "BATATINHA QUANDO NASCE ESPALHA RAMA PELO CHÃO"

pilha = []

# Percurso do palindromo em ordem inversa, colocando cada letra na lista
for letra in texto:
    pilha.append(letra) # append() sempre acrescenta por 

# pilha.insert(10, 'y')
# pilha.insert(19, 'g')
# pilha.insert(6, 'ç')

print(pilha)

inverso = ""

# Remoção de elementos em posições que não são a final
del pilha[11] # Remove a posição 11
del pilha[21] # Remove a posição 21
del pilha[8] # Remove a posição 8
del pilha[25] # Remove a posição 25

# Retira cada letra da lista, de trás pra frente, e coloca no inverso
while len(pilha) > 0:
    inverso += pilha.pop() # pop() retira sempre o ÚLTIMO elemento

print(inverso)

# PILHA
# A pilha é um tipo abstrato de dados (TAD) que permite a entrada e a saida 
# de dados apenas na sua extremidade final. Como consequência, ela segue a 
# regra LIFO (last in, first out - último a entrar, primeiro a sair)