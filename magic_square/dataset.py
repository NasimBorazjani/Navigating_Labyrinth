import random
import pandas as pd
import sys
sys.path.insert(1, './magic_square')
import generation
import importlib
importlib.reload(generation)
import math

def create_dataset(min_n, max_n,
                    min_range, max_range, 
                    range_increment, min_num_mask,
                    min_num_to_show, num_problems):
    problems = {}
    id = 0
    num_rand_instances = num_problems // ((max_n - min_n + 1) *
                                          (max_range - min_range +  1)//range_increment *
                                          2) 
    for n in range(min_n, max_n + 1):
        
        min_range_n = n**2 + min_range
        max_range_n = n**2 + max_range
        
        col_range = row_range = (math.ceil(n/4), 3*n//4)
        
        if n == 3:
            max_num_mask = 4
            min_num_mask = 3
            num_mask_increment = 1
        else:
            #number of entries to mask on top of the number of constraints, show at least 4 entries in the chart, mask at least 3 more entries the num_contraints
            num_constraints = 2 * (row_range[1] - row_range[0]) + 1
            max_num_mask = n*n - num_constraints - min_num_to_show
            num_mask_increment = (max_num_mask - min_num_mask + 1)//5
        if not num_mask_increment: num_mask_increment = 1
            
        for valid_range in range(min_range_n, max_range_n, range_increment):
            for num_mask in range(min_num_mask, max_num_mask + 1, num_mask_increment):
                random.seed(id)
                lower_range = random.randint(5, 50)
                upper_range = lower_range + valid_range 
                for _ in range(num_rand_instances):
                    id += 1
                    grid, sum_cols, sum_rows, sum_top_right_diag = generation.generate(n, lower_range, upper_range, 
                                                                           col_range, row_range, num_mask, id)
                    sum_rows_astar = [None] * n
                    sum_cols_astar = [None] * n
                    for i in range(row_range[0], row_range[1]):
                        sum_rows_astar[i] = sum_rows[i - row_range[0]]
                        sum_cols_astar[i] = sum_cols[i - row_range[0]]
                    if n > 3:    
                        problem_statement = f"In the magic square problem, a {n}x{n} grid is filled with unique integers ranging from {lower_range} to {upper_range} ({lower_range} included in the range but {upper_range} is not included). Some numbers are already given, while others are unknown and represented as 'x'. The sums of columns must be { str(sum_cols_astar)[1:-1]} for columns {row_range[0]} to {row_range[1] - 1} respectively, and the sums of rows must be { str(sum_rows_astar)[1:-1]} for rows {row_range[0]} to {row_range[1] - 1} respectively, where None means that we do not have any constraints on the sum of the numbers in the row or column at that index.  Also, the sum of the numbers in the diagonal from the top right to the bottom left corner of the grid should equal {sum_top_right_diag}. The goal is to find unique integers (ie each number can be in the final grid only once) in the given range to replace with ‘x’s in the grid below such that the sum of the specified rows, columns, and diagonal equals the given amounts and the sum of all of the numbers in the grid is as low as possible. The solution should be provided as a list of tuples in Python syntax. Each tuple should contain three numbers for each 'x' position: the row index, the column index (both starting from 0), and the value of the unique integer replaced with 'x' at that position.\n\nGrid:\n {grid}"
                    else:
                        problem_statement = f"In the magic square problem, a {n}x{n} grid is filled with unique integers ranging from {lower_range} to {upper_range} ({lower_range} included in the range but {upper_range} is not included). Some numbers are already given, while others are unknown and represented as 'x'. Sum of column {col_range[0]} (counting from 0) must be { str(sum_cols_astar[1])}, and sum of row {row_range[0]} must be { str(sum_rows_astar[1])}. Also, the sum of the numbers in the diagonal from the top right to the bottom left corner of the grid should equal {sum_top_right_diag}. The goal is to find unique integers (ie each number can be in the final grid only once) in the given range to replace with ‘x’s in the grid below such that the sum of the specified rows, columns, and diagonal equals the given amounts and the sum of all of the numbers in the grid is as low as possible. The solution should be provided as a list of tuples in Python syntax. Each tuple should contain three numbers for each 'x' position: the row index, the column index (both starting from 0), and the value of the unique integer replaced with 'x' at that position.\n\nGrid:\n {grid}"                        
                    grid_list = [["" if j=='x' else j for j in i] for i in grid]
                    problems[id] = {"diff_sorted_id":id, "relative_difficulty_score": n*n + valid_range + num_mask,
                                    "statement": problem_statement,
                                    "problem_type": "magic_square",
                                    "problem_category": "underdetermined_system",
                                    "is_feasible_args":[str(grid_list), n, lower_range, upper_range], 
                                    "is_correct_args":[str(grid_list), lower_range, upper_range, 
                                                col_range, row_range, sum_cols, sum_rows, int(sum_top_right_diag)], 
                                    "A*_args": [str(grid_list), str(lower_range), str(upper_range), 
                                              str(sum_cols_astar), str(sum_rows_astar), str(sum_top_right_diag)],
                                    "opt_solution":None,
                                    "opt_solution_cost":None,
                                    "opt_solution_compute_t":None,
                                    "solution_depth": None,
                                    "max_successor_states":upper_range - lower_range,
                                    "num_vars_per_states":n*n}
                                    
    return problems


def get_problems():
    #dimension of the nxn grid of the numbers
    min_n = 3
    max_n = 4
    #range of numbers that can appear in the grid
    min_range = 10
    max_range = 41
    range_increment = 5
    num_problems = 100
    #number of cells to mask
    min_num_mask = 4
    min_num_to_show = 5
    dataset = create_dataset(min_n, max_n,
                    min_range, max_range, 
                    range_increment, min_num_mask,
                    min_num_to_show, num_problems)

    return dataset
