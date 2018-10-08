def integral(number):
	dic={}
	for x in range(1,number+1):
		dic[x]=x*x
	print dic

print ("Enter the integral number")
number=input()
integral(number)