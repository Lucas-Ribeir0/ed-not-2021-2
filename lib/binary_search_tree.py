"""
    Classe que representa cada unidade (elemento) da árvore binária de busca
    É dividida em três partes:
    1) Onde fica armezenada a informação relevante para o usuário (data)
    2) O ponteiro para a subárvore esquerda (left)
    3) O ponteiro para a subárvore direita (right)
"""
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

"""
    ESTRUTURA DE DADOS ÁRVORE BINÁRIA DE BUSCA
    - Árvore ~> é uma estrutura de dados não-linear, hierárquica,
      que é formada recursivamente por outras subárvores.
    - Árvore binária ~> uma árvore na qual cada nodo tem grau máximo
      igual a 2 (ou seja, cada nodo pode ter, no máximo, dois descendentes
      diretos).
    - Árvore binária de busca ~> é uma árvore binária otimizada para a
      operação de busca binária. Por isso, na inserção, os valores são 
      colocados já em ordem.
"""
class BinarySearchTree:

    """
        Construtor da classe
    """
    def __init__(self):
        self.__root = None      # Raiz da árvore

    """
        Método PÚBLICO de inserção na árvore
    """
    def insert(self, val):

        inserted = Node(val)

        # 1º caso: a árvore está vazia
        if self.__root is None: self.__root = inserted

        # 2º caso: inserção recursiva ~> percorrer a árvore recursivamente
        else: self.__insert_node(inserted, self.__root)

        # Exibe a árvore (tosco, para debug)
        print(f'[ÁRVORE] data: {self.__root.data}, left: {self.__root.left}, right: {self.__root.right}')

    """
        Método __privado para inserção de um nodo na árvore
    """
    def __insert_node(self, inserted, root):
        # 1º caso: valor do nodo é MENOR que o valor da raiz ~> vai para a ESQUERDA
        if inserted.data < root.data:
            # Se o nodo da esquerda estiver desocupado, faz aí a inserção
            if root.left is None: root.left = inserted
            # Senão, passa a considerar o nodo da esquerda como raiz
            else: self.__insert_node(inserted, root.left)
        # 2º caso: valor do nodo é MAIOR que o valor da raiz ~> vai para a DIREITA
        elif inserted.data > root.data:
            # Se o nodo da direita estiver desocupado, faz aí a inserção
            if root.right is None: root.right = inserted
            # Senão, passa a considerar o nodo da direita como raiz
            else: self.__insert_node(inserted, root.right)

        # OBSERVAÇÃO: quando inserted.data == root.data (tentativa de inserção de um valor que já existe na árvore), nada acontece. A tentativa é ignorada.

    """
        Metódo que exibe a árvore recursivamente
    """
    def to_str(self, root = None):
        if root is None: root = self.__root

        output = ''

        if root is not None:
            output += f'[ROOT data: {root.data}]\n ' # \n = Quebra de linha (enter)

            if root.left is not None:
                output += f'(À esquerda de {root.data}) ' + self.to_str(root.left)

            if root.right is not None:
                output += f'(À direita de {root.data}) ' + self.to_str(root.right)

        return output


    """
        PERCURSOS
    """

    """
        Método que faz o percurso em-ordem (in-order traversal)
        1º caso: vista em-ordem a subàrvore esquerda
        2º caso: visita a raiz
        3º caso: vista em-ordem a subárvore direita
        Este percurso é utilizado quando se deseja recuperar os elementos
        da árvore em ordem
    """
    def in_order_traversal(self, fnCallback, root = False):

        if root is False: root = self.__root

        if root is not None:
            self.in_order_traversal(fnCallback, root.left) # 1°
            fnCallback(root.data) # 2º
            self.in_order_traversal(fnCallback, root.right) # 3°

    """
        Método que faz o percurso pré-ordem
    """

    def pre_order_traversal(self, fnCallback, root = False):
        
        if root is False: root = self.__root

        if root is not None:
            fnCallback(root.data)  # 1º
            self.pre_order_traversal(fnCallback, root.left) # 2º
            self.pre_order_traversal(fnCallback, root.right) # 3º
# ~-~-~-~-~--~-~-~-~-~-

arvore = BinarySearchTree()

arvore.insert(10)
arvore.insert(9)
arvore.insert(8)
arvore.insert(11)
arvore.insert(10)
arvore.insert(0)

print(arvore.to_str())

em_ordem = []

def insere_em_ordem(val):
    em_ordem.append(val)

# arvore.in_order_traversal(insere_em_ordem)
arvore.in_order_traversal(lambda val: em_ordem.append(val))

print('Percurso em ordem:', em_ordem)

sumario = BinarySearchTree()

sumario.insert('2')
sumario.insert('1')
sumario.insert('3')
sumario.insert('1.1')
sumario.insert('3.1')
sumario.insert('2.1')
sumario.insert('2.1.1')

em_ordem = []

sumario.in_order_traversal(lambda val: em_ordem.append(val))
print('Sumário em-ordem: ', em_ordem)

pre_ordem = []
sumario.pre_order_traversal(lambda val: pre_ordem.append(val))
print('Sumário pré-ordem', pre_ordem)