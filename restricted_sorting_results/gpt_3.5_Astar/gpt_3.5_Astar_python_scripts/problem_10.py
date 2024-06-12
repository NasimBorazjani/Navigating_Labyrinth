
import heapq


def a_star():
    # Define the initial state of the stacks, with the leftmost item being the shade of the topmost block in each stack
    initial_state = [[], [], ['Green', 'Blue', 'Blue', 'Blue'], ['Yellow', 'Red', 'Yellow', 'Red'], ['Green', 'Red', 'Green', 'Yellow'], []]
    num_stacks = 6
    stack_capacity = 4
    # Define the cost of moving one block to the top of each stack
    costs = {0: 1, 1: 7, 2: 2, 3: 4, 4: 6, 5: 5}
    # Define the goal state, where all stacks are sorted by shade
    goal_state = [[], ['Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Green'], ['Red', 'Red', 'Red'], ['Yellow', 'Yellow', 'Yellow'], []]

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if all(stack == goal_stack for stack, goal_stack in zip(state, goal_state)):
            return actions

        # Generate all possible actions from the current state, which includes transferring one block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                if from_stack != to_stack:
                    # Check if the transfer is valid, i.e., the from_stack is not empty and the to_stack is either empty or the top block has the same shade
                    if state[from_stack] and (not state[to_stack] or state[from_stack][-1] == state[to_stack][-1]):
                        new_state = [list(stack) for stack in state]
                        new_state[from_stack].pop()
                        new_state[to_stack].append(state[from_stack][-1])
                        new_state = tuple(tuple(stack) for stack in new_state)
                        # Calculate the cost of the new state
                        new_cost = g + costs[from_stack]

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


print(a_star())
