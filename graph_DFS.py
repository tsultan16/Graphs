'''
   Graph Depth-First-Search (DFS) Algorithm

'''
import numpy as np
from math import inf
import random

class stack(object):
   
    def __init__(self) -> None:
        self.stk = []

    def size(self):
        return len(self.stk)

    def stk_push(self, item):
        self.stk.append(item)

    def stk_pop(self):
        if (self.size() > 0):
            return self.stk.pop(-1)            
        else:
            print("Stack is empty. Nothing to pop out!")

    def stk_top(self):
        return self.stk[-1]

    def print_stack(self):
        print("Stack:")
        for i in range (self.size()):
            print(self.stk[-1-i])


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

# Depth first serach algorithm, inputs are the marked vertices (i.e. each vertex has two numbers,the first number tracks the order in which the vertex is visitied and the other one tracks order in which it becomes a dead-end)
def DFS(graph, starting_vertex):

    marked_vertices = {vertex : [0,0] for vertex in graph['vertices']}
    #print(f"Marked vertices: {marked_vertices}")
    adj_list = construct_adjacency_list(graph)

    # create an empty traversal stack
    traversal_stack = stack()
    counts = [0,0]

    print(f"Starting vertex '{starting_vertex}'")

    # recursively visit all the adjacent vertices and mark them accorfding to the order visited
    dfs_rec(starting_vertex, marked_vertices, adj_list, traversal_stack, counts)
            
    return marked_vertices


def dfs_rec(v, marked_vertices, adj_list, traversal_stack, counts):

    # mark the vertex with count and push it onto the traversal stack
    counts[0] += 1
    marked_vertices[v][0] = counts[0]
    traversal_stack.stk_push(v)

    #print(f"Visiting vertex: {v}, order: {counts[0]}")
    #traversal_stack.print_stack()

    adjacent_vertices = list(zip(*adj_list[v]))[0]
    #print(f"'{v}' adjacent vertices: {adjacent_vertices}")

    visited_adjacent_vertices = 0
    # visit each unvisited adjacent vertex  
    for w in adjacent_vertices:
        
        # check of vertex is unvisited, if so visit that vertex
        if(marked_vertices[w][0] == 0):
           #print(f"Will now visit adjacent vertex '{w}'")
           dfs_rec(w, marked_vertices, adj_list, traversal_stack, counts) 
 
        else:
            visited_adjacent_vertices += 1

    # if this vertex is a dead end, pop off the traversal stack and mark it with the count
    #print(f"Vertex '{v}' is a dead-end.")

    counts[1] += 1
    marked_vertices[v][1] = counts[1]
    w = traversal_stack.stk_pop()
    #traversal_stack.print_stack()
    if(traversal_stack.size() == 0):
        print("\n### Depth-first traversal completed!\n")
    #else:
        #print(f"Backtracking to vertex '{traversal_stack.stk_top()}'")
    
def is_connected(graph):

    starting_vertex = random.choice(graph['vertices'])
    marked_vertices = DFS(graph, starting_vertex)

    for v in marked_vertices:
        if(marked_vertices[v][0] == 0):
            return False  

    return True

V = ('a', 'b', 'c', 'd', 'e', 'f')
E = (('a','c', 1),('a', 'd', 1),('d','c',1),('a','e',1),('c','f',1),('f', 'b',1),('e','b',1),('e','f',1))

G = {'vertices': V, 'edges': E}

assert is_undirected(G), "Error! Directed graphs are currently unsupported!"


print(f"Graph vertices: {G['vertices']}")
print(f"Graph edges: {G['edges']}")

adj_mat = construct_adjacency_matrix(G)
adj_list = construct_adjacency_list(G)

marked_vertices = DFS(G, V[0])
print(f"Marked vertices: {marked_vertices}")
print(f"Graph is connected: {is_connected(G)}")
