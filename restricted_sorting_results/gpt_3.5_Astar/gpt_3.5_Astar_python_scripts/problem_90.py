
import heapq
import math


def a_star():
    # Define the initial state of the stacks
    initial_state = [['Pink', 'Black', 'Red', 'White', 'White', 'Black', 'Pink'], [], [], ['Green', 'Green', 'Blue', 'White', 'Pink', 'Pink', 'White'], [], ['Blue', 'Yellow', 'Yellow', 'Black', 'White', 'Green', 'Red'], ['Blue', 'Yellow', 'Blue', 'White', 'Green', 'Red', 'Pink'], ['Pink', 'Yellow', 'Yellow', 'Green', 'Green', 'Black', 'Blue'], [], ['Blue', 'Red', 'Red', 'Black', 'Black', 'Red', 'Yellow'], [], []]
    num_stacks = 12
    stack_capacity = 7
    # Define the cost of moving a block to the top of each stack
    costs = {0: 2, 1: 7, 2: 2, 3: 2, 4: 4, 5: 13, 6: 4, 7: 6, 8: 8, 9: 6, 10: 10, 11: 10}
    # Define the goal state where all stacks are sorted
    goal_state = [[], ['Black', 'Black', 'Black', 'Black', 'Black', 'Black'], ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Green', 'Green', 'Green', 'Green'], ['Pink', 'Pink', 'Pink', 'Pink', 'Pink', 'Pink'], ['Red', 'Red', 'Red', 'Red', 'Red', 'Red'], ['White', 'White', 'White', 'White', 'White', 'White'], ['Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow'], [], [], [], []]

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
                if from_stack != to_stack and state[from_stack] and (not state[to_stack] or state[from_stack][-1] == state[to_stack][-1]):
                    new_state = [list(stack) for stack in state]
                    new_state[from_stack].pop()
                    new_state[to_stack].append(state[from_stack][-1])
                    new_state = tuple(tuple(stack) for stack in new_state)
                    new_cost = g + max(1, costs[from_stack])

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_state, goal_state, costs)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


def heuristic(state, goal_state, costs):
    # The heuristic is the sum of the costs of moving each block to its correct position in the goal state
    h = 0
    for stack, goal_stack in zip(state, goal_state):
        for block, goal_block in zip(stack, goal_stack):
            if block != goal_block:
                h += costs[goal_state.index(goal_stack)]
    return h


print(a_star())
