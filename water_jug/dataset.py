import networkx as nx
import random
import string
import pandas as pd
import sys
sys.path.insert(1, './water_jug')
import generation
import importlib
importlib.reload(generation)
import math

def create_dataset(min_num_jugs, max_num_jugs, num_jugs_step_size,
                   min_capacity, max_capacity, 
                   min_target_rand, max_target_rand, 
                   min_num_targets, max_num_targets, num_problems):
    problems = {}
    id = 0
    num_rand_instances = math.ceil(num_problems/(((max_num_jugs - min_num_jugs + 1)/num_jugs_step_size)*
                                        (max_num_targets - min_num_targets + 1))) - 2
    for num_targets in range(min_num_targets, max_num_targets + 1):
        for num_jugs in range(min_num_jugs, max_num_jugs + 1, num_jugs_step_size):
            # the amount to randomely add to the target amount
            # given the max and min range, incremently increase the rand amount as num_jugs increases 
            num_jugs_progression = (num_jugs - min_num_jugs)//num_jugs_step_size + 1
            max_num_jusgs_progression = max_num_jugs // num_jugs_step_size + 1
            target_rand = min_target_rand + ((max_target_rand - min_target_rand) // (max_num_jusgs_progression/num_jugs_progression))
            for _ in range(num_rand_instances):
                id += 1
                capacities, targets = generation.generate(min_capacity, max_capacity, num_jugs, target_rand, num_targets, id)
                problem_statement = "Given {} labeled water jugs with capacities {} liters, we aim to fill {} unlabeled buckets, numbered 1 to {} and arranged in a line in ascending order, with {} liters of water respectively. The amount of water in each unlabeled bucket can not at any point in time exceed the amount of water in the bucket placed after it. Jugs can only be filled to the top and emptied completely, and the unlabeled buckets cannot be overfilled. An action, represented as a tuple ('+', X, Y) or ('-', X, Y), involves adding to or removing water from the unlabeled bucket numbered Y, using the jug with capacity X. Determine the shortest sequence of actions needed to fill the buckets as specified, and present the solution as a list of action tuples in Python syntax.".format(num_jugs, ', '.join(map(str, capacities)), num_targets, num_targets, ', '.join(map(str, targets)))
                problems[id] = {"diff_sorted_id":id, "relative_difficulty_score":num_jugs_progression + num_targets, 
                                "statement": problem_statement,
                                "problem_type": "water_jug",
                                "problem_category": "subset_sum",
                                "is_feasible_args": [capacities, targets], 
                                "is_correct_args":[capacities, targets], 
                                "A*_args": [str(capacities), str(targets)],
                                "opt_solution":None,
                                "opt_solution_cost":None,
                                "opt_solution_compute_t":None,
                                "solution_depth": None,
                                "max_successor_states":2*len(capacities)*len(targets),
                                "num_vars_per_states":3}
    
    problems = {i:problems[i] for i in range(1, num_problems+1)}
    return problems


def get_problems():
    #number of labeled jugs
    min_num_jugs = 5
    max_num_jugs = 9
    num_jugs_step_size = 2
    #capacity range of labeled jugs
    min_capacity = 10
    max_capacity = 150 
    #amount to randomely add to targets amounts to fill 
    #to ensure they are greater than capacities of the labeld jugs
    min_target_rand = 100
    max_target_rand = 500
    #number of buckets to fill
    min_num_targets = 3
    max_num_targets = 4
    num_problems = 100
    dataset = create_dataset(min_num_jugs, max_num_jugs, num_jugs_step_size, 
                   min_capacity, max_capacity, 
                   min_target_rand, max_target_rand, 
                   min_num_targets, max_num_targets, num_problems)
    
    return dataset


   
    
    
