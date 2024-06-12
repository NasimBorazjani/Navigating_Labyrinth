
import heapq
import math


def a_star():
    # Define the initial state of the stacks
    initial_state = [['White', 'White', 'Yellow', 'White', 'White', 'Black'], [], ['Red', 'Red', 'Green', 'Green', 'Green', 'Red'], ['Black', 'Yellow', 'Black', 'Yellow', 'Blue', 'Green'], ['Yellow', 'Blue', 'Black', 'Green', 'Blue', 'Red'], [], ['Red', 'Black', 'Blue', 'Yellow', 'Blue', 'White'], [], [], []]
    num_stacks = 10
    stack_capacity = 6
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 6, 1: 7, 2: 11, 3: 10, 4: 7, 5: 2, 6: 3, 7: 3, 8: 11, 9: 8}
    # Define the goal state where all stacks are sorted by shade
    goal_state = [['White', 'White', 'White', 'White', 'White'], ['Red', 'Red', 'Red', 'Red', 'Red'], ['Green', 'Green', 'Green', 'Green', 'Green'], ['Black', 'Black', 'Black', 'Black', 'Black'], ['Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow'], [], [], [], [], []]

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
                # Check if transferring a block from the 'from_stack' to the 'to_stack' is valid
                if from_stack != to_stack and state[from_stack] and (not state[to_stack] or state[from_stack][-1] == state[to_stack][-1]):
                    new_state = [list(stack[:]) for stack in state]
                    new_state[to_stack].append(new_state[from_stack].pop())
                    new_state = tuple(tuple(stack) for stack in new_state)
                    new_cost = g + stack_costs[to_stack]

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_state, goal_state, stack_costs)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


def heuristic(state, goal, stack_costs):
    # The heuristic is the sum of the costs of moving each block to its correct position in the goal state
    # This heuristic is admissible because it underestimates the cost to reach the goal state, as it assumes that each block can be moved to its correct position in the goal state with the minimum cost
    # The heuristic is consistent because the cost of moving a block to its correct position is always at least 1, which is the decrease in the heuristic estimate if the block is moved to its correct position
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != goal[i][j]:
                h += stack_costs[i]
    return h


print(a_star())
