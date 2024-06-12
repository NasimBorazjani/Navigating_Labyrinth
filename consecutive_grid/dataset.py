import random
import pandas as pd
import sys
sys.path.insert(1, './consecutive_grid')
import generation
import importlib
importlib.reload(generation)
import math

def create_dataset(min_n, max_n,
                    min_range, max_range, 
                    range_increment, min_num_mask_3, max_num_mask_3,
                    min_num_mask_4, max_num_mask_4, num_problems):
    problems = {}
    id = 0
    num_rand_instances = num_problems // ((max_n - min_n + 1) *
                                          (max_range - min_range +  1)//range_increment *4)
    for n in range(min_n, max_n + 1):
        
        min_range_n = n**2 + min_range
        max_range_n = n**2 + max_range
        
        if n == 3:
            min_num_mask = min_num_mask_3 
            max_num_mask = max_num_mask_3
        elif n == 4:
            min_num_mask = min_num_mask_4
            max_num_mask = max_num_mask_4
            
        for valid_range in range(min_range_n, max_range_n, range_increment):
            for num_mask in range(min_num_mask, max_num_mask + 1):
                for _ in range(num_rand_instances):
                    id += 1
                    random.seed(id)
                    lower_range = random.randint(5, 50)
                    upper_range = lower_range + valid_range - 1
                    rand_seed = random.randint(1, 2**32 - 1)
                    grid = generation.generate(n, lower_range, upper_range, num_mask, rand_seed)
                    if n == 4:    
                        problem_statement = f"We have a 4x4 numerical grid, with numbers ranging from {lower_range} to {upper_range} ({lower_range} included in the range but {upper_range} is not included). The numbers in each row and column must be strictly increasing or decreasing. This means that either first > second > third > fourth or first < second < third < fourth in each row and column. If a grid cell is marked with an 'x', the number in that position is hidden. The objective is to replace the 'x's with unique integers from the given range, ensuring that each number only appears once in the grid. The replacements must maintain the consecutive order in each row and column. Additionally, the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner should be minimized. The solution should be given as a list of tuples in Python syntax. Each tuple should represent the replacement of a number with an  'x' number and contain three elements: the row index of the 'x', the column index  of the 'x' (both starting from 0), and the value of the number that replaces the 'x'. The initial state of the grid is as follows: \n\nGrid:\n {grid}"
                    elif n == 3:
                        problem_statement = f"We have a 3x3 numerical grid, with numbers ranging from {lower_range} to {upper_range} ({lower_range} included in the range but {upper_range} is not included). The numbers in each row and column must be strictly increasing or decreasing. This means that either first > second > third or first < second < third in each row and column. If a grid cell is marked with an 'x', the number in that position is hidden. The objective is to replace the 'x's with unique integers from the given range, ensuring that each number only appears once in the grid. The replacements must maintain the consecutive order in each row and column. Additionally, the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner should be minimized. The solution should be given as a list of tuples in Python syntax. Each tuple should represent the replacement of a number with an  'x' number and contain three elements: the row index of the 'x', the column index  of the 'x' (both starting from 0), and the value of the number that replaces the 'x'. The initial state of the grid is as follows: \n\nGrid:\n {grid}"
                    grid_list = [["" if j=='x' else j for j in i] for i in grid]
                    problems[id] = {"diff_sorted_id":id, "relative_difficulty_score": n + valid_range//max_range + num_mask,
                                    "statement": problem_statement,
                                    "problem_type": "consecutive_grid",
                                    "problem_category": "underdetermined_system",
                                    "is_feasible_args":[str(grid_list), lower_range, upper_range],
                                    "is_correct_args":[str(grid_list), lower_range, upper_range], 
                                    "A*_args": [str(grid_list), str(lower_range), str(upper_range)],
                                    "opt_solution":None,
                                    "opt_solution_cost":None,
                                    "opt_solution_compute_t":None,
                                    "solution_depth": None, 
                                    "max_successor_states":upper_range - lower_range,
                                    "num_vars_per_states":n*n}
                                    
    return problems


def get_problems():
    #dimnesion of the nxn grid of numbers
    min_n = 3
    max_n = 4
    # the number of velid numbers that we can place into the grid
    min_range = 25
    max_range = 46
    range_increment = 5
    num_problems = 100
    # number of cells to mask for the 3x3 grid
    min_num_mask_3 = 4
    max_num_mask_3 = 6
    # number of cells to mask for the 4x4 grid
    min_num_mask_4 = 6
    max_num_mask_4 = 10
    dataset = create_dataset(min_n, max_n,
                    min_range, max_range, 
                    range_increment, min_num_mask_3, max_num_mask_3,
                    min_num_mask_4, max_num_mask_4, num_problems)

    return dataset
