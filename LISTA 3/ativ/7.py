import math
def euler(n,cont=0,soma=0):
	if cont<n:
		soma+=1/math.factorial(cont)
		return euler(n,cont+1,soma)
	if cont==n:
		return soma
def main():
	n = int(input("Numero de termos: "))
	print("Resultado: {0:.5f}".format(euler(n)))
main()