#Atividade 1, conversor de ºF par ºC

fahrenheit = float(input("Digite a temperatura: "))
celsius = (fahrenheit - 32)/1.8
print("{}º Fahrenheit correspondem a {}º celsius".format(fahrenheit,celsius))