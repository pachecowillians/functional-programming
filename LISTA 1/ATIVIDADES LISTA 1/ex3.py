# Atividade 3, Calcular o ritmo médio de um corredor

tempo = int(input("Digite o tempo total gasto na corrida (em min): "))
distancia = int(input("Digite a distância percorrida (em km): "))

ritmoMinutos = tempo//distancia
ritmoSegundos = int(((tempo/distancia)-ritmoMinutos)*60)

print("Ritmo medio do corredor: {0:02d}:{1:02d} min/km".format(ritmoMinutos,ritmoSegundos))