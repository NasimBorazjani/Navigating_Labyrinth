
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Red', 'Green', 'Blue', 'Blue'),
                   ('Blue', 'Red', 'Green', 'Red'),
                   ('Green', 'Blue', 'Red', 'Green'))
   num_tubes = 3


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must be all tubes having balls of only one color
       if len(set(tuple(tube) for tube in state)) == 1:
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for from_tube in range(num_tubes):
           for to_tube in range(num_tubes):
               if from_tube != to_tube:
                   # Check if the new state, containing the moved ball, would be valid; ie the tube we're moving to must not be full
                   if len(state[to_tube]) < 7:
                       # Generate the new state
                       new_state = [list(tube[:]) for tube in state]
                       # Move the top ball from the from_tube to the to_tube
                       new_state[to_tube].append(new_state[from_tube].pop())
                       new_state = tuple(tuple(tube) for tube in new_state)
                       # The additional cost of this state is 1 as we are trying to minimize the number of moves
                       new_cost = g + 1
                      
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state):
   # The heuristic function can be a simulation of moving balls greedily, using the next color ball repeatedly as long as the tube does not exceed its capacity
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved to a tube that is full, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be moved to the tube is by moving the balls of the next color to the tube, which is exactly the balls used to fill the tube in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Iterate through the tubes
   for i in range(len(state)):
       # Sort the balls in the tube by color
       sorted_tube = sorted(state[i])
       # Move the balls to the tubes greedily
       for color in set(sorted_tube):
           while sorted_tube.count(color) > 1 and len(state[i]) < 7:
               state[i].append(sorted_tube.pop(0))
               # Increment the estimated cost to the goal by 1 actions
               h += 1
   return h


print(a_star())
