print('Calculando o ph')
ph = int(input('Digite um valor de 0 a 14: '))

if ph > 7:
  print('Basico')
elif ph < 7:
  print('Acido')
else:
  print('Neutro')