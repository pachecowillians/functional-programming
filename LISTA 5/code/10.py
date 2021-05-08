def maiusculas(i=65):
	if chr(i-1) != "Z":
		print(chr(i))
		maiusculas(i+1)

maiusculas()