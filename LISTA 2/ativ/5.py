import math
def delta(a,b,c):
	delta = (b**2)-4*a*c
	return delta
def raizes(a,b,c,d):
	if d<0:
		print("Equação não possui raizes")
	elif d==0:
		if a==0:
			print("'a' não pode ser zero!")
		else:
			x = (-1*b)/(2*a)
			print("As duas raizes da equação são iguais e são: {}".format(x))
	else:
		x1 = ((-1*b)+math.sqrt(d))/2*a
		x2 = ((-1*b)-math.sqrt(d))/2*a
		print("X1 = {}\nX2 = {}".format(x1,x2))
def main():
	a = int(input("Digite a: ")) #Coloquei int pois não disse nada que iria entrar com valores decimais
	b = int(input("Digite b: ")) 
	c = int(input("Digite c: ")) 
	raizes(a,b,c,delta(a,b,c))
main()
