# Exercicio 2
cidades = []

# Solicitando ao usuário 3 nomes de cidades
for i in range(3):
    cidade = input(f"Digite o nome da cidade {i+1}: ")
    cidades.append(cidade)

print("Cidades cadastradas:", cidades)