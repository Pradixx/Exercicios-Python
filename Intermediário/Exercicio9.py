# Exercicio 4
numeros_digitados = []

# Solicitando ao usuário 10 números
for _ in range(10):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        numero += 1  # Acrescenta 1 se o número for par
    numeros_digitados.append(numero)

# Exibindo os números digitados
print("Números digitados:", numeros_digitados)