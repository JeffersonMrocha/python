# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

usuario_usuario = input ('Digite seu usuario para entrar ou digite [S] para sair ')
senha_usuario = input ('Digite sua senha ')
senha_correta = '123456'
usuario_correto = "tarvox"

if (usuario_usuario == "tarvox" or usuario_usuario == 'TARVOX') and senha_usuario == senha_correta :
    print ('Você entrou no sistema!')
elif usuario_usuario == "s" : 
    print ('vc saiu do sistema')
else :
    print ('Senha ou usuario incorreto')