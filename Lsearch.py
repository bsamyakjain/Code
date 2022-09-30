import array

arr = []

size = int(input("Enter the size of array"))
for i in range(size):
    try:
        arr.append(int(input()))
    except:
        print("Invalid value")


print(arr)

num = int(input("Enter the element you want to find: "))
flag = 0
for i in arr:
    if i == num:
        print("Element found")
        flag = 1
        break

if flag==0:
    print("Element not found")



