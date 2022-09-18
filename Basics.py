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


from SamyakLib import *
stars()


#args and kwargs 

#args is for non keyworded arguments
def arguments(*arg):
    print(type(arg))

arguments(1,"r","new",3)    
#when we don't know how many arguemnts we need to pass then we use (*arg) it returns "tuple"

#kwargs, it returns dict 
def kwargs(**arg):

    for i,j in arg.items():
        print(i,j)

kwargs(name="samyak",age="21")
kwargs(real="unreal",sun="dawn")

stars()
#string

s="samyak"

print(s[-1::-1])
stars()
#opertors
#is operator is used to check the address 
a=10
b=100

print(a is b)
print(id(a),id(b))
