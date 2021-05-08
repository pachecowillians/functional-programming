#Atividade 12. Ler o número de lados e fazer alguma operação com o valor do lado

qtdeLados = int(input("Digite a quantidade de lados do polígono: "))
valLados = int(input("Digite a medida do lado do polígono: "))

perimetro = 0
area = 0

if qtdeLados == 3:
	print("Triângulo")
	perimetro = 3*valLados
	print("O perímetro do polígono é {0:.2f}".format(perimetro))
elif qtdeLados == 4:
	print("Quadrado")
	area = valLados**2
	print("A área do polígono é {0:.2f}".format(area))
elif qtdeLados == 5:
	print("Pentágono")
else:
	print("Polígono não identificado")