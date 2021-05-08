def func1(lista,p,item,i=0):
	if p<0 or p>len(lista):
		print("Posição incorreta")
		return lista
	else:
		return lista[:p] + [item] + lista[p:]
l = [1,2,3]
print(func1(l,4,"a"))