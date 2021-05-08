l1 = list(range(2, 101))
l2 = list(filter(lambda x: True if x%3==0 and x%5==0 else False,l1))
def ehPrimo(x,i=1,cont=0):
	if i<=x:
		if x%i==0:
			return ehPrimo(x,i+1,cont+1)
		else:
			return ehPrimo(x,i+1,cont)
	else:
		return True if cont==2 else False
l3 = list(filter(ehPrimo,l1))
print(l2)
print(l3)