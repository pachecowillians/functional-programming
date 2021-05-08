#Atividade 7, ver se um número é ascendente

numero = int(input("Digite o seu número: "))
numMod = numero
a1 = numero%10
numMod = numero//10
a2 = numMod%10
numMod = numMod//10
a3 = numMod%10

print(a3,a2,a1)

if int(numero)>=100 and int(numero)<= 999:
	if a3<a2 and a2<a1:
		print("É ascendente")
	else:
		print("Não é ascendente")
else:
	print("{} não está no intervalo [100,999]".format(numero))
