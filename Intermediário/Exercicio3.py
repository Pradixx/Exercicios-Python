print("Digite os três lados do triângulo:")
lado_a = int(input("Lado A: "))
lado_b = int(input("Lado B: "))
lado_c = int(input("Lado C: "))

# Verifica se é um triângulo
if lado_a >= (lado_b + lado_c) or lado_b >= (lado_a + lado_c) or lado_c >= (lado_a + lado_b):
    print("Não é um triângulo!")
else:
    if lado_a == lado_b == lado_c:
        tipo_triangulo = "equilátero"
    elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c:
        tipo_triangulo = "isósceles"
    else:
        tipo_triangulo = "escaleno"
    print(f"O triângulo é do tipo: {tipo_triangulo}") 