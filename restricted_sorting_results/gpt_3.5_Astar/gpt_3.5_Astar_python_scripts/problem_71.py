
import heapq
import math


def a_star():
    # Define the initial state of the stacks, where each stack is represented as a list of blocks
    initial_state = [[], [], ['White', 'Yellow', 'Yellow', 'Green', 'Blue', 'Green'], ['Red', 'Yellow', 'White', 'Blue', 'Black', 'Black'], ['Black', 'Red', 'Blue', 'Black', 'Green', 'Green'], ['Green', 'Black', 'Yellow', 'Red', 'White', 'Red'], ['White', 'Blue', 'Red', 'Blue', 'White', 'Yellow'], [], [], []]
    num_stacks = 10
    stack_capacity = 6
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 4, 1: 1, 2: 1, 3: 9, 4: 2, 5: 9, 6: 1, 7: 9, 8: 6, 9: 4}
    # Define the goal state, where all stacks are sorted by shade
    goal_state = [[], ['Black', 'Black', 'Black', 'Black', 'Black', 'Black'], ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Green', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Red', 'Red', 'Red', 'Red'], ['White', 'White', 'White', 'White', 'White', 'White'], ['Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow'], [], [], []]

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if all(state[i] == goal_state[i] for i in range(num_stacks)):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                # Check if transferring a block from the 'from_stack' to the 'to_stack' is a valid action
                if from_stack != to_stack and state[from_stack] and (not state[to_stack] or state[from_stack][-1] == state[to_stack][-1]) and len(state[to_stack]) < stack_capacity:
                    new_state = [list(stack) for stack in state]
                    new_state[to_stack].append(new_state[from_stack].pop())
                    new_state = tuple(tuple(stack) for stack in new_state)
                    # Calculate the cost of the new state based on the cost of moving a block to the top of the 'to_stack'
                    new_cost = g + stack_costs[to_stack]

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        # Calculate the heuristic cost based on the number of blocks out of order in each stack
                        h = heuristic(new_state, goal_state)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


def heuristic(state, goal):
    # The heuristic is calculated based on the number of blocks out of order in each stack
    h = 0
    for i in range(len(state)):
        # Count the number of blocks out of order in each stack
        h += sum(1 for j in range(len(state[i])) if state[i][j] != goal[i][j])
    return h


print(a_star())
