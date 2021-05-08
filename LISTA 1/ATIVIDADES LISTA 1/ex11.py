#Atividade 11, ler o X, aplicar na função e gerar o resultado
#Tive que usar a biblioeteca math para poder calcular, não consegui entender como eu faço para calcular os logaritmos, então peguei a biblioteca pronta "math"
import math 

x = float(input("Digite o número a ser aplicado em f(x): "))

fx = 0

if x <= 1:
	fx = math.log(x)
elif x>1 and x<=2:
	fx = math.log(x,10) + x**(1/2)
elif x>2 and x<=5:
	fx =  x**2 + math.exp(x)
elif x>5: #ou simplesmente else
	fx =  x**(x/2) + math.log(x,2)

print("\nf(x) : ",fx)
print("Arredondando, temos : {0:.2f}".format(fx))