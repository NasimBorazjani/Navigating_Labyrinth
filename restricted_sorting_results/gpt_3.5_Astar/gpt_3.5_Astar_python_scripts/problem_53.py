
import heapq


def a_star():
    # Define the initial state of the stacks, with each stack represented as a list of blocks
    initial_state = [[], ['Blue', 'Green', 'Red', 'Yellow', 'Blue'], ['Green', 'Blue', 'Yellow', 'Black', 'Red'], [], ['Red', 'Yellow', 'Yellow', 'Black', 'Black'], ['Green', 'Blue', 'Green', 'Black', 'Red'], [], []]
    num_stacks = 8
    stack_capacity = 5
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 7, 1: 4, 2: 1, 3: 2, 4: 6, 5: 8, 6: 7, 7: 6}

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if all stacks are sorted
        if all(stack == sorted(stack) for stack in state if stack):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                if from_stack != to_stack:
                    # Check if the from stack is not empty and the to stack has space for another block
                    if state[from_stack] and len(state[to_stack]) < stack_capacity:
                        new_state = [list(stack) for stack in state]
                        block = new_state[from_stack].pop()
                        new_state[to_stack].append(block)
                        new_state = tuple(tuple(stack) for stack in new_state)
                        # Calculate the cost of the transfer based on the cost of moving a block to the top of the to stack
                        new_cost = g + stack_costs[to_stack]

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


print(a_star())
