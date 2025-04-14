import math

num_lados = int(input("Digite o número de lados: "))
med_lado = float(input("Digite a medida do lado: "))

if num_lados < 3:
    print("NÃO É UM POLÍGONO")
elif num_lados > 5:
    print("POLÍGONO NÃO IDENTIFICADO")
elif num_lados == 3:
    p = (med_lado * 3) / 2
    area = math.sqrt(p * (p - med_lado) * (p - med_lado) * (p - med_lado))
    print(f"TRIÂNGULO\nÁrea: {area:.2f}")
elif num_lados == 4:
    print(f"QUADRADO\nÁrea: {med_lado * med_lado:.2f}")
else:
    area = (5 * med_lado * med_lado) / (4 * math.tan(math.pi / 5))
    print(f"PENTÁGONO\nÁrea: {area:.2f}") 