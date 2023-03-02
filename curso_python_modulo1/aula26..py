"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""



variavel = 'ABC'
print (f'.{variavel: >10}')
print (f'{variavel: <10}.')
print (f'{variavel: ^10}.')
print (f'{variavel:0^10}.')
print (f'{1548.545416465:0>10.2f}')
print (f' o hexadecimal de 1500 é {1500:08x}')