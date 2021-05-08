def a(n=1):
	print(n)
	if n<10:
		a(n+1)
def b(n=1000):
	n1 = n//1000
	n2 = (n-(n1*1000))//100
	n3 = (n-(n1*1000)-(n2*100))//10
	n4 = n%10

	if (n1==n4 and n3==n2 and n3!=9):
		print(n)
		b(n+110)
	elif(n1==n4 and n3==n2 and n3==9):
		print(n)
		b(n+1)
	elif n<9999:
		b(n+1)

def c(n,m=1):
	print(m)
	if m<n:
		c(n,m+1)
def d(a,b):
	if int(a+1)<b:
		print(int(a+1))
		d(a+1,b)
def e(a,b,cont=0,soma=1):
	if cont<b:
		return e(a,b,cont+1,soma*a)
	else:
		return soma
def f(n,cont=1,div=0):
	if n%cont==0:
		div+=1
	if cont<=n:
		return f(n,cont+1,div)
	else:
		return div
def g(n,cont=1,div=0):
	if n%cont==0:
		div+=1
	if cont<=n:
		return True if(f(n,cont+1,div))==2 else False
	else:
		return True if(div==2) else False
def h(n,soma=0):
	if n==0:
		return soma
	else:
		return h((n-(n%10))//10,soma+(n%10))

print(h(12345))