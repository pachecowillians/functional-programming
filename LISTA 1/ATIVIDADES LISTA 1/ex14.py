#Atividade 14, calcular tempo e colocação de maratonistas

print("Tempo do corredor 1: ")
h1 = int(input("  -> Quantas horas? "))
m1 = int(input("  -> Quantos minutos? "))
s1 = int(input("  -> Quantos segundos? "))
print("Tempo do corredor 2: ")
h2 = int(input("  -> Quantas horas? "))
m2 = int(input("  -> Quantos minutos? "))
s2 = int(input("  -> Quantos segundos? "))

t1 = h1*3600 + m1*60 + s1
t2 = h2*3600 + m2*60 + s2

dif = 0
difH = 0
difM = 0
difS = 0

if t1 < t2:
	print("Vencedor: corredor 1")
	dif = t2 - t1
	difH = dif//3600
	difM = (dif - (difH*3600))// 60
	difS = dif - (difH*3600 + difM*60)
	print("Diferença: {} horas {} minutos {} segundos".format(difH,difM,difS))
elif t1 > t2:
	print("Vencedor: corredor 2")
	dif = t1 - t2
	difH = dif//3600
	difM = (dif - (difH*3600))// 60
	difS = dif - (difH*3600 + difM*60)
	print("Diferença: {} horas {} minutos {} segundos".format(difH,difM,difS))
else:
	print("Vencedor: Houve empate")
