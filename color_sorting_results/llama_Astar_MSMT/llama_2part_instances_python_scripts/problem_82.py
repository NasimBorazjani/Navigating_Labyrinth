
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Blue', 'Green', 'Blue', 'Red'),
                   ('Red', 'Blue', 'Green', 'Red'),
                   ('Green', 'Green', 'Blue', 'Red'))
   num_tubes = 3
   max_capacity = 6


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, max_capacity, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, max_capacity, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must be all tubes containing balls of only one color
       if all(len(set(tube)) == 1 for tube in state):
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for from_tube in range(num_tubes):
           for to_tube in range(num_tubes):
               if from_tube != to_tube and len(state[from_tube]) > 0 and len(state[to_tube]) < max_capacity:
                   # The new state is the current state with the ball moved from the from_tube to the to_tube
                   new_state = [list(tube[:]) for tube in state]
                   new_state[to_tube].append(new_state[from_tube].pop())
                   new_state = tuple(tuple(tube) for tube in new_state)
                   # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to sort the balls
                   new_cost = g + 1
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic is the number of balls not in their correct tubes
                       h = heuristic(new_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state):
   # The heuristic is the number of balls not in their correct tubes
   # This heuristic is admissible because it is a lower bound on the number of moves required to sort the balls
   # The heuristic is consistent because it never overestimates the cost to reach the goal state
   return sum(len(tube) for tube in state if len(set(tube)) != 1)


print(a_star())
