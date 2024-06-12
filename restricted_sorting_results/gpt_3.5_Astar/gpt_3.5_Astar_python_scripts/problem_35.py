
import heapq


def a_star():
    # Define the initial state of the stacks
    initial_state = [[], ['Green', 'Blue', 'Yellow', 'Black', 'Blue'], [], [], ['Blue', 'Black', 'Green', 'Yellow', 'Red'], [], ['Green', 'Red', 'Black', 'Yellow', 'Blue'], ['Red', 'Green', 'Red', 'Black', 'Yellow']]
    num_stacks = 8
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 2, 1: 4, 2: 5, 3: 2, 4: 2, 5: 3, 6: 2, 7: 5}

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if all stacks are sorted
        if all(stack == sorted(stack, key=lambda x: (x == 'Red', x == 'Green', x == 'Blue', x == 'Yellow', x == 'Black')) for stack in state):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                if from_stack != to_stack:
                    # Check if the transfer is valid, ie the from_stack is not empty and the to_stack is either empty or the top block is of the same shade
                    if state[from_stack] and (not state[to_stack] or state[from_stack][-1] == state[to_stack][-1]):
                        new_state = [list(stack[:]) for stack in state]
                        block = new_state[from_stack].pop()
                        new_state[to_stack].append(block)
                        new_state = tuple(tuple(stack) for stack in new_state)
                        new_cost = g + max(1, stack_costs[from_stack])

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


print(a_star())
