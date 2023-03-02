nome = input ('Digite seu nome completo ')
#j 0 s 18
base_para_o_contador = len(nome)
contador = 0
novo_nome = ''
nome2 = ""
while contador < base_para_o_contador :
    novo_nome += nome[contador]
    nome2 += nome[contador]+'*'
    contador += 1
    print (novo_nome)
print (nome2)



