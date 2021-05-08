def myMap(f,l):
	return list(map(f,l))

print(myMap(lambda x: x**2,[1,2,3,4,5]))
