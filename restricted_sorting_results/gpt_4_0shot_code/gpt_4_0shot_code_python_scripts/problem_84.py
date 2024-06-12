
from collections import deque
from itertools import combinations

def min_cost_moves(stacks, costs):
    # Create a list of all colors
    colors = set(color for stack in stacks for color in stack)
    
    # Create a dictionary to store the minimum cost to reach a state
    min_costs = {tuple(tuple(stack) for stack in stacks): 0}
    
    # Create a queue for BFS and add the initial state
    queue = deque([stacks])
    
    while queue:
        stacks = queue.popleft()
        for color in colors:
            # Find all stacks that contain the color at the top
            from_stacks = [i for i, stack in enumerate(stacks) if stack and stack[-1] == color]
            
            # Find all stacks that are either empty or contain the color
            to_stacks = [i for i, stack in enumerate(stacks) if not stack or stack[-1] == color]
            
            for from_stack, to_stack in combinations(from_stacks + to_stacks, 2):
                if from_stack in from_stacks and to_stack in to_stacks:
                    # Make a move
                    new_stacks = [list(stack) for stack in stacks]
                    new_stacks[to_stack].append(new_stacks[from_stack].pop())
                    
                    # Calculate the cost of the move
                    cost = min_costs[tuple(tuple(stack) for stack in stacks)] + costs[to_stack]
                    
                    # Convert the new state to a tuple for hashing
                    new_stacks_tuple = tuple(tuple(stack) for stack in new_stacks)
                    
                    # If the new state has not been visited or the cost is lower, update the cost and add the state to the queue
                    if new_stacks_tuple not in min_costs or cost < min_costs[new_stacks_tuple]:
                        min_costs[new_stacks_tuple] = cost
                        queue.append(new_stacks)
    
    # Find the state with the minimum cost
    min_cost_state = min(min_costs, key=min_costs.get)
    
    # Return the minimum cost and the state
    return min_costs[min_cost_state], min_cost_state
