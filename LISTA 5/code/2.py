def repetidos(l1,l=[],i=0):
	if i<len(l1):
		if l1[i] not in l:
			return repetidos(l1,l+[l1[i]],i+1)
		else:
			return repetidos(l1,l,i+1)
	else:
		return l

print(repetidos([0,1,2,3,4,4,1,4,4]))