# FATORIAL DE UM NÚMERO n
# É igual ao número n multiplicado por todos os seus antecessores até 1
#
# 5! = 5 * 4 * 3 *  2 * 1 (120)
# 7! = 7 * 6 * 5 * 4 * 3 * 2 * 1 (5040)
#
# 5! = 5 * 4 * 3 * 2 * 1 (120)
# 4! = 4 * 3 * 2 * 1 (24)
# 3! = 3 * 2 * 1 (6)
# 2! = 2 * 1 (2)
# 1! = 1
# 0! = 1 (por convenção)
#
# 5! = 5 * 4!
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1 * 0!

# n! = n * (n - 1)! para qualquer n > 1

# Implementação iterativa (iter = caminho)
def fatorial(n):
    """
    """

    resultado = 1
    if(n > 1):
        # range começa no número n e vai descendo até 1
        print(f"O fatorial de {n} é: \n")

        for i in range(n, 1, -1):
            resultado *= i
            print(f"Resultado: {resultado}, i: {i}")
    return resultado


print(f'\n5! = {fatorial(5)}\n')

# n! = n * (n - 1) p/ n > 1
# Recursividade ocorre quando a definição de uma função inclui a própria função sendo definida

# Em programação, a recursividade se traduz quando uma função efetua chamadas a si própria.

# Implementação recurisva
def fatorial2(n):
    # Em uma função recursiva, condição de saida é aquela em que a função é capaz de retornar um resultado SEM chamar novamente a si mesmo
    if n <= 1:
        return 1 # Condição de saída
    return n * fatorial2(n - 1)


print(f"5! = {fatorial2(537)}")

# import sys
# print(sys.maxsize)

