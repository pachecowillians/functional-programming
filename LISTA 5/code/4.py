def crescente(l1,i=0):
	if i<len(l1)-1:
		if l1[i]<l1[i+1]:
			return crescente(l1,i+1)
		else:
			return False
	else:
		return True

print(crescente([1,2,3,4,0]))