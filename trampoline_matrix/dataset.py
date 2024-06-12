import random
import string
import pandas as pd
import sys
sys.path.insert(1, './trampoline_matrix')
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
            #print(id)
            random.seed(id)
            rand_seed = random.randint(0, 2**32 - 1)
            matrix, start, end, num_diag_req = generation.generate(n, rand_seed)
            problem_statement = f"Alex is at a trampoline park with a grid of mini trampolines, arranged in a square of {n}x{n}. Some trampolines are broken and unusable. A map of the park is provided below, with 1 indicating a broken trampoline and 0 indicating a functional one. Alex can jump to any of the eight adjacent trampolines, as long as they are not broken. However, Alex must make excatly {num_diag_req} diagonal jumps, no more, no less, on his path to his destination. He is currently on the trampoline at position {start} (positions are counted from 0, left to right, top to bottom) and wants to reach the trampoline at position {end}. What is the shortest sequence of trampolines he should jump on to reach his destination (including the first and final trampolines)? The answer should be a list of tuples, in Python syntax, indicating the row and column of each trampoline Alex jumps on. \n" + generation.matrix_to_string(matrix)            
            problems[id] = {"diff_sorted_id":id, "relative_difficulty_score": n, 
                            "statement": problem_statement,
                            "problem_type": "trampoline_matrix",
                            "problem_category": "pathfinding",
                            "is_feasible_args":[str(matrix), int(num_diag_req)],
                            "is_correct_args":[str(matrix), start, end, int(num_diag_req)],
                            "A*_args": [str(matrix), str(start), str(end), str(num_diag_req)],
                            "opt_solution":None,
                            "opt_solution_cost":None,
                            "opt_solution_compute_t":None,
                            "solution_depth": None,
                            "max_successor_states":8,
                            "num_vars_per_states":2}
    
    return problems


def get_problems():
    # dimension of the nxn matrix map
    min_n = 9
    max_n = 15
    num_problems = 100
    dataset = create_dataset(min_n, max_n, num_problems)

    return dataset

