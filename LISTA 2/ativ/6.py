import math
def a(n):
	if n>1000 and n<9999:

		n1 = n//100
		n2 = n%100
		if math.pow(n1+n2,2) == n:
			return True
		else:
			return False
	else:
		return False
def b():
	num = int(input("Digite o número: "))
	resp = a(num)
	if resp == True:
		print("O número {} possui essa propriedade!".format(num))
	else:
		print("O número {} não possui essa propriedade ou não possui 4 dígitos!".format(num))

