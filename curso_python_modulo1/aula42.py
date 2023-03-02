""" #minha resolução

frase = 'Um ninho de mafagafos tinha sete mafagafinhos. \
Quem desmafagar esses mafagafinhos bom desmagafigador será.'

indice= 0
quantidade_letras_apareceu = 0
letras_mais_vezes = ''

while indice < len (frase) :
    
    letra_atual = frase[indice]
    contador_letras = frase.count (letra_atual)
    if quantidade_letras_apareceu < contador_letras and letra_atual != ' ' :
        quantidade_letras_apareceu = contador_letras
        letras_mais_vezes = letra_atual
    
    

    indice += 1
print (frase)
print (f'a letra que mais apareceu foi "{letras_mais_vezes}" \
que apareceu {quantidade_letras_apareceu} vezes') """


""" #resolução do professor
frase = 'aaaooo'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
) """