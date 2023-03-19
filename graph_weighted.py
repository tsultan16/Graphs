'''
    Simple (weighted) graph data structure implementation, given the set of vertices and edges, both adjacency matrix and adjacency list representations are constructed.

    find_path() uses exhaustive search to find if a path exists between a pair of nodes

'''
import numpy as np
from math import inf

print(inf)

def construct_adjacency_matrix(graph):

    V = graph['vertices']
    E = graph['edges']
    adj_mat = np.ones(shape=(len(V), len(V))) * inf

    for edge in E:
        print(edge)
        i = V.index(edge[0])
        j = V.index(edge[1])
        adj_mat[i,j] = edge[2]
        adj_mat[j,i] = edge[2]

    print("Adjacency matrix: ")
    print(adj_mat)

    return adj_mat

def construct_adjacency_list(graph):
    V = graph['vertices']
    E = graph['edges']

    adj_list = {}
    for vertex in V:
        adj_list[vertex] = []    
  
    for edge in E:
        adj_list[edge[0]].append((edge[1], edge[2]))    
        adj_list[edge[1]].append((edge[0], edge[2]))    

    print("Adjacency list:")
    print(adj_list)    
    return adj_list

# find thre path between vertex 'u' and vertex 'v', given the adjavcency list representation of a graph 
def find_path(u, v, path, final_path, visited, adj_list, count):

    count += 1
    current_path = path[:] 
    current_path.append(u)
    current_visited = visited.copy()
    current_visited.add(u)
                
    print("#"*count + f" u = '{u}', v = '{v}', current_path = {current_path}, visited_nodes = {current_visited}")

    # first check if v is in the adjacency list of u
    current_adjacency_list = list(zip(*adj_list[u]))[0]
    print("#"*count + f" Adjacent list for '{u}': {current_adjacency_list}")
    
    for w in current_adjacency_list:
        print("#"*count + f" Considering node '{w}' from adjacency list..")

        # if v is in the adjacenecy_list then we've found a path!
        if (w == v):
            current_path.append(v) 
            print("#"*count + f" {v} is in adjacency list. Path found: {current_path}")
            final_path.append(current_path)
            current_visited.add(v)

        # only traverse to unvisited nodes
        if(w not in current_visited):
         
            # recursilvely check all other nodes adjacent to u
            #print(f"{v} is not in adjacency list..")
            print("#"*count + f" Traversing to node {w}")
            #print(f"Current path: {current_path}")
            #print(f"Current visited: {current_visited}")
            find_path(w[0], v, current_path, final_path, current_visited, adj_list, count)          
    
        else:
            if(w != v):
                print("#"*count + f" Node '{w}' already traversed.")
       
          
    if(len(final_path) == 0):
        print("#"*count + f" No path found between {u} and {v}\n")        
    return final_path


# determine if a connected graph is tree (i.e. doesn't have cycles)
def is_tree(graph):

    # first make sure the graph is connected
    adj_list = construct_adjacency_list(graph) 
    
    has_isolated_node = False
    for vertex in graph['vertices']:
        has_isolated_node = (len(adj_list[vertex]) == 0) 

    # check that there's a path between all connected nodes
    for ix, vertex1 in enumerate(graph['vertices']):
        for vertex2 in graph['vertices'][ix+1:]:
            print(f"({vertex1},{vertex2})", end = "   ")
            # find path between vertex 1 and 2
            path = list(vertex1)
            find_path(vertex1, vertex2, path, adj_list)
       
        print("")
    
    if(has_isolated_node):
        print("Error! Graph is not connected because it has isolated node.")
        return None

    # a connected graph (i.e. graph without any isolated nodes) is acyclic iff the number of edges extactly equals one less than the number of vertices
    # (i.e. it's a tree)
    no_cycle = False
    if ((len(graph['vertices'])-1) == len(graph['edges'])):
        print("The graph is acyclic")
        no_cycle = True
    return no_cycle   

V = ('a', 'b', 'c', 'd', 'e', 'f', 'h')
E = (('a', 'd', 20),('a','c', 4),('c','e',9),('c','b',12),('b','f',3),('d','e', 5),('e','f',32))

G = {'vertices': V, 'edges': E}

print(f"Graph vertices: {G['vertices']}")
print(f"Graph edges: {G['edges']}")

construct_adjacency_matrix(G)
adj_list = construct_adjacency_list(G)
#print(is_tree(G))
path = list() #list(V[0])
final_path = []
visited = set() #set(V[0])
vertex_i = V[3]
vertex_f = V[6]
print(f"Path between {vertex_i} and {vertex_f} = {find_path(vertex_i, vertex_f, path, final_path, visited, adj_list, count = 0)}")