
import heapq
from collections import Counter


def a_star(initial_state, cost_dict, capacity, num_blocks_per_tube_final):
    """# Define the initial state of the stacks, as a 2d tuple of color of the blocks in stacks 0 to 5
    initial_state = [[], [], [], ['Blue', 'Yellow', 'Blue', 'Blue'], ['Red', 'Green', 'Yellow', 'Green'], ['Red', 'Red', 'Yellow', 'Green']]
    
    # Encoding other variables given in the problem statement
    num_stacks = 6
    capacity = 4
    cost_dict = {0: 5, 1: 5, 2: 3, 3: 1, 4: 5, 5: 1}
    
    initial_state = [['Pink', 'Pink', 'Purple', 'Black', 'Black', 'Purple', 'Green', 'Red'], [], ['Purple', 'Blue', 'Purple', 'Yellow', 'White', 'Black', 'Black', 'Red'], ['White', 'Blue', 'Green', 'Pink', 'Purple', 'Purple', 'Blue', 'Yellow'], ['Black', 'Green', 'Green', 'White', 'Pink', 'Black', 'Yellow', 'Yellow'], [], [], ['Red', 'Red', 'Blue', 'White', 'White', 'Yellow', 'Blue', 'Black'], ['Yellow', 'Pink', 'Red', 'White', 'Blue', 'Green', 'Blue', 'Red'], [], [], ['Purple', 'Green', 'Red', 'White', 'Green', 'Pink', 'Yellow', 'Pink'], [], []]
    cost_dict = {0: 4, 1: 13, 2: 14, 3: 8, 4: 1, 5: 12, 6: 7, 7: 4, 8: 15, 9: 15, 10: 11, 11: 14, 12: 13, 13: 13}
    capacity = 8"""
    
    initial_state = tuple(tuple(element) for element in initial_state)
    num_stacks = len(initial_state)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0


    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state)]


    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)


        # Check of the current state is the goal state
        # The goal state is where each stack only contains blocks of 1 single color
        if all(((len(set(stack)) == 1 and len(stack) == num_blocks_per_tube_final) or len(stack) == 0) for stack in state):
            return actions


        # Generate all possible actions from the current state, which includes moving a block from any of the 6 stacks to another stack
        for from_stack_ind in range(num_stacks):
            for to_stack_ind in range(num_stacks):
                # Check if the new state would be valid, ie from_stack and to_stack must not be the same stack
                # And from_stack must at least have 1 block to move and the to_stack cannot be at capacity
                if (from_stack_ind != to_stack_ind and 
                    state[from_stack_ind] and
                    len(state[to_stack_ind]) < capacity):
                    
                    block_to_move = state[from_stack_ind][0]
                    
                    if (not state[to_stack_ind] or (len(set(state[to_stack_ind])) == 1 and state[to_stack_ind][0] == block_to_move)):
                        # Generate the new state
                        new_state = [list(stack[:]) for stack in state]
                        block_to_move = new_state[from_stack_ind].pop(0)
                        # Add the block to the top of the to_stack
                        new_state[to_stack_ind].insert(0, block_to_move)
                        new_state = tuple(tuple(stack) for stack in new_state)
                        # The cost so far is the number of moves made, as the task is to minimize the number of moves required
                        new_cost = g + cost_dict[to_stack_ind]

                        # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost + heuristic(new_state, cost_dict), g + 1, actions + [(from_stack_ind, to_stack_ind)], new_state))
    return None


def heuristic(stacks, cost_dict):

    least_cost = min(list(cost_dict.values()))
    
    h = 0
    for stack in stacks:
        if stack:
            # If there are ties in the frequency of colors, the most_common_color must be match the color of the blocks lower that are in the stack, as moving lower blocks is costlier          
            reversed_stack = stack[:]
            reversed_stack = reversed_stack[::-1]
            # Get the most common color
            most_common_color = Counter(reversed_stack).most_common(1)[0][0]
            for block in stack:
                if block != most_common_color:
                    h += least_cost
    return h

import sys
def main():
    # Read the initial state from the command line
    
    initial_state = eval(sys.argv[1])
    cost_dict = eval(sys.argv[2])
    capacity = eval(sys.argv[3])
    num_blocks_per_tube_final = eval(sys.argv[4])

    print(a_star(initial_state, cost_dict, capacity, num_blocks_per_tube_final))

    #print(e-s)

if __name__ == "__main__":
    main()
