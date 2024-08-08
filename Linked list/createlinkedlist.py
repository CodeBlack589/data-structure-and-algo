class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
    def insertatbeginning(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node

    def insertatlast(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head=new_node
        else:
            current_node=self.head
            while current_node.next:
                current_node=current_node.next
            current_node.next=new_node

    def address_of_node_contain_data_x(self,data):
        if self.head is None:
            print("Linked List Empty")
        else:
            current_node=self.head
            while current_node and current_node.data != data:
                current_node=current_node.next
            if current_node is None:
                print(f"Node with data {data} is not present")
            elif current_node.data == data:
                print(id(current_node))
    def viewlist(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            new_head=self.head
            while new_head is not None:
                print(new_head.data)
                new_head=new_head.next
    def secondlastnode(self):
        if self.head==None:
            print("Linked list empty")
        elif self.head.next==None:
            print(f"Only one element is present {self.head.data}")
        else:
            current_node=self.head
            while current_node.next.next is not None:
                current_node=current_node.next
            print(id(current_node))
            print(current_node.data)
    def addxbeforey(self,x,y):
        if self.head is None:
            print("Linked list empty")
        elif self.head.data==y:
            new_node = Node(x)
            current_node=self.head
            new_node.next=current_node
            self.head=new_node
        else:
            current_node=self.head
            while current_node.data!=y and current_node.next is not None:
                previous_node=current_node
                current_node=current_node.next
            if current_node.data==y:
                new_node=Node(x)
                new_node.data=x
                new_node.next=current_node
                previous_node.next=new_node
            else:
                print(f"No {y} found")

    def deltefirstnode(self):
        if self.head is None:
            print("Linked list empty")
        elif self.head.next is None:
            print(f"node deleted {self.head.data}")
            self.head=None
        else:
            print(f"node deleted {self.head.data}")
            self.head=self.head.next
    def deletelastnode(self):
        if self.head is None:
            print("Linked List empty")
        elif self.head.next is None:
            print(f"node deleted {self.head.data}")
            self.head = None
        else:
            current_node=self.head
            while current_node.next is not None:
                previous_node=current_node
                current_node=current_node.next
            print(f"node deleted {current_node.data}")
            previous_node.next=None
    def deletenodecontainx(self,x):
        if self.head is None:
            print("Linked list empty")
        elif self.head.data==x:
            print(f"node deleted {self.head.data}")
            self.head=self.head.next
        else:
            current_node=self.head
            while current_node.data!=x and current_node.next is not None:
                previous_node=current_node
                current_node=current_node.next
            if current_node.data==x:
                print(f"node deleted {x}")
                previous_node.next=current_node.next
            else:
                print(f"node does not exits {x}")
    def reverselist(self):
        if self.head is None:
            print("Linked List Empty")
        elif self.head.next is None:
            print("Only one element is present")
        else:
            previous = None
            current = self.head

            while current is not None:
                next_node = current.next  # Save the next node
                current.next = previous  # Reverse the link
                previous = current  # Move previous to current
                current = next_node  # Move to the next node

            self.head = previous
            self.viewlist()
    def kthnodefromend(self,k):
        if self.head is None:
            print("Linked list is empty")
        else:
            current_node=self.head
            new_node=self.head
            i=1
            k=int(k)
            while current_node.next is not None and i<k:
                i=i+1
                current_node=current_node.next
            while current_node.next is not None:
                new_node=new_node.next
                current_node=current_node.next
            print(f"Kth node from end is {new_node.data}")


def start():
    print("1.Add node at beginning")
    print("2.Add node at last")
    print("3. Find node address with data x")
    print("4.Print linked list")
    print("5.Address of 2nd last node")
    print("6. Add node x before node y")
    print("7. Delete first node")
    print("8. Delete last node")
    print("9. Delete node contain x")
    print("10. Reverse the Linked list")
    print("11. Kth node from end")
    print("Q/q for quit")
    k=True

    linklist = Linkedlist()
    while k:
        user_input = input("Enter the number")
        if user_input=="1":
            datas=input("enter the data")
            linklist.insertatbeginning(datas)
        elif user_input=="2":
            datas=input("enter the data")
            linklist.insertatlast(datas)
        elif user_input=="3":
            datas = input("enter the data")
            linklist.address_of_node_contain_data_x(datas)
        elif user_input=="4":
            linklist.viewlist()
        elif user_input=="5":
            linklist.secondlastnode()
        elif user_input=="6":
            x=input("Enter value of x: ")
            y=input("Enter value of y: ")
            linklist.addxbeforey(x,y)
        elif user_input=="7":
            linklist.deltefirstnode()
        elif user_input=="8":
            linklist.deletelastnode()
        elif user_input=="9":
            x=input("Enter the value of x")
            linklist.deletenodecontainx(x)
        elif user_input=="10":
            linklist.reverselist()
        elif user_input=="11":
            k=input("Enter the number from last k : ")
            linklist.kthnodefromend(k)
        else:
            k=False
            print("Programs end")

if __name__=="__main__":
    start()
