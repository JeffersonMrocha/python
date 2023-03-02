for i in range (21):
    if i == 5 :
        print (f'I e igual a 5 e contando....')
        continue
    
    """ if i == 15 :
        print ('seu else não executara')
        break """

    for j in range (1, 4):
        print (i, j)

else:
    print ('seu for foi executado')