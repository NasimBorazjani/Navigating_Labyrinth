
import heapq


def a_star():
    # Define the initial state of the stacks
    initial_state = [[], [], [], ['Blue', 'Yellow', 'Red', 'Blue', 'Black'], ['Red', 'Yellow', 'Blue', 'Yellow', 'Blue'], ['Green', 'Red', 'Black', 'Red', 'Yellow'], [], ['Green', 'Green', 'Black', 'Green', 'Black']]
    num_stacks = 8
    stack_capacity = 5
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 6, 1: 4, 2: 3, 3: 8, 4: 7, 5: 5, 6: 9, 7: 9}

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if all stacks are sorted
        if all(stack == sorted(stack, key=lambda x: (x == 'Red', x == 'Yellow', x == 'Blue', x == 'Green', x == 'Black')) for stack in state):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                if from_stack != to_stack:
                    # Check if the from_stack is not empty and the to_stack has space for another block
                    if state[from_stack] and len(state[to_stack]) < stack_capacity:
                        new_state = [list(stack) for stack in state]
                        block = new_state[from_stack].pop()
                        new_state[to_stack].append(block)
                        new_state = tuple(tuple(stack) for stack in new_state)
                        # Calculate the cost of the transfer based on the cost of moving a block to the top of the to_stack
                        new_cost = g + stack_costs[to_stack]

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


print(a_star())
