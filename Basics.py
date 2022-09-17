# slicing always returns a new copy of the anything it performed on

a = list(range(10))
b=[]
for i in range(10):
    b.append(i)
print(a,b)

for j in range(3):
    for i in range(10):

        if i==2:
            continue

        elif i==3:
            print("Its three")

        elif i==5:
            break

        elif i==4:
            print()
        

        print(i)
    print("its J ", j)


import SamyakLib as sj

print(sj.stars(5))


#args and kwargs 

def myFun(arg1, *argv):
	print("First argument :", arg1)
	for arg in argv:
		print("Next argument through *argv :", arg)


myFun('Hello')
