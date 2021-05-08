def f(l,cont=0):
	n = int(input("Digite os valores (um número <0 ou >9 indica o fim da leitura): "))
	if n in [0,1,2,3,4,5,6,7,8,9]:
		l[n]+=1
		return f(l,cont+1)
	else:
		return l,cont

def printResultado(l,i=0):
	if i<len(l):
		print("{}: {}".format(i,l[i]))
		return printResultado(l,i+1)

lista = [0,0,0,0,0,0,0,0,0,0]
lista,cont = f(lista)
print("\nNumeros digitados: {}".format(cont))
print("Frequência de cada numero")
printResultado(lista)

