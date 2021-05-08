def intercala(l1,l2):
	if l1!=[] and l2!=[] and l1[0]<l2[0]:
		print(l1[0])
		return intercala(l1[1:],l2)
	elif l1!=[] and l2!=[] and l1[0]==l2[0]:
		print(l1[0])
		return intercala(l1[1:],l2)
	elif l1!=[] and l2!=[] and l1[0]>l2[0]:
		print(l2[0])
		return intercala(l1,l2[1:])
	elif l1!=[]:
		print(l1[0])
	elif l2!=[]:
		print(l2[0])

intercala([1,6,8,10],[2,3,9])