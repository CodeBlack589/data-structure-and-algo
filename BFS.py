""""Breadth First Search"""
from collections import deque
print("Breadth First Search(BFS)")
print("1.BFS uses queue data structure")
print("2.Time complexity is O(V+E) when using adjacency list and O(V^2) when using matrix")
print("3.Space complexity is V+V=2V which is O(V)")
print("4.BFT also know as Level Order Traversal")
def bfs(graph,start_node):
    queue = deque([start_node])
    visited = set([start_node])
    while queue:
        current_node=queue.popleft()
        print(f"Visited: {current_node}")
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
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
    bfs(graph,start_node)

def application_of_bfs():
    print("1.After completing bfs check the visited array 0 or 1 if 1 then connected else not connected")
    print("2.Using bfs how many time it runs then it is number of connected component")
    print("3.Component:- a maximal connected subgraph")
    print("4.We can verify given graph is connected or not")
    print("5.From a vertex x is reachable or not")
    print("6.We can verify given graph contain cycle or not")
    print("7.From given source to other vertex give shortest path in undirected graph")
    print("8.Using BFS we can verify given graph is bipartite or not.")
if __name__=="__main__":
    main()
    application_of_bfs()
