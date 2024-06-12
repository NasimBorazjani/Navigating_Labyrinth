
import heapq

def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Blue', 'Green', 'Red', 'Red'),
                   ('Red', 'Blue', 'Green', 'Red'),
                   ('Blue', 'Blue', 'Green', 'Green'))

   num_tubes = 3
   tube_capacity = 7
   # Create the set of the valid colors that could be in the tubes
   colors = set(['Blue', 'Green', 'Red'])

   visited_costs = {}
   visited_costs[initial_state] = 0

   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, tube_capacity, colors, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, tube_capacity, colors, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must have all tubes sorted, thus we need to check whether the current state is the goal state
       if all(len(set(color for color in tube if color != 'x')) == 1 for tube in state):
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for from_tube in range(num_tubes):
           for to_tube in range(num_tubes):
               # Check if the new state, containing the ball moved between tubes, would be valid
               if len(state[from_tube]) > 0 and len(state[to_tube]) < tube_capacity and state[from_tube][-1] != 'x':
                   # Generate the new state
                   new_state = [list(tube[:]) for tube in state]
                   new_state[from_tube].pop()
                   new_state[to_tube].append(state[from_tube][-1])
                   new_state = tuple(tuple(tube) for tube in new_state)
                   # The additional cost of this state is 1 as we are trying to minimize the number of moves
                   new_cost = g + 1

                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic is the number of colors in the tubes, assuming the cost of moving a ball between tubes is 1
                       h = heuristic(new_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None


def heuristic(state):
   # The heuristic is the number of colors in the tubes, assuming the cost of moving a ball between tubes is 1
   return len(set(color for tube in state for color in tube if color != 'x'))


print(a_star())
