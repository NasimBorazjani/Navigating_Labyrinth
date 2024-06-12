
import heapq


def a_star():
    # Define the initial state of the stacks, with the leftmost item being the shade of the topmost block in each stack
    initial_state = [[], [], ['White', 'Black', 'Green', 'White', 'Green', 'Blue'], ['Red', 'Green', 'Black', 'Red', 'White', 'Yellow'], [], ['Yellow', 'Black', 'Yellow', 'Red', 'Green', 'White'], [], ['White', 'Blue', 'Red', 'Red', 'Blue', 'Black'], [], ['Yellow', 'Blue', 'Yellow', 'Blue', 'Green', 'Black']]
    num_stacks = 10
    stack_capacity = 6
    # Define the cost of moving one block to the top of each stack
    stack_costs = {0: 4, 1: 5, 2: 2, 3: 10, 4: 6, 5: 8, 6: 2, 7: 11, 8: 2, 9: 8}


    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


    queue = [(0, 0, [], initial_state)]


    while queue:
        _, g, actions, state = heapq.heappop(queue)


        # Check if the current state is the goal state, where all stacks are sorted by shade
        if all(stack == sorted(stack, key=lambda x: (x == 'White', x == 'Black', x == 'Green', x == 'Red', x == 'Blue', x == 'Yellow')) for stack in state):
            return actions


        # Generate all possible actions from the current state, which includes transferring one block at a time from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                # Check if transferring a block from the 'from_stack' to the 'to_stack' is a valid action
                if from_stack != to_stack and state[from_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]):
                    new_state = [list(stack[:]) for stack in state]
                    new_state[from_stack].pop()
                    new_state[to_stack].append(state[from_stack][-1])
                    new_state = tuple(tuple(stack) for stack in new_state)
                    # Calculate the cost of the new state based on the cost of moving one block to the top of each stack
                    new_cost = g + stack_costs[to_stack]
                  
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))
    return None


print(a_star())
