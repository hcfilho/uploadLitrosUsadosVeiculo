tempo = int(input('Informe o tempo gasto na viagem em horas: '))
velocidade = int(input('Informe a velocidade média da viagem em km: '))
distancia = tempo * velocidade
litros_usados = distancia/12
print('A velocidade média é',velocidade,'km!')
print('O tempo gasto na viagem é', tempo,'h!')
print('A distância percorrida é', distancia,'km!')
print('A quantidade de litros usados é', litros_usados,'l!')
