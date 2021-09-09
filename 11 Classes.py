# Classe é uma estrutura que representa conjuntamente
# dados e algoritmos. Uma classe é como uma "forma de bolo"
# com a qual podemos criar diferentes "bolos" (objetos).
# Cada "bolo" (objeto) pode ser feito com seus próprios
# ingredientes (dados) e modo de fazer (algoritmos), mas 
# terão sempre o formato determinado pela "forma" (classe).

class FormaGeometrica():

    # Dados
    # Quando pertence a uma classe, ganham o  nome de atributos

    # ATRIBUTOS
    base = 0
    altura = 0
    tipo = "R" # Retângulo

    # Algoritmos
    # São representados por funções que, quando se encontram
    # dentro de uma classe, ganham nome de MÉTODOS

    # Este método é executado quando um objeto é criado a partir
    # de uma classe (construtor)

    def __init__(self, base = 0, altura = 0, tipo="R"):
        # Recebe os valores passados ao construtor e os armazena 
        # dentro dos atributos
        if base <= 0:
            raise Exception("A base deve ser maior que 0")
        elif altura <= 0:
            raise Exception("A altura deve ser maior que zero")
        elif tipo not in ["R", "T", "E"]:
            raise Exception("O tipo deve ser R, T ou E")

        self.base = base
        self.altura = altura
        self.tipo = tipo


#____________________________________________________#

retangulo1 = FormaGeometrica(15, 10, "R") # Chama o __init__
triangulo1 = FormaGeometrica(6, 9, "T") # Chama o __init__

print(f"[retangulo1] base: {retangulo1.base}, altura: {retangulo1.altura}, tipo: {retangulo1.tipo}")

print(f"[triangulo1] base: {triangulo1.base}, altura: {triangulo1.altura}, tipo: {triangulo1.tipo}")