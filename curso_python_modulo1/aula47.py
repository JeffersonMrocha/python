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
import os
jogatinas = 1
palavra_secreta = 'ventilador'
letras_acertadas = ''
verificador_numero = None
contagem_tentativas = 0 
reiniciar_jogo = ''
while True:
    
    letra_usuario = input ('Digite uma letra: ')

    try:
        int(letra_usuario)
        verificador_numero = True
    except:
        verificador_numero = False

    if verificador_numero:
        print ('Pf digite apenas letras!')
        continue
    
    contagem_tentativas +=1
    palavra_formada = ''
    if len(letra_usuario) > 1:
        print ('pf digite apenas uma letra')
        continue

    if letra_usuario in palavra_secreta:
        letras_acertadas += letra_usuario

    for i in palavra_secreta:
        if i in letras_acertadas:
            palavra_formada += i
            
        else:
            palavra_formada += '*'
    print (palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system ('cls')
        print (f'Parabens você venceu!! o Numero de tentativas foi de {contagem_tentativas} Tentativas')
        print (f'A palavra secreta era {palavra_secreta}')
        jogatinas += 1
        reiniciar_jogo = input ('Deseja, jogar novamente? [S]im [N]ao:').lower ()
        if reiniciar_jogo == 's' :
            letras_acertadas = ''
            contagem_tentativas = 0
            reiniciar_jogo = ''
            if jogatinas == 2:
                palavra_secreta = palavra_secreta.replace ('ventilador','televisao')
                continue
            elif jogatinas == 3:
                palavra_secreta = palavra_secreta.replace ('televisao','motocicleta')
                continue
            elif jogatinas == 4:
                palavra_secreta = palavra_secreta.replace ('motocicleta','computador')
                continue
            elif jogatinas == 5:
                palavra_secreta = palavra_secreta.replace ('computador','ventilador')
                jogatinas = 1
                continue
        else:
            break

    

