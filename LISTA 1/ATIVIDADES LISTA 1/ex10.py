prova1 = float(input("Digite a nota da primeira prova: "))
prova2 = float(input("Digite a nota da segunda prova: "))
prova3 = float(input("Digite a nota da terceira prova: "))

media = (prova1 + prova2 + prova3)/3

if media >= 7:
	print("\nAluno aprovado com média {0:.2f}!".format(media))
else:
	print("\nAluno de prova final!")
	provaFinal = float(input("\nDigite a nota do aluno na prova final: "))
	if provaFinal>=5:
		print("Aluno foi aprovado na prova final com média {0:.2f}!".format(provaFinal))
	else:
		print("Aluno reprovado na prova final com média {0:.2f}!".format(provaFinal))
