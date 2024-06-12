
import heapq


def a_star():
    # Define the initial state of the stacks
    initial_state = [['Red', 'Yellow', 'Red', 'Yellow', 'Black'],
                     ['Black', 'Blue', 'Green', 'Green', 'Blue'],
                     [],
                     [],
                     [],
                     [],
                     ['Black', 'Blue', 'Green', 'Black', 'Yellow'],
                     ['Blue', 'Green', 'Yellow', 'Red', 'Red']]
    
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 2, 1: 3, 2: 5, 3: 9, 4: 8, 5: 5, 6: 8, 7: 1}
    
    # Encoding other variables of the problem
    num_stacks = 8
    stack_capacity = 5
    
    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0
    
    queue = [(0, 0, [], initial_state)]
    
    while queue:
        _, g, actions, state = heapq.heappop(queue)
        
        # Check if the state is the goal state, where all stacks are sorted
        if all(stack == sorted(stack) for stack in state if stack):
            return actions
        
        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                if from_stack != to_stack:
                    # Check if transferring a block from the top of the from_stack to the to_stack is valid
                    if state[from_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]) and len(state[to_stack]) < stack_capacity:
                        new_state = [list(stack) for stack in state]
                        block = new_state[from_stack].pop()
                        new_state[to_stack].append(block)
                        new_state = tuple(tuple(stack) for stack in new_state)
                        new_cost = g + stack_costs[to_stack]
                        
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))
    
    return None


print(a_star())
