import math

a = float(input("Digite o valor do primeiro lado do triângulo: "))
b = float(input("Digite o valor do segundo lado do triângulo: "))
c = float(input("Digite o valor do terceiro lado do triângulo: "))

if (abs(b-c) < a and a< b+c) and (abs(a-c)<b and b<a+c) and (abs(a-b) < c and c<a+b):
	if a ==b and b==c:
		print("\nTriângulo existe e é equilátero")
	if (a==b and b!=c and a!= c) or (a!=b and b==c and a!= c) or (a!=b and b!=c and a== c):
		print("\nTriângulo existe e é isósceles")
	if a!=b and b!=c and a!=c:
		print("\nTriângulo existe e é escaleno")
else:
	print("\nTriângulo não existe!")