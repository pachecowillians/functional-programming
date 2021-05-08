import math
def ehPar(n):
	if type(n)==int :
		x = 10
		if n%10<1:
			print(x)
			x+=10
			ehPar(x)
	else:
		print("Não são numeros inteiros!")
		return False
def main():
	print(ehPar(60))
main()