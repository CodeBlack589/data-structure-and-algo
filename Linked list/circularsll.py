class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # Pointer to next node

    def __str__(self):
        return str(self.value)


class CSLinkedList:  # Circular Singly Linked List
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def addatlast(self, value):
        new_node = Node(value)
        if self.head is None:
            # First node case
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head  # Circular link to itself
        else:
            self.tail.next = new_node  # Link old tail to new node
            new_node.next = self.head  # Make it circular
            self.tail = new_node  # Update tail
        self.length += 1

    def addatbegin(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self.length += 1

    def insert(self, index, value):
        if index > self.length or index < 0:
            raise Exception("Index Out Of Range")
        new_node = Node(value)
        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = self.head
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = self.head

        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    def search(self, target):
        if self.head is None:
            return False
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def get(self, index):
        if index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def removefirst(self):
        if self.head is None:
            print("Oops No node Present")
            return None
        delete_node = self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.tail.next=self.head
        print(f"Deleted node is {delete_node} = {delete_node.value}")
        del delete_node
        self.length-=1

    def removeLast(self):
        delete_node=self.tail
        if self.length==0:
            print("Oops No Node Present")
            return None
        elif self.length==1:
            self.head=None
            self.tail=None
        else:
            current=self.head
            prev=None
            while current!=delete_node:
                prev=current
                current=current.next
            prev.next=self.head
            current.next=None
            self.tail=prev
        self.length-=1
        print(f"Deleted node is {delete_node} = {delete_node.value}")
        del delete_node



    def removebyIndex(self, index):
        if index<0 or index>=self.length:
            print("Index Out of Range")
            return None
        elif index==0:
            self.removefirst()
        elif index==self.length-1:
            self.removeLast()
        else:
            prev_node=self.get(index-1)
            delete_node=prev_node.next
            prev_node.next=delete_node.next
            delete_node.next=None
            self.length-=1
            print(f"Deleted node is {delete_node} = {delete_node.value}")
            del delete_node

    def delete_cll(self):
        pass

    def __str__(self):
        result = ""
        if self.head is None:
            result += "The list is empty."
            return result

        current = self.head

        while True:
            result += str(current.value)
            current = current.next
            if current == self.head:  # Stop when loop completes
                break
            result += " ->"
        return result


def main():
    print("Create a list. Press:")
    print("1 - Add at last")
    print("2 - Add at first")
    print("3 - Add at any index first")
    print("4 - Search An element")
    print("5 - Search An element using index")
    print("6 - Search An element using index and update it")
    print("7 - Remove first Node")
    print("8 - Remove last Node")
    print("9 - Remove any Node by Index")
    print("10 - Delete Circular Linked List")
    print("p - Print list")
    print("x - Exit")

    l = CSLinkedList()

    while True:
        inp = input("Enter choice: ")
        if inp == '1':
            number = int(input("Enter the number to add: "))
            l.addatlast(number)
        elif inp == '2':
            number = int(input("Enter the number to add: "))
            l.addatbegin(number)
        elif inp == 'p':
            print(l)
        elif inp == '4':
            number = int(input("Enter the number to search: "))
            print(l.get(number))
        elif inp == '3':
            number = int(input("Enter the number to add: "))
            index = int(input("Enter the Index"))
            l.insert(index, number)
        elif inp == '5':
            index = int(input("Enter the Index"))
            print(l.get(index))
        elif inp == '6':
            number = int(input("Enter the number to add: "))
            index = int(input("Enter the Index"))
            l.set_value(index, number)
        elif inp == '7':
            l.removefirst()
            print(l)
        elif inp == '8':
            l.removeLast()
            print(l)
        elif inp == '9':
            index = int(input("Enter the Index"))
            l.removebyIndex(index)
            print(l)
        elif inp == '10':
            l.delete_cll()
            print(l)
        elif inp == 'x':
            print("Exiting...")
            break
        else:
            print("Invalid input! Try again.")


main()
