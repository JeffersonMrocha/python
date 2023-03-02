"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
#minha respota
numero_inteiro = input('Digite um numero inteiro ')
Numero_inteiro_checagem = str.isnumeric (numero_inteiro)


if Numero_inteiro_checagem : 
    if int (numero_inteiro) % 2 == 0 : #checagem de numero par
        print (f'O numero {numero_inteiro} é par')
    else: 
        print (f'O numero {numero_inteiro} é um numero impar')
else:
    print (f'{numero_inteiro} Não se trata de um numero inteiro')

# resposta professor
""" entrada = input('Digite um número: ') """

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')

""" try:
    entrada_int = float(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro') """


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

#minha resposta
hora_usuario = input  ('qual a hora atual? ' )
bom_dia = int(hora_usuario) >= 0 and int(hora_usuario) <= 11 
boa_tarde = int(hora_usuario) >= 12 and int(hora_usuario) <= 17
boa_noite = int(hora_usuario) >= 18 and int(hora_usuario) <= 23


if bom_dia :
    print(f'A hora atual é {hora_usuario}, Bom dia!')
elif boa_tarde :
    print(f'A hora atual é {hora_usuario}, Boa tarde!')
elif boa_noite :
    print(f'A hora atual é {hora_usuario}, Boa noite!')
else :
    print ('Digite um numero valido')

#resposta professor
"""
entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Bom tarde')
    elif hora >= 18 and hora <= 23:
        print('Bom noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

primeiro_nome_usuario = input ('Qual seu primeiro nome? ' )
nome_quantidade_letras = len(primeiro_nome_usuario)
nome_curto = nome_quantidade_letras <= 4
nome_normal = nome_quantidade_letras >= 5 and nome_quantidade_letras <= 6
nome_muito_grande = nome_quantidade_letras > 6

if  nome_curto :
    print ('Seu nome é curto')
elif nome_normal :
    print ('seu nome é normal')
elif nome_muito_grande :
    print ('Seu nome é muito grande')
else:
    print ('pf digite apenas letras')

#reposta professor
"""     nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.') """