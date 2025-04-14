#Desafio da bola mágica

import random

print('Bola mágica 8')
num = random.randint(1, 9)

if num == 1:
  print('Sim, definitivamente')
elif num == 2: 
  print('É decididamente assim')
elif num == 3:
  print('Sem dúvida')
elif num == 4:
  print('Responder nebuloso, tente novamente.')
elif num == 5:
  print('Pergunte novamente mais tarde')
elif num == 6:
  print('Melhor não contar agora.')
elif num == 7:
  print('MInhas fontes dizem que não')
elif num == 8:
  print('Perspectiva não tão boa.')
else:
  print('Muito duvidoso')