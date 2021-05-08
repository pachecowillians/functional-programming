def fibonacci(n,a=1,b=1,c=0,cont=0,lista=[]):
	if cont==0:
		return fibonacci(n,a,b,c,cont+1,lista + [a])
	elif cont<n:
		c = a+b
		a = b
		b = c
		return fibonacci(n,a,b,c,cont+1,lista + [a])
	else:
		return lista
print(fibonacci(12))
