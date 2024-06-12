
import heapq


def initialize():
    # Define the initial state of the stacks as a list of lists
    initial_state = [[], [], [], ['Yellow', 'Black', 'Yellow', 'Black', 'Green'], ['Red', 'Yellow', 'Blue', 'Black', 'Black'], [], ['Red', 'Blue', 'Green', 'Red', 'Blue'], ['Green', 'Blue', 'Red', 'Yellow', 'Green']]
    num_stacks = 8
    stack_capacity = 5
    # Define the cost of moving one block to the top of each stack
    move_costs = {0: 2, 1: 1, 2: 6, 3: 3, 4: 1, 5: 5, 6: 4, 7: 2}
    # The goal state is when each stack has 4 blocks of a single shade or is empty
    goal_state = [['Yellow'], ['Black'], ['Yellow'], ['Black'], ['Green', 'Red'], ['Blue'], ['Red', 'Blue', 'Green'], ['Yellow']]

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]
  
    return initial_state, num_stacks, stack_capacity, move_costs, goal_state, visited_costs, queue
  
def a_star():
    initial_state, num_stacks, stack_capacity, move_costs, goal_state, visited_costs, queue = initialize()

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        if state == goal_state:
            return actions

        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                if from_stack != to_stack:
                    # Check if moving a block from the from_stack to the to_stack results in a valid state
                    new_state = [list(stack[:]) for stack in state]
                    block = new_state[from_stack].pop()
                    new_state[to_stack].append(block)
                    # The cost of the new state is the cost of the move plus the cost so far
                    new_cost = g + move_costs[to_stack]

                    if new_state[from_stack] or new_state[to_stack] == goal_state[to_stack]:
                        new_state = [list(stack[:]) for stack in new_state]
                        if new_state not in visited_costs or new_cost < visited_costs[tuple(tuple(stack) for stack in new_state)]:
                            visited_costs[tuple(tuple(stack) for stack in new_state)] = new_cost
                            h = heuristic(new_state, goal_state)
                            heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
  
    return None


def heuristic(state, goal_state):
    h = 0
    for from_stack in range(len(state)):
        for block in state[from_stack]:
            # The heuristic is the sum of the costs of moving each block to its goal position
            to_stack = goal_state.index(block)
            h += move_costs[to_stack]
    return h


print(a_star())
