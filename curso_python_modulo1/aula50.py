"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
lista_com_palavras = ['Televisao', 'Carro', 'Ventilador', 'Banana', 'Armario', 'Janela', \
                      'Piscina', 'Bicicleta', 'Computador', 'Papelao', 'Telhado', \
                        'Tomada', 'Comoda', 'Cachorro', 'Cavalo', 'Paralelepipedo', \
                              'Tubarao', 'inconstitucionalissimamente', ]
##print (len(lista_com_palavras))
indice_lista = 0  

##print (palavra_secreta)
letras_acertadas = ''
checagem_int = None
tentativas= 0
while True:
    palavra_secreta = lista_com_palavras[indice_lista].lower()
    palavra_input= input ('Digite uma letra: ').lower()

    try:
        int (palavra_input)
        checagem_int = True
    except:
        checagem_int = None

    if checagem_int :
        print ('Pf Digite apens letras!')
        continue
    if len(palavra_input) > 1 :
        print ('Pf Digite apenas uma letra!')
        continue
    if palavra_input == ' ' :
        print ('PF digite algo!')
        continue
    if palavra_input in palavra_secreta:
        letras_acertadas += palavra_input
    
    tentativas += 1
    
    palavra_mostrada = ''

    for letra in palavra_secreta:
        
        if letra in letras_acertadas:
            palavra_mostrada += letra
            
        else:
            palavra_mostrada += '*'
            
    print (palavra_mostrada)
    
    if palavra_mostrada == palavra_secreta:
        print (f'Parabéns, você venceu!! \n a palavra secreta era "{palavra_secreta}".\n Você levou {tentativas} para conseguir acertar!')
        reset_input = input ('Deseja Jogar novamente? [S]im [N]ão?: ').lower ()
        if reset_input == 's':
            tentativas = 0
            letras_acertadas = ''
            indice_lista += 1
            continue
        else:
            break
