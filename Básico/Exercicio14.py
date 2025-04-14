# Exercicio 3
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Solicitando um número ao usuário
numero_usuario = int(input("Digite um número: "))

# Verificando se o número está na lista
if numero_usuario in numeros:
    print(f"O número {numero_usuario} está na lista.")
else:
    print(f"O número {numero_usuario} não está na lista.")