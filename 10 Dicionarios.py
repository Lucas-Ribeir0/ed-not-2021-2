pessoa = {
    # "nome" é a chave
    # "Fulano de Tal" é valor

    "nome": "Fulano de Tal",
    "sexo": "M",
    "idade": 39,
    "peso": 76,
    "altura": 1.82
}

# Calculando o IMC (índice de Massa Corporal)
imc = pessoa["peso"] / (pessoa["altura"] ** 2)
print(f"O IMC de {pessoa['nome']} é {imc}."
)

forma1 = {
    "base": 7.5,
    "altura": 12,
    "tipo": "R" # Retângulo
}

forma2 = {
    "base": 6,
    "altura": 2.5,
    "tipo": "T"    #Triângulo
}

forma3 = {
    "base": 5,
    "altura": 3,
    "tipo": "E"     # Elipse
}

forma4 = {
    "base": 10,
    "altura": 5,
    "tipo": "W"
}

forma5= {
    "legume": "batata",
    "fruta": "abacate",
    "tipo": "T"
}

from math import pi

def calcular_area(forma):
    if forma["tipo"] == "R":
        return forma["base"] * forma["altura"]
    elif forma["tipo"] == "T":
        return forma["base"] * forma["altura"] / 2
    elif forma["tipo"] == "E":
        return forma["base"] / 2 * forma["altura"] / 2 * pi
    else:
        # Gerar um erro
        raise Exception("Forma inválida.")

# print(f"Área de um retângulo de 7.5x12: {calcular_area(forma1)}\n")

# print(f"Área de um triângulo de 6.2x5: {calcular_area(forma2)}\n")

# print(f"Área de uma elipse de 5x3: {calcular_area(forma3)}")

# print(f"Área de uma elipse de 5x3: {calcular_area(forma4)}")

print(f"Área de uma elipse de 5x3: {calcular_area(forma5)}")
