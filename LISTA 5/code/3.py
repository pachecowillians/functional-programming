def intersecao(l1,l2,l=[],i=0):
	if i<len(l1):
		if l1[i] in l2 and l1[i] not in l:
			return intersecao(l1,l2,l+[l1[i]],i+1)
		else:
			return intersecao(l1,l2,l,i+1)
	else:
		return l

print(intersecao([1,2,3,3,1,10],[10,1,5,3,2]))