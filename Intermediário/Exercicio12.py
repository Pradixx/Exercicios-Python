#Montanha russa

print('Bem vindo a The Cyclone')
print('Para começar, vamos pegar algumas informações')
height = int(input('Digite a sua altura: '))
credits = int(input('Digite os seus créditos: '))

if height >= 137 and credits >= 10:
  print('Aproveite o passeio!')
elif height < 137 and credits < 10:
  print('Infelizmente, você não atendeu a nenhum dos requisitos.')
elif height >= 137 or credits < 10:
  print('Você não tem créditos suficientes!')
elif height < 137 or credits >= 10:
  print('Você não é alto o suficiente para andar.')