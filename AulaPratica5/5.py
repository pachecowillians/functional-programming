import math
def ehPar(n):
	if type(n)==int :
		if n%2==0:
			return True
		else:
			return False
	else:
		print("Não são numeros inteiros!")
		return False
def main():
	print(ehPar(6))
main()