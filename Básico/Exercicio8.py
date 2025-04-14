# Exercicio 4
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# Utiliza condição ternária para determinar qual é o maior valor
maior_valor = valor1 if valor1 > valor2 else valor2

# Mostra o resultado
print(f"O maior valor entre {valor1} e {valor2} é: {maior_valor}")