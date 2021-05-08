def AreaEsfera1():
	r = float(input("Digite o raio da esfera: "))
	print("A área da esfera é: {}".format(4*3.14*(r**2)))
def AreaEsfera2(r):
	print("A área da esfera é: {}".format(4*3.14*(r**2)))
def AreaEsfera3(r):
	return 4*3.14*(r**2)
def main():
	AreaEsfera1()
	AreaEsfera2(2)
	print(AreaEsfera3(2))
main()	