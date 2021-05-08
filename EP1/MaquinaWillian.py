from os import system, name #Bibliotecas usadas para limpar o console.

def limpaTela(): 

	"""A função limpaTela limpa o console toda vez que é chamada. 
	Ela é muito útil para manter uma interface limpa e mais simples para o usuário."""
	
	if name == 'nt': 
		system('cls') 
	else: 
		system('clear') #Função que limpa o console.
def printMenu(estoque1,estoque2,estoque3,estoque4):

	""" A função printMenu Imprime na tela o menu inicial para que o usuário possa compreender 
	quais códigos se relacionam com cada produto, e selecionar, por meio do código, qual produto
	ele deseja comprar. Além disso, ele pode analisar os preços dos produtos por aqui. Essa função também
	reconhece quando o produto está ou não disponível e já o apresenta como disponível ou indisponível 
	dependendo da quantidade em estoque."""
	
	limpaTela()

	#A seguir foram usadas expressões ternárias para mostrar a disponibilidade do produto de forma dinâmica de acordo com a quantidade em estoque.

	print("\n--------------------------------------")
	print("1 - Batata Recursiva	- R$5.00" if estoque1>0 else "1 - Batata Recursiva	- Indisponível")
	print("2 - BarraDe(Chocolate)	- R$3.50" if estoque2>0 else "2 - BarraDe(Chocolate)	- Indisponível")
	print("3 - Coca def Cola	- R$7.00" if estoque3>0 else "3 - Coca def Cola	- Indisponível")
	print("4 - str(Fanta)		- R$6.50" if estoque4>0 else "4 - str(Fanta)		- Indisponível")
	print("--------------------------------------\n")

def printValorPagoTroco(valorPago,troco):

	""" A função printValorPagoTroco imprime uma mensagem na tela que diz qual foi o valor 
	total que o usuário depositou na máquina e já imprime o troco que ele tem que receber de volta. """

	print("\nValor pago: R${0:.2f}".format(valorPago)) #Foi usado o .format() para que o valor possa ser formatado da melhor forma
	print("Troco: R${0:.2f}\n".format(troco))

def printNotasTroco(n20,n10,n5,n2,m1,m50):

	""" A função printNotasTroco é uma função recursiva que recebe por parâmetro a quantidade de
	cada nota que precisa ser devolvida no troco, e imprime na tela a nota repetidas vezes de acordo com 
	a quantidade de notas do mesmo valor que precisam ser usadas para o troco """

	# Essa função analisa a quantidade de cada nota e imprime na tela a nota até que ele sane toda a quantidade necessária. 
	# A cada incremento da função recursiva, é subtraída uma unidade da quantidade da nota que acabou de ser impressa, e assim ela imprime todas as notas baseado no tanto de notas de cada valor que precisa ser impressa.

	if n20!=0:
		print("R$20.00")
		printNotasTroco(n20-1,n10,n5,n2,m1,m50)  
	elif n10!=0:
		print("R$10.00")
		printNotasTroco(n20,n10-1,n5,n2,m1,m50)
	elif n5!=0:
		print("R$5.00")
		printNotasTroco(n20,n10,n5-1,n2,m1,m50)
	elif n2!=0:
		print("R$2.00")
		printNotasTroco(n20,n10,n5,n2-1,m1,m50)
	elif m1!=0:
		print("R$1.00")
		printNotasTroco(n20,n10,n5,n2,m1-1,m50)
	elif m50!=0:
		print("R$0.50")
		printNotasTroco(n20,n10,n5,n2,m1,m50-1)

def printDescricaoProduto(preco,prod):

	""" A função printDescricaoProduto imprime na tela a descrição do produto e o preço dele. 
	Essa é uma função que não retorna nenhum valor, apenas imprime valores na tela. 
	Ela foi usada para apresentar uma mensagem ao usuário. """

	print("\nVocê escolheu {}".format(prod))
	print("Preço: R${0:.2f}\n".format(preco))

def produtoValido(codProd):

	""" A função produtoValido verifica se o código inserido pelo usuário corresponde a um produto. 
	Se o código corresponder a algum produto, a função retorna True, se não False """

	# Nesse if foi verificado como string pois o usuário pode inserir algum caracter, e isso daria um problema ao converter um caracter para float ou inteiro. 
	# Dessa forma, ao converter para int ou float após ter certeza que é um número é mais seguro.

	if codProd == "1" or codProd =="2" or codProd == "3" or codProd == "4": 
		return True
	else:
		return False

def descricaoProduto(codProd):

	""" A função descricaoProduto retorna o nome e o preço do produto com base no código inserido pelo usuário. """

	prod = ""
	preco = 0
	if codProd ==1:
		prod = "Batata Recursiva"
		preco = 5.00
	elif codProd ==2:
		prod = "BarraDe(Chocolate)"
		preco = 3.50
	elif codProd ==3:
		prod = "Coca def Cola"
		preco = 7.00
	elif codProd ==4:
		prod = "str(Fanta)"
		preco = 6.50
	return preco,prod

def escolherProduto(estoque1,estoque2,estoque3,estoque4,codProd):

	""" A função escolherProduto retorna o estoque a ser alterado com base no código do produto. 
	Com isso, não é necessário que esse teste seja realizado diversas vezes, apenas que ele seja feito uma vez. """

	# Como o produto a ser comprado vai ser o mesmo em toda a compra, posso assumir apenas um estoque para ser alterado durante cada compra.

	if codProd == 1:
		return estoque1
	elif codProd == 2:
		return estoque2
	elif codProd == 3:
		return estoque3
	elif codProd == 4:
		return estoque4

def disponivel(estoque):

	""" A função disponivel verifica se o produto está disponível no estoque e retorna True caso sim e False caso não. """

	if estoque>0:
		return True
	else:
		return False

def maquinaVazia(estoque1,estoque2,estoque3,estoque4):

	""" A função maquinaVazia verifica se a máquina está vazia (estoques zerados), e retorna True ou False com base no resultado do teste lógico. """

	if estoque1==0 and estoque2==0 and estoque3==0 and estoque4==0:
		return True
	return False

def receber(preco,soma=0,notaRecebida20=0,notaRecebida10=0,notaRecebida5=0,notaRecebida2=0,moedaRecebida1=0,moedaRecebida50=0):
	
	""" A função receber é uma função recursiva que lê os valores que são inseridos na máquina. Ela verifica se os valores são 
	iguais a 20,10,5,2,1 ou 0.5, que são os valores permitidos, e incrementa um contador a cada nova nota de um valor que é inserida. 
	Porfim, ela retorna a soma total dos valores inseridos pelo usuário e as somas das quantidades de cada cédula."""

	if soma<preco:
		valor = input("Coloque o dinheiro: ")
		if valor == "20" or valor == "10" or valor== "5" or valor== "2" or valor =="1" or valor =="0.5": # Verifica se o valor é permitido.
			if valor == "20":
				notaRecebida20 += 1;
			elif valor == "10":
				notaRecebida10 += 1;
			elif valor == "5":
				notaRecebida5 += 1;
			elif valor == "2":
				notaRecebida2 += 1;
			elif valor == "1":
				moedaRecebida1 += 1;
			elif valor == "0.5":
				moedaRecebida50 += 1;
			return receber(preco,soma+float(valor),notaRecebida20,notaRecebida10,notaRecebida5,notaRecebida2,moedaRecebida1,moedaRecebida50) # Chama a função recursivamente incrementando a soma total a cada nota inserida.
		else:
			print("Valor não reconhecido!")
			return receber(preco,soma,notaRecebida20,notaRecebida10,notaRecebida5,notaRecebida2,moedaRecebida1,moedaRecebida50) # Se o valor não for reconhecido, uma mensagem de erro é apresentada e a função é chamada novamente sem somar nada ao total.
	else:
		return soma,notaRecebida20,notaRecebida10,notaRecebida5,notaRecebida2,moedaRecebida1,moedaRecebida50 # Retorna todos os valores quando tudo terminar.

def adicionar20(nota20,valorRecebido20):

	"""A função adicionar20 é uma função bem específica e utilizada para organizar o código.
	Ela apenas lê a antiga quantidade de cédulas de R$20,00 na máquina e soma a quantidade de 
	notas que foi inserida na compra."""

	return nota20+valorRecebido20

def adicionar10(nota10,valorRecebido10):

	"""A função adicionar10 é uma função bem específica e utilizada para organizar o código.
	Ela apenas lê a antiga quantidade de cédulas de R$10,00 na máquina e soma a quantidade de 
	notas que foi inserida na compra."""

	return nota10+valorRecebido10

def adicionar5(nota5,valorRecebido5):

	"""A função adicionar5 é uma função bem específica e utilizada para organizar o código.
	Ela apenas lê a antiga quantidade de cédulas de R$5,00 na máquina e soma a quantidade de 
	notas que foi inserida na compra."""

	return nota5+valorRecebido5

def adicionar2(nota2,valorRecebido2):

	"""A função adicionar2 é uma função bem específica e utilizada para organizar o código.
	Ela apenas lê a antiga quantidade de cédulas de R$2,00 na máquina e soma a quantidade de 
	notas que foi inserida na compra."""

	return nota2+valorRecebido2

def adicionar1(moeda1,valorRecebido1):

	"""A função adicionar1 é uma função bem específica e utilizada para organizar o código.
	Ela apenas lê a antiga quantidade de moedas de R$1,00 na máquina e soma a quantidade de 
	moedas que foi inserida na compra"""

	return moeda1+valorRecebido1

def adicionar05(moeda50,valorRecebido05):

	"""A função adicionar05 é uma função bem específica e utilizada para organizar o código.
	Ela apenas lê a antiga quantidade de moedas de R$0,50 na máquina e soma a quantidade de 
	moedas que foi inserida na compra"""

	return moeda50+valorRecebido05

def remover20(nota20,valorRecebido20):

	"""A função remover20 é o oposto da somar20. Ela subtrai a quantidade de notas de R$20,00 
	que foi inserida na compra da quantidade total, o que faz o caixa voltar ao valor inicial 
	como se nenhum valor houvesse sido inserido. Essa função é usada quando o usuário cancela 
	a compra por não ter troco, dessa forma, a quantidade é subtraída do estoque e pode ser devolvida
	a ele."""

	return nota20-valorRecebido20

def remover10(nota10,valorRecebido10):

	"""A função remover10 é o oposto da somar10. Ela subtrai a quantidade de notas de R$10,00 
	que foi inserida na compra da quantidade total, o que faz o caixa voltar ao valor inicial 
	como se nenhum valor houvesse sido inserido. Essa função é usada quando o usuário cancela 
	a compra por não ter troco, dessa forma, a quantidade é subtraída do estoque e pode ser devolvida
	a ele."""

	return nota10-valorRecebido10

def remover5(nota5,valorRecebido5):

	"""A função remover5 é o oposto da somar5. Ela subtrai a quantidade de notas de R$5,00 
	que foi inserida na compra da quantidade total, o que faz o caixa voltar ao valor inicial 
	como se nenhum valor houvesse sido inserido. Essa função é usada quando o usuário cancela 
	a compra por não ter troco, dessa forma, a quantidade é subtraída do estoque e pode ser devolvida
	a ele."""

	return nota5-valorRecebido5

def remover2(nota2,valorRecebido2):

	"""A função remover2 é o oposto da somar2. Ela subtrai a quantidade de notas de R$2,00 
	que foi inserida na compra da quantidade total, o que faz o caixa voltar ao valor inicial 
	como se nenhum valor houvesse sido inserido. Essa função é usada quando o usuário cancela 
	a compra por não ter troco, dessa forma, a quantidade é subtraída do estoque e pode ser devolvida
	a ele."""

	return nota2-valorRecebido2

def remover1(moeda1,valorRecebido1):

	"""A função remover1 é o oposto da somar1. Ela subtrai a quantidade de moedas de R$1,00 
	que foi inserida na compra da quantidade total, o que faz o caixa voltar ao valor inicial 
	como se nenhum valor houvesse sido inserido. Essa função é usada quando o usuário cancela 
	a compra por não ter troco, dessa forma, a quantidade é subtraída do estoque e pode ser devolvida
	a ele."""

	return moeda1-valorRecebido1

def remover05(moeda50,valorRecebido05):

	"""A função remover05 é o oposto da somar05. Ela subtrai a quantidade de moedas de R$0,50 
	que foi inserida na compra da quantidade total, o que faz o caixa voltar ao valor inicial 
	como se nenhum valor houvesse sido inserido. Essa função é usada quando o usuário cancela 
	a compra por não ter troco, dessa forma, a quantidade é subtraída do estoque e pode ser devolvida
	a ele."""

	return moeda50-valorRecebido05

def calculaTroco(valorPago,precoProduto):

	""" A função calculaTroco apenas tira a diferença entre o valor total que o usuário pagou e o preço
	do produto, para que se obtenha o troco a ser devolvido. """

	return valorPago-precoProduto

def troco20(valorPago,n20,somaTroco20=0):

	""" A função troco20 verifica se existe a nota em estoque, e usa elas para gerar o troco necessário para o cliente.
	Caso não tenha notas para compor o troco, vai sobrar um resto, e esse resto vai ser o tanto que a máquina vai ficar devendo ao usuário. """

	if n20>0 and valorPago>=20:
		return troco20(valorPago-20,n20-1,somaTroco20+1)
	else:
		return valorPago,n20,somaTroco20;

def troco10(valorPago,n10,somaTroco10=0):

	""" A função troco10 é uma função recursiva que verifica se existe a nota em estoque, e usa elas para gerar o troco necessário para o cliente.
	Caso não tenha notas para compor o troco, vai sobrar um resto, e esse resto vai ser o tanto que a máquina vai ficar devendo ao usuário. """


	if n10>0 and valorPago>=10:
		return troco10(valorPago-10,n10-1,somaTroco10+1)
	else:
		return valorPago,n10,somaTroco10;

def troco5(valorPago,n5,somaTroco5=0):

	""" A função troco5 é uma função recursiva que verifica se existe a nota em estoque, e usa elas para gerar o troco necessário para o cliente.
	Caso não tenha notas para compor o troco, vai sobrar um resto, e esse resto vai ser o tanto que a máquina vai ficar devendo ao usuário. """

	if n5>0 and valorPago>=5:
		return troco5(valorPago-5,n5-1,somaTroco5+1)
	else:
		return valorPago,n5,somaTroco5;

def troco2(valorPago,n2,somaTroco2=0):

	""" A função troco2 é uma função recursiva que verifica se existe a nota em estoque, e usa elas para gerar o troco necessário para o cliente.
	Caso não tenha notas para compor o troco, vai sobrar um resto, e esse resto vai ser o tanto que a máquina vai ficar devendo ao usuário. """

	if n2>0 and valorPago>=2:
		return troco2(valorPago-2,n2-1,somaTroco2+1)
	else:
		return valorPago,n2,somaTroco2;

def troco1(valorPago,m1,somaTroco1=0):

	""" A função troco1 é uma função recursiva que verifica se existe a moeda em estoque, e usa elas para gerar o troco necessário para o cliente.
	Caso não tenha moedas para compor o troco, vai sobrar um resto, e esse resto vai ser o tanto que a máquina vai ficar devendo ao usuário. """

	if m1>0 and valorPago>=1:
		return troco1(valorPago-1,m1-1,somaTroco1+1)
	else:
		return valorPago,m1,somaTroco1;

def troco05(valorPago,m50,somaTroco05=0):

	""" A função troco05 é uma função recursiva que verifica se existe a moeda em estoque, e usa elas para gerar o troco necessário para o cliente.
	Caso não tenha moedas para compor o troco, vai sobrar um resto, e esse resto vai ser o tanto que a máquina vai ficar devendo ao usuário. """

	if m50>0 and valorPago>=0.5:
		return troco05(valorPago-0.5,m50-1,somaTroco05+1) # Subtrai o valor do valorPago, reduz o número de moedas de 50 centavos no caixa
	else:
		return valorPago,m50,somaTroco05;

def comprarOutroProduto(estoque1,estoque2,estoque3,estoque4,nota20,nota10,nota5,nota2,moeda1,moeda50,quebraLinha=True):

	""" A função comprarOutroProduto verifica se o usuário deseja comprar outro produto e verifica se ele respondeu a pergunta da forma correta. """

	if quebraLinha == True:
		resp = input("\nDeseja comprar outro produto? (S/N): ")
	else:
		resp = input("Deseja comprar outro produto? (S/N): ")
	if resp == "s" or resp == "S":
		maquina(estoque1,estoque2,estoque3,estoque4,nota20,nota10,nota5,nota2,moeda1,moeda50)
	elif resp == "n" or resp == "N":
		print("Obrigado pela preferência.")
		print("Volte Sempre!!!")
	else:
		print("\nPor favor, responda apenas com S ou N\n")
		comprarOutroProduto(estoque1,estoque2,estoque3,estoque4,nota20,nota10,nota5,nota2,moeda1,moeda50)

def removerProdutoEstoque(prod,estoque1,estoque2,estoque3,estoque4):

	""" A função removerProdutoEstoque remove um produto do estoque de acordo com qual produto seja e qual o estóque está relacionado a ele. """

	if prod == 1:
		estoque1-=1
	elif prod ==2:
		estoque2-=1
	elif prod ==3:
		estoque3 -=1
	elif prod == 4:
		estoque4 -=1

	return estoque1,estoque2,estoque3,estoque4

def removerNotasEstoque(n20,n10,n5,n2,m1,m50):

	""" A função removerNotasEstoque apenas retorna o que ela recebe. Ela foi usada para que se possa atribuir os valores dela às variáveis principais da função em uma linha só. 
	Isso torna o código mais enxuto e simples. """

	return n20,n10,n5,n2,m1,m50

def maquina(estoque1,estoque2,estoque3,estoque4,nota20,nota10,nota5,nota2,moeda1,moeda50,valorIncorreto=False):

	"""Esta é a função principal do programa, é como se fosse a função main. Nela são chamadas todas as outras funções e são tratados todos os casos e condições. Essa é a única função que precisa ser chamada para iniciar todo o programa.
	Ela recebe por parâmetro os estoques dos 4 produtos e a quantidade de notas de cada tipo disponível."""

	if not maquinaVazia(estoque1,estoque2,estoque3,estoque4): # Verifica se a máquina não está vazia (se não são todos os produtos que estão zerados)

		printMenu(estoque1,estoque2,estoque3,estoque4) # Imprime o menu base

		if valorIncorreto: #Imprime a mensagem de erro logo abaixo do menu para que o usuário possa compreender o erro
			print("O valor digitado não corresponde a nenhum produto. Por favor, escolha um dos produtos: \n")

		codProd = input("Escolha seu produto: ") # Lê o código do produto, mas não converte ainda, pois não se sabe se o usuário inseriu números ou letras ainda.

		if produtoValido(codProd): # Verifica se o código inserido é um número e equivale a um produto da máquina. 

			codProd = int(codProd) # Agora que sabe-se que o valor inserido for realmente um número no intervalo, então pode-se convertê-lo e usá-lo.

			estoqueProduto = escolherProduto(estoque1,estoque2,estoque3,estoque4,codProd) # Define qual o estoque vai ser usado com base no código do produto.
			precoProduto,nomeProduto = descricaoProduto(codProd) # define e retorna as informações do produto como o nome e o preço.

			if disponivel(estoqueProduto): # verifica se o produto está disponível.
				printDescricaoProduto(precoProduto,nomeProduto) # Imprime na tela a descrição do produto.
				valorRecebido,notaRecebida20,notaRecebida10,notaRecebida5,notaRecebida2,moedaRecebida1,moedaRecebida50 = receber(precoProduto) # função recursiva que lê os valores que o usuário vai inserir para pagar e retorna a quantidade de cada nota que foi depositada e o total de R$ que o usuário pagou para que se possa dar o troco.

				nota20 = adicionar20(nota20,notaRecebida20) #Adiciona ao estoque as notas recebidas ao usuário pagar pelo produto.
				nota10 = adicionar10(nota10,notaRecebida10)
				nota5 = adicionar5(nota5,notaRecebida5)
				nota2 = adicionar2(nota2,notaRecebida2)
				moeda1 = adicionar1(moeda1,moedaRecebida1)
				moeda50 = adicionar05(moeda50,moedaRecebida50)

				trocoProduto = calculaTroco(valorRecebido,precoProduto) #Calcula e retorna o troco com base no valor do produto e no valor que o usuário pagou.
				printValorPagoTroco(valorRecebido,trocoProduto) # Imprime na tela o valor pago pelo usuário e o troco do produto.

				trocoOriginal = trocoProduto

				if trocoProduto>0:

					trocoProduto,n20,somaTroco20 = troco20(trocoProduto,nota20) #Gerando os trocos para cada cédula e armazenando nas variáveis que guardam o resto do troco, o resto da quantidade de notas que não foi usada e a soma de notas que foi usada.
					trocoProduto,n10,somaTroco10 = troco10(trocoProduto,nota10)
					trocoProduto,n5,somaTroco5 = troco5(trocoProduto,nota5)
					trocoProduto,n2,somaTroco2 = troco2(trocoProduto,nota2)
					trocoProduto,m1,somaTroco1 = troco1(trocoProduto,moeda1)
					trocoProduto,m50,somaTroco05 = troco05(trocoProduto,moeda50)

					if trocoProduto == 0: # Se o troco restante for igual a zero, o caixa tem troco para que possa pagar tudo que deve ao comprador de troco.
						print("Pegue seu troco:")
						nota20,nota10,nota5,nota2,moeda1,moeda50 = removerNotasEstoque(n20,n10,n5,n2,m1,m50) # Remove uma unidade do produto oo estoque
						estoque1,estoque2,estoque3,estoque4 = removerProdutoEstoque(codProd,estoque1,estoque2,estoque3,estoque4)
						printNotasTroco(somaTroco20,somaTroco10,somaTroco5,somaTroco2,somaTroco1,somaTroco05) # Imprime as notas que têm de ser devolvidas de troco
						comprarOutroProduto(estoque1,estoque2,estoque3,estoque4,nota20,nota10,nota5,nota2,moeda1,moeda50) # Pergunta se o usuário quer comprar outro produto.
					else:
						print("Não temos troco para o valor pago.")
						print("Temos apenas R${0:.2f} para voltar de troco.".format(trocoOriginal-trocoProduto)) #mostra o tanto que a máquina tem para devolver de trodo.
						resp = input("Deseja comprar assim mesmo? (S/N):") # Verifica se o usuário quer continuar a compra, mesmo que ele não receba o troco completo.
						if resp == "s" or resp == "S":
							if trocoOriginal-trocoProduto > 0: # Se o troco disponível for de R$0,00, não precisa mostrar 'Pegue seu troco'
								print("Pegue seu troco:")
							nota20,nota10,nota5,nota2,moeda1,moeda50 = removerNotasEstoque(n20,n10,n5,n2,m1,m50) # Remove as notas dadas no troco do estoque.
							estoque1,estoque2,estoque3,estoque4 = removerProdutoEstoque(codProd,estoque1,estoque2,estoque3,estoque4) # Remove o produto comprado do estoque
							printNotasTroco(somaTroco20,somaTroco10,somaTroco5,somaTroco2,somaTroco1,somaTroco05) # Imprime na tela as notas do troco.
							print("Ficamos te devendo: R${0:.2f}".format(trocoProduto))
							comprarOutroProduto(estoque1,estoque2,estoque3,estoque4,nota20,nota10,nota5,nota2,moeda1,moeda50) # Pergunta se quer comprar outro produto e reiniciar o processo.

						elif resp == "n" or resp == "N": # Se o usuário não quiser receber o troco a menos, ele recebe o dinheiro de volta.
							nota20 = remover20(nota20,notaRecebida20)
							nota10 = remover10(nota10,notaRecebida10)
							nota5 = remover5(nota5,notaRecebida5)
							nota2 = remover2(nota2,notaRecebida2)
							moeda1 = remover1(moeda1,moedaRecebida1)
							moeda50 = remover05(moeda50,moedaRecebida50)
					
							print("Sem problemas. Pegue seu dinheiro de volta")
							printNotasTroco(notaRecebida20,notaRecebida10,notaRecebida5,notaRecebida2,moedaRecebida1,moedaRecebida50) # Imprime novamente o investimento inicial do usuário e devolve para ele, já que ele pediu o dinheiro de volta.
							comprarOutroProduto(estoque1,estoque2,estoque3,estoque4,nota20,nota10,nota5,nota2,moeda1,moeda50) # Pergunta se o usuário quer comprar outros produtos.

				else: # se o produto não precisar de troco, pois o usuário pagou o valor exato.
					estoque1,estoque2,estoque3,estoque4 = removerProdutoEstoque(codProd,estoque1,estoque2,estoque3,estoque4) # Subtrai do estoque.
					comprarOutroProduto(estoque1,estoque2,estoque3,estoque4,nota20,nota10,nota5,nota2,moeda1,moeda50,False) # pergunta se quer comprar outro produto.

			else: # Quando um produto está indisponível e um usuário tenta comprar o produto, mas ele não pode pois ñão tem mais em estoque.
				print("\nDesculpe, mas a {} está indisponível.\n".format(nomeProduto))
				comprarOutroProduto(estoque1,estoque2,estoque3,estoque4,nota20,nota10,nota5,nota2,moeda1,moeda50,False) 

		else: # Se o produto não for válido, o sistema vai solicitar novamente o produto e processar tudo novamente.
			maquina(estoque1,estoque2,estoque3,estoque4,nota20,nota10,nota5,nota2,moeda1,moeda50,True)

	else:
		print("Desculpa, mas a máquina está sem produtos.")
		print("Obrigado pela preferência.")
		print("Volte Sempre!!!")

maquina(5,5,5,5,5,5,5,5,5,5)