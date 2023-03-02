""" projeto de calculadora com while """

while True :
    numero1 = input ('Digite um numero:  ')
    numero2 = input ('Digite outro numero:  ')
    numero1_f = 0
    numero2_f = 0
    expressao = input('Digite o um dos operadores "+,-,*,/"  :')
    verificador_float = None
    operadores_validos = '*/+-'


    try:
        numero1_f = float (numero1)
        numero2_f = float (numero2)
        verificador_float = True

    except:
        verificador_float = None

    if verificador_float == None :
        print ('Um ou ambos os numeros que você digitou não são validos')
        continue
    if expressao not in operadores_validos :
        print ('O operador que vc digitou não é valido :( ')
        continue
    if len (expressao) > 1 :
        print ('Digite apenas um operador')
        continue
    
    if expressao == '+' :
        print (f'{numero1_f} + {numero2_f} = {numero1_f + numero2_f}')

    elif expressao == '-' :
        print (f'{numero1_f} - {numero2_f} = {numero1_f - numero2_f}')
    elif expressao == '/' :
        print (f'{numero1_f} / {numero2_f} = {numero1_f / numero2_f}')
    elif expressao == '*' :
        print (f'{numero1_f} * {numero2_f} = {numero1_f * numero2_f}')
    else:
        print (' em todo esses anos nessa industria vital, está é a primeira vez que isso acontece')
    
    sair = input ('Quer sair? Digite [s] para sair ou tecle [enter] para continuar  ').lower().startswith('s')
    
    if sair :
        break

    
