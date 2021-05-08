def buscaBinaria(L,x):
	return buscaBinariaR(L,x,0,len(L)-1)

def buscaBinariaR(L,x,ini,fim):
	if L!=[]:
		#Meio pra frente
		print(L)
		meio = int(fim/2) #pega o do meio no ímpar
		if x > L[meio]:
			return buscaBinariaR(L[meio+1:],x,ini+meio+1,len(L[meio+1:]))
		elif x<L[meio]:
			return buscaBinariaR(L[:meio],x,ini,len(L[:meio]))
		elif x==L[meio]:
			return meio+ini
	else:
		return None
l1 = [12,21,32,45,82,98,110]
print(buscaBinariaR(l1,110,0,len(l1)-1))