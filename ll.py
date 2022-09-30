class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    # initializing head with None
    def __init__(self):
        self.head = None
    
    def sortedAdd(self,value):
        # if linkedlist is empty then
        if self.head == None:
            new_node = Node(value)
            self.head = new_node

        else:

            #checking if first element is greater than the value
            if self.head.data >= value:
                new_node = Node(value)
                new_node.next = self.head
                self.head = new_node

            # now inserting the newnode at appropiate position
            temp = self.head.next
            prev = temp
            if temp == None:
                new_node = Node(value)
                self.head.next = new_node

            else:
                while(temp != None):
                    if temp.data < value:
                        prev = temp
                        temp = temp.next

                # if the node is last node then
                if prev.next == None:
                    new_node = Node(value)
                    prev.next = new_node

                #If inserting in between
                else:
                    new_node = Node(value)
                    new_node.next = prev.next
                    prev.next = new_node

    def findMax(self):

        maximum = self.head.data
        temp = self.head
        if self.head.next == None:
            return self.head.data

        elif self.head == None:
            return "Linked List is empty"

        else:
            while(temp.next != None):
                temp = temp.next

            return temp.data

    def display(self):

        ptr = self.head
        if ptr == None:
            print("Empty List")

        else:
            while(ptr.next != None):
                print(ptr.data,"->")
                ptr = ptr.next
            print("this",ptr.data)



l = LinkedList()

l.display()
l.sortedAdd(20)
l.sortedAdd(20)
l.display()

l.sortedAdd(23)
l.display()
