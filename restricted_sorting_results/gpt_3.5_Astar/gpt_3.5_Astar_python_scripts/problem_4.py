
import heapq


def a_star():
    # Define the initial state of the stacks
    initial_state = [['Red', 'Green', 'Yellow', 'Blue'], [], ['Yellow', 'Green', 'Blue', 'Red'], [], ['Green', 'Red', 'Blue', 'Yellow'], []]
    num_stacks = 6
    stack_capacity = 4
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 2, 1: 6, 2: 5, 3: 2, 4: 5, 5: 7}
    # Define the goal state, where each stack is sorted by shade
    goal_state = [['Red', 'Red', 'Red', 'Red'], ['Green', 'Green', 'Green', 'Green'], ['Yellow', 'Yellow', 'Yellow', 'Yellow'], ['Blue', 'Blue', 'Blue', 'Blue'], [], []]

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if all([state[i] == goal_state[i] for i in range(num_stacks)]):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                if from_stack != to_stack:
                    # Check if the transfer is valid, i.e., the from_stack is not empty and the to_stack is either empty or has blocks of the same shade
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
