# Exercício 2
nome_namorada = "Julia"
nome_amigo = "Jesus"

print("\n\n")  # Pulando duas linhas
print("Nome da namorada:", nome_namorada)
print("Nome do amigo:", nome_amigo)

# Desenho do retângulo
altura = 3
largura = max(len(nome_namorada), len(nome_amigo)) + 4

print("+" + "-" * (largura - 2) + "+")
print("| " + nome_namorada + " " * (largura - len(nome_namorada) - 3) + "|")
print("| " + nome_amigo + " " * (largura - len(nome_amigo) - 3) + "|")
print("+" + "-" * (largura - 2) + "+")
