import random
import string
import pandas as pd
import sys
sys.path.insert(1, './restricted_sorting')
import generation
import importlib
importlib.reload(generation)
import math

def create_dataset(min_num_colors, max_num_colors, num_problmes):
    problems = {}
    id = 0
    num_rand_instances = math.ceil(num_problmes / (max_num_colors - min_num_colors + 1)) + 5
    for num_colors in range(min_num_colors, max_num_colors + 1):
        for _ in range(num_rand_instances):
            id += 1
            random.seed(id)
            rand_seed = random.randint(0, 1000)
            stacks, capacity, num_stacks_full, cost_dict, num_blocks_per_tube_final = generation.generate(num_colors, rand_seed)
        
            problem_statement = f"In 'Restricted Sorting', there are {len(stacks)} stacks each with a capacity of {capacity} blocks, with {num_stacks_full} stacks filled with blocks of varying shades and the remaining are empty. The challenge is to sort the blocks by shade such that if a stack is not empty, it is stacked with {num_blocks_per_tube_final} blocks of a single shade. The player can only transfer one block at a time from the top of a stack to an empty stack or to a stack that has only blocks of that shade, without exceeding the stacks’ capacity. Transferring blocks to certain stacks is more expensive than others. The cost of moving one block to the top of each stack is: {cost_dict}, where the keys are the index of each stack, indexing from 0. The cost of moving a block is always at least 1. The solution should be a list of tuples, each containing, first, the index of the stack from which a block is picked up from and, second, the index of the stack to which it is transferred, indexing from 0. Given the initial state of the stacks, represented by the lists below (with the leftmost item being the shade of the topmost block in each stack)(and the first stack being the stack at index 0), what is the list of transfer pairs (reported in python syntax) with the least possible cost, that will result in all the blocks being correctly sorted? " + str(stacks)            
            problems[id] = {"diff_sorted_id":id, "relative_difficulty_score": num_colors - min_num_colors + 1,
                            "statement": problem_statement,
                            "problem_type": "restricted_sorting",
                            "problem_category": "sorting",
                            "is_feasible_args":[stacks, capacity, cost_dict],
                            "is_correct_args":[stacks, capacity, cost_dict, num_blocks_per_tube_final],
                            "A*_args": [str(stacks), str(cost_dict), str(capacity), str(num_blocks_per_tube_final)],
                            "opt_solution":None,
                            "opt_solution_cost":None,
                            "opt_solution_compute_t":None,
                            "solution_depth": None,
                            "max_successor_states":len(stacks)*(len(stacks) - 1),
                            "num_vars_per_states":num_stacks_full*capacity}
    
    return problems


def get_problems():
    #number of different colored blocks in the game
    min_num_colors = 4
    max_num_colors = 7
    num_problems = 100
    dataset = create_dataset(min_num_colors, max_num_colors, num_problems)
    return dataset

