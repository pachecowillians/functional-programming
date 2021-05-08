import math

def areaQuadrado(r):
	return r**2
def areaCirculo(r):
	return math.pi*(r**2)
def areaHexagono(r):
	return ((3*math.sqrt(3))/2)*(r**2)
def imprime(r,func):
	print("A área da figura é: {0:.2f}".format(func(r)))

imprime(4,areaQuadrado)
imprime(5,areaCirculo)
imprime(4,areaHexagono)