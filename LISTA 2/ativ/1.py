import math
def a(x,y):
	if x>y:
		return x
	else:
		return y
def b(n):
	if n<0:
		n*=-1
	return n
def c(n):
	if n%5==0:
		return True
	else:
		return False
def d(x,y,z):
	mai = x
	med = x
	men = x

	if y> mai:
		mai = y
	if z> mai:
		mai = z

	if y<men:
		men = y
	if z<men:
		men = z

	if mai != y and men != y:
		med = y
	if mai != x and men != x:
		med = x
	if mai != z and men != z:
		med = z

	print(men)
	print(med)
	print(mai)
def e(x,y,z):
	mai = x
	med = x
	men = x

	if y> mai:
		mai = y
	if z> mai:
		mai = z

	if y<men:
		men = y
	if z<men:
		men = z

	if mai != y and men != y:
		med = y
	if mai != x and men != x:
		med = x
	if mai != z and men != z:
		med = z

	return men,med,mai
def f(r):
	a = 4*math.pi*r**2
	v = (4*math.pi*r**3)/3
	print("Area: {}".format(a))
	print("Volume: {}".format(v))
	return a,v
	#Não definiu o número de casas decimais, então deixei todas
def g(x,y,z):

	if x<y and x<z:
		return (y**2)+(z**2)
	elif y<x and y<z:
		return (x**2)+(z**2)
	elif z<x and z<y:
		return (x**2)+(y**2)
def h(t):
	h = t//3600
	m = (t-(h*3600))//60
	s = t - ((h*3600) + (m*60))
	print("{}:{}:{}".format(h,m,s))
def i(v,w,x,y,z):
	somaPar = 0
	somaImpar = 0
	contPar = 0
	contImpar = 0
	mediaPar = 0
	mediaImpar = 0

	if v%2==0:
		somaPar += v
		contPar += 1
	else:
		somaImpar += v
		contImpar += 1

	if w%2==0:
		somaPar += w
		contPar += 1
	else:
		somaImpar += w
		contImpar += 1

	if x%2==0:
		somaPar += x
		contPar += 1
	else:
		somaImpar += x
		contImpar += 1

	if y%2==0:
		somaPar += y
		contPar += 1
	else:
		somaImpar += y
		contImpar += 1

	if z%2==0:
		somaPar += z
		contPar += 1
	else:
		somaImpar += z
		contImpar += 1

	if contPar != 0:
		mediaPar = somaPar/contPar
	if contImpar != 0:
		mediaImpar = somaImpar/contImpar

	return somaPar,mediaPar,somaImpar,mediaImpar

def j(v):
	if type(v)==int:
		print("Inteiro")
	elif type(v)==float:
		print("Ponto flutuante")
	elif type(v)==str:
		print("String")
	elif type(v)==bool:
		print("Booleano")
	else:
		print("Outro tipo ({})".format(type(v)))
def k(n):
	if n>=100 and n<=999 and type(n)==int:
		n1 = n//100
		n2 = (n%100)//10
		n3 = (n%100)%10

		if n1<n2 and n2<n3:
			return True
		else:
			return False
	else:
		print("O número não está no intervalo [100,999] ou não é inteiro")
		return False
def l(n):
	if n>=1000 and n<=9999 and type(n)==int:
		n1 = n//1000
		n2 = (n%1000)//100
		n3 = ((n%1000)%100)//10
		n4 = ((n%1000)%100)%10
		
		if n1==n4 and n2==n3:
			return True
		else:
			return False
	else:
		print("O número não está no intervalo [1000,9999] ou não é inteiro")
		return False