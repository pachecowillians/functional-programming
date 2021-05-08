def ehVogal(c):
	return True if c in "aeiouAEIOU" else False
def contaVogal(s,i=0,cont=0):
	if i<len(s):
		if ehVogal(s[i]):
			return contaVogal(s,i+1,cont+1)
		else:
			return contaVogal(s,i+1,cont)
	else:
		return cont
def contaConsoante1(s,i=0,cont=0):
	if i<len(s):
		if ehVogal(s[i]):
			return contaConsoante1(s,i+1,cont)
		else:
			return contaConsoante1(s,i+1,cont+1)
	else:
		return cont
def contaConsoante2(s):
	return len(s)-contaVogal(s)
def main():
	txt = input("Digite a string: ")
	print(contaConsoante1(txt))
	print(contaConsoante2(txt))

main()