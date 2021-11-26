# 1. Veja, na imagem "torres-hanoi.png", como funciona o jogo das Torres de Hanoi.
#
# 2. Cada uma das torres do jogo se comporta como uma pilha. Importe a classe
#    apropriada e crie três pilhas, representando as três torres.
#
# 3. Use os valores 1, 2 e 3 para representar os discos. Empilhe-os na primeira
#    torre.
#
# 4. Desempilhe um dos discos da primeira torre e empilhe-o na segunda.
#
# 5. Desempilhe o disco remanescente da primeira torre e coloque-o na terceira.
#
# 6. Desempilhe o disco da terceira torre e coloque-o sobre o disco da segunda torre.
#
# 7. Desempilhe o disco da primeira torre e coloque-o na terceira torre.
#
# 8. Desempilhe um dos discos da segunda torre e coloque-o na primeira torre.
#
# 9. Desempilhe o disco da segunda torre e coloque-o sobre o disco da terceira torre.
#
# 10.Finalmente, desempilhe o disco da primeira torre e coloque-o na terceira torre.
#
# 11.Use o método to_str() para exibir as três pilhas. As duas primeiras devem estar
#    vazias e a terceira deve conter os três discos, na ordem (3 na base, 1 no topo).

from lib.stack import Stack

pilhaA = Stack()
pilhaB = Stack()
pilhaC = Stack()

pilhaA.push(3)
pilhaA.push(2)
pilhaA.push(1)

print(f'Pilha A: {pilhaA.to_str()};\n Pilha B: {pilhaB.to_str()};\n Pilha C: {pilhaC.to_str()}')

pilhaC.push(pilhaA.pop())

# print(f'Pilha A: {pilhaA.to_str()};\n Pilha B: {pilhaB.to_str()};\n Pilha C: {pilhaC.to_str()}')

pilhaB.push(pilhaA.pop())

# print(f'Pilha A: {pilhaA.to_str()};\n Pilha B: {pilhaB.to_str()};\n Pilha C: {pilhaC.to_str()}')

pilhaB.push(pilhaC.pop())

# print(f'Pilha A: {pilhaA.to_str()};\n Pilha B: {pilhaB.to_str()};\n Pilha C: {pilhaC.to_str()}')

pilhaC.push(pilhaA.pop())

# print(f'Pilha A: {pilhaA.to_str()};\n Pilha B: {pilhaB.to_str()};\n Pilha C: {pilhaC.to_str()}')

pilhaA.push(pilhaB.pop())

# print(f'Pilha A: {pilhaA.to_str()};\n Pilha B: {pilhaB.to_str()};\n Pilha C: {pilhaC.to_str()}')

pilhaC.push(pilhaB.pop())

# print(f'Pilha A: {pilhaA.to_str()};\n Pilha B: {pilhaB.to_str()};\n Pilha C: {pilhaC.to_str()}')

pilhaC.push(pilhaA.pop())

print(f'Pilha A: {pilhaA.to_str()};\n Pilha B: {pilhaB.to_str()};\n Pilha C: {pilhaC.to_str()}')