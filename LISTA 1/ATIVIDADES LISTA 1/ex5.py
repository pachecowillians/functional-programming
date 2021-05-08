#Atividade 5, soma e média de par e ímpar isolada

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))

contPares = 0
contImpares = 0
somaPares = 0
somaImpares = 0
mediaPares = 0
mediaImpares = 0
	
if n1%2 ==0:
	somaPares = somaPares + n1
	contPares = contPares + 1
else:
	somaImpares = somaImpares + n1
	contImpares = contImpares + 1

if n2%2 ==0:
	somaPares = somaPares + n2
	contPares = contPares + 1
else:
	somaImpares = somaImpares + n2
	contImpares = contImpares + 1

if n3%2 ==0:
	somaPares = somaPares + n3
	contPares = contPares + 1
else:
	somaImpares = somaImpares + n3
	contImpares = contImpares + 1

if n4%2 ==0:
	somaPares = somaPares + n4
	contPares = contPares + 1
else:
	somaImpares = somaImpares + n4
	contImpares = contImpares + 1

if contPares > 0:
	mediaPares = somaPares/contPares
if contImpares > 0:
	mediaImpares = somaImpares/contImpares

print("\nExistem {} números pares. A soma deles é {} e a média é {}".format(contPares,somaPares,mediaPares))
print("Existem {} números ímpares. A soma deles é {} e a média é {}".format(contImpares,somaImpares,mediaImpares))