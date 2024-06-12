
import heapq


def initialize():
   # Define the initial state of the tubes as a 2d tuple
   initial_state = (('Red', 'Blue', 'Blue', 'Red'),
                   ('Blue', 'Green', 'Blue', 'Green'),
                   ('Green', 'Red', 'Green', 'Red'))
   num_tubes = 3
   max_capacity = 7


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, max_capacity, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, max_capacity, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the balls are correctly sorted in the tubes, return the actions taken
       if state == (('Red', 'Red', 'Red', 'Red'), ('Blue', 'Blue', 'Blue', 'Blue'), ('Green', 'Green', 'Green', 'Green')):
           return actions


       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for from_tube in range(num_tubes):
           for to_tube in range(num_tubes):
               if from_tube != to_tube:
                   # Check if the move is valid, ie the ball to be moved is not the last one in the tube and the tube to move to is not full
                   if state[from_tube][1:] and len(state[to_tube]) < max_capacity:
                       # Generate the new state
                       new_state = [list(tube[:]) for tube in state]
                       new_state[from_tube].pop(0)
                       new_state[to_tube].insert(0, state[from_tube][0])
                       new_state = tuple(tuple(tube) for tube in new_state)
                       # The cost so far is the number of moves made, as we aim to minimize the number of moves to sort the balls
                       new_cost = g + 1
                      
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state, new_state)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_tube, to_tube)], new_state))
   return None




def heuristic(state, goal):
   # The heuristic function can be a simulation of sorting the balls greedily, using the next color ball repeatedly as long as it is possible to move it
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the balls the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a ball is moved back to a tube, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of balls that can be moved to a tube is by using the next color ball, which is exactly the ball used to move in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Iterate through the tubes
   for i in range(len(state)):
       # Sort the balls in the tube by color
       sorted_tube = sorted(state[i])
       # Move the balls to the correct tubes using the next color ball repeatedly as long as it is possible to move it
       for color in sorted_tube:
           while state[i][0] != color and state[sorted_tube.index(color)][1:] and len(state[sorted_tube.index(color)]) < max_capacity:
               # Move the ball to the correct tube
               state[sorted_tube.index(color)].insert(0, state[i].pop(0))
               # Increment the estimated cost to the goal by 1 actions
               h += 1
   return h


print(a_star())
