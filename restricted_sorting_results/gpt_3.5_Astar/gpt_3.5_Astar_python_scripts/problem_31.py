
import heapq


def a_star():
    # Define the initial state of the stacks, with the blocks represented by their colors
    initial_state = [[], [], ['Yellow', 'Yellow', 'Green', 'Black', 'Red'], ['Black', 'Green', 'Black', 'Blue', 'Yellow'], ['Green', 'Blue', 'Yellow', 'Red', 'Blue'], [], [], ['Black', 'Red', 'Green', 'Red', 'Blue']]
    num_stacks = 8
    stack_capacity = 5
    # Define the cost of moving a block to the top of each stack
    costs = {0: 7, 1: 2, 2: 1, 3: 1, 4: 9, 5: 4, 6: 2, 7: 7}

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the state is the goal state, where all stacks are sorted
        if all(stack == sorted(stack, key=lambda x: (x == 'Red', x == 'Green', x == 'Blue', x == 'Yellow')) for stack in state):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                if from_stack != to_stack:
                    # Check if transferring a block from the 'from_stack' to the 'to_stack' is valid
                    if state[from_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]):
                        new_state = [list(stack) for stack in state]
                        new_state[from_stack].pop()
                        new_state[to_stack].append(state[from_stack][-1])
                        new_state = tuple(tuple(stack) for stack in new_state)
                        # Calculate the cost of the new state
                        new_cost = g + costs[to_stack]

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


print(a_star())