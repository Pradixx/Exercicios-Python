# Exercicio 3
idade = int(input("Digite sua idade: "))

# Classificação etária
if 0 <= idade <= 11:
    print("Você é uma criança.")
elif 12 <= idade <= 18:
    print("Você é um adolescente.")
elif 19 <= idade <= 24:
    print("Você é jovem.")
elif 25 <= idade <= 40:
    print("Você é um adulto.")
elif 41 <= idade <= 60:
    print("Você está na meia-idade.")
else:
    print("Você é idoso.")