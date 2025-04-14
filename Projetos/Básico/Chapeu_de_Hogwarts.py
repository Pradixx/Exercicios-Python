import time

grifinoria = 0
cornival = 0
lufa = 0
sonserina = 0

print('Bem vindo ao chapeu seletor de hogwarts!')
print('Para escolher sua casa, vamos precisar fazer algumas perguntas')

print('')

print('Você gosta do amanhecer ou do anoitecer:')
print('1- Amanhecer')
print('2- Anoitecer')
amaAno = int(input('Qual a resposta: '))

print('')

if amaAno == 1:
  grifinoria = grifinoria + 1
  cornival = cornival + 1
elif amaAno == 2:
  lufa = lufa + 1
  sonserina + 1
else:
  print('Entrada errada')

print('Quando você morrer, quer que as pessoas lembre de você, como:')
print('1- O bom')
print('2- O grande')
print('3- O sábio')
print('4- O ousado')
morte = int(input('Qual a resposta: '))

print('')

if morte == 1:
  lufa = lufa + 2
elif morte == 2:
  sonserian = sonserina + 2
elif morte == 3:
  cornival = cornival + 2
elif morte == 4:
  grifinoria = grifinoria + 2
else:
  print('Entrada errada')

print('Que tipo de instrumento mais agrada o seu ouvido:')
print('1- O violino')
print('2- A trombeta')
print('3- O piano')
print('4- O tambor')
instrumento = int(input('Qual a resposta: '))

print('')

if instrumento == 1:
  sonserina = sonserina + 4
elif instrumento == 2:
  lufa = lufa + 4
elif instrumento == 3:
  cornival = cornival + 4
elif instrumento == 4:
  grifinoria = grifinoria +4
else:
  print('Entrada errada')

print('')

print('Está foi a sua pontuação!')
print('Grifinória: ', grifinoria)
print('Cornival: ', cornival)
print('Lufa-Lufa: ', lufa)
print('Sonserina: ', sonserina)

print('')

print('A casa escolhida para você...')
time.sleep(1.5)
print('...')
time.sleep(1.5)

#Tenho certeza que tem um sistema melhor do que vou fazer agora, mas estou aprendendo, tenha paciência
if grifinoria > cornival and grifinoria > lufa and grifinoria > sonserina:
  print('Sua casa é a Grifinória!')
elif cornival > grifinoria and cornival > lufa and cornival > sonserina:
  print('Sua casa é a Cornival!')
elif lufa > grifinoria and lufa > cornival and lufa > sonserina:
  print('Sua casa é a Lufa-Lufa')
elif sonserina > grifinoria and sonserina > cornival and sonserina > lufa:
  print('sua casa é a sonserina')
else:
  print('Por favor, se retire de Hogwarts, nenhuma casa te aceitou!')

#Tentei dessa forma,  mas só aparece o valor
"""
maior = max(grifinoria, cornival, lufa, sonserina)
print(f'Sua casa é {maior}')
"""