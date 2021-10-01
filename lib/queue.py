class Queue:
    """
        Estruturas de dados FILA
        - Fila é uma lista linear de acesso restrito, que permite apenas as operações
        de enfileramento (enqueue) e desenfileiramento (dequeue), a primeira ocorrendo no final da estrutura e
        a segunda no inicio da estrutura
        - Como consequência, a fila funciona pelo princípio FIFO (First In, First Out / Primeiro a entrar, primeiro a sair).
        - A principal aplicação das filas são tarefas que envolvem o processamento de tarefas por ordem de chegada.
    """

    """
        Construtor da classe
    """

    def __init__(self):
        self.__data = []  # Inicializa uma lista privada vazia

    """
        Método para inserção 
        O nome do método para inserção em filas é padronizado: enqueue()
    """

    def enqueue(self, val):
        self.__data.append(val)  # Insere no final da fila

    """
        Método para retirada
        O nome do método de retirada em filas também é padrozinado: dequeue()
    """

    def dequeue(self):
        if self.is_empty():
            return None
        removed = self.__data[0]  # Salva o primeiro da fila
        # Destrói a posição 0 e causa renumeração das demais posições
        del self.__data[0]
        return removed # Retornamos o antigo primeiro da fila

    """ 
        Metódo para consultar o inicio da fila (primeiro elemento), sem retirá-lo
        Nome padrozinado: peek()
    """
    def peek(self):
        if self.is_empty(): return None
        return self.__data[0]
    
    """
        Método para verificar se a pilha está vazia ou não
        Retorna True se vazia ou False caso contrário
    """
    def is_empty(self):
        return len(self.__data) == 0

    """
        Método que exibe a pilha como uma string (para fins de depuração)
    """
    def to_str(self):
        string = ""
        for el in self.__data:
            if string != "": string += ", "
            string += str(el)
        return "[ " + string + " ]"

###############################################
    