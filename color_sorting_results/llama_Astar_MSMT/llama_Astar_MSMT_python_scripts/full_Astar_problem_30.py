
import heapq


def initialize():
   # Define the initial state of the game as a 2d tuple
   initial_state = (('Red', 'Blue', 'Green', 'Green'),
                   ('Blue', 'Red', 'Green', 'Blue'),
                   ('Green', 'Blue', 'Red', 'Red'))
   num_tubes = 3


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # The goal state must not have any balls left to sort
       if not any(len(tube) > 0 for tube in state):
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for from_tube in range(num_tubes):
           for to_tube in range(num_tubes):
               # Check if the action is valid, ie if the tube we're moving the ball to has capacity for another ball and the balls are not already sorted
               if len(state[to_tube]) < 7 and state[from_tube][-1] != state[to_tube][-1 if len(state[to_tube]) > 0 else 0]:
                   temp_state = [list(tube[:]) for tube in state]
                   # Perform the action
                   temp_state[from_tube].pop()
                   temp_state[to_tube].append(state[from_tube][-1])
                   # Generate the new state
                   new_state = tuple(tuple(tube) for tube in temp_state)
                   # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to sort the balls
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic is the number of balls out of place, plus the number of balls in the tubes with more than 7 balls
                       h = heuristic(state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state):
   # The heuristic is an admissible and consistent estimate of the cost to reach the goal state, considering the number of balls out of place and the number of balls in the tubes with more than 7 balls
   # The heuristic is admissible because it never overestimates the cost to reach the goal state
   # The heuristic is consistent because the estimated cost of the next node is higher if a ball is moved to a tube with more than 7 balls, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of balls that can be moved to a tube with more than 7 balls is by moving the balls from the tubes with more than 7 balls, which is exactly the number of balls moved in the heuristic
   h = 0
   for tube in state:
       for ball in tube:
           if ball not in tube:
               h += 1
   for tube in state:
       if len(tube) > 7:
           h += len(tube) - 7
   return h


print(a_star())
