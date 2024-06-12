
import heapq


def a_star():
    # Define the initial state of the stacks
    initial_state = [[], [], ['Blue', 'Green', 'Yellow', 'Green'], ['Red', 'Yellow', 'Yellow', 'Green'], [], ['Red', 'Blue', 'Red', 'Blue']]
    num_stacks = 6
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 7, 1: 6, 2: 2, 3: 7, 4: 7, 5: 4}
    # Define the goal state where all stacks are sorted by shade
    goal_state = [[], [], ['Blue', 'Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Red', 'Red'], ['Yellow', 'Yellow', 'Yellow', 'Yellow']]

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if all(stack == goal_stack for stack, goal_stack in zip(state, goal_state)):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                # Check if transferring a block from the 'from_stack' to the 'to_stack' is a valid action
                if from_stack != to_stack and state[from_stack] and (not state[to_stack] or state[from_stack][-1] == state[to_stack][-1]):
                    new_state = [list(stack) for stack in state]
                    new_state[from_stack].pop()
                    new_state[to_stack].append(state[from_stack][-1])
                    new_state = tuple(tuple(stack) for stack in new_state)
                    # Calculate the cost of the new state
                    new_cost = g + max(1, stack_costs[from_stack])

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        # Add the transfer action to the list of actions
                        heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


print(a_star())
