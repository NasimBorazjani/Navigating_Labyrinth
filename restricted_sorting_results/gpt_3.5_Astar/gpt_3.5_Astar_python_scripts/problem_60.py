
import heapq


def a_star():
    # Define the initial state of the stacks
    initial_state = [['Yellow', 'Green', 'Green', 'Black', 'Black'], [], ['Yellow', 'Green', 'Black', 'Green', 'Red'], ['Red', 'Black', 'Blue', 'Blue', 'Yellow'], [], [], ['Red', 'Blue', 'Yellow', 'Blue', 'Red'], []]
    num_stacks = 8
    stack_capacity = 5
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 6, 1: 1, 2: 8, 3: 8, 4: 1, 5: 6, 6: 4, 7: 1}
    # Define the goal state, which is an empty stack
    goal_state = [[], [], [], [], [], [], [], []]


    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


    queue = [(0, 0, [], initial_state)]


    while queue:
        _, g, actions, state = heapq.heappop(queue)


        # If the current state is the goal state, return the actions taken
        if state == goal_state:
            return actions


        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                # Check if transferring a block from the 'from_stack' to the 'to_stack' is valid
                if state[from_stack] and (not state[to_stack] or state[from_stack][-1] == state[to_stack][-1]) and len(state[to_stack]) < stack_capacity:
                    # Generate the new state after transferring the block
                    new_state = [list(stack[:]) for stack in state]
                    new_state[from_stack].pop()
                    new_state[to_stack].append(state[from_stack][-1])
                    new_state = tuple(tuple(stack) for stack in new_state)
                    # Calculate the cost of the transfer
                    new_cost = g + stack_costs[from_stack]
                  
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))
    return None


print(a_star())
