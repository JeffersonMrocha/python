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

entrar = input ('Digite [E] para entrar e [S] para sair ')
senha_usuario = input ('Digite sua senha ')
senha_correta = '123456'

if entrar == "e" and senha_usuario == senha_correta :
    print ('Você entrou no sistema!')
elif entrar == "s" : 
    print ('vc saiu do sistema')
else :
    print ('Senha ou usuario incorreto')