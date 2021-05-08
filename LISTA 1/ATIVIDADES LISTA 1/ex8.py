n1 = int(input("Digite o seu número: "))
n2 = int(input("Digite o seu número: "))

media = (n1+n2)/2

if media >= 9.0:
	print ("A")
else:
	if media >= 8.0:
		print ("B")
	else:
		if media >= 7.0:
			print ("C")
		else:
			if media >= 6.0:
				print ("D")
			else:
				print ("R")

# Tive de adicionar os ":" no final de cada if pois estava com erros de sintaxe
# Adicionei a variável media na primeira linha para não dar erros de execução