import random
import string
import pandas as pd
import sys
sys.path.insert(1, './8_puzzle')
import generation
import importlib
importlib.reload(generation)
import math


def create_dataset(max_height, max_width, min_num_swaps,
                   max_num_swaps, num_swaps_increment, num_problems):
    problems = {}
    id = 0
    num_rand_instances = round(num_problems / ((max_height - 3 + 1) * (max_width - 3 + 1) 
                                               * (max_num_swaps - min_num_swaps + 1) / num_swaps_increment)) 
    for height in range(3, max_height + 1):
        for width in range(3, max_width + 1):
            for num_swaps in range(min_num_swaps, max_num_swaps + 1, num_swaps_increment):
                for _ in range(num_rand_instances):
                    id += 1
                    random.seed(id)
                    rand_seed = random.randint(1, 10000)
                    board = generation.generate_puzzle(height, width, num_swaps, rand_seed)
                    problem_statement = "In the 8-puzzle game, you are given a grid with numbered square tiles arranged randomly and one tile missing. The goal is to arrange the tiles in descending order by sliding them into the empty space. The tiles can move in 4 directions: left, right, up, and down.  Given the initial state of the puzzle below, where the empty spot is represented as “_”, provide the shortest list of tiles that need to be swapped with the empty spot to achieve the goal state. The goal state is when all tiles are in descending order, with the largest number in the top left corner, and the empty spot is in the bottom right corner. The solution should be a list of numbers in Python format, where each number represents the number on the tile that the empty spot is swapped with at each turn. Initial state of the puzzle: " + str(board)
                    problems[id] = {"diff_sorted_id":id, "relative_difficulty_score": num_swaps//num_swaps_increment + height - 3 + width - 3, 
                                    "statement": problem_statement,
                                    "problem_type": "8_puzzle",
                                    "problem_category": "puzzle",
                                    "is_feasible_args":[board], "is_correct_args":[board], "A*_args": [str(board)],
                                    "opt_solution":None,
                                    "opt_solution_cost":None,
                                    "opt_solution_compute_t":None,
                                    "solution_depth": None,
                                    "max_successor_states":4,
                                    "num_vars_per_states":height*width}
    
    #cutting the dataset to num_problem, becuase puzzle problmes are fast to solve due to the small branching factor (max_successor_states)
    problems = {i:problems[i] for i in range(1, num_problems+1)}
    return problems

#min_height, min_width is 3
def get_problems():
    #maximum height and width of the table
    max_height = 3
    max_width = 6
    #number of random swaps to create the initla table
    min_num_swaps = 70
    max_num_swaps = 200
    num_swaps_increment = 30
    num_problems = 100
    dataset = create_dataset(max_height, max_width, min_num_swaps, max_num_swaps, num_swaps_increment, num_problems)
    return dataset

