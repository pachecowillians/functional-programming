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
def main():
	txt = input("Digite a string: ")
	print(contaVogal(txt))

main()