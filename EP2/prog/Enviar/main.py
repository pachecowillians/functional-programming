import integral as i #importa o módulo integral e renomeia ele como i para facilitar a chamada das funções
import math as m #importa a biblioteca e renomeia ela como m para facilitar a chamada das funções
import grafico as g
#Minhas integrais são a 10,2,4

def func1(x): #Função associada a função 2: (sin²(x) + 2sin^4(2x)dx) de o a pi
	"""Essa função aplica a primeira função em um x e retorna o resultado. 
	É uma das funções obrigatórias"""
	return (m.sin(x))**2 + 2*((m.sin(2*x))**4)

def func2(x): #Função associada a função 4: (1/[1+(x−π)²]dx) de 0 a 6
	"""Essa função aplica a segunda função em um x e retorna o resultado. 
	É uma das funções obrigatórias"""
	return 1/(1 + (x-m.pi)**2)

def func3(x): #Função associada a função 10: (xe^−x dx) de 0 a 15
	"""Essa função aplica a terceira função em um x e retorna o resultado. 
	É uma das funções obrigatórias"""
	return x*m.exp(-x)

def integralDefinidaExata(n): #retorna o valor da integral definida de acordo com a função escolhida
	"""Uma função que foi feita para que seja mais fácil realizar o processo.
	Já que foi dado um valor exato para a integral definida de cada função, essa função retorna esse valor
	de acordo com a função escolhida. """
	if n==1:
		return (5*m.pi)/4 # = 7.853981633974483
	elif n==2:
		return m.atan(6-m.pi) + m.atan(m.pi) # = 2.4968867041877525
	elif n==3:
		return 1-(16/(m.exp(15))) # = 0.999995105562872
	else:
		print("Valor inválido")

def escolhaFuncao(n): #Escolhe de qual função vai ser calculada a integral
	"""A função escolhaFuncao recebe um número relativo a função que se deseja 
	usar e retorna todos os a,b,n e integral definida relativos a essa função"""
	if n==1:
		return func1,0,m.pi,"sen^2(x) + 2sen^4(2x)",integralDefinidaExata(n)
	elif n==2:
		return func2,0,6,"1/(1+[x−π]^2)",integralDefinidaExata(n)
	elif n==3:
		return func3,0,15,"xe^{−x}",integralDefinidaExata(n)
	else:
		print("Função inexistente, a integral foi calculada com a função 1")
		return func1,0,m.pi,integralDefinidaExata(1)

def imprimirRecursivo(integralMetodo,erroRelativo,listaN,i=0):
	"""Função utilizada para imprimir a lista de integrais e erros relativos a cada N"""
	if i<len(listaN):
		print("{0}	{1:.020f}	{2:.020f}".format(listaN[i],integralMetodo[i],erroRelativo[i]))
		imprimirRecursivo(integralMetodo,erroRelativo,listaN,i+1)


def printResultado(func,a,b,listaN,integralTrapezio,integralSimpson,integralDefinida):
	"""Função usada par facilitar a organizar o processo de imprimir na tela a tabela"""
	print("Função: {} com a = {} e b = {}".format(func,a,b))
	print("Valor Exato = {0:.020f}\n".format(integralDefinida))

	print("==> Regra dos Trapézios")
	print("---------------------------------------------------------")
	print("n 		Integral		Erro")
	print("---------------------------------------------------------")
	erroRelativoT = list(map(lambda n: i.erroRelativo(n,integralDefinida),integralTrapezio)) #Utilizei o map pois fica mais curto e simples de fazer
	imprimirRecursivo(integralTrapezio,erroRelativoT,listaN)

	print("---------------------------------------------------------")
	print("==> Regra de Simpson")
	print("---------------------------------------------------------")
	print("n 		Integral		Erro")
	print("---------------------------------------------------------")
	erroRelativoS = list(map(lambda n: i.erroRelativo(n,integralDefinida),integralSimpson)) #Utilizei o map pois fica mais curto e simples de fazer
	imprimirRecursivo(integralSimpson,erroRelativoS,listaN)
	print("---------------------------------------------------------")

def plotGrafico(x,listaN,integralTrapezio,integralSimpson,nomeFuncao,intDefinida,f,a,b):
	"""Função usada para plotar os gráficos. Por meio dela são chamadas todas as funções 
	relativas a gráficos do módulo grafico.py."""
	g.graficoBarras(integralTrapezio[len(integralTrapezio)-1],integralSimpson[len(integralSimpson)-1],nomeFuncao)
	g.geraGrafico(f,a,b,x)
	g.g1(listaN,integralTrapezio,integralSimpson,nomeFuncao)
	g.g2(listaN,integralTrapezio,integralSimpson,nomeFuncao,intDefinida)
	g.g3(listaN,integralTrapezio,integralSimpson,nomeFuncao,intDefinida,i.erroRelativo)
	g.g4(listaN,integralTrapezio,integralSimpson,nomeFuncao,intDefinida,i.erroRelativo)
	g.g5(listaN,integralTrapezio,integralSimpson,nomeFuncao,intDefinida,i.erroRelativo)

def main():
	"""Função principal que chama e conecta todas as outras funções. 
	Ela não recebe nada por parâmetro nem retorna nada."""
	f,a,b,nomeFuncao,intDefinida = escolhaFuncao(1) # Chamando a primeira função
	listaN = [4,10,50,100,150,200,300,400,500,600,700,800,900]
	integralTrapezio = (i.calculaIntegralMetodos(i.regraTrapezios,f,a,b,listaN))
	integralSimpson = (i.calculaIntegralMetodos(i.regraSimpson,f,a,b,listaN))
	printResultado(nomeFuncao,a,b,listaN,integralTrapezio,integralSimpson,intDefinida)
	#plotGrafico(1,listaN,integralTrapezio,integralSimpson,nomeFuncao,intDefinida,f,a,b)
	

	f,a,b,nomeFuncao,intDefinida = escolhaFuncao(2) # Chamando a segunda função
	integralTrapezio = (i.calculaIntegralMetodos(i.regraTrapezios,f,a,b,listaN))
	integralSimpson = (i.calculaIntegralMetodos(i.regraSimpson,f,a,b,listaN))
	printResultado(nomeFuncao,a,b,listaN,integralTrapezio,integralSimpson,intDefinida)
	#plotGrafico(2,listaN,integralTrapezio,integralSimpson,nomeFuncao,intDefinida,f,a,b)

	f,a,b,nomeFuncao,intDefinida = escolhaFuncao(3) # Chamando a terceira função
	integralTrapezio = (i.calculaIntegralMetodos(i.regraTrapezios,f,a,b,listaN))
	integralSimpson = (i.calculaIntegralMetodos(i.regraSimpson,f,a,b,listaN))
	printResultado(nomeFuncao,a,b,listaN,integralTrapezio,integralSimpson,intDefinida)
	#plotGrafico(3,listaN,integralTrapezio,integralSimpson,nomeFuncao,intDefinida,f,a,b)

main()