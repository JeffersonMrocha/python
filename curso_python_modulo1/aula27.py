"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""

olamundo = "Olá mundo!"
print (f'{olamundo[2]}')
print (f'{olamundo[-8]}')
print (f'{olamundo[4:9]}')#se vc omitir o final ele irá pegar todo o resto da string
print (f'{olamundo[:9]}')#se vc omitir o começo ele irá puzar do começo até o final que vc escolheu
print (len(f'{olamundo}')) # saber quantos caracteres possui a str
print (olamundo[0:len(olamundo):1])
print (olamundo[0:len(olamundo):2])
print (olamundo[::-1])
print (olamundo[-1:-11:-1])

