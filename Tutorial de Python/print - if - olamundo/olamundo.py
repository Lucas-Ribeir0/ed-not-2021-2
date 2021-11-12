print("Olá Mundo")

nome = input("Qual é o seu nome? \n")

#print("Olá", nome,"!")

print(f"Olá, {nome}!")

#print("Olá, {nome}!")

# int() converte o que foi informado no input() de texto para número inteiro
idade = int(input("Informe a sua idade: "))

if idade >= 18: 
    print("Você pode ingerir bebidas alcoólicas")
    print("Você pode tirar habilitação.")
else:
    print("Você não pode beber.")
    print("Você não pode tirar habilitação.")