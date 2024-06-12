
import heapq
import math


def a_star():
    # Define the initial state of the stacks
    initial_state = [['Red', 'Green', 'Blue', 'Yellow', 'Yellow', 'Blue'], [], [], [], ['White', 'Black', 'White', 'Red', 'White', 'Blue'], ['Black', 'Green', 'Red', 'Black', 'Green', 'Yellow'], [], ['Red', 'White', 'Yellow', 'Black', 'Green', 'White'], [], ['Blue', 'Blue', 'Black', 'Green', 'Red', 'Yellow']]
    num_stacks = 10
    stack_capacity = 6
    # Define the cost of moving a block to the top of each stack
    costs = {0: 11, 1: 5, 2: 9, 3: 5, 4: 2, 5: 2, 6: 6, 7: 6, 8: 6, 9: 2}
    # Define the goal state where all stacks are sorted by shade
    goal_state = [['Red', 'Red', 'Red', 'Red', 'Red', 'Red'], ['Green', 'Green', 'Green', 'Green', 'Green', 'Green'], ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'], ['Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow'], ['White', 'White', 'White', 'White', 'White', 'White'], ['Black', 'Black', 'Black', 'Black', 'Black', 'Black'], [], [], [], []]

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
                # Check if transferring a block from the 'from_stack' to the 'to_stack' is valid
                if from_stack != to_stack and state[from_stack] and (not state[to_stack] or state[from_stack][-1] == state[to_stack][-1]) and len(state[to_stack]) < stack_capacity:
                    new_state = [list(stack) for stack in state]
                    new_state[to_stack].append(new_state[from_stack].pop())
                    new_state = tuple(tuple(stack) for stack in new_state)
                    new_cost = g + costs[from_stack]

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_state, goal_state, costs)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


def heuristic(state, goal, costs):
    # The heuristic is the sum of the costs of moving each block to its correct position in the goal state
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != goal[i][j]:
                # Find the cost of moving the block to its correct position
                h += costs[i]
    return h


print(a_star())
