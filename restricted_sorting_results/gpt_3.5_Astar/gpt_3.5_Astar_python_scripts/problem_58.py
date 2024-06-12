
import heapq


def a_star():
    # Define the initial state of the stacks, with each stack represented as a list of blocks
    initial_state = [[], ['Green', 'Yellow', 'Red', 'Red', 'Red'], [], ['Green', 'Yellow', 'Green', 'Blue', 'Black'], ['Red', 'Yellow', 'Black', 'Blue', 'Black'], [], [], ['Green', 'Black', 'Yellow', 'Blue', 'Blue']]
    num_stacks = 8
    stack_capacity = 5
    # Define the cost of moving a block to the top of each stack
    costs = {0: 4, 1: 8, 2: 9, 3: 9, 4: 5, 5: 7, 6: 9, 7: 6}

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
                    # Check if the from_stack is not empty and the to_stack has space for another block or has blocks of the same shade
                    if state[from_stack] and (len(state[to_stack]) < stack_capacity or all(block == state[from_stack][-1] for block in state[to_stack])):
                        new_state = [list(stack[:]) for stack in state]
                        new_state[from_stack].pop()
                        new_state[to_stack].append(state[from_stack][-1])
                        new_state = tuple(tuple(stack) for stack in new_state)
                        new_cost = g + max(1, costs[from_stack])

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


print(a_star())
