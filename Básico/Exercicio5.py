# Exercício 5
def is_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

numero = int(input("Digite um número: "))
idade_usuario = int(input("Qual sua idade? "))

maioridade = idade_usuario >= 18
print("É primo?", is_primo(numero))
print("Maioridade:", maioridade)