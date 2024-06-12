
import heapq

def initialize():
    # Define the initial state of the stacks as a list of lists
    initial_state = [[], ['Yellow', 'Blue', 'Blue', 'Yellow', 'Green'], ['Black', 'Red', 'Black', 'Green', 'Red'], ['Yellow', 'Yellow', 'Red', 'Black', 'Blue'], [], ['Blue', 'Red', 'Green', 'Green', 'Black'], [], []]
    # Define the goal state, where each stack has 4 blocks of a single shade
    goal_state = [['Yellow', 'Yellow', 'Yellow', 'Yellow'], ['Blue', 'Blue', 'Blue', 'Blue'], ['Black', 'Black', 'Black', 'Black'], ['Red', 'Red', 'Red', 'Red'], ['Green', 'Green', 'Green', 'Green']]
    # Define the cost of moving a block to a stack
    cost_per_stack = {0: 6, 1: 3, 2: 5, 3: 2, 4: 8, 5: 3, 6: 8, 7: 5}
    # Define the maximum capacity of a stack
    max_capacity = 5

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    return initial_state, goal_state, cost_per_stack, max_capacity, visited_costs, queue
