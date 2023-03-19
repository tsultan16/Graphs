'''
    Simple (weighted) graph data structure implementation, given the set of vertices and edges, both adjacency matrix and adjacency list representations are constructed
'''
import numpy as np

def construct_adjacency_matrix(graph):

    V = graph['vertices']
    E = graph['edges']
    adj_mat = np.zeros(shape=(len(V), len(V)))

    for edge in E:
        #print(edge)
        i = V.index(edge[0])
        j = V.index(edge[1])
        adj_mat[i,j] = 1
        adj_mat[j,i] = 1

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
        adj_list[edge[0]].append(edge[1])    
        adj_list[edge[1]].append(edge[0])    

    print("Adjacency list:")
    print(adj_list)    

V = ('a', 'b', 'c', 'd', 'e', 'f')
E = (('a', 'd'),('a','c'),('c','e'),('c','b'),('b','f'),('d','e'),('e','f'))

G = {'vertices': V, 'edges': E}

print(f"Graph vertices: {G['vertices']}")
print(f"Graph edges: {G['edges']}")

construct_adjacency_matrix(G)
construct_adjacency_list(G)