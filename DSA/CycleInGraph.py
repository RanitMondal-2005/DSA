# Detecting cycles in a graph 

# DETECTING CYCLES IN AN UNDIRECTED GRAPH
n=6
e=7
edges=[(0,1),(0,3),(0,4),(1,5),(1,2),(3,1)]
adj_list=[]
for i in range(n):
    adj_list.append([])
for edge in edges:
    u=edge[0]
    v=edge[1]
    adj_list[u].append(v)
    adj_list[v].append(u)
for i in range(n):
    print(i,"->",adj_list[i])

visited=[False]*n
ans=[]

# logic to detect cycles in an undirected graph-> using DFS :
# each node has a parent and neighbors,for node of each neighbors:
# case 1 : if neighbor , not visited then visit it , using DFS traversal
# case 2 : if neighbor visited :
# case 2.1 : if that neighbor is same as parent of the curr node -> then ignore
# case 2.2 : if the neighbor is NOT same as Parent node -> a cycle found


def Detect_cycle_using_DFS(i,parent,adj_list,visited):
    visited[i]=True # mark i as visited
    for x in adj_list[i]: # go through all neighbors of node(i)
        # case 1: if curr node's neighbor(x) is equal to parent -> ignore
        if x==parent:
            continue
        # case 2: if curr node neighbor(x) is visited but not parent of curr node 
        if visited[x]:
            return True # cycle found
        # else do recursive call and move deeper 
        if Detect_cycle_using_DFS(x,i,adj_list,visited):
            return True
    return False # no cycle found


cycle_found=False
# 0 be start node and -1 be parent of starting node(initially)
for i in range(n): # if graph had any disconnected components , so better traverse through all nodes in graph
    if not visited[i]:
        if Detect_cycle_using_DFS(i,-1,adj_list,visited):
            cycle_found=True
            break
print("Cycle present?", cycle_found)



# DETECTING CYCLES IN A DIRECTED GRAPH
# here no concept of parent,
n=4

edges=[(0,1),(1,2),(2,3),(3,0)]
adj_list=[]
for i in range(n):
    adj_list.append([])
for edge in edges:
    u=edge[0]
    v=edge[1]
    adj_list[u].append(v) # as it is directed , only connect u->v
for i in range(n):
    print(i,"->",adj_list[i])

visited=[False]*n
inPath=[False]*n

def detect_cycle_in_graph(i,inPath,adj_list,visited): # using DFS
    inPath[i]=True
    visited[i]=True
    # traverse through neighbors
    for x in adj_list[i]:
        if not visited[x]: # if neighbor is not visited 
            # call dfs recursively
            if detect_cycle_in_graph(x,inPath,adj_list,visited):
                return True # cycle found
        elif inPath[x]:
            return True # if neighbor visited and in curr recursive path then cycle found
    inPath[i]=False
    return False

cycle=False
for i in range(n):
    if not visited[i]:
        if detect_cycle_in_graph(i,inPath,adj_list,visited): # let 0 be start node 
            cycle=True
            break
print("cycle found?",cycle)