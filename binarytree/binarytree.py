COUNT=[10]
class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

class Node:
    def __init__(self):
        self.root=None
    def addtoright(self,data):
        new_node=BinaryTree(data)
        if self.root is None:
            self.root=new_node
        else:
            new_root=self.root
            while new_root.right is not None:
                new_root=new_root.right
            new_root.right=new_node
    def addtoleft(self,data):
        new_node=BinaryTree(data)
        if self.root is None:
            self.root=new_node
        else:
            new_root=self.root
            while new_root.left is not None:
                new_root=new_root.left
            new_root.left=new_node
    def searchelement(self,node,data):
        if node is None:
            return None
        if node.data == data:
            return node

        # Otherwise, recursively search the left and right subtrees
        return self.searchelement(node.left, data) or self.searchelement(node.right, data)

    def addatspecificloaction(self,node,x,y,l):
        k=self.searchelement(node,y)
        if k is None:
            print("No element found")
            return None
        new_node = BinaryTree(x)
        if l=='r' or l=='R':

            k.right=new_node
        else:
            k.left=new_node


    def findleafnodes(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        else:
            a=self.findleafnodes(root.left)
            b=self.findleafnodes(root.right)
            c=a+b
            return (c)
    def findnonleafnodes(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        else:
            a=self.findnonleafnodes(root.left)
            b=self.findnonleafnodes(root.right)
            c=a+b+1
            return (c)

    def heightoftree(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        else:
            l=self.heightoftree(root.left)
            r=self.heightoftree(root.right)
            c=max(l,r)+1
            return c

    def checkstrict(self,root):
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        else:
            if root.left is not None and root.right is not None:
                return (self.checkstrict(root.left) and self.checkstrict(root.right))
            return False

    def preorder(self,root):
        if root is None:
            return None
        else:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if root is None:
            return None
        else:
            self.postorder(root.left)
            self.preorder(root.right)
            print(root.data,end=" ")

    def inorder(self,root):
        if root is None:
            return None
        else:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.preorder(root.right)

    def printbinarytree(self, node, space):
        if node is None:
            return False
        space += COUNT[0]
        self.printbinarytree(node.right, space)
        print()
        for i in range(COUNT[0], space):
            print(end=" ")
        print(node.data)
        self.printbinarytree(node.left, space)

def start():
    print("1.Add node at right")
    print("2.Add node at left")
    print("3.Search an element")
    print("4.Enter new data to specific location")
    print("5. Find number of leaf nodes")
    print("6. Find number of non leaf nodes")
    print("7. Find total number of nodes")
    print("8. Height of Tree")
    print("9. tree is strict or not")
    print("10. Preorder traversal")
    print("11. Postorder traversal")
    print("12. Inorder traversal")
    print("13.To view binary tree")
    print("Q/q for quit")
    k=True

    tree = Node()
    while k:
        user_input = input("Enter the number")
        if user_input=="1":
            datas=input("enter the data")
            tree.addtoright(datas)
        elif user_input=="2":
            datas=input("enter the data")
            tree.addtoleft(datas)
        elif user_input=="3":
            datas = input("enter the data")
            k=tree.searchelement(tree.root,datas)
            if k is None:
                print("elemet not found")
            else:
                print("Element found")
        elif user_input=="4":
            datas = input("enter the data")
            data1=input("to which node you want to add")
            location=input("Where to add left or right")
            tree.addatspecificloaction(tree.root,datas,data1,location)
        elif user_input=="5":
            noofleafnode=tree.findleafnodes(tree.root)
            print("Number of leafnodes : ",noofleafnode)

        elif user_input=="6":
            noofnonleafnode=tree.findnonleafnodes(tree.root)
            print("Number of Non leaf node : ",noofnonleafnode)



        elif user_input=="7":
            noofleafnode = tree.findleafnodes(tree.root)
            noofnonleafnode = tree.findnonleafnodes(tree.root)
            print("Number of node : ", noofnonleafnode+noofleafnode)

        elif user_input=="8":
            heightoftree=tree.heightoftree(tree.root)
            print("Height of tree is : ",heightoftree)

        elif user_input=="9":
            t=tree.checkstrict(tree.root)
            if t is False:
                print("Tree is not strict")
            else:
                print("tree is Strict")

        elif user_input=="10":
            tree.preorder(tree.root)

        elif user_input=="11":
            tree.postorder(tree.root)

        elif user_input=="12":
            tree.inorder(tree.root)

        elif user_input=="13":
            tree.printbinarytree(tree.root, 0)

        elif user_input.lower()=='q':
            k=False
            print("Programs end")
        else:
            print("wrong input")

if __name__=="__main__":
    start()

