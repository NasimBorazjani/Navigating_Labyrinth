
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Red', 'Blue', 'Green', 'Blue'),
                   ('Red', 'Red', 'Red', 'Green'),
                   ('Blue', 'Green', 'Blue', 'Green'))
   num_tubes = 3
   # Define the goal state
   goal_state = (('Red', 'Red', 'Red', 'Red', 'Red', 'Red'),
                 ('Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'),
                 ('Green', 'Green', 'Green', 'Green', 'Green', 'Green'))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for from_tube in range(num_tubes):
           for to_tube in range(num_tubes):
               # Check if the move is valid, ie if the tube we are moving to is not full
               if len(state[to_tube]) < 6:
                   # Perform the move
                   new_state = [list(tube[:]) for tube in state]
                   new_state[to_tube].append(new_state[from_tube].pop())
                   new_state = tuple(tuple(tube) for tube in new_state)
                   # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to sort the balls
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None


print(a_star())
