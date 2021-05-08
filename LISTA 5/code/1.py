def u(l1,l2,i=0):
	if i<len(l2):
		if l2[i] not in l1:
			return u(l1+[l2[i]],l2,i+1)
		else:
			return u(l1,l2,i+1)
	else:
		return l1

print(u([1,2,3],[3,4,5,6]))