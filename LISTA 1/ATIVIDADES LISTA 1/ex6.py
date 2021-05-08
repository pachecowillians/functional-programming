#Números palíndromos

numero = int(input("Digite o número: "))

numMod = numero

a1 = numero%10
numMod = numero//10
a2 = numMod%10
numMod = numMod//10
a3 = numMod%10
numMod = numMod//10
a4 = numMod%10

if numero>=1000 and numero <=9999:
	if a1==a4 and a2==a3:
		print("O número é palíndromo!")
	else:
		print("O número não é palíndromo!")
else:
	print("O número inserido não se encontra no intervalo [1000,9999]")