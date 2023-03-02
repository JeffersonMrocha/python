# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
#nome = 'jefferson'
#print (nome[-1])
#print (f'a quinta letra do nome {nome} é: {nome[4]}')
#print ( 'r' in nome)
#print ( 'y' in nome)
#print ('a' not in nome)
#print ('o' not in nome)

nome = input ('Digite uma palavra ou texto ' )
nome_pesquisa = input ('Digite uma palavra ou trecho que deseja buscar entre o primero texto ou palavra digitado ' )

if nome_pesquisa in nome:
    print (f'{nome_pesquisa} Foi localizado em {nome}')
else :
    print(f'{nome_pesquisa} Não foi localizado em {nome}')
