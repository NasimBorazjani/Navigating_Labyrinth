
import heapq


def a_star():
    # Define the initial state of the stacks
    initial_state = [['Yellow', 'Yellow', 'Pink', 'Black', 'Green', 'Green', 'Yellow'],
                     ['Pink', 'Yellow', 'White', 'Red', 'Black', 'Blue', 'Blue'],
                     [],
                     [],
                     ['Pink', 'Green', 'Pink', 'Pink', 'Blue', 'Red', 'Red'],
                     ['Black', 'Black', 'Black', 'Blue', 'Yellow', 'Red', 'White'],
                     [],
                     [],
                     [],
                     [],
                     ['Green', 'Blue', 'Red', 'Red', 'Green', 'White', 'Black'],
                     ['White', 'White', 'Green', 'Yellow', 'Blue', 'White', 'Pink']]
    num_stacks = 12
    stack_capacity = 7
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 12, 1: 11, 2: 5, 3: 11, 4: 10, 5: 9, 6: 5, 7: 5, 8: 3, 9: 10, 10: 5, 11: 5}

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the state is the goal state where all stacks are sorted
        if all(all(stack[i] == stack[0] for i in range(len(stack)) if stack) for stack in state):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                if from_stack != to_stack and state[from_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]):
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
