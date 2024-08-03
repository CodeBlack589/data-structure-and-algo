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

def start():
    print("1.Add node at beginning")
    print("2.Add node at last")
    print("3. Find node address with data x")
    print("4.Print linked list")
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
        else:
            k=False
            print("Programs end")

if __name__=="__main__":
    start()
