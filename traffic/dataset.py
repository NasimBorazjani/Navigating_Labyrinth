import random
import string
import pandas as pd
import sys
sys.path.insert(1, './traffic')
import generation
import importlib
importlib.reload(generation)
import math

def create_dataset(min_n, max_n, num_problems):
    problems = {}
    id = 0
    num_rand_instances = math.ceil(num_problems / (max_n - min_n + 1)) 
    for n in range(min_n, max_n + 1):
        for _ in range(num_rand_instances):
            id += 1
            random.seed(id)
            rand_seed = random.randint(0, 2**32 - 1)
            matrix, start, end, d1_last_row, d2_last_row = generation.generate(n, rand_seed)
            matrix_string = generation.matrix_to_string(matrix).replace(',','')
            problem_statement = f"Using the provided matrix map of a city, where numbers represent travel time in minutes (all numbers are positive integers) and 'x' marks closed workshops, find the quickest route for Ben to travel from his current workshop at index {start} to his destination workshop at index {end}, indexing from 0. Ben's car can move north, south, east, or west from a given crossroad, provided there's no x in that direction. Also, there are 3 districts in the city with district 1 covering rows 0 to {d1_last_row}, district 2 covering rows {d1_last_row+1} to {d2_last_row}, and district 3 covering rows {d2_last_row+1} to {n-1}. Ben has to visit at least 1 workshop in each district on his path to the destination. The roads are bidirectional. The answer should be a list of tuples (in Python syntax) indicating the index of workshops on Ben's path. The start and end workshops must be included in the path.\n" + matrix_string
            problems[id] = {"diff_sorted_id":id, "relative_difficulty_score": n - min_n + 1,
                            "statement": problem_statement,
                            "problem_type": "traffic",
                            "problem_category": "pathfinding",
                            "is_feasible_args":[matrix], 
                            "is_correct_args":[matrix, start, end, d1_last_row, d2_last_row], 
                            "A*_args":[str(matrix), str(start), str(end), str(d1_last_row), str(d2_last_row)],
                            "opt_solution":None,
                            "opt_solution_cost":None,
                            "opt_solution_compute_t":None,
                            "solution_depth": None,
                            "max_successor_states":4,
                            "num_vars_per_states":4}
    
    return problems


def get_problems():
    #dimension of the nxn matrix representign the map of the workshops
    min_n = 9
    max_n = 15
    num_problems = 100
    dataset = create_dataset(min_n, max_n, num_problems)
    return dataset
