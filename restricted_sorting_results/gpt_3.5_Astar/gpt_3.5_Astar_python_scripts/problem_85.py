
import heapq


def a_star():
    # Define the initial state of the stacks
    initial_state = [['Pink', 'Red', 'Black', 'Green', 'Yellow', 'Yellow', 'Pink'], [], [], ['Pink', 'White', 'Yellow', 'Blue', 'Green', 'Blue', 'Black'], ['Black', 'Blue', 'Red', 'Pink', 'Yellow', 'Yellow', 'Blue'], [], ['White', 'Black', 'Yellow', 'Green', 'Red', 'Green', 'Green'], [], [], ['Pink', 'Red', 'Black', 'White', 'White', 'Red', 'White'], ['Blue', 'Green', 'Pink', 'Blue', 'White', 'Red', 'Black'], []]
    num_stacks = 12
    stack_capacity = 7
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 8, 1: 5, 2: 4, 3: 12, 4: 9, 5: 9, 6: 3, 7: 2, 8: 11, 9: 9, 10: 3, 11: 2}


    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


    queue = [(0, 0, [], initial_state)]


    while queue:
        _, g, actions, state = heapq.heappop(queue)


        # Check if the state is the goal state, where all stacks are sorted
        if all(stack == sorted(stack, key=lambda x: (x == 'Pink', x == 'Red', x == 'Black', x == 'White', x == 'Yellow', x == 'Green', x == 'Blue')) for stack in state):
            return actions


        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                # Check if transferring a block from the 'from_stack' to the 'to_stack' is valid
                if from_stack != to_stack and state[from_stack] and (not state[to_stack] or state[from_stack][-1] == state[to_stack][-1]):
                    new_state = [list(stack[:]) for stack in state]
                    new_state[from_stack].pop()
                    new_state[to_stack].append(state[from_stack][-1])
                    new_state = tuple(tuple(stack) for stack in new_state)
                    # Calculate the cost of the new state
                    new_cost = g + stack_costs[to_stack]
                  
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))
    return None


print(a_star())
