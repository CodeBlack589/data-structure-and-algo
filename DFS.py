print("Depth First Search (DFS) is an algorithm for traversing or searching tree or graph data structures.\nIt starts at a given node (often called the 'root')"
      " and explores as far as possible along each branch before backtracking.")
print("1.DFS uses stack data structure")
print("2.DFS time complexity O(V+E)")
print("3.DFS space complexity O(V)")
print("Applications of DFS")
print("Graph connected or not")
print("Connected component we can find")
print("We can find cycle")
print("We can not find shortest path")
print("From s vertex x is reachable or not")
print("We can verify given directed graph is strongly connected")
print("After apply dft all vertex came and after that reverse the edges and again apply dft if all vextex"
      "came then strongly connected or not")
print("We can find articulation point")
print("We can find topological sorting")
print("push/pop")

def dfs(graph,start_node,visited):
    visited.add(start_node)
    print(start_node,end=" ")
    for neighboor in graph[start_node]:
        if neighboor not in visited:
            dfs(graph,neighboor,visited)

def main():
    no_of_nodes=int(input("Enter number of nodes : "))
    graph={}
    for i in range(no_of_nodes):
        name_of_node=input("Enter the  node name : ")
        neighbors = input(f"Enter neighbors of {name_of_node} separated by space: ").split()
        graph[name_of_node]=neighbors
    print("The Graph is : ")
    print(graph)
    start_node=input("Enter the Start Node : ")
    visited=set()
    dfs(graph,start_node,visited)
if __name__=="__main__":
    main()
