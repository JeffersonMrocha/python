"""
se usa %
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome =  'jefferson'
preco = 50.458548454
variavel = '%s, o Preço é: %.2f' %(nome, preco)
print (variavel)
print (' O hexadecimal de %i é %04x' %(15, 15))