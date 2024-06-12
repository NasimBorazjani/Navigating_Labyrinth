
import heapq
import math


def a_star():
    # Define the initial state of the stacks
    initial_state = [['Black', 'Blue', 'Green', 'Green', 'Pink', 'Black', 'Red'], [], ['Green', 'White', 'Yellow', 'Red', 'White', 'Blue', 'Pink'], [], [], ['Black', 'Green', 'Black', 'Yellow', 'Black', 'Blue', 'Black'], ['Green', 'Blue', 'Yellow', 'Yellow', 'Red', 'Yellow', 'Pink'], ['Red', 'White', 'Blue', 'Pink', 'Red', 'Blue', 'White'], [], [], ['Red', 'White', 'Pink', 'Green', 'Yellow', 'White', 'Pink'], []]
    num_stacks = 12
    stack_capacity = 7
    # Define the cost of moving a block to each stack
    costs = {0: 7, 1: 9, 2: 13, 3: 3, 4: 4, 5: 4, 6: 6, 7: 11, 8: 12, 9: 3, 10: 13, 11: 5}
    # Define the goal state where all stacks are sorted
    goal_state = [['Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black'], ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green'], ['Pink', 'Pink', 'Pink', 'Pink', 'Pink', 'Pink', 'Pink'], ['Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red'], ['White', 'White', 'White', 'White', 'White', 'White', 'White'], ['Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow'], [], [], [], []]
  
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
                if from_stack != to_stack and state[from_stack] and (not state[to_stack] or state[from_stack][-1] == state[to_stack][-1]):
                    new_state = [list(stack) for stack in state]
                    new_state[from_stack] = new_state[from_stack][:-1]
                    new_state[to_stack].append(state[from_stack][-1])
                    new_state = tuple(tuple(stack) for stack in new_state)
                    new_cost = g + max(1, costs[from_stack])

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state, costs), new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


def heuristic(state, goal, costs):
    # The heuristic is the sum of the costs of moving each block to its correct position in the goal state
    # This heuristic is admissible because it underestimates the cost to reach the goal state, as it assumes that each block can be moved directly to its correct position without considering the cost of moving other blocks
    # The heuristic is consistent because the cost of moving a block to its correct position is always at least 1, which is the decrease in the heuristic estimate if the block is moved towards its correct position
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != goal[i][j]:
                h += max(1, costs[i])
    return h


print(a_star())
