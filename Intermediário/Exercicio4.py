import math

def calcular_potencia_e_raiz():
    while True:
        try:
            # Solicitar ao usuário os dois números
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
            
            # Calcular a potência
            potencia = numero1 ** numero2
            print(f"A potência de {numero1} elevado a {numero2} é: {potencia}")

            # Calcular a raiz quadrada
            raiz_quadrada = math.sqrt(numero1)
            print(f"A raiz quadrada de {numero1} é: {raiz_quadrada}")

            # Perguntar se o usuário deseja continuar
            continuar = input("Deseja realizar outro cálculo? (s/n): ")
            if continuar.lower() != 's':
                print("Processamento encerrado.")
                break
            
        except ValueError:
            print("Por favor, insira números válidos.")

# Executar a função
calcular_potencia_e_raiz()