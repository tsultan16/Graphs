'''
   Graph Breadth-First-Search (BFS) Algorithm

'''
import numpy as np
from math import inf


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

def is_undirected(graph):
    adj_mat = construct_adjacency_matrix(graph)

    for i in range(adj_mat.shape[0]):
        for i2 in range(adj_mat.shape[0]-i):
            j = i + i2
            if(adj_mat[i,j] != adj_mat[j,i]):
                print(f"adt_mat[{i},{j}] = {adj_mat[i,j]}, adt_mat[{j},{i}] = {adj_mat[j,i]} => not symmetric => directed")
                return False

    return True


V = ('a', 'b', 'c', 'd', 'e', 'f')
E = (('a', 'd', 1),('a','c', 1),('d','c',1),('a','e',1),('c','f',1),('e','f',1),('e','b',1),('b','f',1))

G = {'vertices': V, 'edges': E}

assert is_undirected(G), "Error! Directed graphs are currently unsupported!"


print(f"Graph vertices: {G['vertices']}")
print(f"Graph edges: {G['edges']}")

adj_mat = construct_adjacency_matrix(G)
adj_list = construct_adjacency_list(G)

