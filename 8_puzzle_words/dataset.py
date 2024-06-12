import random
import string
import pandas as pd
import sys
sys.path.insert(1, './8_puzzle_words')
import generation
import importlib
importlib.reload(generation)
import math

def create_dataset(max_height, max_width, min_num_swaps, max_num_swaps, num_swaps_increment, num_problems):
    problems = {}
    id = 0
    num_rand_instances = math.ceil(num_problems / ((max_height - 4 + 1) * (max_width - 4 + 1) * (max_num_swaps - min_num_swaps + 1) / num_swaps_increment)) 
    for height in range(4, max_height + 1):
        for width in range(4, max_width + 1):
            for num_swaps in range(min_num_swaps, max_num_swaps + 1, num_swaps_increment):
                for _ in range(num_rand_instances):
                    id += 1
                    random.seed(id)
                    rand_seed = random.randint(0, 200000)
                    board, target_words = generation.generate_puzzle(height, width, num_swaps, rand_seed)
                    problem_statement = "In the game 'Sort the Chars', we are given a table of n by m dimensions. This table contains n words, each with m characters, except for the first word which has m - 1 characters. Each character is written on a separate tile. The objective of the game is to rearrange the characters such that row i spells the i-th word in the list, with the blank tile ('_') placed in the top left corner of the board in the end. We can rearrange the tiles by swapping the blank space with any of its 4 diagonal neighboring tiles. Given the list of words and initial state of the board below, where the black space is represented as '_', what is the shortest list of swap actions (reported in python syntax) that can sort the board into the given list of target words? The list must only include the 4 diagonal swap directions: up-right, down-right, up-left, or down-left, representing the direction in ehich the blank space was swpped in. Target words: "+  ', '.join(target_words) + "   The initial board: " + str(board)
                    problems[id] = {"diff_sorted_id": id, "relative_difficulty_score": height + width - 7, 
                                    "statement": problem_statement,
                                    "problem_type": "8_puzzle_words",
                                    "problem_category": "puzzle",
                                    "is_feasible_args":[board], "is_correct_args":[board, target_words], 
                                    "A*_args":[str(board), str(target_words)],
                                    "opt_solution":None,
                                    "opt_solution_cost":None,
                                    "opt_solution_compute_t":None,
                                    "solution_depth": None,
                                    "max_successor_states":4,
                                    "num_vars_per_states":height*width}

    problems = {i:problems[i] for i in range(1, num_problems + 1)}
    return problems

#min_height and min_width in this case must be 4
def get_problems():
    max_height = 6
    max_width = 6
    #number of random swaps to genrate the initla board state
    min_num_swaps = 100
    max_num_swaps = 210
    num_swaps_increment = 50
    num_problems = 100
    dataset = create_dataset(max_height, max_width, min_num_swaps,
                             max_num_swaps, num_swaps_increment, num_problems)
    
    return dataset

