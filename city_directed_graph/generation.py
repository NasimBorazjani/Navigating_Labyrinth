import networkx as nx
import random
import string

#min number of nodes is 4
def create_directed_graph(n, seed):
    random.seed(seed)
    # Create a directed graph
    G = nx.DiGraph()
            
    start = random.choice(string.ascii_uppercase)
    destination = random.choice(string.ascii_uppercase)
    while destination == start:
        seed += 1
        random.seed(seed)
        start = random.choice(string.ascii_uppercase)
        destination = random.choice(string.ascii_uppercase)

    upper_chars = [chr(i) for i in range(65, 91)]
    if start in upper_chars:
        upper_chars.remove(start)
    if destination in upper_chars:
        upper_chars.remove(destination)
    # Add n nodes to the graph
    nodes = [start, destination] + random.sample(upper_chars, n-2)
    random.shuffle(nodes)
    G.add_nodes_from(nodes)

    # Add random edges between nodes
    for i in range(n):
        for j in range(i+1, n):
            rand = random.random()
            if rand < 0.2:
                G.add_edge(nodes[i], nodes[j])
            elif rand < 0.5:
                G.add_edge(nodes[j], nodes[i])
    
                
    # Find nodes that are not X or Y
    intermediate_nodes = [node for node in nodes if node not in {start, destination}]
    random.shuffle(intermediate_nodes)

    # Add a random number of intermediate nodes between X and Y
    path = random.sample(intermediate_nodes, len(intermediate_nodes))
    
    intermediate_stop = path[len(path)//2]
    path.append(intermediate_stop)
    
    path.insert(len(path)//4, destination)
    path.insert(3*len(path)//4, destination)
    path = [start] + path

    
    if nx.has_path(G, start, intermediate_stop):
        shortest_path = nx.shortest_path(G, start, intermediate_stop)
        # Remove the edges in the shortest path
        for i in range(len(shortest_path) - 1):
            G.remove_edge(shortest_path[i], shortest_path[i + 1])
    
    # Ensure there is a path from X to Y with a random number of intermediate nodes
    if nx.has_path(G, start, destination):
        shortest_path = nx.shortest_path(G, start, destination)
        # Remove the edges in the shortest path
        for i in range(len(shortest_path) - 1):
            G.remove_edge(shortest_path[i], shortest_path[i + 1])
                

    for i in range(len(path) - 1):
        G.add_edge(path[i], path[i+1])
   

    return G, start, destination, intermediate_stop


def print_adjacency_matrix(G):
    nodes = list(G.nodes)
    matrix = nx.adjacency_matrix(G, nodelist=nodes).toarray()

    print(' ', end=' ')
    for node in nodes:
        print(node, end=' ')
    print()

    for i in range(len(nodes)):
        print(nodes[i], end=' ')
        for j in range(len(nodes)):
            print(matrix[i][j], end=' ')
        print()


def return_adjacency_matrix_string(G):
    nodes = list(G.nodes)
    matrix = nx.adjacency_matrix(G, nodelist=nodes).toarray()
    result = '  '

    for node in nodes:
        result += str(node) + ' '
    result += '\n'

    for i in range(len(nodes)):
        result += str(nodes[i]) + ' '
        for j in range(len(nodes)):
            result += str(matrix[i][j]) + ' '
        result += '\n'
    
    return result




"""G, start, destination, intermediate_stop= create_directed_graph(10, 2)
print(return_adjacency_matrix_string(G))
print_adjacency_matrix(G)
nodes = list(G.nodes)
matrix = nx.adjacency_matrix(G, nodelist=nodes).toarray()
print(matrix)"""

