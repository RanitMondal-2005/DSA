# # dijkstra algorithm - single source shortest path
# undirected graph
import heapq
n=5 # no of nodes
edges=[(0,1,9),(0,2,75),(1,2,95),(1,3,19),(1,4,42),(2,3,51),(2,4,66),(3,4,31)]
adj_list=[[ ]for _ in range(n)]
for u,v,w in edges:
    adj_list[u].append((v,w))
    adj_list[v].append((u,w))
for i in range(n):
    print(i,"->",adj_list[i])

dist=[float('inf')]*n
heap=[]
source=0
dist[source]=0
heapq.heappush(heap,(dist[source],source))
while len(heap)>0:
    d,u=heapq.heappop(heap)
    for v,w in adj_list[u]: # look for neighbors of node u
        if dist[u]+w< dist[v]:
            dist[v]=dist[u]+w
            heapq.heappush(heap,(dist[v],v))
print(dist)


# bellman ford algorithm- single source shortest path
n=5 # no of nodes
edges=[(0,1,9),(0,2,75),(1,2,95),(1,3,19),(1,4,42),(2,3,51),(2,4,66),(3,4,31)]
# no need of priority Queue and adjacency list
dist=[float('inf')]*n
s=0
dist[s]=0
# just relax v-1 times , v is no of nodes/vertices
for i in range(n-1):
    for u,v,w in edges:
        if dist[u]+w < dist[v]:
            dist[v]=dist[u]+w
# negative cycle check
for u,v,w in edges:
    if dist[u]+w< dist[v]:
        print("negative cycle present")
        break
print(dist)