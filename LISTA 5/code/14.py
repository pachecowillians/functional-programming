a = list(map(lambda x: (x**2)+2,list(range(0,11))))
b = list(map(lambda x: x,list(filter(lambda x: True if x%3==0 and x%5==0 else False,range(-100,100)))))

def ehPerfeito(x,i=1,cont=0):
	if i<x:
		if x%i==0:
			return ehPerfeito(x,i+1,cont+i)
		else:
			return ehPerfeito(x,i+1,cont)
	else:
		return True if cont==x else False

c = list(map(lambda x: x,list(filter(ehPerfeito,range(0,501)))))

def ehPrimo(x,i=1,cont=0):
	if i<=x:
		if x%i==0:
			return ehPrimo(x,i+1,cont+1)
		else:
			return ehPrimo(x,i+1,cont)
	else:
		return True if cont==2 else False

d = list(map(lambda x: x,list(filter(ehPrimo,range(0,101)))))

def fibonacci(n,i=0,v1=1,v2=1):
	if i<n-1:
		aux = v1
		v1 = v2
		v2 = aux + v1
		return fibonacci(n,i+1,v1,v2)
	else:
		return v1

e = list(map(fibonacci,list(range(1,11))))
print(e)
		 
