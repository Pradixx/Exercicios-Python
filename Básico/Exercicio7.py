# exercicio 1
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcular a média
media = (nota1 + nota2 + nota3) / 3

# Indicar aprovação ou reprovação
if media >= 7:
    print(f"A média é {media:.2f}. O aluno foi aprovado.")
else:
    print(f"A média é {media:.2f}. O aluno foi reprovado.")