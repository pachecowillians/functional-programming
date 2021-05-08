import math
def volumeCilindro(r,h):
	if (type(r)==int or type(r)==float) and (type(h)==int or type(h)==float):
		return (math.pi*math.pow(r,2))*h
	else:
		print("Não são numeros!")
		return None
def main():
	print(volumeCilindro(1,3))
main()