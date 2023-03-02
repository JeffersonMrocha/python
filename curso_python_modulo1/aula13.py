nome = "jefferson medeiros rocha"
altura = 1.75
peso = 105
imc = peso / altura ** 2

#introdução a formatação de strings
print (nome, "tem", altura, "de altura", "e", peso, "de peso, e seu IMC é:", imc)
print (f"{nome} tem {altura} de altura e {peso} de peso e seu IMC é: {imc:.1f}")