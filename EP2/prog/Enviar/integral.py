def numeroValido(n,i=0): #verifica se o número todo está certo
	"""Verifica se o valor recebido é realmente um número ou não"""
	return True if isinstance(n,int) or isinstance(n,float) else False

def regraTrapezios(func,a,b,n,i=1,soma=0,dx=0): #Primeira função obrigatória
	"""Calcula a integral definida por meio da regra dos trapézios. Antes disso, 
	verifica se os valores de a,b e n são números. Se o valor não for um número ela 
	imprime uma mensagem na tela e retorna False"""
	if numeroValido(a) and numeroValido(b) and numeroValido(n):
		if i<n:
			dx = (b-a)/n 
			xn = a+(i*dx)
			yn = 2*func(xn)
			return regraTrapezios(func,a,b,n,i+1,soma+yn,dx)
		else:
			return (soma+func(a)+func(b))*dx/2
	else:
		print("Números inválidos")
		return False

def regraSimpson(func,a,b,n,i=1,soma=0,dx=0): #Segunda função obrigatória
	"""Calcula a integral definida por meio da regra de Simpson. Antes disso, 
	verifica se os valores de a,b e n são números. Se o valor não for um número ela 
	imprime uma mensagem na tela e retorna False"""
	if numeroValido(a) and numeroValido(b) and numeroValido(n):
		if i<n:
			dx = (b-a)/n 
			xn = a+(i*dx)
			if i%2==0:
				yn = 2*func(xn)
			else:
				yn = 4*func(xn)
			return regraSimpson(func,a,b,n,i+1,soma+yn,dx)
		else:
			return (soma+func(a)+func(b))*dx/3
	else:
		print("Números inválidos")
		return False

def calculaIntegralMetodos(funcMetodo,func,a,b,listaN): #Terceira função obrigatória
	"""Calcula a integral definida por meio da regra de Simpson ou dos trapézios para 
	todo N pertencente a lista e retorna uma lista com os valores."""
	listaIntegralMetodo = list(map(lambda n: funcMetodo(func,a,b,n),listaN))
	return listaIntegralMetodo

def erroRelativo(integralMetodo,integralDefinida):
	"""Calcula e retorna o erro relativo ao receber o valor da integral calculada pelo método
	e a integral exata."""
	return (abs(integralMetodo-integralDefinida))/integralDefinida