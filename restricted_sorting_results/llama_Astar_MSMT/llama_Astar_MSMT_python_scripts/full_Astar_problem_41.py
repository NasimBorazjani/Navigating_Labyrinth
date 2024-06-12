
def initialize():
    # Define the initial state of the stacks as a list of lists
    initial_state = [['Green', 'Blue', 'Yellow', 'Green', 'Blue'],
                     ['Black', 'Green', 'Red', 'Red', 'Black'],
                     [],
                     ['Blue', 'Yellow', 'Red', 'Black', 'Yellow'],
                     [],
                     [],
                     ['Blue', 'Red', 'Black', 'Yellow', 'Green'],
                     []]
    
    # Define the cost of moving one block to the top of each stack
    stack_costs = {0: 2, 1: 1, 2: 2, 3: 8, 4: 4, 5: 3, 6: 6, 7: 3}
    
    # Initialize visited_costs and the priority queue
    visited_costs = {}
    visited_costs[tuple(map(tuple, initial_state))] = 0
    queue = [(0, 0, [], initial_state)]
    
    return initial_state, stack_costs, visited_costs, queue
