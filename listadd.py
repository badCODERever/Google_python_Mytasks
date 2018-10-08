def listadd(list1,list2):
	tlist=[]
	for x in list1:
		tlist.append(x**2)
	for y in list2:
		tlist.append(x**3)
	result=sum(tlist)
	print result
A=[1,2,3]	
B=[2,3]
listadd(A,B)
