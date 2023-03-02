
quantidade_de_linhas = 50
quantidade_de_colunas = 5
colunas = 0 #colunas foi colocado aqui tambem para nao deixar a criação da variavel atrelada ao while
linhas = 0

while linhas < quantidade_de_linhas :
    linhas += 1
    colunas = 0
    while colunas < quantidade_de_colunas :
        colunas += 1
        print (f'{linhas=} {colunas=}')

print ('acabou')