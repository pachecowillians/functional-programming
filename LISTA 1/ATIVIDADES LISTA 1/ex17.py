# Atividade 17, descobrir a data da páscoa de acordo com o ano

ano = int(input("Digite um ano: "))

x = 0
y = 0

if 1582<=ano<=1699:
	x = 22
	y = 2
elif 1700<=ano<=1799:
	x = 23
	y = 3
elif 1800<=ano<=1899:
	x = 23
	y = 4
elif 1900<=ano<=1999:
	x = 24
	y = 5
elif 2000<=ano<=2099:
	x = 24
	y = 5
elif 2100<=ano<=2199:
	x = 24
	y = 6
elif 2200<=ano<=2299:
	x = 25
	y = 0
elif 2300<=ano<=2399:
	x = 26
	y = 1
elif 2400<=ano<=2499:
	x = 25
	y =  1

a = ano%19
b = ano%4
c = ano%7
d = (19*a+x)%30
e = (2*b+4*c+6*d+y)%7

p = (22+d+e)

if p<=31:
	print("Em {} a Páscoa foi ou será em {} de {}".format(ano,p,"Março"))
elif (d+e-9)<=25:
	print("Em {} a Páscoa foi ou será em {} de {}".format(ano,d+e-9,"Abril"))
elif (d+e-9)-7<=25:
	print("Em {} a Páscoa foi ou será em {} de {}".format(ano,(d+e-9)-7,"Abril"))
