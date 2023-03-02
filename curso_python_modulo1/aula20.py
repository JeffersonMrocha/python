valor1 = input ('Digite um numero: ' )
valor2 = input ('Digite outro numero: ' )
primeiro_valor = int(valor1)
segundo_valor = int(valor2)
if primeiro_valor > segundo_valor:
    print (f'O {primeiro_valor=} é maior que o {segundo_valor=}')
elif primeiro_valor < segundo_valor:
    print (f'O {segundo_valor=} é maior que o {primeiro_valor=}')
elif primeiro_valor == segundo_valor:
    print (f'Os valores {primeiro_valor} e {segundo_valor} são equivalentes')
else:
    print(f'Favor digitar apenas numeros')