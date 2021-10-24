import igraph as ig

#g = Graph.Full(6)
#g = Graph([(0,1), (1,2), (2,3), (3,4), (4,5), (5,6), (6,7), (7,8)])
g = ig.Graph.Full_Bipartite(3, 3)
#g = ig.Graph.Adjacency([[0, 1, 1], [0, 0, 0], [0, 0, 1]])


# Python Program to implement
# the above approach
  
# Recursive Function to find the
# Maximal Independent Vertex Set    
def graphSets(graph):
      
    # Base Case - Given Graph 
    # has no nodes
    if(len(graph) == 0):
        return []
     
    # Base Case - Given Graph
    # has 1 node
    if(len(graph) == 1):
        return [list(graph.keys())[0]]
      
    # Select a vertex from the graph
    vCurrent = list(graph.keys())[0]
      
    # Case 1 - Proceed removing
    # the selected vertex
    # from the Maximal Set
    graph2 = dict(graph)
      
    # Delete current vertex 
    # from the Graph
    del graph2[vCurrent]
      
    # Recursive call - Gets 
    # Maximal Set,
    # assuming current Vertex 
    # not selected
    res1 = graphSets(graph2)
      
    # Case 2 - Proceed considering
    # the selected vertex as part
    # of the Maximal Set
  
    # Loop through its neighbours
    for v in graph[vCurrent]:
          
        # Delete neighbor from 
        # the current subgraph
        if(v in graph2):
            del graph2[v]
      
    # This result set contains VFirst,
    # and the result of recursive
    # call assuming neighbors of vFirst
    # are not selected
    res2 = [vCurrent] + graphSets(graph2)
      
    # Our final result is the one 
    # which is bigger, return it
    if(len(res1) > len(res2)):
        return res1
    return res2
  
# Driver Code
V = 8
  
# Defines edges
E = [ (1, 2),
      (1, 3),
      (2, 4),
      (5, 6),
      (6, 7),
      (4, 8)]
  
graph = dict([])
  
# Constructs Graph as a dictionary 
# of the following format-
  
# graph[VertexNumber V] 
# = list[Neighbors of Vertex V]
for i in range(len(E)):
    v1, v2 = E[i]
      
    if(v1 not in graph):
        graph[v1] = []
    if(v2 not in graph):
        graph[v2] = []
      
    graph[v1].append(v2)
    graph[v2].append(v1)
  
# Recursive call considering 
# all vertices in the maximum 
# independent set
maximalIndependentSet = graphSets(graph)
  
# Prints the Result 
for i in maximalIndependentSet:
    print(i, end =" ")

print(g.largest_independent_vertex_sets())
