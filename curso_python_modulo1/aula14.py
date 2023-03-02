a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
formato = "a= {0} b= {1} c= {2:.2f} d= {2}".format(a, b, c) #edição de strings usando o .format
formato2 = "a= {nome1} b= {nome2} c= {nome3:.2f} d= {nome3}".format (nome1=a, nome2=b, nome3=c)
#edição usando .format e parametros nomeados
print (formato)
print(formato2)