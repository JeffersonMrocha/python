
lista_com_palavras = ['Televisao', 'Carro', 'Ventilador', 'Banana', 'Armario', 'Janela', \
                      'Piscina', 'Bicicleta', 'Computador', 'Papelao', 'Telhado', \
                        'Tomada', 'Comoda', 'Cachorro', 'Cavalo', 'Paralelepipedo', \
                              'Tubarao', 'inconstitucionalissimamente', ]

indice_lista = 0  
letras_acertadas = ''
checagem_int = None
tentativas= 0
reset_p2 = None

while True:
    p1_ou_p2 = input('vc quer jogar sozinho[1] ou com outra pessoa[2]?: ')
    
    if p1_ou_p2 == '1':
        
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
                reset_p = input ('deseja resetar o modo de jogo tbm? [S]im [Não]?: ').lower ()
                
                if reset_p == 's':
                    tentativas = 0
                    letras_acertadas = ''
                    indice_lista += 1
                    break
                

                if reset_input == 's':
                    tentativas = 0
                    letras_acertadas = ''
                    indice_lista += 1
                    continue
                else:
                    break

    if p1_ou_p2 == '2':
        while True:
            if reset_p2 == True:
                reset_p2 = None
                break
            palavra_secreta = input ('peça para que a pessoa ao lado digite uma palavra! NÃO OLHE X)!!!!! \n após a palavra secreta ser digitada digite uma letra por vez! \n Digite a palavra: ')
            while True:
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
                    reset_p = input ('deseja resetar o modo de jogo tbm? [S]im [Não]?: ').lower ()
                    
                    if reset_p == 's':
                        tentativas = 0
                        letras_acertadas = ''
                        indice_lista += 1
                        reset_p2 = True
                        break 
                    

                    if reset_input == 's':
                        tentativas = 0
                        letras_acertadas = ''
                        indice_lista += 1
                        break
                    else:
                        break
                    reset_p2 = True