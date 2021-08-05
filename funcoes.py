# Função é um trecho de código que tem um nome e pode
# receber informações externas para fazer seu trabalho.
# Opcionalmente, uma função pode também produzir um valor
# de resultado.
# Uma função é definida apenas uma vez e pode ser utilizada
# (chamada) várias vezes, evitando repetições de código.
# Existem funções já providas pela linguagem, como por exemplo,
# len(), range e sort(), e podemos definir também nossos próprios
# funções.

# Os termos que aparecem entre parentêses são chamados parâmetros ou argumentos
def imc(peso, altura): #Definição (ou declaração) da função
    """
        Função que calcula o indíce de Massa Corpórea (IMC)
    """
    #Trechos entre aspas triplas são um tipo especial de comentário
    # chamado docstring, e servem para documentar 
    # o propósito de um função ou classe
    return peso / altura ** 2 # peso / (altura)²


#float(): converte o valor informado em número com casas especiais
#(floating point)
p = float(input("Informe o peso da pessoa:"))
a = float(input("Informe a altura da pessoa:"))

#fazendo uma chamada da função imc()
resultado = imc(p,a)

print(f"O IMC calculado é: {resultado}.")