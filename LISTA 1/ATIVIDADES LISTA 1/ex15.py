# Atividade 15, calcular a idade da pessoa

print("Digite a data de nascimento:")
d1 = int(input("-> Dia? "))
m1 = int(input("-> Mês? "))
a1 = int(input("-> Ano? "))
print("Digite a data atual: ")
d2 = int(input("-> Dia? "))
m2 = int(input("-> Mês? "))
a2 = int(input("-> Ano? "))

idade = a2-a1

if d1>d2 and m1>=m2:
	idade = idade -1
print("Idade: {} anos".format(idade))