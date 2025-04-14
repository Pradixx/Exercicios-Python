# Exercicio 2
ano_nascimento = int(input("Digite o ano em que você nasceu: "))

# Obter o ano atual
import datetime
ano_atual = datetime.datetime.now().year

# Calcular a idade
idade = ano_atual - ano_nascimento

# Verificar se o usuário já fez 18 anos
if idade >= 18:
    print("Você já fez 18 anos.")
else:
    print("Você ainda não fez 18 anos.")