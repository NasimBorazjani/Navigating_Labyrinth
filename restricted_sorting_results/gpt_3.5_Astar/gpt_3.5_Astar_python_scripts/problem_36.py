
import heapq


def a_star():
    # Define the initial state of the stacks, with the leftmost item being the shade of the topmost block in each stack
    initial_state = [['Blue', 'Yellow', 'Yellow', 'Green', 'Black'], [], [], [], ['Blue', 'Red', 'Black', 'Yellow', 'Green'], ['Black', 'Red', 'Green', 'Blue', 'Red'], ['Green', 'Yellow', 'Black', 'Red', 'Blue'], []]
    num_stacks = 8
    stack_capacity = 5
    # Define the cost of moving one block to the top of each stack
    stack_costs = {0: 4, 1: 4, 2: 7, 3: 1, 4: 8, 5: 8, 6: 8, 7: 4}


    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


    queue = [(0, 0, [], initial_state)]


    while queue:
        _, g, actions, state = heapq.heappop(queue)


        # If all stacks are sorted, return the actions taken
        if all(stack == sorted(stack) for stack in state if stack):
            return actions


        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                # Check if transferring a block from the 'from_stack' to the 'to_stack' is a valid action
                if from_stack != to_stack and state[from_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]) and len(state[to_stack]) < stack_capacity:
                    new_state = [list(stack[:]) for stack in state]
                    new_state[to_stack].append(new_state[from_stack].pop())
                    new_state = tuple(tuple(stack) for stack in new_state)
                    # Calculate the cost of the new state
                    new_cost = g + stack_costs[to_stack]
                  
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))
    return None


print(a_star())
