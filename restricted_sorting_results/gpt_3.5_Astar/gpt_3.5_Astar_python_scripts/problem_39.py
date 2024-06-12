
import heapq


def a_star():
    # Define the initial state of the stacks
    initial_state = [['Green', 'Green', 'Black', 'Blue', 'Black'], [], [], [], ['Yellow', 'Red', 'Black', 'Red', 'Blue'], ['Yellow', 'Blue', 'Red', 'Black', 'Blue'], ['Red', 'Green', 'Green', 'Yellow', 'Yellow'], []]
    num_stacks = 8
    stack_capacity = 5
    # Define the cost of moving a block to the top of each stack
    costs = {0: 8, 1: 8, 2: 1, 3: 2, 4: 9, 5: 4, 6: 7, 7: 8}

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if all stacks are sorted
        if all(stack == sorted(stack, key=lambda x: (x, -ord(x))) for stack in state if stack):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                if from_stack != to_stack:
                    # Check if the transfer is valid, i.e., the from_stack is not empty and the to_stack is either empty or the top block matches the block being transferred
                    if state[from_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]):
                        new_state = [list(stack) for stack in state]
                        new_state[from_stack].pop()
                        new_state[to_stack].append(state[from_stack][-1])
                        new_state = tuple(tuple(stack) for stack in new_state)
                        new_cost = g + costs[from_stack]

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


print(a_star())
