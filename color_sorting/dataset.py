import random
import string
import pandas as pd
import sys
sys.path.insert(1, './color_sorting')
import generation
import importlib
importlib.reload(generation)
import math

def create_dataset(min_num_tubes, max_num_tubes, min_tube_capacity,
                   max_tube_capacity, num_problems):
    problems = {}
    id = 0
    num_rand_instances = math.ceil(num_problems/((max_num_tubes - min_num_tubes + 1) * 
                                                 (max_tube_capacity - min_tube_capacity + 1)))
    for num_tubes in range(min_num_tubes, max_num_tubes + 1):
        for capacity in range(min_tube_capacity, max_tube_capacity + 1):
            for _ in range(num_rand_instances):
                id += 1
                random.seed(id)
                rand_seed = random.randint(0, 1000)
                tubes = generation.generate(num_tubes, capacity, rand_seed)
                problem_statement = f"The game of 'Sort It' begins with {num_tubes} tubes, each filled with {len(tubes[0])} balls of different colors. The goal is to sort the balls by color, with each tube containing balls of only one color. Only one ball can be moved at a time, taken from the top of one tube and placed on top of another. The capacity of each tube (maximum number of balls we can fit in each tube) is {capacity} balls. It is not allowed to place a ball in a tube that already has {capacity} balls. The solution should be a list of tuples, each containing, first, the index of the tube from which a ball is taken and, second, the index of the tube to which it is moved, indexing from 0. Given the initial state of the tubes, represented by the lists below (with the leftmost item being the color of the topmost ball in each tube), what is the shortest list of move tuples that will result in all the balls being correctly sorted? " + str(tubes)
                problems[id] = {"diff_sorted_id":id, "relative_difficulty_score": num_tubes - min_num_tubes + 1 + capacity,
                                "statement": problem_statement,
                                "problem_type": "color_sorting",
                                "problem_category": "sorting",
                                "is_feasible_args":[tubes, capacity],
                                "is_correct_args":[tubes, capacity], 
                                "A*_args": [str(tubes), str(capacity)],
                                "opt_solution":None,
                                "opt_solution_cost":None,
                                "opt_solution_compute_t":None,
                                "solution_depth": None,
                                "max_successor_states":num_tubes*(num_tubes - 1),
                                "num_vars_per_states":num_tubes*len(tubes[0])}

    return problems


def get_problems():
    min_num_tubes = 3
    max_num_tubes = 3
    min_tube_capacity = 6
    max_tube_capacity = 9
    num_problmes = 100
    dataset = create_dataset(min_num_tubes, max_num_tubes, min_tube_capacity, 
                             max_tube_capacity, num_problmes)
    
    return dataset