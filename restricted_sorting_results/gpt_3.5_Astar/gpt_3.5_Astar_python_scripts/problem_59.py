
import heapq


def a_star():
    # Define the initial state of the stacks
    initial_state = [['Green', 'Blue', 'Green', 'Yellow', 'Yellow'], [], ['Red', 'Red', 'Green', 'Black', 'Black'], [], ['Blue', 'Yellow', 'Black', 'Yellow', 'Blue'], [], [], ['Black', 'Blue', 'Red', 'Red', 'Green']]
    num_stacks = 8
    stack_capacity = 5
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 1, 1: 5, 2: 5, 3: 4, 4: 8, 5: 6, 6: 8, 7: 9}


    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


    queue = [(0, 0, [], initial_state)]


    while queue:
        _, g, actions, state = heapq.heappop(queue)


        # Check if all stacks are sorted
        if all(stack == sorted(stack, key=lambda x: (x == 'Black', x == 'Blue', x == 'Green', x == 'Red', x == 'Yellow')) for stack in state):
            return actions


        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                if from_stack != to_stack:
                    # Check if the transfer is valid, ie the from_stack is not empty and the to_stack is either empty or the top block in the to_stack has the same shade as the block being transferred
                    if state[from_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]):
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
