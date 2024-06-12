
import pandas as pd
import sys
import importlib
sys.path.insert(1, './coin_exchange')
import generation
importlib.reload(generation)
import math

def create_dataset(min_num_coins, max_num_coins, num_coins_step_size,
                   min_target_lower, max_target_lower, target_range, 
                   target_lower_step_size, num_problems_est):
    problems = {}
    id = 0
    num_rand_instances = math.floor(num_problems_est / (((max_num_coins - min_num_coins +1)/num_coins_step_size) * (max_target_lower - min_target_lower + 1) / target_lower_step_size))
    for target_lower in range(min_target_lower, max_target_lower + 1, target_lower_step_size):
        target_upper = target_lower + target_range
        for num_coins in range(min_num_coins, max_num_coins + 1, num_coins_step_size):
            for _ in range(num_rand_instances):
                id += 1
                eligible_coins, tax_values, target = generation.generate(target_lower, target_upper, num_coins, id)
                problem_statement = f"In the 'taxed coin exchange' problem, you are required to choose a subset of coins from this list {eligible_coins}, such that the sum of the chosen coins adds up to {target}. Each coin in the list is unique and can only be used once. Also coins carry a tax value. The tax values for each coin is {tax_values}, where the tax for coins of the same value is the same. Also, if the coin chosen is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value. The objective is to determine which subset of coins should be selected to minimize the total tax paid. The solution should be presented as a list of numbers, representing the value of the coins chosen in order, with the first coins chosen being in index 0, formatted in Python syntax."
                problems[id] = {"diff_sorted_id":id, "relative_difficulty_score": num_coins,
                                "statement": problem_statement,
                                "problem_type": "coin_exchange",
                                "problem_category": "subset_sum",
                                "is_feasible_args": [eligible_coins],
                                "is_correct_args":[eligible_coins, tax_values, target], 
                                "A*_args":[str(eligible_coins), str(tax_values), str(target)],
                                "opt_solution":None,
                                "opt_solution_cost":None,
                                "opt_solution_compute_t":None,
                                "solution_depth": None,
                                "max_successor_states":len(eligible_coins),
                                "num_vars_per_states":len(eligible_coins)}

    return problems


def get_problems():
    min_num_coins = 15
    max_num_coins = 35
    num_coins_step_size = 1
    min_target_lower = 200
    max_target_lower = 450
    target_lower_step_size = 60
    target_range = 50
    num_problems_est = 100
    dataset = create_dataset(min_num_coins, max_num_coins, num_coins_step_size,
                   min_target_lower, max_target_lower, target_range, 
                   target_lower_step_size, num_problems_est)

    return dataset

    
    
