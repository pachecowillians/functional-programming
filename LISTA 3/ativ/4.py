def fibonacci(n,n1=1,n2=1,cont=1):
	if int(n) == n and n>0:
		if cont<=n:
			if n1==1 or n2==1:
				print(1)
				aux = n1+n2
				n1=n2
				n2=aux
				fibonacci(n,n1,n2,cont+1)
			elif n1>1:
				print(n1)
				aux = n1+n2
				n1=n2
				n2=aux
				fibonacci(n,n1,n2,cont+1)
	else:
		print("O número não é natural")
		return None
