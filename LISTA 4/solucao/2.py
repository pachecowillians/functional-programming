#a)
def numeros(lista,i=0):
	if i<len(lista):
		if isinstance(lista[i],int) or isinstance(lista[i],float):
			return numeros(lista,i+1)
		else:
			return False
	else:
		return True
l = [3,2.3,4,2]
#print(numeros(l))



#b)

def soma(lista,i=0,s=0):
	if i<len(lista):
		return soma(lista,i+1,s + lista[i])
	else:
		return s

#print(soma(l))


#c)

def media(lista,i=0,s=0):
	if i<len(lista):
		return media(lista,i+1,s + lista[i])
	else:
		return s/i

#print(media(l))

#d)

def maiMen(lista,i=0,mai=0,men=0):
	if i==0:
		mai = lista[i]
		men = lista[i]
		return maiMen(lista,i+1,mai,men)
	elif i<len(lista):
		if lista[i]>mai:
			return maiMen(lista,i+1,lista[i],men)
		elif lista[i]<men:
			return maiMen(lista,i+1,mai,lista[i])
		else:
			return maiMen(lista,i+1,mai,men)
	else:
		return mai,men
l = [1,2,0.5,7]
#print(maiMen(l))

def contPares(lista,i=0,c=0):
	if i<len(lista):
		if lista[i]%2==0:
			return contPares(lista,i+1,c+1)
		else:
			return contPares(lista,i+1,c)
	else:
		return c

#print(contPares([1,2,3,4,5]))

def inverso(lista,i=0,lista2 = []):
	if i<len(lista):
		return inverso(lista,i+1,[lista[i]]+lista2)
	else:
		return lista2

#print(inverso([1,2,3,4,2,4]))

def dentroLista(lista,elemento):
	return elemento in lista

#print(dentroLista([1,2,3,4],0))

def contElemento(lista,elemento,i=0,c=0):
	if i<len(lista):
		if lista[i] == elemento:
			return contElemento(lista,elemento,i+1,c+1)
		else:
			return contElemento(lista,elemento,i+1,c)
	else:
		return c

#print(contElemento([1,1,1,3,4,1,4,2,4],0))

def divisores(n,i=1,lista=[]):
	if i<=n:
		if n%i==0:
			return divisores(n,i+1,lista+[i])
		else:
			return divisores(n,i+1,lista)
	else:
		return lista

#print(divisores(10))

def pares(lista,i=0,lista2=[]):
	if i<len(lista):
		if lista[i]%2==0:
			return pares(lista,i+1,lista2+[lista[i]])
		else:
			return pares(lista,i+1,lista2)
	else:
		return lista2

#print(pares([1,2,3,4,5,6]))

def multiplos(x,n,lista = [],i=0):
	if i<n:
		return multiplos(x,n,lista+[x*i],i+1)
	else:
		return lista

#print(multiplos(3,8))

def l(fim,i=0,lista=[]):
	if fim<0:
		return lista
	else:
		if i<=fim:
			return l(fim,i+1,lista+[i])
		else:
			return lista

#print(l(10))


def m(ini,fim,lista=[]):
	if fim<ini:
		return lista
	else:
		if ini<=fim:
			return m(ini+1,fim,lista+[ini])
		else:
			return lista

#print(m(10,15))

def n(fim,s,i=0,lista=[]):
	if fim<0 or s<=0:
		return lista
	else:
		if i<=fim:
			return n(fim,s,i+1,lista+[i*s])
		else:
			return lista

#print(n(10,2))

def o(ini,fim,s,lista=[]):
	if fim<0 or s<=0:
		return [] 
	elif fim<ini:
		return lista
	else:
		if ini<=fim:
			return o(ini+1,fim,s,lista+[ini*s])
		else:
			return lista

#print(o(5,10,2))