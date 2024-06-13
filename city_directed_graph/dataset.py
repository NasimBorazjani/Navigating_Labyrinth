import networkx as nx
import random
import string
import pandas as pd
import sys
sys.path.insert(1, './city_directed_graph')
import generation
import importlib
importlib.reload(generation)
import math


def create_dataset(min_number_nodes, max_number_nodes, num_problems):
    problems = {}
    id = 0
    num_rand_instances = math.ceil(num_problems / (max_number_nodes - min_number_nodes + 1))
    for num_nodes in range(min_number_nodes, max_number_nodes + 1):
        for _ in range(num_rand_instances):
            id += 1
            random.seed(id) 
            rand_seed = random.randint(1, 100000)
            G, start, dest, intermediate_stop = generation.create_directed_graph(num_nodes, rand_seed)
            adjacency_matrix_str = generation.return_adjacency_matrix_string(G)
            adjacency_matrix = nx.adjacency_matrix(G, nodelist=list(G.nodes)).toarray()
            problem_statement = f"We have a map of cities, each represented by a letter, and they are connected by one-way roads. The adjacency matrix below shows the connections between the cities. Each row and column represents a city, and a '1' signifies a direct road from the city of the row to the city of the column. The travel time between any two directly connected cities is the same. Currently, we are located in city '{start}'. Our task is to visit city {dest} and city {intermediate_stop} excatly twice. Determine the quickest route that allows us to visit both these destination cities, ensuring that we stop at the two destinations twice on our path. The sequence in which we visit the destination cities is not important. However, apart from {intermediate_stop} and {dest}, we can only visit each city once on our path. Provide the solution as a list of the city names on our path, including the start, in Python syntax.\n\n{adjacency_matrix_str}"            
            problems[id] = {"diff_sorted_id":id, "relative_difficulty_score": num_nodes, 
                            "statement": problem_statement,
                            "problem_type": "city_directed_graph",
                            "problem_category": "pathfinding",
                            "is_feasible_args":[adjacency_matrix.tolist(), list(G.nodes), dest, intermediate_stop], 
                            "is_correct_args":[adjacency_matrix.tolist(), list(G.nodes), start, dest, intermediate_stop], 
                            "A*_args": [str(adjacency_matrix.tolist()), str(list(G.nodes)), str([start]), str([dest, intermediate_stop])],
                            "opt_solution":None,
                            "opt_solution_cost":None,
                            "opt_solution_compute_t":None,
                            "solution_depth": None,
                            "max_successor_states":num_nodes,
                            "num_vars_per_states":num_nodes + 3}
    
    problems = {i:problems[i] for i in range(1, num_problems + 1)}
    return problems


def get_problems():
    #size of the graph
    min_number_nodes = 10
    max_number_nodes = 15
    num_problems = 100
    dataset = create_dataset(min_number_nodes, max_number_nodes, num_problems)

    return dataset

    
    
    
