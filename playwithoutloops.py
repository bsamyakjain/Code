x= int(input("Enter value 1st: ")) # lower bound of angela
y= int(input("Enter value 2nd: ")) # upper bound of angela
a= int(input("Enter value 3rd: ")) # lower bound of dan
b= int(input("Enter value 4th: ")) # upper bound of dan


if x<=y and a<=b: # constraints
	if x==a and y==b:
		print("EMPTY")

	elif x>=0 and y>=0 and a>=0 and b>=0:
		print("POSITIVE")
		

	elif ((x<=0 and y>=0) and (((a<0 and a!=0) and (b!=0 and b<0)) or a>0)) or ((a<=0 and b>=0) and ((x<0 and x!=0) and (y!=0 and y<0)) or x>0):
		print("ZERO")

	elif(x<0 and y<0) and (a<0 and b<0):
		sum = abs(a-b)+1
		sum1 = abs(x-y)+1
		if(sum+sum1)%2 ==0:
			print("POSITIVE")
		else:
			print("NEGATIVE")
	
	elif (x<0 and y>=0) and (a<0 and b>=0):
		sum = abs(x)
		sum1 = abs(a)
		if(sum+sum1)%2 ==0:
			print("POSITIVE")
		else:
			print("NEGATIVE")

	elif((x>=0 and y>=0) and (a<0 and b<0)):
		sum = abs(a-b)+1
		if sum%2 ==0:
			print("POSITIVE")
		else:
			print("NEGATIVE")

	elif((a>0 and b>0) and (x<=0 and y<=0)):
		sum = abs(x-y)+1
		if sum%2 ==0:
			print("POSITIVE")
		else:
			print("NEGATIVE")

else:
	print("Enter right limits")