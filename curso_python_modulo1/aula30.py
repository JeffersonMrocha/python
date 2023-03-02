"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 59  # velocidade atual do carro
local_carro = 101  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

Velocidade_para_ser_multado = velocidade > RADAR_1
radar_range_1 = local_carro >= (LOCAL_1 - RADAR_RANGE)
radar_range_2 = local_carro <= (LOCAL_1 + RADAR_RANGE)
local_para_checagem_de_velocidade =  radar_range_1 and radar_range_2 


'''
if velocidade > RADAR_1 and local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE):
    print (f'Você ultrapassou a velocidade permitida de {RADAR_1}KM/h e por isso foi multado')
else:
    print (f'Velocidade permitida, Dirija com cuidado')
'''

if Velocidade_para_ser_multado and local_para_checagem_de_velocidade :
    print (f'Você ultrapassou a velocidade permitida de {RADAR_1}KM/h e por isso foi multado')
else:
    print (f'Velocidade permitida, Dirija com cuidado')