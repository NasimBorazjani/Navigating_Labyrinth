
import heapq

def initialize():
    # Define the initial state of the stacks as a list of lists
    initial_state = [['Green', 'Yellow', 'Red', 'Red'], [], ['Yellow', 'Green', 'Blue', 'Yellow'], [], [], ['Red', 'Blue', 'Green', 'Blue']]
    # Define the costs of moving one block to the top of each stack
    costs = {0: 3, 1: 7, 2: 7, 3: 7, 4: 2, 5: 4}
    # The maximum number of blocks in a stack
    max_blocks = 4
    # The number of stacks
    num_stacks = 6
    # The goal state is when all stacks have only one shade of block
    goal_state = [['Green'], ['Yellow'], ['Red'], ['Blue']]

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]
   
    return initial_state, costs, max_blocks, num_stacks, goal_state, visited_costs, queue
  
def a_star():
   
    initial_state, costs, max_blocks, num_stacks, goal_state, visited_costs, queue = initialize()

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                # The block can be moved if the to_stack is empty or has the same shade as the top block of the from_stack
                if not state[to_stack] or state[from_stack][-1] == state[to_stack][-1]:
                    # And the to_stack does not exceed its capacity
                    if len(state[to_stack]) < max_blocks:
                        # Perform the action
                        new_state = [stack[:] for stack in state]
                        new_state[to_stack].append(new_state[from_stack].pop())
                        # Calculate the cost of the action
                        new_cost = g + costs[to_stack]
                        # The new state must be a tuple to be used as a key in the visited_costs dictionary
                        new_state = tuple(tuple(stack) for stack in new_state)
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            # The heuristic is the sum of the differences between the number of blocks in each stack and the goal state
                            h = heuristic(new_state, goal_state)
                            heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))
   return None

def heuristic(state, goal_state):
    # The heuristic is admissible and consistent, as it always underestimates the cost to reach the goal state
    return sum(abs(len(state[i]) - len(goal_state[i])) for i in range(len(state)))

print(a_star())
