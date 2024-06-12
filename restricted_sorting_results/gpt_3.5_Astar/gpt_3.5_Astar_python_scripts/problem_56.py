
import heapq


def a_star():
    # Define the initial state of the stacks, with each stack represented as a list of blocks
    initial_state = [[], ['Yellow', 'Red', 'Black', 'Yellow', 'Green'], [], [], ['Green', 'Red', 'Blue', 'Blue', 'Black'], ['Green', 'Blue', 'Yellow', 'Red', 'Yellow'], [], ['Blue', 'Green', 'Black', 'Red', 'Black']]
    num_stacks = 8
    stack_capacity = 5
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 5, 1: 5, 2: 5, 3: 6, 4: 5, 5: 5, 6: 9, 7: 6}

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if all stacks are sorted
        if all(all(stack[i] == stack[i+1] for i in range(len(stack)-1)) for stack in state if stack):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                if from_stack != to_stack:
                    # Check if the from_stack is not empty and the to_stack has the same shade as the block being transferred or is empty
                    if state[from_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]):
                        new_state = [stack[:] for stack in state]
                        new_state[from_stack] = new_state[from_stack][:-1]
                        new_state[to_stack].append(state[from_stack][-1])
                        new_state = tuple(tuple(stack) for stack in new_state)
                        new_cost = g + max(1, stack_costs[from_stack])

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


print(a_star())
