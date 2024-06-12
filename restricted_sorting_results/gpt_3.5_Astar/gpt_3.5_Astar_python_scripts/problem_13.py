
import heapq


def a_star():
    # Define the initial state of the stacks
    initial_state = [['Green', 'Red', 'Blue', 'Blue'], [], ['Yellow', 'Red', 'Green', 'Green'], [], [], ['Red', 'Yellow', 'Blue', 'Yellow']]
    num_stacks = 6
    stack_capacity = 4
    # Define the cost of moving a block to the top of each stack
    costs = {0: 4, 1: 2, 2: 2, 3: 7, 4: 4, 5: 5}
    # Define the goal state where all blocks are sorted by shade
    goal_state = [['Green', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Red', 'Red'], ['Blue', 'Blue', 'Blue', 'Blue'], ['Yellow', 'Yellow', 'Yellow', 'Yellow'], [], []]

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
                    # Check if the transfer is valid, ie the from_stack is not empty and the to_stack has space for the block
                    if state[from_stack] and len(state[to_stack]) < stack_capacity and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]):
                        new_state = [list(stack[:]) for stack in state]
                        new_state[from_stack].pop()
                        new_state[to_stack].append(state[from_stack][-1])
                        new_state = tuple(tuple(stack) for stack in new_state)
                        # Calculate the cost of the transfer
                        new_cost = g + costs[from_stack]

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


print(a_star())
