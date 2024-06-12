
import heapq


def a_star():
    # Define the initial state of the stacks, with the colors of the blocks represented as strings
    initial_state = [[],
                      ['Blue', 'Black', 'Black', 'Yellow', 'White', 'Green'],
                      ['Green', 'Black', 'Red', 'Green', 'Yellow', 'Blue'],
                      [],
                      ['Green', 'Red', 'Blue', 'Yellow', 'Green', 'Blue'],
                      ['Black', 'White', 'White', 'Red', 'White', 'Black'],
                      [],
                      ['White', 'Red', 'Blue', 'Yellow', 'Yellow', 'Red'],
                      [],
                      []]
    num_stacks = 10
    stack_capacity = 6
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 5, 1: 4, 2: 7, 3: 7, 4: 11, 5: 11, 6: 8, 7: 3, 8: 7, 9: 9}


    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0


    queue = [(0, 0, [], initial_state)]


    while queue:
        _, g, actions, state = heapq.heappop(queue)


        # Check if all stacks are sorted
        if all(all(stack[i] == stack[i+1] for i in range(len(stack) - 1)) for stack in state if stack):
            return actions


        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                if from_stack != to_stack:
                    # Check if the from stack is not empty and the to stack is either empty or the top block matches the color of the block being transferred
                    if state[from_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]):
                        new_state = [list(stack[:]) for stack in state]
                        new_state[from_stack].pop()
                        new_state[to_stack].append(state[from_stack][-1])
                        new_state = tuple(tuple(stack) for stack in new_state)
                        # Calculate the cost of the transfer based on the cost of moving a block to the top of the stack
                        new_cost = g + stack_costs[to_stack]
                        
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            heapq.heappush(queue, (new_cost, new_cost, actions + [(from_stack, to_stack)], new_state))
    return None


print(a_star())
