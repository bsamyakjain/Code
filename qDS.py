class queue:
    top = -1
    __arr = []
    size_of_array = 2

    @classmethod
    def enqueue(cls,num):
        if cls.top == cls.size_of_array:
            print("Overflow condition, please delete some item.")
        else:
            cls.top+=1
            cls.__arr.append(num)
            print("Added successfully")

    @classmethod
    def dequeue(cls):
        if cls.top == -1:
            print("Underflow condition, please insert some item.")
        
        else:
            cls.top-=1
            print("Deleted successfully")
            
    @classmethod
    def display(cls):
        if cls.top == -1:
            print("Nothing inside")

        for i in range(cls.top+1):
            print("->",cls.__arr[i],end=" ")


q1  = queue()

q1.enqueue(12)
q1.dequeue()
q1.dequeue()
q1.enqueue(121)
q1.enqueue(1)
q1.enqueue(0)
q1.enqueue(3)
q1.display()
q1.dequeue()
q1.display()