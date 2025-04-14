# Exercicio 4
nomes = []

# Preenchendo a lista com 5 nomes
for i in range(5):
    nome = input(f"Digite o nome {i+1}: ")
    nomes.append(nome)

# Solicitando um número de 0 a 4
indice = int(input("Digite um número de 0 a 4 para remover o nome nessa posição: "))

# Removendo o elemento da posição indicada
if 0 <= indice < len(nomes):
    nomes.pop(indice)
    print("Lista após remoção:", nomes)
else:
    print("Número inválido! Por favor, insira um número entre 0 e 4.")