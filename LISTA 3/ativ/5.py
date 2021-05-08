def ehPerfeito(n,soma=0,cont=1):
	if int(n) == n and n>0:
		if cont<n:
			if n%cont==0:
				soma+=cont
			return ehPerfeito(n,soma,cont+1)
		if cont==n:
			return True if soma== n else False
	else:
		print("O número não é Natural")
def perfeitos(n,cont=1):
	if int(n) == n and n>0:
		if cont<=n:
			if ehPerfeito(cont)==True:
				print(cont)
			perfeitos(n,cont+1)
	else:
		print("O número não é Natural")
def main():
	n = int(input("Insira um número inteiro: "))
	perfeitos(n)
main()