def min(a, b):
	if a < b: #retorna o menor entre a e b
		return a
	return b
def mystery (a, b, c, d):
	"""A função retorna o menor valor dentre os 4 passados. Por meio da função min, ele calcula o menor valor dentre dois valores, ele agrupa isso em pares, vê o menor de cada par, depois agrupa o menor número de cada par e checa o menor entre eles. Com isso, ele praticamente descobre qual é o menor número dentre os 4."""
	x = min(a, b) #menor entre A e B
	y = min(c, d) #menor entre C e D
	return min(x, y) #retorna o menor entre os 4 valores
def main ():
	a = 10
	b = 15
	c = 20
	d = 5
	print (mystery (a, b, c, d))
main ()

"""A função retorna o menor valor dentre os 4 passados. Por meio da função min, ele calcula o menor valor dentre 
dois valores, ele agrupa isso em pares, vê o menor de cada par, depois agrupa o menor número de cada par e checa o
menor entre eles. Com isso, ele praticamente descobre qual é o menor número dentre os 4."""