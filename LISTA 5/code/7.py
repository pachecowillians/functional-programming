def leituraTemperatura(n,i=0,l=[]):
	if i<n:
		temp = float(input("Temperatura: "))
		l = l[:]+[temp]
		return leituraTemperatura(n,i+1,l)
	else:
		return l
def media(listaTemp,cont=0,soma=0):
	#retorna media
	if cont<len(listaTemp):
		return media(listaTemp,cont+1,soma+listaTemp[cont])
	else:
		return soma/cont

def desvioPadrao(l,m,i=0,soma=0):
	#calcula e retorna o desvio padrão
		if i<len(l):
			return desvioPadrao(l,m,i+1,soma+((l[i]-m)**2))
		else:
			return ((soma/len(l))**(1/2))

def main():
	l = leituraTemperatura(3)
	med = media(l)
	return desvioPadrao(l,med)

print(main())	
