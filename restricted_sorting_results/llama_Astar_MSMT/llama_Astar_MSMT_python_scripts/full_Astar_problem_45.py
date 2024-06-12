
import heapq


def initialize():
   # Define the initial state of the stacks as a list of lists
   initial_state = [['Red', 'Yellow', 'Red', 'Yellow', 'Black'],
                   ['Black', 'Blue', 'Green', 'Green', 'Blue'],
                   [],
                   [],
                   [],
                   [],
                   ['Black', 'Blue', 'Green', 'Black', 'Yellow'],
                   ['Blue', 'Green', 'Yellow', 'Red', 'Red']]

   # Create a dictionary to map the colors to their indices
   color_to_index = {'Red': 0, 'Yellow': 1, 'Black': 2, 'Blue': 3, 'Green': 4}

   # Create a dictionary to map the indices to their colors
   index_to_color = {0: 'Red', 1: 'Yellow', 2: 'Black', 3: 'Blue', 4: 'Green'}

   # Create a dictionary to map the indices to their costs
   stack_costs = {0: 2, 1: 3, 2: 5, 3: 9, 4: 8, 5: 5, 6: 8, 7: 1}

   num_stacks = 8
   capacity = 5

   # Create a list of empty stacks
   empty_stacks = [[] for _ in range(num_stacks)]

   visited_costs = {}
   visited_costs[tuple(initial_state)] = 0

   # The information we must encode for each state includes the current state of the stacks and the total cost so far
   initial_state = (initial_state, 0)

   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_stacks, capacity, color_to_index, index_to_color, stack_costs, empty_stacks, visited_costs, queue
  
def a_star():
  
   initial_state, num_stacks, capacity, color_to_index, index_to_color, stack_costs, empty_stacks, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the stacks are sorted, return the actions taken
       if state[0] == empty_stacks:
           return actions


       # Generate all possible actions from the current state
       for from_stack in range(num_stacks):
           for to_stack in range(num_stacks):
               # Check if moving the top block from the from_stack to the to_stack would result in a valid state
               if state[0][from_stack] and (not state[0][to_stack] or color_to_index[state[0][from_stack][-1]] == color_to_index[state[0][to_stack][-1]]):
                   # Generate the new state
                   new_state = [list(stack[:]) for stack in state[0]]
                   new_state[from_stack].pop()
                   new_state[to_stack].append(index_to_color[color_to_index[state[0][from_stack][-1]]])
                   new_state = (new_state, state[1] + stack_costs[to_stack])


                   # If the new state is valid, add it to the queue
                   if new_state not in visited_costs or visited_costs[new_state] > new_state[1]:
                       visited_costs[new_state] = new_state[1]
                       # The heuristic is the difference between the maximum shade count and the current shade count
                       h = max(len(stack) for stack in new_state[0]) - len(new_state[0][color_to_index[max(state[0][from_stack])]])
                       heapq.heappush(queue, (new_state[1] + h, new_state[1], actions + [(from_stack, to_stack)], new_state))
   return None


print(a_star())
