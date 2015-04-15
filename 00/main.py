i=0
while i>0:
	for y in range(1,i+1):
		print(str(y)+"*"+str(i)+"=",y*i,sep="",end=" ")
	i-=1
	print("\n")