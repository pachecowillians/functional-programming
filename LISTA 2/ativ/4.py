import math
def Ritmo(h,m,s,d):
	t = h*60 + m + s/60
	ritM = t//d
	ritS = math.ceil((t/d - ritM) * 60)
	print("--> Ritmo: {0:02d}:{1:02d} min/km".format(int(ritM),int(ritS)))
def main():
	print("Tempo do corredor (horas, minutos e segundos): ")
	hora = int(input())
	minuto = int(input())
	segundo = int(input())
	distancia = float(input("Distância percorrida (em km): "))
	Ritmo(hora,minuto,segundo,distancia)
main()