# path must start with the start cities and end with the dest node, 
# path must be a sequence of capitalized letters representation each node

import networkx as nx
import sys
sys.path.insert(1, './city_directed_graph')
from generation import *

def string_to_adjacency_matrix(s):
    lines = s.strip().split('\n')
    cities = lines[0].split()
    matrix = []

    for line in lines[1:]:
        row = list(map(int, line.split()[1:]))
        matrix.append(row)

    G = nx.Graph()
    G.add_cities_from(cities)

    for i in range(len(cities)):
        for j in range(len(cities)):
            if matrix[i][j] == 1:
                G.add_edge(cities[i], cities[j])
                
    return G
                

def is_feasible(matrix, cities, stop1, stop2, path):
    """G = string_to_adjacency_matrix(G_string)
    cities = list(G.cities)
    matrix = nx.adjacency_matrix(G, nodelist=cities).toarray()"""
    
    visited_cities = [path[0]]
    for i in range(len(path)-1):
        start_node = path[i]
        end_node = path[i+1]
        
        if end_node in visited_cities and end_node != stop1 and end_node!=stop2:
            return False
        visited_cities.append(end_node)
        
        if start_node not in cities or end_node not in cities:
            return False

        # Get the indices of the start and end cities
        start_index = cities.index(start_node)
        end_index = cities.index(end_node)

        # Check if there is an edge from the start node to the end node
        if matrix[start_index][end_index] == 0:
            return False


    return True
   


def is_correct(matrix, cities, start, stop1, stop2, path):
    #G = string_to_adjacency_matrix(G_string)
    
    if (is_feasible(matrix, cities, stop1, stop2, path)
        and  path[0] == start and
        path.count(stop1) == 2 and path.count(stop2) == 2):
        return True, len(path)
    
    return False, None


"""
print(is_correct([[0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
       [1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
       [1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0],
       [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
       [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1],
       [0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0]], 'S', 'N', 'R', ['S', 'D', 'Q', 'R', 'N', 'R']))
    
    
"""