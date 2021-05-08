def ehTriangulo(a,b,c):
	if (abs(b-c) < a and a< b+c) and (abs(a-c)<b and b<a+c) and (abs(a-b) < c and c<a+b):
		return True		
	else:
		return False
def tipoTriangulo(a,b,c,resp):

	if resp == True:
		if a ==b and b==c:
			print("equilátero")
		elif a!=b and b!=c and a!=c:
			print("escaleno")
		else:
			print("isósceles")
	else:
		print("As medidas não formam um triângulo")
def main():
	a = int(input("Digite o a: "))
	b = int(input("Digite o b: "))
	c = int(input("Digite o c: "))
	tipoTriangulo(a,b,c,ehTriangulo(a,b,c))
main()