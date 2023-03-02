"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""


numero_str = input ('Digite um numero ', )




try:
    numero_float = float(numero_str)
    print (f'Float {numero_float}')
    print (f'O drobro de {numero_float} é {numero_float * 2}')
except:
    print (f'"{numero_str}" Não é um numero.')


