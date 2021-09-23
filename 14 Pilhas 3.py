"""
    Analisador de expressões matemáticas
"""

from lib.stack import Stack

simbolos = {
    "P": "parêntese",
    "C": "colchete",
    "X": "chave" 
}

# expressao = "2 * 4 - {7 / [5 - (7 * 9) + 1] * 3} / 5"

# expressao = "2 * 4 - {7 / [5 - (7 * 9) + 1} * 3] / 5"

# expressao = "2 * 4 - {7 / [5 - (7 * 9) + 1]] * 3} / 5"

expressao = "2 * {4 - {7 / [(5 - (7 * 9) + 1] * 3} / 5"

analisador = Stack() # Cria a pilha

def verif_fechamento(tipo, pos, dados):
    # Se o tipo que veio da pilha for igual ao tipo encontrado
    # no fechamento, OK
    # print(f"DEBUG -> tipo_fecha: {tipo}, pos_fecha: {pos}, dados_abre: {dados}:")

    # A pilha ficou vazia antes do término da análise da expressão
    if dados is None: 
        print(f"ERRO: há mais símbolos de fechamento que símbolos de abertura na expressão; tipo {tipo}, posição {pos}")
    elif dados["tipo"] == tipo:
        print(f"Símbolo {tipo} aberto na posição {dados['pos']} e fechado na posição {pos}")
    else: # Tipos errados
        print(f"ERRO: símbolo de fechamento do tipo {tipo} encontrado na posição {pos}; esperado símbolo do tipo {dados['tipo']}")

# Percorre a expressão em busca de parênteses, colchetes e chaves
for pos in range(len(expressao)):
    if expressao[pos] == "(":
        # Empilha informações sobre o abre parênteses
        analisador.push({"tipo": "P", "pos": pos})
    elif expressao[pos] == "[":
        # Empilha informações sobre o abre parênteses
        analisador.push({"tipo": "C", "pos": pos})
    elif expressao[pos] == "{":
        # Empilha informações sobre o abre parênteses
        analisador.push({"tipo": "X", "pos": pos})
        
    elif expressao[pos] == ")":
        verif_fechamento("P", pos, analisador.pop())
    elif expressao[pos] == "]":
        verif_fechamento("C", pos, analisador.pop())
    elif expressao[pos] == "}":
        verif_fechamento("X", pos, analisador.pop())

# print(analisador.to_str())

while not analisador.is_empty():
    sobra = analisador.pop()
    print(f"ERRO: símbolo de abertura {sobra['tipo']} sem símbolo de fechamento correspondente na posição {sobra['pos']}")
    