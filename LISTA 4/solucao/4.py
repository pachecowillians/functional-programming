def divisores(x,i=1,cont=0):
	if i<=x:
		if x%i==0:
			return divisores(x,i+1,cont+1)
		else:
			return divisores(x,i+1,cont)
	else:
		return cont

def primos(n,i=0,cont=0,lista=[]):
	if cont<n:
		if divisores(i)==2:
			return primos(n,i+1,cont+1,lista+[i])
		else:
			return primos(n,i+1,cont,lista)
	else:
		return lista

print(primos(3))
